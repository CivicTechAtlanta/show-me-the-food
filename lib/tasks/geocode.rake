namespace :geocode do
  desc "Geocode locations that have an address but no coordinates (throttled to 1 req/s)"
  task backfill: :environment do
    scope = Location.not_geocoded.where.not(address: [ nil, "" ])
    total = scope.count
    puts "Geocoding #{total} locations…"

    scope.find_each.with_index(1) do |location, index|
      location.geocode

      if location.latitude.present? && location.save
        puts "[#{index}/#{total}] #{location.address} → #{location.latitude}, #{location.longitude}"
      else
        puts "[#{index}/#{total}] #{location.address} — no result"
      end

      sleep 1 # Nominatim's usage policy allows at most 1 request per second
    end
  end
end
