# Seed db with city of atlanta CSV

file = File.join(Rails.root, "db", "seed_data", "filter_collection_companies.csv")

CSV.parse(file.file.read, headers: true, header_converters: :symbol) do |row|

  attributes = row.to_hash

  Location.create

end