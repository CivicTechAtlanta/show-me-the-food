require "csv"

# Seeds the locations table from the CSV snapshots in db/seed_data (sources
# documented in Datasources.txt and db/seed_data/README.md). Coordinates come
# straight from the CSVs where available; run `bin/rails geocode:backfill`
# afterwards to geocode the rest. Re-running replaces each source's rows
# wholesale.

def replace_source(source, rows)
  Location.where(source: source).delete_all
  rows.each_slice(1000) { |slice| Location.insert_all(slice, record_timestamps: true) }
  puts "Seeded #{rows.size} locations from #{source}"
end

def blank_to_nil(value)
  value.to_s.strip.presence
end

# --- USDA SNAP retailers, Georgia (with coordinates) ----------------------

ebt_file = Rails.root.join("db/seed_data/GA-EBT.csv")

ebt_rows = CSV.read(ebt_file, headers: true).map do |row|
  address = [
    row["Address"],
    row["Address Line #2"],
    row["City"],
    "#{blank_to_nil(row['State'])} #{blank_to_nil(row['Zip5'])}"
  ].filter_map { |part| blank_to_nil(part) }.join(", ")

  {
    name: row["Store_Name"],
    latitude: blank_to_nil(row["Latitude"])&.to_f,
    longitude: blank_to_nil(row["Longitude"])&.to_f,
    address: address,
    county: row["County"],
    ebt: true,
    source: ebt_file.basename.to_s
  }
end

replace_source(ebt_file.basename.to_s, ebt_rows)

# --- Atlanta Strategic Community Investment parcels (no coordinates) ------

sci_file = Rails.root.join("db/seed_data/Atlanta_Strategic_Community_Investment_2013.csv")

sci_rows = CSV.read(sci_file, headers: true).map do |row|
  situs = blank_to_nil(row["SITUS"])

  {
    # City/state are appended so the bare parcel address geocodes unambiguously.
    address: situs && "#{situs}, Atlanta, GA",
    land_use_description: row["LandUse_Description"],
    neighborhood_name: row["Neighborhood_Name"],
    sidewalks: blank_to_nil(row["Sidewalks"])&.casecmp?("yes"),
    violations: blank_to_nil(row["Multiple_Violations"]),
    lot_condition: blank_to_nil(row["Lot_Condition"]),
    structure_condition: blank_to_nil(row["Structure_Condition"]),
    digest_year: row["DIGEST"],
    owner: row["OWNER"],
    tax_district: row["TAX_DISTR"],
    objectid_1: row["OBJECTID_1"],
    objectid: row["OBJECTID"],
    val_acres: row["VAL_ACRES"],
    structure_year: row["STRUCT_YR"],
    ebt: false,
    source: sci_file.basename.to_s
  }
end

replace_source(sci_file.basename.to_s, sci_rows)
