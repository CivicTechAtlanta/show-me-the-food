# Seed db with city of atlanta CSV

file = File.join(Rails.root, "db", "seed_data", "Atlanta_Strategic_Community_Investment_2013.csv")

CSV.parse(open(file), headers: true, :encoding => 'UTF-8') do |row|

  Location.create address: row["SITUS"], land_use_description: row["LandUse_Description"],
                  neighborhood_name: row["Neighborhood_Name"], sidewalks: row["Sidewalks"],
                  violations: row["Multiple_Violations"], lot_condition: row["Lot_Condition"],
                  structure_condition: row["Structure_Condition"], digest_year: row["DIGEST"],
                  owner: row["OWNER"], tax_district: row["TAX_DISTR"], objectid_1: row["OBJECTID_1"],
                  objectid: row["OBJECTID"], val_acres: row["VAL_ACRES"], structure_year: row["STRUCT_YR"]


end
