import xml.etree.ElementTree as ET
import urllib

url = urllib.urlopen('http://python-data.dr-chuck.net/comments_269237.xml').read()
root = ET.fromstring(url)

countTagList = root.findall('comments/comment/count')
sum = 0
for countTag in countTagList:
    print countTag.text
    sum += int(countTag.text)

print "sum = ", sum

nameTagList = root.findall("comments/comment/name")

for name in nameTagList:
    print name.text