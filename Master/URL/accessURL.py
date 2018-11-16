#!/usr/bin/env python3
#
# accessURL.py - Rick Wightman, September 2018
#
# Use swapi.co to demonstrate pretty printing json.
#
# Note that swapi.co appears to not like programatic use of their api,
# and so we need to disguise our client in the header.
#

import urllib.request
import json

def getData(url):
	user_agent = 'curl/7.29.0'
	headers = { 'User-Agent' : user_agent }

	try:
		req = urllib.request.Request(url=url, headers=headers)
		response = urllib.request.urlopen(req)
		data = response.read()
	except Exception as e:
		print(e)

	#data is of type bytes. Convert to json
	strData = data.decode('utf8').replace("'", '"')
	jsonData = json.loads(strData)
	return jsonData
