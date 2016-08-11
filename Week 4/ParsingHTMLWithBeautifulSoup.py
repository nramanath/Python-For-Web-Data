import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/comments_42.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
    print tag
