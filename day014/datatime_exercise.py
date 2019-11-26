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

if __name__ == '__main__':
    pass
