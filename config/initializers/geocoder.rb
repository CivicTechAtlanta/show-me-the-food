Geocoder.configure(
  timeout: 5,
  units: :mi,
  # The default lookup (Nominatim/OpenStreetMap) requires a User-Agent that
  # identifies the application: https://operations.osmfoundation.org/policies/nominatim/
  http_headers: { "User-Agent" => "show-me-the-food (https://github.com/codeforatlanta/show-me-the-food)" }
)
