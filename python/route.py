from flask import Flask
from flask import request
import googlemaps
import flightinfo
import scraper
app = Flask(__name__)

# after user presses submit, sending post request with flight details
@app.route('/flight', methods=['GET', 'POST'])
def getEventData():
    if request.method == 'POST':
        flightNumber = request.form.get("flightNumber")
        date = request.form.get("flightDate")
        destination = flightinfo.getDestination(flightNumber, date)
        arrivalTime = flightinfo.getArrivalTime(flightNumber, date)

        eventData = scraper.returnResult() # use destination when we get API access for tripadvisor
        return eventData
        # maybe return eventData in json form as a response
    else:
        # do nothing for a GET request
