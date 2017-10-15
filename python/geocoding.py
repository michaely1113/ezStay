from tokens import GOOGLEMAPS_KEY
import scraper
import googlemaps
import json
import requests

GMAPS_GEOCODE_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
gmaps = googlemaps.Client(key=GOOGLEMAPS_KEY)

# convert list of addresses to list of geocoded addresses
def getGeocodedEvents():
    # addressesOfEvents = scraper.getAddressesOfEvents()   #TODO COMMENT OUT NEXT THREE LINES
    addressesOfEvents = []
    addressesOfEvents.append('315 NE Campus Pkwy, Seattle, WA')
    addressesOfEvents.append('5015 16th Ave NE, Seattle, WA')
    geocodedEvents = []
    for address in addressesOfEvents:
        geocodedEvents.append(gmaps.geocode(address))
    return geocodedEvents


# get geocoded addresses, run algo where we find midpoint between all points
def findMidpoint(geocodedEvents):
    locations = []
    for geocodedEvent in geocodedEvents:
        locations.append(geocodedEvent[0]['geometry']['location'])
    lat = 0
    lng = 0
    for location in locations:
        lat += location['lat']
        print(location['lat'])
        lng += location['lng']
        print(location['lng'])
    averageLat = lat / locations.__len__()
    averageLng = lng / locations.__len__()

    #find address
    midpointAddress = gmaps.reverse_geocode((averageLat, averageLng))
    return (midpointAddress[0]['formatted_address'])

print(findMidpoint(getGeocodedEvents()))

#################### - SAMPLE HTTP REQUEST - ####################
# sample http request
# url = GMAPS_GEOCODE_API_ENDPOINT % (addressesOfEvents[0], GOOGLEMAPS_KEY)
# response = json.loads(requests.get(url).text)
# results = response['results']
# response = results[0]
#print(response)
#print(response['geometry']['location'])
#################### - SAMPLE HTTP REQUEST - ####################
