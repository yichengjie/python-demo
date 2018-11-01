import os
from single_xml import GroupSingleXmlStatistic
from base_xml import GroupBaseXmlStatistic

class GroupMutiXmlStatistic(GroupBaseXmlStatistic):
	def __init__(self, basedir):
		self.basedir = basedir
		self.retData = {}

	def __getXmlDtlCount(self,xmlData):
		dc = 0	
		for item in xmlData['list']:
		 	dc += item['dtlCount']
		return dc

	def __searchXmls(self):
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
		filenames = self.__searchXmls()
		for filename in filenames:
			filepath = os.path.join(self.basedir,filename)
			groupSingleXmlStatistic = GroupSingleXmlStatistic(filepath)
			fileData = groupSingleXmlStatistic.parse()
			carrCode = self.__getCarrCode(filename)
			#print('carrCode : ' ,carrCode)
			#self.retData.append(fileData)

			if (self.retData.get(carrCode , -1) == -1):
				ll = [fileData]
				self.retData.update({carrCode:ll})
			else:
				self.retData.get(carrCode).append(fileData)

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
		#  将数据展示出来
		filecount = 0
		createCount = 0
		createDtlCount = 0
		otherCount = 0
		otherDtlCount = 0

		for data in fileInfos:
			filecount += 1
			if(data['isCreate'] == 'Y'):
				createCount += len(data['list'])
				createDtlCount += self.getXmlDtlCount(data)
			else:
				otherCount += len(data['list'])
				otherDtlCount += self.getXmlDtlCount(data)
		print('carrCode:%s, FCount:%d, ICount:%d, IDCount:%d, \
				ACount:%d, ADCount:%d' % (carrCode,filecount,\
				createCount,createDtlCount,otherCount,otherDtlCount))

		return filecount,createCount,createDtlCount,otherCount,otherDtlCount
