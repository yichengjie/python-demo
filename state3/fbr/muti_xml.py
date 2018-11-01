import os
from single_xml import FbrSingleXmlStatistic

class FbrMutiXmlStatistic(object):
	"""docstring for FareXmlStatistic"""
	def __init__(self, basedir):
		super(FbrMutiXmlStatistic, self).__init__()
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

			fbrSingleXmlStatistic = FbrSingleXmlStatistic(filepath)
			item = fbrSingleXmlStatistic.parse()

			self.retData.append(item)

	#遍历xml中所有的fbr，每个item代表一个fbr
	def getSingleXmlDtlCount(self,item):
		dc = 0
		for fbr in item['list']:
			dtlCount = fbr['dtlCount']
			dc += dtlCount
		return dc

	#遍历xml中fbr的个数
	def getSingleXmlFbrCount(self,item):
		return len(item['list'])

	def print(self):
		filecount = 0
		createCount = 0
		createDtlCount = 0
		cancelCount = 0
		cancelDtlCount = 0

		for item in self.retData:
			filecount += 1
			if(item['isCreate'] == 'Y'):
				createCount += self.getSingleXmlFbrCount(item)
				createDtlCount += self.getSingleXmlDtlCount(item)
			else:
				otherCount += self.getSingleXmlFbrCount(item)
				otherDtlCount += self.getSingleXmlDtlCount(item)

			print('filename :%s, isCreate :%s, fbrCount :%d, \
				fbrDtlCount:%d'% (item['filename'],item['isCreate'],\
					self.getSingleXmlFbrCount(item),self.getSingleXmlDtlCount(item)))


		print('FileCount : '  , filecount)
		print('CreateCount : ' , createCount)
		print('CreateDtlCount : ' , createDtlCount)
		print('OtherCount : ' , otherCount)
		print('OtherDtlCount : ' , otherDtlCount)