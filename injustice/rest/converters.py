import urllib
import urllib.request
import json

def address_to_coords(address):
	url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + urllib.request.quote(address)
	print(url)
	request = urllib.request.Request(url)
	with urllib.request.urlopen(request) as response:
		data = response.read()
		jsonResponse = json.loads(data.decode('UTF-8'))

		return jsonResponse['results'][0]['geometry']['location']