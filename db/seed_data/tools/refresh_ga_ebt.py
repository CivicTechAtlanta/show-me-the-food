#!/usr/bin/env python3
"""Regenerate db/seed_data/GA-EBT.csv from the USDA-FNS SNAP retailer service.

Fetches all currently authorized SNAP retailers in Georgia from the USDA-FNS
ArcGIS feature service (refreshed by USDA roughly every two weeks), validates
the download, and writes the 10-column CSV consumed by db/seeds.rb.

Usage:
    python3 db/seed_data/tools/refresh_ga_ebt.py [--out db/seed_data/GA-EBT.csv]

Stdlib only; no dependencies.
"""

import argparse
import csv
import json
import re
import sys
import urllib.parse
import urllib.request

SERVICE = (
    "https://services1.arcgis.com/RLQu0rK7h4kbsBq5/arcgis/rest/services/"
    "snap_retailer_location_data/FeatureServer/0/query"
)
WHERE = "State='GA'"
FIELDS = [
    "Record_ID", "Store_Name", "Store_Street_Address", "Additonal_Address",
    "City", "State", "Zip_Code", "Zip4", "County", "Latitude", "Longitude",
]
PAGE_SIZE = 1000
# Georgia bounding box, with a little slack for border towns.
GA_BBOX = {"lat": (30.3, 35.1), "lng": (-85.7, -80.7)}
HEADER = [
    "Store_Name", "Longitude", "Latitude", "Address", "Address Line #2",
    "City", "State", "Zip5", "Zip4", "County",
]


def query(params):
    url = SERVICE + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=120) as resp:
        payload = json.load(resp)
    if "error" in payload:
        raise RuntimeError("ArcGIS error: %s" % payload["error"])
    return payload


def fetch_all():
    total = query({"where": WHERE, "returnCountOnly": "true", "f": "json"})["count"]
    print("service reports %d GA retailers" % total)
    rows = []
    offset = 0
    while True:
        page = query({
            "where": WHERE,
            "outFields": ",".join(FIELDS),
            "orderByFields": "Record_ID",
            "resultOffset": offset,
            "resultRecordCount": PAGE_SIZE,
            "returnGeometry": "false",
            "f": "json",
        })
        feats = page.get("features", [])
        rows.extend(f["attributes"] for f in feats)
        print("  fetched %d/%d" % (len(rows), total))
        if len(feats) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    if len(rows) != total:
        raise RuntimeError("fetched %d rows but service reported %d" % (len(rows), total))
    return rows


def validate(rows):
    ids = [r["Record_ID"] for r in rows]
    if len(set(ids)) != len(ids):
        raise RuntimeError("Record_ID values are not unique")
    bad_state = [r for r in rows if (r.get("State") or "").strip() != "GA"]
    if bad_state:
        raise RuntimeError("%d rows are not State=GA" % len(bad_state))
    out_of_bbox = 0
    for r in rows:
        lat, lng = r.get("Latitude"), r.get("Longitude")
        if lat is None or lng is None:
            raise RuntimeError("row %s has null coordinates" % r["Record_ID"])
        if not (GA_BBOX["lat"][0] <= lat <= GA_BBOX["lat"][1]
                and GA_BBOX["lng"][0] <= lng <= GA_BBOX["lng"][1]):
            out_of_bbox += 1
            print("  outside GA bbox: %s %s (%s, %s)"
                  % (r["Record_ID"], r.get("Store_Name"), lat, lng))
    if out_of_bbox > len(rows) * 0.005:
        raise RuntimeError("%d rows outside Georgia bounding box" % out_of_bbox)
    atlanta = sum(1 for r in rows if (r.get("City") or "").strip().upper() == "ATLANTA")
    print("Atlanta rows: %d" % atlanta)
    if not 550 <= atlanta <= 700:
        raise RuntimeError("Atlanta count %d outside expected 550-700 range" % atlanta)


def clean(value):
    text = str(value if value is not None else "")
    # USDA data occasionally carries stray 0xFF padding bytes decoded as 'ÿ'.
    text = text.replace("ÿ", "")
    return re.sub(r"\s+", " ", text).strip()


def transform(rows):
    out = []
    for r in rows:
        zip5 = clean(r.get("Zip_Code")).split(".")[0]
        if zip5:
            zip5 = zip5.zfill(5)
        zip4 = clean(r.get("Zip4")).split(".")[0]
        out.append([
            clean(r.get("Store_Name")),
            "%s" % r["Longitude"],
            "%s" % r["Latitude"],
            clean(r.get("Store_Street_Address")),
            clean(r.get("Additonal_Address")),  # USDA's own field-name typo
            clean(r.get("City")),
            clean(r.get("State")),
            zip5,
            zip4,
            clean(r.get("County")),
        ])
    seen = set()
    deduped = []
    for row in out:
        key = (row[0].upper(), row[3].upper(), row[5].upper(), row[7])
        if key in seen:
            print("  dropping duplicate: %s | %s | %s" % (row[0], row[3], row[5]))
            continue
        seen.add(key)
        deduped.append(row)
    deduped.sort(key=lambda r: (r[9], r[5], r[3], r[0]))
    return deduped


def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(HEADER)
        writer.writerows(rows)


def verify_output(path, expected):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        if header != HEADER:
            raise RuntimeError("output header mismatch: %s" % header)
        n = sum(1 for _ in reader)
    if n != expected:
        raise RuntimeError("output has %d rows, expected %d" % (n, expected))
    print("wrote %d rows to %s" % (n, path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="db/seed_data/GA-EBT.csv")
    args = parser.parse_args()
    rows = fetch_all()
    validate(rows)
    cleaned = transform(rows)
    write_csv(args.out, cleaned)
    verify_output(args.out, len(cleaned))


if __name__ == "__main__":
    sys.exit(main())
