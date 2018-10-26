import xml.etree.ElementTree as ET
root = ET.parse('country_data.xml')
for actor in root.findall('{http://people.example.com}actor'):
	name = actor.find('{http://people.example.com}name')
	print(name.text)
	for char in actor.findall('{http://characters.example.com}character'):
		print(' |--> ',char.text)
