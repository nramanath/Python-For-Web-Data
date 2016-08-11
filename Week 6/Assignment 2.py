import urllib
import json

address = raw_input("Enter a place name: ")
serviceurl = 'http://python-data.dr-chuck.net/geojson?'
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})


print "Retrieving {0}".format(url)
data = urllib.urlopen(url).read()
print "Retrieved {0} characters".format(len(data))
parsed_data = json.loads(data)

print "Place id", parsed_data["results"][0]["place_id"]