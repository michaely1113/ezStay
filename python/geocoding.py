from tokens import GOOGLEMAPS_KEY
#import scraper
import googlemaps
import json

gmaps = googlemaps.Client(key=GOOGLEMAPS_KEY)

# geocoding an address sample
geocoded_address = gmaps.geocode('315 NE Campus Pkwy, Seattle, WA')
print(geocoded_address)


# now, we need to be able to get a list of <addresses from tyler> then convert it to a list of geocoded addresses
#addressesOfEvents = scraper.getAddressesOfEvents()   #TODO COMMENT OUT NEXT THREE LINES
addressesOfEvents = []
addressesOfEvents.append('315 NE Campus Pkwy, Seattle, WA')
addressesOfEvents.append('5015 16th Ave NE, Seattle, WA')
geocodedEvents = []
for address in addressesOfEvents:
    geocodedEvents.append(gmaps.geocode(address))

for geocodedEvent in geocodedEvents:
    print(geocodedEvent['geometry'])

# get geocoded addresses, run algo where we find midpoint between all points