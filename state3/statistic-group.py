#!usr/bin/python
# -*- coding:utf-8 -*-
# iconv -f GB2312 -t UTF-8 group2.xml > group3.xml
# find *.xml -exec sh -c "iconv -f GBK -t UTF8 {} > {}.xml" \;
import xml.etree.ElementTree as ET

class GroupXmlStatistic(object):
	def __init__(self, filePath):
		self.filePath = filePath
		self.retData = []

	def parseXml(self):
		# 解析xml数据
		root = ET.parse(self.filePath)
		groups = root.getroot()
		#  根节点
		isCreate = groups.attrib['isCreate']
		#  group 的记录条数
		for group in groups.findall('group'):
			carrier_code = group.attrib['carrier_code']
			location_code = group.attrib['location_code']
			id = group.attrib['id']
			groupdtls = group.findall('groupdtl')
			self.retData.append({'isCreate':isCreate,'carrCode':carrier_code,'locCode':location_code,'id':id,'dtlCount':len(groupdtls)})
			#print('carrCode : %s , locCode : %s , id : %s , dtlCount : %d' % (carrier_code,location_code,id,len(groupdtls)))
		return self.retData

	def printXml(self):
		#  将数据展示出来
		dc = 0	
		for item in self.retData:
			dc += item['dtlCount']
		print('group count is : %d , dtl count is : %d ' % (len(self.retData) ,dc))


#  调用程序
#  group文件路径
xmlpath = r'./data/20180508_CA_BJS_yicj_265214_GroupImport.xml' 
statistic = GroupXmlStatistic(xmlpath)
#  解析xml文件并统计数据
statistic.parseXml()	
#  打印统计信息
statistic.printXml()




