import requests
from bs4 import BeautifulSoup
#checking commit address again#
class NameAddress:
    names = []
    addresses = []
    def __init__(self, names, addresses):
        self.names = names
        self.addresses = addresses

toReturn = NameAddress([], [])
cityID = "g6098"
city = "Atlanta_Georgia"
r = requests.get("https://www.tripadvisor.com/Attractions-g60898-Activities-Atlanta_Georgia.html")
content = r.content
soup = BeautifulSoup(content, "html.parser")
topAttractions = soup.find_all("div", {"class": "listing_title"})
codes = []

for i in topAttractions:
    name = i.text
    name = name[1:-1]
    name = name.replace(" ", "_")
    toReturn.names.append(name)

del toReturn.names[6]

for i in topAttractions:
    link = str(i)
    startInd = link.index("<a")
    endInd = link.index("</a>") + 4
    mainPart = link[startInd:endInd]
    parts = mainPart.split("-")
    code = parts[2]
    codes.append(code)

del codes[6]

addresses = []

def getAddress(url):
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    addressSection1 = soup.find_all("div", {"class": "blEntry address clickable colCnt1"})
    addressSection2 = soup.find_all("div", {"class": "blEntry address clickable colCnt2"})
    #one doesn't have an address$
    addressSection = str(addressSection1 + addressSection2)
    indexStAddStart = addressSection.index("street-address") + 15
    indexStAddEnd = addressSection.index("</span>, <span class")
    indexCityStart = addressSection.index("locality") + 10
    indexCityEnd = addressSection.index("GA") + 2
    streetAddress = addressSection[indexStAddStart:indexStAddEnd]
    city = addressSection[indexCityStart:indexCityEnd]
    toReturn.addresses.append(streetAddress + ', ' + city)

for i in range(0, toReturn.names.__len__()):
    currCode = codes[i]
    currName = toReturn.names[i]
    url = 'https://www.tripadvisor.com/Attraction_Review-' + cityID + '-' + currCode + '-Reviews-' + currName + '-' + city + '.html'
    getAddress(url)

def returnResult():
    return toReturn

print(toReturn.names)