# Show Me The Food

RubyOnRails application, utilizing geocoder and gmaps4rails to map data.

## Goal

Identify food deserts and areas only serviced by convenience stores, sourcing data from government sources
such as EBT programs and tax digests. Data is contained in CSV files in db/seed_data, which is then normalized
and seeded to a PostgreSQL database during `rake db:setup`. Eventually we'd like to be able to use the app to canvas these
areas in person, so that data is updatable from user input and locations can have notes/comments/pictures/etc.

The ultimate goal is to be able to use this data to effectively campaign grocery stores and healthy food providers
to locate in "food deserts."

## Setup

Clone the repo.

`bundle`

`rake db:setup`

And `rails s` to start the server. 