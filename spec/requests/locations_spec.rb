require "rails_helper"

RSpec.describe "Locations", type: :request do
  describe "GET /" do
    it "renders the map page" do
      get root_path

      expect(response).to have_http_status(:ok)
      expect(response.body).to include("map")
    end
  end

  describe "GET /locations.json" do
    it "returns markers for geocoded locations only" do
      geocoded = create(:location)
      create(:location, :ungeocoded, address: nil)

      get locations_path(format: :json)

      expect(response).to have_http_status(:ok)
      markers = response.parsed_body
      expect(markers.size).to eq(1)
      expect(markers.first).to include(
        "lat" => geocoded.latitude,
        "lng" => geocoded.longitude,
        "name" => geocoded.name,
        "ebt" => true
      )
    end
  end

  describe "GET /locations/search" do
    it "returns locations within the radius, nearest first" do
      near = create(:location, latitude: 33.80, longitude: -84.39)
      nearest = create(:location, latitude: 33.749, longitude: -84.388)
      create(:location, name: "Savannah", latitude: 32.08, longitude: -81.09)

      get search_locations_path, params: { lat: 33.749, lng: -84.388 }

      lats = response.parsed_body.map { |marker| marker["lat"] }
      expect(lats).to eq([ nearest.latitude, near.latitude ])
    end

    it "returns every geocoded location when no point is given" do
      create(:location)
      create(:location, latitude: 32.08, longitude: -81.09)

      get search_locations_path

      expect(response.parsed_body.size).to eq(2)
    end

    it "limits results to SNAP/EBT retailers when requested" do
      retailer = create(:location, ebt: true)
      create(:location, ebt: false)

      get search_locations_path, params: { ebt: "1" }

      markers = response.parsed_body
      expect(markers.size).to eq(1)
      expect(markers.first).to include("name" => retailer.name)
    end
  end
end
