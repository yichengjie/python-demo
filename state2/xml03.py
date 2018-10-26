import xml.etree.ElementTree as ET

root = ET.parse('country_data.xml')

#  top-level elements
t1 = root.findall('.')
print('----------------------------')
for t in t1:
	print(t.tag)
print('----------------------------')
t2 = root.findall('./country/neighbor')
for tmp in t2:
	print(tmp.attrib['name'])
print('----------------------------')
root.findall(".//year/..[@name='Singapore']")

root.findall(".//*[@name='Singapore']/year")

t4 = root.findall(".//neighbor[2]")
for tmp in t4:
	print(tmp.attrib['name'])
print('len(t4) : ' ,len(t4))

print('----------------------------')