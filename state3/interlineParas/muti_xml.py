import os
from single_xml import InterlineParasSingleXmlStatistic

class InterlineParasMutiXmlStatistic(object):
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
			interlineParasSingleXmlStatistic = InterlineParasSingleXmlStatistic(filepath)
			item = interlineParasSingleXmlStatistic.parse()
			self.retData.append(item)

	def print(self):
		for item in self.retData:
			print('filename :%s, icount:%d'\
		 		% (item['filename'], item['icount']))