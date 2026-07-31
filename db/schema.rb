# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[8.1].define(version: 2026_07_29_000001) do
  create_table "locations", force: :cascade do |t|
    t.string "address"
    t.string "county"
    t.datetime "created_at", null: false
    t.string "digest_year"
    t.boolean "ebt", default: false, null: false
    t.string "land_use_description"
    t.float "latitude"
    t.float "longitude"
    t.string "lot_condition"
    t.string "name"
    t.string "neighborhood_name"
    t.string "objectid"
    t.string "objectid_1"
    t.string "owner"
    t.boolean "sidewalks"
    t.string "source"
    t.string "structure_condition"
    t.string "structure_year"
    t.string "tax_district"
    t.datetime "updated_at", null: false
    t.string "val_acres"
    t.string "violations"
    t.index ["ebt"], name: "index_locations_on_ebt"
    t.index ["latitude", "longitude"], name: "index_locations_on_latitude_and_longitude"
  end
end
