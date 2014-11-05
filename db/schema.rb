# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141105040212) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "locations", force: true do |t|
    t.float    "latitude"
    t.float    "longitude"
    t.string   "name"
    t.string   "address"
    t.string   "land_use_description"
    t.string   "neighborhood_name"
    t.boolean  "sidewalks"
    t.string   "violations"
    t.string   "lot_condition"
    t.string   "structure_condition"
    t.string   "digest_year"
    t.string   "owner"
    t.string   "tax_district"
    t.string   "objectid_1"
    t.string   "objectid"
    t.string   "val_acres"
    t.string   "structure_year"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.boolean  "ebt"
    t.string   "county"
    t.string   "source"
  end

end
