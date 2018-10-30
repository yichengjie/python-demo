#!usr/bin/python
# -*- coding:utf-8 -*-
# iconv -f GB2312 -t UTF-8 group2.xml > group3.xml
# find *.xml -exec sh -c "iconv -f GBK -t UTF8 {} > {}.xml" \;
import os
import sys
import xml.etree.ElementTree as ET

from muti_xml import InterlineParasMutiXmlStatistic

def main():
	basedir = '../data/interlineParas'
	interlineParasMutiXmlStatistic = InterlineParasMutiXmlStatistic(basedir)
	interlineParasMutiXmlStatistic.parse()
	interlineParasMutiXmlStatistic.print()

#  调用程序
if __name__=='__main__':
    main()






