from flask import Flask, request, render_template
import googlemaps
import scraper
import flightinfo
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
        return render_template('checkboxHTML.html')
        # maybe return eventData in json form as a response

@app.route('/airbnb', methods=['GET', 'POST'])
def getAirbnbLink():
    return render_template('Link.html')
    if request.method == 'POST':
        return render_template('Link.html')
        # maybe return eventData in json form as a response



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
