import os
from single_xml import FbrSingleXmlStatistic

class FbrMutiXmlStatistic(object):
	"""docstring for FareXmlStatistic"""
	def __init__(self, basedir):
		super(FbrMutiXmlStatistic, self).__init__()
		self.basedir = basedir
		self.retData = {}

	def __searchXmls(self,basedir):
		retData = []
		for filename in os.listdir(self.basedir):
			extname = os.path.splitext(filename)[1]
			if extname == '.xml':
				retData.append(filename)
		return retData
	#从文件名称中匹配出航司二字码
	def __getCarrCode(self,filename):
		#20181010_CN_HDQ_xming_
		#20181010_ 忽略日期字符串
		#CN_HDQ_xming_
		datestr = '20181010_'
		index = len(datestr)
		tmpstr = filename[index:]
		index2 = tmpstr.index('_')
		return tmpstr[0:index2]

	def parse(self):
		xmlnames = self.__searchXmls(self.basedir)
		for xmlname in xmlnames:
			filepath = os.path.join(self.basedir,xmlname)
			fbrSingleXmlStatistic = FbrSingleXmlStatistic(filepath)
			item = fbrSingleXmlStatistic.parse()
			carrCode = self.__getCarrCode(xmlname)

			if (self.retData.get(carrCode , -1) == -1):
				ll = [item]
				self.retData.update({carrCode:ll})
			else:
				self.retData.get(carrCode).append(item)
			#self.retData.append(item)

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
		all_filecount = 0
		all_createCount = 0
		all_createDtlCount = 0
		all_otherCount = 0
		all_otherDtlCount = 0
		for key,values in  self.retData.items():
			t1,t2,t3,t4,t5 = self.printCarrierInfos(key,values)
			all_filecount += t1
			all_createCount += t2
			all_createDtlCount += t3
			all_otherCount += t4
			all_otherDtlCount += t5
		print('--------------------------------------------------')
		print('sum [fcount:%d, createCount:%d, createDtlCount:%d,\
			otherCount:%d, otherDtlCount:%d]' % (all_filecount,
			all_createCount,all_createDtlCount,all_otherCount,\
			all_otherDtlCount))
		print('--------------------------------------------------')

	def printCarrierInfos(self,carrCode,fileInfos):
		filecount = 0
		createCount = 0
		createDtlCount = 0
		otherCount = 0
		otherDtlCount = 0

		for item in fileInfos:
			filecount += 1
			if(item['isCreate'] == 'Y'):
				createCount += self.getSingleXmlFbrCount(item)
				createDtlCount += self.getSingleXmlDtlCount(item)
			else:
				otherCount += self.getSingleXmlFbrCount(item)
				otherDtlCount += self.getSingleXmlDtlCount(item)
		print('carrCode:%s, FCount:%d, ICount:%d, IDCount:%d, \
				ACount:%d, ADCount:%d' % (carrCode,filecount,\
				createCount,createDtlCount,otherCount,otherDtlCount))
		return filecount,createCount,createDtlCount,otherCount,otherDtlCount