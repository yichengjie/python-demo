#!usr/bin/python
# -*- coding:utf-8 -*-
# iconv -f GB2312 -t UTF-8 group2.xml > group3.xml
# find *.xml -exec sh -c "iconv -f GBK -t UTF8 {} > {}.xml" \;
import xml.etree.ElementTree as ET

filePath = r'./data/20180508_CA_BJS_yicj_265214_GroupImport.xml' 
# 解析xml数据
root = ET.parse(filePath)
groups = root.getroot()
#  根节点
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



