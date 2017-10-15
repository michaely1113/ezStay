from flask import Flask
app = Flask(__name__)
import json
import urllib.request as request

@app.route('/test')
def hello_world():
    return getDestination('800', '2017-10-10')

# 4 digit flightNumber
# date in YYYY-MM-DD format
def getFlightInfo(flightNumber, date):
    API_endpoint = "https://demo30-test.apigee.net/v1/hack/status?flightNumber=%s&flightOriginDate=%s&apikey=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW"
    url = API_endpoint % (flightNumber, date)
    return json.loads(request.urlopen(url).read())

def getDestination(flightNumber, date):
    response = getFlightInfo(flightNumber, date)
    return response['flightStatusResponse']['statusResponse']['flightStatusTO']['flightStatusLegTOList']["arrivalCityName"]

def getArrivalTime(flightNumber, date):
    response = getFlightInfo(flightNumber, date)
    return response['flightStatusResponse']['statusResponse']['flightStatusTO']['flightStatusLegTOList']['arrivalLocalTimeScheduled']
