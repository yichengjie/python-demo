import os


groupfilePath = r'./data/group'
groupcnstrarr = ('代理人添加','副本群组导入模板 ','大客户代理人',\
	'第13批9HGP政府公务分销渠道','直减','政府采购',\
	'群组政府采购机票服务系统（1）','群组1234567机票服务系统（1）',\
	'群组1234567机票服务系统（2）')
#################################################################
farefilepath = './data/fare'
farecnstr = ('舱新模板','新模版','黑屏运价','特价批量导入','普投',\
	'月北方普投','等普投',' 普投','舱新模板','秦皇岛新增航班',\
	'福兰','导出','新增公布运价','黑屏运价','黑屏运价-固定价格',\
	'特价新模板','特价批量导入','等普投','宜太等','高永前','特价批量导入',\
	' 团队','鑸变骇鍝佽繍浠锋ā鏉_2018391涓婅埅鍋囨湡')
#################################################################
fbrfilepath = './data/fbr'
fbrcnstr = ()
#################################################################


renameifnos=[
 {'filepath':groupfilePath,'cnstrs':groupcnstrarr},
 {'filepath':farefilepath,'cnstrs':farecnstr}
]


def dealFileName(filename,cnstrarr):
	for cn in cnstrarr:
		filename = filename.replace(cn,'1234567')
	return filename


def dealFilePath(filePath,cnstrarr):
	filenames = os.listdir(filePath)
	print(len(filenames))
	for filename in filenames:
		newfilename = dealFileName(filename,cnstrarr)
		oldfile = os.path.join(filePath,filename)
		newfile = os.path.join(filePath,newfilename)
		os.rename(oldfile, newfile)


def main(infos):
	for info in infos:
		filepath = info['filepath']
		cnstrs = info['cnstrs']
		dealFilePath(filepath,cnstrs)


if __name__ == '__main__':
	main(renameifnos)

