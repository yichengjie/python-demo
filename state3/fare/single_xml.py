import xml.etree.ElementTree as ET
import os

class FareSingleXmlStatistic(object):
	"""docstring for ClassName"""
	def __init__(self, filepath):
		self.filepath = filepath
		filename = os.path.split(filepath)[1]
		self.retData = {'filename':filename,'isCreate':'N',\
			'refNo':'','fcount':0}

	def parse(self):
		# 解析xml数据
		root = ET.parse(self.filepath)
		fares = root.getroot()
		#  根节点
		isCreate = fares.attrib['isCreate']
		refNo = fares.attrib['refNo']

		self.retData['isCreate'] = isCreate
		self.retData['refNo']
		#  fare 的记录条数
		fcount = len(fares.findall('fare'))
		self.retData['fcount'] = fcount
			
		return self.retData

	def print(self):
		data = self.retData ;
		print('filename :%s, isCreate:%s, refNo:%s, fcount:%d'\
		 % (data['filename'], data['isCreate'],data['refNo'],data['fcount']))