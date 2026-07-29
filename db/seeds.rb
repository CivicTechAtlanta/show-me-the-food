# Seed db with City of Atlanta SCI 2013 parcels and current USDA SNAP retailers.
# Not idempotent: running twice creates duplicate rows.

# --- Atlanta Strategic Community Investment 2013 (food-related parcels) ---
# This file has no coordinates; rows geocode on save (see Location model).
# City/state are appended so the bare parcel address geocodes unambiguously.

sci_file = File.join(Rails.root, "db", "seed_data", "Atlanta_Strategic_Community_Investment_2013.csv")

sidewalks_to_boolean = lambda do |value|
  case value.to_s.strip.upcase
  when "YES" then true
  when "NO" then false
  end
end

CSV.parse(File.read(sci_file), headers: true, :encoding => 'UTF-8').each do |row|

  Location.create! address: "#{row['SITUS']}, Atlanta, GA",
                   land_use_description: row["LandUse_Description"],
                   neighborhood_name: row["Neighborhood_Name"],
                   sidewalks: sidewalks_to_boolean.call(row["Sidewalks"]),
                   violations: row["Multiple_Violations"], lot_condition: row["Lot_Condition"],
                   structure_condition: row["Structure_Condition"], digest_year: row["DIGEST"],
                   owner: row["OWNER"], tax_district: row["TAX_DISTR"], objectid_1: row["OBJECTID_1"],
                   objectid: row["OBJECTID"], val_acres: row["VAL_ACRES"], structure_year: row["STRUCT_YR"],
                   source: "Atlanta_Strategic_Community_Investment_2013.csv"

end

# --- USDA SNAP retailers, Georgia (GA-EBT.csv) ---
# Coordinates come straight from the CSV, so these rows skip geocoding.

ebt_file = File.join(Rails.root, "db", "seed_data", "GA-EBT.csv")

CSV.parse(File.read(ebt_file), headers: true, :encoding => 'UTF-8').each do |row|

  address_parts = [row["Address"], row["Address Line #2"], row["City"], "GA #{row['Zip5']}"]
  address = address_parts.reject { |part| part.nil? || part.strip.empty? }.join(", ")

  Location.create! name: row["Store_Name"],
                   address: address,
                   county: row["County"],
                   ebt: true,
                   latitude: row["Latitude"].to_f,
                   longitude: row["Longitude"].to_f,
                   source: "GA-EBT.csv"

end
