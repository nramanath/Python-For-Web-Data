import urllib
import json

url = "http://python-data.dr-chuck.net/comments_269241.json "
data = urllib.urlopen(url).read()

jsonData = json.loads(data)
counts = []

comments = jsonData["comments"]

for comment in comments:
    counts.append(comment['count'])

print "Count: {0}".format(len(counts))
print "Sum: {0}".format(sum(counts))

print sum(counts)

for comment in comments:
    print comment['name']