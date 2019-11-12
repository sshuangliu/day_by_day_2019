#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/11/12 20:29
#@Author: max liu
#@File  : datatime_exercise.py

from datetime import datetime,timedelta,timezone,date

file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_context = str((datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S.%f')).encode()
with open(file_name+'.txt', 'wb+') as f:
    f.write(file_context)





if __name__ == '__main__':
    pass