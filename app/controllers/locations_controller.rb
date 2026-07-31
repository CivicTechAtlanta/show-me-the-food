class LocationsController < ApplicationController
  DEFAULT_SEARCH_RADIUS_MILES = 10

  def index
    respond_to do |format|
      format.html
      format.json { render json: MapJsonPresenter.markers(Location.geocoded) }
    end
  end

  # Markers near a point (?lat=&lng=&radius=), nearest first. Without a point,
  # every geocoded location. Pass ?ebt=1 to limit to SNAP/EBT retailers.
  def search
    locations = Location.geocoded
    locations = locations.ebt_retailers if params[:ebt].present?
    locations = filter_by_distance(locations) if params[:lat].present? && params[:lng].present?

    render json: MapJsonPresenter.markers(locations)
  end

  private

  # Distances are computed in Ruby because SQLite lacks the trig functions
  # geocoder's `near` scope needs; fine at this dataset's size (~10k rows).
  def filter_by_distance(locations)
    center = [ params[:lat].to_f, params[:lng].to_f ]
    radius = params.fetch(:radius, DEFAULT_SEARCH_RADIUS_MILES).to_f

    locations
      .map { |location| [ Geocoder::Calculations.distance_between(center, location.to_coordinates), location ] }
      .select { |distance, _location| distance <= radius }
      .sort_by(&:first)
      .map(&:last)
  end
end
