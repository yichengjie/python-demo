import os
from single_xml import CommissionSingleXmlStatistic

class CommissionMutiXmlStatistic(object):
	"""docstring for FareXmlStatistic"""
	def __init__(self, basedir):
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
			commissionSingleXmlStatistic = CommissionSingleXmlStatistic(filepath)
			item = commissionSingleXmlStatistic.parse()
			carrCode = self.__getCarrCode(xmlname)
			if (self.retData.get(carrCode , -1) == -1):
				ll = [item]
				self.retData.update({carrCode:ll})
			else:
				self.retData.get(carrCode).append(item)

	def print(self):
		fcount = 0
		createCount = 0
		otherCount = 0
		for key,values in self.retData.items():
			t1,t2,t3 = self.printCarrierInfos(key,values)
			fcount += t1
			createCount += t2
			otherCount += t3
		print('--------------------------------------------------')
		print('sum [fcount:%d, createCount:%d,otherCount:%d]'\
		 	% (fcount,createCount,otherCount))
		print('--------------------------------------------------')	

	def printCarrierInfos(self,carrCode,fileInfos):
		fcount = 0
		ccount = 0
		acount = 0
		for item in fileInfos:
			fcount += 1
			if (item['isCreate'] == 'Y'):
				ccount += item['ccount']
			else:
				acount += item['ccount']

		print('carrCode:%s, FCount:%d, ICount:%d, ACount:%d'\
			 % (carrCode,fcount,ccount,acount))
		return fcount,ccount,acount
