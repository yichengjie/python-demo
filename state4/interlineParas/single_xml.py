import xml.etree.ElementTree as ET
import os

class InterlineParasSingleXmlStatistic(object):
	"""docstring for ClassName"""
	def __init__(self, filepath):
		self.filepath = filepath
		filename = os.path.split(filepath)[1]
		self.retData = {'filename':filename,'icount':0}

	def parse(self):
		# 解析xml数据
		root = ET.parse(self.filepath)
		fares = root.getroot()
		#  根节点
		#  interlinePara 的记录条数
		icount = len(fares.findall('interlinePara'))
		self.retData['icount'] = icount
			
		return self.retData

	def print(self):
		data = self.retData ;
		print('filename :%s, icount:%d'\
		 % (data['filename'],data['icount']))