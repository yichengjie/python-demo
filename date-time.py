#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import calendar

ticks = time.time()
print("当前时间戳为 : ", ticks)
# localtime = time.localtime(time.time())
# print("本地时间为 : ", localtime)
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 : ", localtime)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


cal = calendar.month(2016,1)
print("以下输出2016年1月份的日历: ")
print(cal)