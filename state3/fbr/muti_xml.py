import os
from single_xml import GroupSingleXmlStatistic
from base_xml import GroupBaseXmlStatistic

class GroupMutiXmlStatistic(GroupBaseXmlStatistic):
	def __init__(self, basedir):
		self.basedir = basedir
		self.retData = []

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

	def parse(self):
		filenames = self.__searchXmls()
		for filename in filenames:
			filepath = os.path.join(self.basedir,filename)
			groupSingleXmlStatistic = GroupSingleXmlStatistic(filepath)
			fileData = groupSingleXmlStatistic.parse()
			self.retData.append(fileData)

	def print(self):
		#  将数据展示出来
		for data in self.retData:
			print('Fname:%s, isCreate: %s, GCount is : %d, DtlCount is : %d ' \
		     % (data['filename'], data['isCreate'], \
		  	len(data['list']), self.getXmlDtlCount(data)))