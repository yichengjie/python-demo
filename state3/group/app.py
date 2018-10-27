#!usr/bin/python
# -*- coding:utf-8 -*-
# iconv -f GB2312 -t UTF-8 group2.xml > group3.xml
# find *.xml -exec sh -c "iconv -f GBK -t UTF8 {} > {}.xml" \;
import os
from muti_xml import GroupMutiXmlStatistic

#  group文件路径
def main():
	#  xml文件基础路径
	basedir = r'./data' 
	#  groups解析类
	s = GroupMutiXmlStatistic(basedir)
	#  解析xml数据
	s.parse()
	#  打印解析完成的数据
	s.print()

#  调用程序
main()





