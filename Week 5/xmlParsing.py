import xml.etree.ElementTree as ET

data = '''<person><name>Ramanathan</name></person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text


