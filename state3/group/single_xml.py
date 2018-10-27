import xml.etree.ElementTree as ET
import os

class GroupSingleXmlStatistic(object):
	"""docstring for ClassName"""
	def __init__(self, filepath):
		self.filepath = filepath
		filename = os.path.split(filepath)[1]
		self.retData = {'isCreate':'N',\
			'filename':filename,'list':[]}

	def parse(self):
		# 解析xml数据
		root = ET.parse(self.filepath)
		groups = root.getroot()
		#  根节点
		isCreate = groups.attrib['isCreate']
		self.retData['isCreate'] = isCreate
		#  group 的记录条数
		for group in groups.findall('group'):
			carrCode = group.attrib['carrier_code']
			locCode = group.attrib['location_code']
			id = group.attrib['id']
			groupdtls = group.findall('groupdtl')
			retGroupData = {'carrCode':carrCode,\
				'locCode':locCode,'id':id,'dtlCount':len(groupdtls)}
			self.retData['list'].append(retGroupData)
		return self.retData

	def print(self):
		print('Fname:%s, isCreate: %s, GCount is : %d, DtlCount is : %d ' \
		     % (self.retData['filename'], self.retData['isCreate'], \
		  	len(self.retData['list']), dc))