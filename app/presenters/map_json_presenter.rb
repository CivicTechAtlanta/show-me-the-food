# Builds the marker hashes consumed by the Leaflet map
# (app/javascript/controllers/map_controller.js).
class MapJsonPresenter
  def self.markers(locations)
    locations.map do |location|
      {
        lat: location.latitude,
        lng: location.longitude,
        name: location.name,
        address: location.address,
        ebt: location.ebt,
        source: location.source
      }
    end
  end
end
