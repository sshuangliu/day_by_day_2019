#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/12 20:29
# @Author: max liu
# @File  : datatime_exercise.py

from datetime import datetime, timedelta, timezone, date

file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_context = str((datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S.%f')).encode()  # 把datetime对象转换为字符串
print(file_name)
print(file_context)

# with open(file_name+'.txt', 'wb+') as f:
#     f.write(file_context)


#  把字符串格式化为datetime对象,自动解析 包括英文日期字符串
# pip3 install python-dateutil

from dateutil import parser

strtime = str(datetime.now())
print(strtime)

print('字符串格式化为datetime对象')
i = parser.parse(strtime)
print(type(i))
print(i)
print(i.year)

#  切换时区

from datetime import timezone

tzutc_8 = timezone(timedelta(hours=8))
ctstime = datetime.now().astimezone(tzutc_8)  # 东八区时间

# 随机生成时间

import datetime, random


def randomtimes(start, end, n, frmt="%Y-%m-%d"):
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    print(stime)
    print(etime)
    return [random.random() * (etime - stime) + stime for _ in range(n)]


print(randomtimes('2018-06-01', '2018-11-01', 2))

#
import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 本地时间为 : time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10, tm_min=28, tm_sec=49, tm_wday=3, tm_yday=98, tm_isdst=0)




# 打印月历
'''
import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)
以上实例输出结果：

以下输出2016年1月份的日历:
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
'''




if __name__ == '__main__':
    pass
