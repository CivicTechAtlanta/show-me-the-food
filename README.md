# Show Me The Food

A Code for Atlanta civic app that maps SNAP/EBT retailers and Atlanta tax-digest
parcels on an interactive map, built with Ruby on Rails, [geocoder], and
[Leaflet]/OpenStreetMap.

[geocoder]: https://github.com/alexreisner/geocoder
[Leaflet]: https://leafletjs.com/

## Goal

Identify food deserts and areas only serviced by convenience stores, sourcing
data from government sources such as EBT programs and tax digests. Data is
contained in CSV files in `db/seed_data` (see `Datasources.txt`), which is
normalized and seeded into the database. Eventually we'd like to be able to use
the app to canvas these areas in person, so that data is updatable from user
input and locations can have notes/comments/pictures/etc.

The ultimate goal is to be able to use this data to effectively campaign
grocery stores and healthy food providers to locate in "food deserts."

## Requirements

- Ruby (see `.ruby-version`)
- No database server needed — the app uses SQLite. To use PostgreSQL instead,
  swap `sqlite3` for `pg` in the `Gemfile` and update `config/database.yml`.

## Setup

### With Docker (no Ruby install needed)

```
docker compose up
```

This builds the dev image, prepares and seeds the SQLite database, and serves
the app at <http://localhost:3000>. The source tree is bind-mounted, so code
edits reload live. The database lives in a named Docker volume; to reset it,
run `docker compose down --volumes`.

### Natively

With Ruby installed (see `.ruby-version`):

```
bin/setup
```

This installs gems, prepares the SQLite database, seeds it from the CSVs, and
starts the server. Already set up? Seed and run with:

```
bin/rails db:prepare db:seed
bin/rails server
```

The SNAP/EBT retailer data ships with coordinates. The Atlanta Strategic
Community Investment parcels only have street addresses; geocode them
(throttled to 1 request/second per Nominatim's usage policy — the 245 rows
take about 4 minutes) with:

```
bin/rails geocode:backfill
```

## Deploying to Fly.io

The production `Dockerfile` plus `fly.toml` deploy to [Fly.io](https://fly.io)
with SQLite on a persistent volume. With [flyctl](https://fly.io/docs/flyctl/)
installed and signed in:

```
fly launch --copy-config --no-deploy
fly secrets set RAILS_MASTER_KEY=$(cat config/master.key)
fly deploy --ha=false
```

`--ha=false` keeps the app to a single machine — required because SQLite lives
on one volume. First boot creates, migrates, and seeds the database
automatically; then optionally geocode the parcel data with
`fly ssh console -C "bin/rails geocode:backfill"`.

## Tests and checks

```
bundle exec rspec
bin/rubocop
bin/brakeman
```

CI (GitHub Actions) runs all three plus `bundler-audit` and `importmap audit`
on every push and pull request, and Dependabot keeps dependencies current.

## History

Originally built at Code for Atlanta hack nights in 2014 on Rails 4.1 with
Google Maps (gmaps4rails). Rebuilt in 2026 on Rails 8 with Leaflet and
OpenStreetMap — no API key required. The seed CSVs are 2013–2014 snapshots;
refreshing them from current USDA sources (e.g. the Food Access Research
Atlas and SNAP Retailer Locator) would be a great next contribution.

## License

MIT — see `LICENSE`.
