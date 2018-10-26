#import xml.etree.ElementTree as ET
#root = ET.parse('country_data.xml')
from xml.etree.ElementTree import ElementTree
tree = ElementTree()
root = tree.parse('country_data.xml')

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

for actor in root.findall('real_person:actor',ns):
	name = actor.find('real_person:name',ns)
	print(name.text)
	for char in actor.findall('role:character',ns):
		print('|-->',char.text)