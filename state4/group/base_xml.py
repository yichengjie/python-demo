class GroupBaseXmlStatistic(object):
	def getXmlDtlCount(self,xmlData):
		dc = 0	
		for item in xmlData['list']:
		 	dc += item['dtlCount']
		return dc
