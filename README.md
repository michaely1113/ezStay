# ezStay
In /python, create a file "tokens.py" on local version that includes a key value pair as such: GOOGLEMAPS_KEY = 'key'
To get the API key, go to https://developers.google.com/maps/documentation/ and find the specific API you want.

# PyCharm
PyCharm has issues with imported modules. See https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
to import modules separately or use pip and connect with system directory (where pip connects to)

import the module httpsproxy_urllib2 to make https connections

For anyone running Python 2.7 or less, in flightinfo.py, use import urllib2 as request instead of import urllib.request as request. This earlier version has been deprecated on later versions of Python.

flightinfo.py is added to .gitignore for this reason so that it doesn't create conflicts across different machines running different versions of Python.
