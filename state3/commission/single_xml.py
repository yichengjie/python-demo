import xml.etree.ElementTree as ET
import os

class CommissionSingleXmlStatistic(object):
	"""docstring for ClassName"""
	def __init__(self, filepath):
		self.filepath = filepath
		filename = os.path.split(filepath)[1]
		self.retData = {'filename':filename,'isCreate':'N','ccount':0}

	def parse(self):
		# 解析xml数据
		root = ET.parse(self.filepath)
		fares = root.getroot()
		#  根节点
		isCreate = fares.attrib['isCreate']
		self.retData['isCreate'] = isCreate
		#  commission 的记录条数
		ccount = len(fares.findall('commission'))
		self.retData['ccount'] = ccount
			
		return self.retData

	def print(self):
		data = self.retData ;
		print('filename :%s, isCreate:%s, ccount:%d'\
		 % (data['filename'], data['isCreate'],data['ccount']))