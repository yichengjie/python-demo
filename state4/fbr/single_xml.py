import xml.etree.ElementTree as ET
import os

class FbrSingleXmlStatistic(object):
	"""docstring for ClassName"""
	def __init__(self, filepath):
		self.filepath = filepath
		filename = os.path.split(filepath)[1]
		self.retData = {'filename':filename,'isCreate':'N','list':[]}

	def parse(self):
		# 解析xml数据
		root = ET.parse(self.filepath)
		fares = root.getroot()
		#  根节点
		isCreate = fares.attrib['isCreate']
		self.retData['isCreate'] = isCreate
		fbrNodeList = fares.findall('fbr')
		
		for fbrNode in fbrNodeList:
			carrCode = fbrNode.attrib['carrier_code']
			locCode = fbrNode.attrib['location_code']
			id = fbrNode.attrib['id']
			dtlNodeList = fbrNode.findall('fbrdtl')
			fbrData = {'carrCode':carrCode,'locCode':locCode,\
			'id':id,'dtlCount':len(dtlNodeList)}
			self.retData['list'].append(fbrData)
		return self.retData

	def __getSingleDtlCount(self):
		dc = 0
		for fbr in self.retData['list']:
			dtlCount = fbr['dtlCount']
			dc += dtlCount
		return dc

	def print(self):
		data = self.retData ;
		print('filename :%s, isCreate :%s, fbrCount :%d, allDtlCount:%d' % (data['filename'],\
			 data['isCreate'], len(data['list']),self.__getSingleDtlCount()))