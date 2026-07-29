class Location < ActiveRecord::Base
  geocoded_by :address
  # Rows seeded with coordinates (GA-EBT.csv) must not be re-geocoded.
  after_validation :geocode, if: lambda { |location| location.address.present? && location.latitude.blank? }

end
