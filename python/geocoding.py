from tokens import GOOGLEMAPS_KEY
import googlemaps


gmaps = googlemaps.Client(key=GOOGLEMAPS_KEY)

# geocoding an address
geocoded_address = gmaps.geocode('315 NE Campus Pkwy, Seattle, WA ')
print(geocoded_address)