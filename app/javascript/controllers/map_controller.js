import { Controller } from "@hotwired/stimulus"
import * as L from "leaflet"

const ATLANTA = [33.749, -84.388]

// Renders the locations map: OpenStreetMap tiles via Leaflet, one canvas
// marker per geocoded location, and a "you are here" marker when the
// visitor shares their position.
export default class extends Controller {
  static values = { markersUrl: String }

  connect() {
    this.map = L.map(this.element, { preferCanvas: true }).setView(ATLANTA, 11)
    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map)

    this.addMarkers()
    this.showCurrentPosition()
  }

  disconnect() {
    this.map.remove()
  }

  async addMarkers() {
    const response = await fetch(this.markersUrlValue, { headers: { "Accept": "application/json" } })
    if (!response.ok) return

    for (const marker of await response.json()) {
      L.circleMarker([marker.lat, marker.lng], {
        radius: 5,
        weight: 1,
        color: marker.ebt ? "#2f9e44" : "#1971c2",
        fillOpacity: 0.6
      }).bindPopup(() => this.popupFor(marker)).addTo(this.map)
    }
  }

  showCurrentPosition() {
    if (!navigator.geolocation) return

    navigator.geolocation.getCurrentPosition(({ coords }) => {
      L.circleMarker([coords.latitude, coords.longitude], { radius: 8, color: "#e8590c", fillOpacity: 0.9 })
        .bindPopup("You are here")
        .addTo(this.map)
      this.map.setView([coords.latitude, coords.longitude], 13)
    })
  }

  // Popup content is built with DOM APIs so CSV-sourced text is never parsed as HTML.
  popupFor(marker) {
    const popup = document.createElement("div")
    const lines = [marker.name, marker.address, marker.ebt ? "Accepts SNAP/EBT" : null]
    for (const line of lines) {
      if (!line) continue
      const paragraph = document.createElement("p")
      paragraph.textContent = line
      popup.appendChild(paragraph)
    }
    return popup
  }
}
