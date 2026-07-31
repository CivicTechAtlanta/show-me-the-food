#!/usr/bin/env python3
"""Cross-check the Atlanta SCI 2013 parcels against SNAP retailer snapshots.

Compares each SCI parcel address against two USDA SNAP retailer snapshots
(the archived Oct-2014 GA-EBT.csv and the current regenerated one) and sorts
every row into a tier:

  ACTIVE            exact address match in the current snapshot -> keep
  FUZZY             near match in the current snapshot          -> keep, flag
  NO-NUMBER         SITUS has no street number                  -> keep, flag
  SERVICE-STATION   land use 333/334, not ACTIVE                -> keep, flag
  NEVER-SEEN        in neither snapshot                         -> keep, flag
  and, for rows that were in the 2014 snapshot but are gone from the current
  one (food land use 323/326/347/348), a per-row manual web verification
  (tools/sci_web_verification.csv) decides:
  CONFIRMED-CLOSED  web check confirms the store is gone        -> REMOVE
  OPEN-NOT-SNAP     web check shows the store still operating   -> keep, flag
  SNAP-DROPPED      web evidence ambiguous or missing           -> keep, flag

Only CONFIRMED-CLOSED rows are removed: removal requires BOTH that the same
normalized address was SNAP-authorized in 2014 and has since dropped out, AND
a web check confirming closure. SNAP absence alone proves nothing — the
2014-vs-now sweep showed most SNAP dropouts are stores that simply left the
program while staying open.

Usage:
    python3 db/seed_data/tools/sci_cross_check.py \
        --sci db/seed_data/Atlanta_Strategic_Community_Investment_2013.csv \
        --old-ebt /path/to/GA-EBT-2014.csv \
        --new-ebt db/seed_data/GA-EBT.csv \
        --report db/seed_data/SCI_2013_cross_check.md \
        [--write]     # actually rewrite the SCI csv (otherwise dry run)

Stdlib only; no dependencies.
"""

import argparse
import csv
import re

SUFFIXES = {
    "STREET": "ST", "STR": "ST",
    "AVENUE": "AVE", "AV": "AVE",
    "BOULEVARD": "BLVD",
    "DRIVE": "DR",
    "ROAD": "RD",
    "HIGHWAY": "HWY",
    "PARKWAY": "PKWY", "PKWAY": "PKWY",
    "PLACE": "PL",
    "COURT": "CT",
    "CIRCLE": "CIR",
    "LANE": "LN",
    "TERRACE": "TER",
    "POINT": "PT",
    "PLAZA": "PLZ",
    "EXPRESSWAY": "EXPY",
    "FREEWAY": "FWY",
    "SQUARE": "SQ",
}
DIRECTIONALS = {
    "NORTHEAST": "NE", "NORTHWEST": "NW",
    "SOUTHEAST": "SE", "SOUTHWEST": "SW",
    "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W",
}
UNIT_WORDS = {"STE", "SUITE", "UNIT", "APT", "BLDG", "FL", "FLOOR"}
# Known Atlanta street renamings / spelling variants.
ALIASES = [
    (re.compile(r"\bM\s?L\s?K(?:\s?JR)?\b|\bMARTIN\s?LUTHER\s?KING(?:\s?JR)?\b|\bM\s?L\s?KING(?:\s?JR)?\b"), "MLK"),
    (re.compile(r"\bDONALD\s?LEE\s?HOLLOWELL\b|\bBANKHEAD\b"), "HOLLOWELL"),
    (re.compile(r"\bRALPH\s?(?:DAVID|D)\s?ABERNATHY\b"), "ABERNATHY"),
]
SERVICE_STATION_CODES = {"333", "334"}
FOOD_CODES = {"323", "326", "347", "348"}


def normalize(address):
    """Return (street_number or None, normalized street body)."""
    text = address.upper()
    text = re.sub(r"[.,#]", " ", text)
    for pattern, replacement in ALIASES:
        text = pattern.sub(replacement, text)
    tokens = text.split()
    out = []
    skip_next = False
    for tok in tokens:
        if skip_next:
            skip_next = False
            continue
        if tok in UNIT_WORDS:
            skip_next = True
            continue
        out.append(DIRECTIONALS.get(tok, SUFFIXES.get(tok, tok)))
    number = None
    if out and re.fullmatch(r"\d+[A-Z]?", out[0]):
        number = re.sub(r"[A-Z]$", "", out[0])
        out = out[1:]
    return number, " ".join(out)


def strip_suffix_dir(body):
    """Street body without suffix/directional tokens, for loose comparison."""
    keep = [t for t in body.split()
            if t not in SUFFIXES.values() and t not in DIRECTIONALS.values()]
    return " ".join(keep)


def levenshtein(a, b):
    if abs(len(a) - len(b)) > 2:
        return 3
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def load_ebt(path):
    """Load an EBT snapshot -> list of dicts with normalized address parts."""
    rows = []
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.DictReader(f):
            city = (row.get("City") or "").strip().upper()
            county = (row.get("County") or "").strip().upper()
            if city != "ATLANTA" and county not in ("FULTON", "DEKALB"):
                continue
            number, body = normalize((row.get("Address") or "").strip())
            rows.append({
                "name": (row.get("Store_Name") or "").strip(),
                "city": city,
                "number": number,
                "body": body,
            })
    return rows


def exact_matches(pool, number, body):
    return [r for r in pool if r["number"] == number and r["body"] == body]


def fuzzy_matches(pool, number, body):
    if number is None:
        return []
    loose = strip_suffix_dir(body)
    found = []
    for r in pool:
        if r["number"] == number:
            if r["body"] != body and (
                    levenshtein(r["body"], body) <= 2
                    or (loose and strip_suffix_dir(r["body"]) == loose)):
                found.append(r)
        elif r["body"] == body and r["number"] and r["number"].isdigit() \
                and number.isdigit() and abs(int(r["number"]) - int(number)) <= 10:
            found.append(r)
    return found


def landuse_code(description):
    match = re.search(r"(\d+)\*?\s*$", description or "")
    return match.group(1) if match else ""


def load_verification(path):
    """SITUS -> (verdict, evidence) from the manual web-verification overlay."""
    verdicts = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verdicts[row["SITUS"].strip().upper()] = (
                row["verdict"].strip().lower(), row["evidence"].strip())
    return verdicts


def classify(sci_rows, old_pool, new_pool, verification):
    results = []
    for row in sci_rows:
        situs = (row.get("SITUS") or "").strip()
        code = landuse_code(row.get("LandUse_Description"))
        number, body = normalize(situs)
        new_exact = exact_matches(new_pool, number, body)
        new_fuzzy = fuzzy_matches(new_pool, number, body)
        old_exact = exact_matches(old_pool, number, body)
        evidence = ""
        if new_exact:
            tier = "ACTIVE"
        elif number is None:
            tier = "NO-NUMBER"
        elif new_fuzzy:
            tier = "FUZZY"
        elif code in SERVICE_STATION_CODES:
            tier = "SERVICE-STATION"
        elif old_exact and code in FOOD_CODES:
            verdict, evidence = verification.get(situs.upper(), ("", ""))
            if verdict == "closed":
                tier = "CONFIRMED-CLOSED"
            elif verdict == "open":
                tier = "OPEN-NOT-SNAP"
            else:
                tier = "SNAP-DROPPED"
                if not verdict:
                    evidence = "not yet web-verified"
        else:
            tier = "NEVER-SEEN"
        results.append({
            "row": row,
            "situs": situs,
            "code": code,
            "tier": tier,
            "evidence": evidence,
            "old_names": sorted({r["name"] for r in old_exact}),
            "new_names": sorted({r["name"] for r in new_exact or new_fuzzy}),
        })
    return results


TIER_NOTES = {
    "ACTIVE": ("keep", "SNAP-authorized food retailer operates at this address today."),
    "FUZZY": ("keep, flagged", "Near match in the current snapshot; address formats differ."),
    "NO-NUMBER": ("keep, flagged", "SITUS has no street number, so address matching is impossible."),
    "SERVICE-STATION": ("keep, flagged", "Gas stations may or may not be SNAP-authorized; SNAP absence proves nothing about the parcel."),
    "CONFIRMED-CLOSED": ("REMOVED", "Had a SNAP retailer at this exact address in 2014, no longer SNAP-authorized, and a web check confirms the store is gone."),
    "OPEN-NOT-SNAP": ("keep, flagged", "Dropped out of SNAP since 2014 but a web check shows the store still operating."),
    "SNAP-DROPPED": ("keep, flagged", "Dropped out of SNAP since 2014; web evidence of current status is ambiguous."),
    "NEVER-SEEN": ("keep, flagged", "Not in the 2014 or current snapshot; cannot distinguish closed from never-SNAP-authorized."),
}
TIER_ORDER = ["CONFIRMED-CLOSED", "OPEN-NOT-SNAP", "SNAP-DROPPED", "ACTIVE",
              "FUZZY", "SERVICE-STATION", "NO-NUMBER", "NEVER-SEEN"]
EVIDENCE_TIERS = {"CONFIRMED-CLOSED", "OPEN-NOT-SNAP", "SNAP-DROPPED"}


def write_report(path, results, snapshot_note):
    counts = {t: sum(1 for r in results if r["tier"] == t) for t in TIER_ORDER}
    lines = []
    lines.append("# SCI 2013 cross-check against USDA SNAP retailer data")
    lines.append("")
    lines.append(snapshot_note)
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append(
        "Each parcel's `SITUS` address was normalized (uppercased, punctuation and unit "
        "designators stripped, USPS suffix and directional abbreviations, plus aliases for "
        "known Atlanta street renamings: MLK Jr Dr variants, Bankhead Hwy / Donald Lee "
        "Hollowell Pkwy, Ralph David Abernathy Blvd) and matched against SNAP retailer "
        "addresses in the city of Atlanta plus Fulton/DeKalb counties, in two snapshots: "
        "the archived October 2014 `GA-EBT.csv` and the current USDA export.")
    lines.append("")
    lines.append(
        "Rows that had a SNAP retailer at the same normalized address in 2014 but not in "
        "the current snapshot were then **individually web-verified** (business listings, "
        "Yelp open/closed status, chain store locators, redevelopment news — July 2026; "
        "verdicts and evidence recorded in `tools/sci_web_verification.csv`). That sweep "
        "showed most SNAP dropouts are stores that left the program while staying open, so "
        "SNAP absence alone is never treated as proof of closure. A row is **removed "
        "only** when it dropped out of SNAP **and** the web check confirms the store is "
        "gone (tier CONFIRMED-CLOSED). Every other row is kept, flagged for human review "
        "where status is uncertain.")
    lines.append("")
    lines.append("## Tier counts")
    lines.append("")
    lines.append("| Tier | Rows | Action |")
    lines.append("|---|---|---|")
    for tier in TIER_ORDER:
        lines.append("| %s | %d | %s |" % (tier, counts[tier], TIER_NOTES[tier][0]))
    lines.append("| **Total** | **%d** | |" % len(results))
    for tier in TIER_ORDER:
        rows = [r for r in results if r["tier"] == tier]
        if not rows:
            continue
        lines.append("")
        lines.append("## %s (%d) — %s" % (tier, len(rows), TIER_NOTES[tier][0]))
        lines.append("")
        lines.append(TIER_NOTES[tier][1])
        lines.append("")
        with_evidence = tier in EVIDENCE_TIERS
        header_cols = "| SITUS | Land use | Neighborhood | 2014 SNAP match | Current SNAP match |"
        if with_evidence:
            header_cols += " Web verification (July 2026) |"
        lines.append(header_cols)
        lines.append("|---|---|---|---|---|" + ("---|" if with_evidence else ""))
        for r in sorted(rows, key=lambda x: x["situs"]):
            cells = "| %s | %s | %s | %s | %s |" % (
                r["situs"],
                (r["row"].get("LandUse_Description") or "").strip(),
                (r["row"].get("Neighborhood_Name") or "").strip(),
                "; ".join(r["old_names"]) or "—",
                "; ".join(r["new_names"]) or "—",
            )
            if with_evidence:
                cells += " %s |" % (r["evidence"] or "—")
            lines.append(cells)
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def rewrite_sci(path, raw_lines, results):
    removed = {id(r["row"]) for r in results if r["tier"] == "CONFIRMED-CLOSED"}
    kept_lines = [raw_lines[0]]  # header
    for r, line in zip((x["row"] for x in results), raw_lines[1:]):
        if id(r) in removed:
            continue
        kept_lines.append(line.replace("Deterirated", "Deteriorated"))
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(kept_lines) + "\n")
    return len(kept_lines) - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sci", default="db/seed_data/Atlanta_Strategic_Community_Investment_2013.csv")
    parser.add_argument("--old-ebt", required=True)
    parser.add_argument("--new-ebt", default="db/seed_data/GA-EBT.csv")
    parser.add_argument("--verification", default="db/seed_data/tools/sci_web_verification.csv")
    parser.add_argument("--report", default="db/seed_data/SCI_2013_cross_check.md")
    parser.add_argument("--snapshot-note", default="")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    with open(args.sci, newline="", encoding="utf-8", errors="replace") as f:
        raw = f.read()
    raw_lines = raw.splitlines()
    sci_rows = list(csv.DictReader(raw.splitlines()))
    if len(sci_rows) != len(raw_lines) - 1:
        raise RuntimeError("SCI row/line mismatch (%d rows, %d data lines) — "
                           "multiline fields?" % (len(sci_rows), len(raw_lines) - 1))

    old_pool = load_ebt(args.old_ebt)
    new_pool = load_ebt(args.new_ebt)
    verification = load_verification(args.verification)
    print("pools: old=%d new=%d (Atlanta + Fulton/DeKalb); %d web verdicts"
          % (len(old_pool), len(new_pool), len(verification)))

    results = classify(sci_rows, old_pool, new_pool, verification)
    for tier in TIER_ORDER:
        print("%-17s %d" % (tier, sum(1 for r in results if r["tier"] == tier)))
    for r in results:
        if r["tier"] == "CONFIRMED-CLOSED":
            print("  remove: %-30s was: %s" % (r["situs"], "; ".join(r["old_names"])))

    write_report(args.report, results, args.snapshot_note)
    print("report: %s" % args.report)
    if args.write:
        kept = rewrite_sci(args.sci, raw_lines, results)
        print("rewrote %s: %d rows kept, %d removed"
              % (args.sci, kept, len(results) - kept))
    else:
        print("dry run - SCI csv not modified (pass --write)")


if __name__ == "__main__":
    main()
