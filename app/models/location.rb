class Location < ApplicationRecord
  geocoded_by :address
  after_validation :geocode, if: :needs_geocoding?

  scope :ebt_retailers, -> { where(ebt: true) }

  private

  # Only hit the geocoding API when an address is set or changed and we don't
  # already have coordinates (most seed data ships with its own). Bulk backfill
  # belongs in `bin/rails geocode:backfill`, not per-record saves.
  def needs_geocoding?
    address.present? && address_changed? && (latitude.blank? || longitude.blank?)
  end
end
