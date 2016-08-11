import urllib

fileHandler = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')


for line in fileHandler:
    print line.strip()
