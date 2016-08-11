import urllib
from BeautifulSoup import *

url = raw_input('Enter Url:')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
sum = 0

tags = soup('span')
for tag in tags:
    #print tag.contents[0]
    sum += int(tag.contents[0])


print sum
# spantags = soup.get('span',None)


#for spantag in spantags:
#    print spantag