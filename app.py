from flask import Flask, request, render_template
import googlemaps
from python import scraper
from python import flightinfo
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

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
