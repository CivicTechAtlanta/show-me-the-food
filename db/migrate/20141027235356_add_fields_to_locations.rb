class AddFieldsToLocations < ActiveRecord::Migration
  def change
    add_column :locations, :ebt, :boolean
    add_column :locations, :county, :string
  end
end
