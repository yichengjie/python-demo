import xml.etree.ElementTree as ET
parser = ET.XMLPullParser(['start','end'])
parser.feed('<mytag>sometext')
print(list(parser.read_events()))
print('---------------------------------------')
parser.feed('more text</mytag>')
for event,elem in parser.read_events():
	#print(event)
	print(elem.tag,'text = ',elem.text)

