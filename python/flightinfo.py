import json
import urllib.request as request

def getFlightInfo():
	return request.urlopen("https://demo30-test.apigee.net/v1/hack/status?flightNumber=1500&flightOriginDate=2016-09-25&apikey=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW").read()

response = json.loads(getFlightInfo())
arrivalCity = response['flightStatusResponse']['statusResponse']['flightStatusTO']['flightStatusLegTOList']["arrivalCityName"]
arrivalTime = response['flightStatusResponse']['statusResponse']['flightStatusTO']['flightStatusLegTOList']["arrivalLocalTimeEstimatedActual"]


def getDestination():
    return arrivalCity

def getArrivalTime():
    return arrivalTime
