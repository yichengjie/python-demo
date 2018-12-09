#!/usr/bin/python
#-*- coding:utf-8 -*-
from ftplib import FTP

def ftpconnect(host,username,password):
	ftp = FTP()
	# ftp.set_debuglevel(2)
	ftp.connect(host,21)
	ftp.login(username,password)
	return ftp

# 从ftp下载文件
'''def downloadfile(ftp,remotepath,localpath):
	bufsize = 1024
	fp = open(localpath,'wb')
	ftp.retrbinary('RETR ' + remotepath , fp.write,bufsize)
	ftp.set_debuglevel(0)
	ft.close()'''


# 从本地上传文件
'''def uploadfile(ftp,remotepath,localpath):
	bufsize = 1024
	fp = open(localpath,'rb')
	ftp.storbinary('STOR ' + remotepath , fp,bufsize)
	ftp.set_debuglevel(0)
	fp.close()'''
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
	ftp = ftpconnect("192.168.99.128","yicj","123")
	#lst = ftp.getdirs()  # 返回目录下文件夹和文件列表
	#lst = ftp.cwd("/")
	#print(lst)
	#uploadfile(ftp,'/home/yicj/ftp','/Users/yicj/Desktop/mianshi.txt')
	uploadfile(ftp,'./','/Users/yicj/Desktop/mianshi.txt')
	ftp.quit()

