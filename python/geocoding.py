import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAGQh741SvVZndL19xOcQx-fVY9YuuEjuQ')

# geocoding an address
geocoded_address = gmaps.geocode('315 NE Campus Pkwy, Seattle, WA ')
print(geocoded_address)