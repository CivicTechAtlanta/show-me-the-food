class CreateLocations < ActiveRecord::Migration[8.1]
  def change
    create_table :locations do |t|
      t.float :latitude
      t.float :longitude
      t.string :name
      t.string :address
      t.string :source

      # SNAP/EBT retailer data (db/seed_data/GA-EBT.csv)
      t.boolean :ebt, default: false, null: false
      t.string :county

      # Atlanta Strategic Community Investment tax-digest data
      # (db/seed_data/Atlanta_Strategic_Community_Investment_2013.csv)
      t.string :land_use_description
      t.string :neighborhood_name
      t.boolean :sidewalks
      t.string :violations
      t.string :lot_condition
      t.string :structure_condition
      t.string :digest_year
      t.string :owner
      t.string :tax_district
      t.string :objectid_1
      t.string :objectid
      t.string :val_acres
      t.string :structure_year

      t.timestamps
    end

    add_index :locations, [ :latitude, :longitude ]
    add_index :locations, :ebt
  end
end
