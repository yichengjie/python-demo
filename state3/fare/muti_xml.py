import os
from single_xml import FareSingleXmlStatistic

class FareMutiXmlStatistic(object):
	"""docstring for FareXmlStatistic"""
	def __init__(self, basedir):
		self.basedir = basedir
		self.retData = []

	def __searchXmls(self,basedir):
		retData = []
		for filename in os.listdir(self.basedir):
			extname = os.path.splitext(filename)[1]
			if extname == '.xml':
				retData.append(filename)
		return retData

	def parse(self):
		xmlnames = self.__searchXmls(self.basedir)
		for xmlname in xmlnames:
			filepath = os.path.join(self.basedir,xmlname)
			fareSingleXmlStatistic = FareSingleXmlStatistic(filepath)
			item = fareSingleXmlStatistic.parse()
			self.retData.append(item)

	def print(self):
		filecount = 0
		createCount = 0
		otherCount = 0
		for item in self.retData:
			filecount += 1
			if(item['isCreate'] == 'Y'):
				createCount += item['fcount']
			else:
				otherCount += item['fcount']
			print('filename :%s, isCreate:%s, refNo:%s, fcount:%d'\
		 		% (item['filename'], item['isCreate'],\
		 		item['refNo'],item['fcount']))
			
		print('FileCount : ', filecount)
		print('CreateCount : ', createCount)
		print('otherCount : ', otherCount)