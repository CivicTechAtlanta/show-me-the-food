# Seed data

## GA-EBT.csv

Currently authorized SNAP (EBT) retailers in Georgia, from the USDA-FNS
[SNAP Retailer Location Data](https://usda-snap-retailers-usda-fns.hub.arcgis.com/datasets/USDA-FNS::snap-retailer-location-data/about)
ArcGIS feature service (USDA refreshes it roughly every two weeks).

- Snapshot date: **2026-07-29** — 9,314 GA retailers reported by the service,
  9,313 rows after deduplication (610 in the city of Atlanta).
- Columns: `Store_Name,Longitude,Latitude,Address,Address Line #2,City,State,Zip5,Zip4,County`
- Sorted by (County, City, Address, Store_Name) so regeneration produces stable diffs.

Regenerate with:

```
python3 db/seed_data/tools/refresh_ga_ebt.py
```

The script fetches, validates (row counts, GA-only, unique IDs, coordinate
bounding box), dedups, and writes the CSV. This file replaced an October 2014
export of the same USDA dataset (10,194 rows) that had two format bugs — a
trailing comma in the header and a trailing space on every line — which made
stock Ruby `CSV` raise `MalformedCSVError`. The regenerated file parses clean.
The service also offers a `Store_Type` field, currently not included; add it to
the script's field list if wanted.

## Atlanta_Strategic_Community_Investment_2013.csv

Food-related commercial parcels from the City of Atlanta Strategic Community
Investment report (2013; 2010 Fulton / 2009 DeKalb tax digest plus a 2011–2012
windshield survey). See `Datasources.txt`. No updated edition of this report
exists, so the file cannot be refreshed — instead each parcel was cross-checked
against USDA SNAP retailer snapshots (2014 vs. current) plus an individual web
check for closure candidates, and 4 confirmed-closed locations were removed
(246 → 242 rows). Methodology, per-row verdicts, and evidence:
[SCI_2013_cross_check.md](SCI_2013_cross_check.md).

Re-run the cross-check with:

```
python3 db/seed_data/tools/sci_cross_check.py --old-ebt <path to archived 2014 GA-EBT.csv> --write
```

Manual web-verification verdicts for SNAP-dropout candidates live in
`tools/sci_web_verification.csv`; extend that file when verifying more rows.
