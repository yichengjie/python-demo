#!usr/bin/python
# -*- coding:utf-8 -*-
# iconv -f GB2312 -t UTF-8 group2.xml > group3.xml
# find *.xml -exec sh -c "iconv -f GBK -t UTF8 {} > {}.xml" \;
import os
from muti_xml import GroupMutiXmlStatistic
from single_xml import GroupSingleXmlStatistic
import sys

#  group文件路径
def mainMuti():
	#  xml文件基础路径
	basedir = r'./data' 
	#  groups解析类
	s = GroupMutiXmlStatistic(basedir)
	#  解析xml数据
	s.parse()
	#  打印解析完成的数据
	s.print()

def mainSingle():
	filepath = r'./data/20180508_CA_BJS_yicj_265214_GroupImport.xml'
	groupSingleXmlStatistic = GroupSingleXmlStatistic(filepath)
	groupSingleXmlStatistic.parse()
	groupSingleXmlStatistic.print()


def main():
	 args = sys.argv
	 argLen = len(args)
	 if argLen == 2:
	 	s = args[1]
	 	if s == 'single':
	 		mainSingle()
	 		return
	 mainMuti()

#  调用程序
if __name__=='__main__':
    main()






