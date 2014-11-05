require 'rails_helper'

RSpec.describe LocationsController, :type => :controller do
  describe "#index" do
    subject{ assigns(:locations) }
    it 'assigns @locations' do
      location = FactoryGirl.create(:location)
      xhr :get, :index, {}
      expect(subject).to include(location)
    end
  end
end
