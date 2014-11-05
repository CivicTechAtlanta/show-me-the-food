class LocationsController < ApplicationController
  def index
    @locations = Location.all
    respond_to do |format|
      format.html
      format.json { MapJsonPresenter.create_location_hash(@locations) }
    end
  end

  def search
    locations = Location.all
    hash = MapJsonPresenter.create_location_hash(locations)
    render json: hash
  end
end
