require "rails_helper"

RSpec.describe Location do
  describe "geocoding" do
    it "geocodes a new location that has an address but no coordinates" do
      location = create(:location, :ungeocoded)

      expect(location.latitude).to eq(33.749)
      expect(location.longitude).to eq(-84.388)
    end

    it "keeps coordinates that are already present" do
      location = create(:location, latitude: 1.0, longitude: 2.0)

      expect(location.latitude).to eq(1.0)
      expect(location.longitude).to eq(2.0)
    end

    it "leaves locations without an address ungeocoded" do
      location = create(:location, :ungeocoded, address: nil)

      expect(location.latitude).to be_nil
    end
  end

  describe ".ebt_retailers" do
    it "returns only SNAP/EBT retailers" do
      retailer = create(:location, ebt: true)
      create(:location, ebt: false)

      expect(described_class.ebt_retailers).to contain_exactly(retailer)
    end
  end
end
