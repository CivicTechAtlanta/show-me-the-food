class CreateLocations < ActiveRecord::Migration
  def change
    create_table :locations do |t|
      t.float :latitude
      t.float :longitude
      t.string :name
      t.string :address
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
  end
end
