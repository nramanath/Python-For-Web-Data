import urllib
from BeautifulSoup import *

url = raw_input('Enter the URL:')
position = raw_input('Position:')
count = raw_input('Count:')



# for tag in tags:
#    print tag.get('href')


count = int(count)
print count

while (count > 0):
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html)

    tags = soup('a')
    url = tags[(int(position) - 1)].get('href')
    print 'Retrieving', url
    print tags[(int(position) - 1)].contents[0]
    count -= 1