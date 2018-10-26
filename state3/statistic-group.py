#!usr/bin/python
# -*- coding:utf-8 -*-

from xml.etree.ElementTree import ElementTree
#import xml.etree.ElementTree as ET
#xmlname = '20180508_CA_BJS_yicj_265214_GroupImport'
xmlname = 'group-utf8'
path = r'C:\\Users\\yicj\\Desktop\\excel\\group\\%s.xml' % xmlname
tree = ElementTree()
tree.parse(path)


#  根节点
groups = tree.getroot()
isCreate = groups.attrib['isCreate']
#  group 的记录条数
gcount = 0
for group in groups.findall('group'):
	gcount = gcount + 1
	carrier_code = group.attrib['carrier_code']
	location_code = group.attrib['location_code']
	id = group.attrib['id']
	print('carrier_code : %s , location_code : %s , id : %s' % (carrier_code,location_code,id))
print('group count is : %d' % gcount)		



