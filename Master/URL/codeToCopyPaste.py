#
# codeToCopyPaste.py - Rick Wightman, September 2018
#
# Driver code
#
###############################################################################
# Part A
import urllib.request
import json
import pprint
# if we specify "import acessURL", then we have to call "accessURL.getData()"
from accessURL import getData
pp = pprint.PrettyPrinter(indent=3)

###############################################################################
# Part B
url = input("url to query (e.g. https://www.stuff.com ): ")
data = getData(url)

###############################################################################
# Optional idea

# Want to beautify the json?
pp.pprint(data)
