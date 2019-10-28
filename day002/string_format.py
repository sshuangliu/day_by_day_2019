#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

##4:完成课堂作业(1)
#补齐被删除的代码
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'shuang_liu'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

line1 = ('Department1 name:%s  Manager:%s       COURSE FEES:%.2f The End!'%(department1,depart1_m,COURSE_FEES_SEC))
line2 = ('Department2 name:%s    Manager:%s    COURSE FEES:%.2f   The End!'%(department2,depart2_m,COURSE_FEES_Python))
# infor = {
# 'department1' : 'Security',
# 'department2' : 'Python',
# 'depart1_m' : 'cq_bomb',
# 'depart2_m' : 'shuang_liu',
# 'COURSE_FEES_SEC' : 456789.123456,
# 'COURSE_FEES_Python' : 1234.3456,
# }
#line1 = ('Department1 name:{department1}  Manager:{depart1_m}       COURSE FEES:{COURSE_FEES_SEC:.2f} The End!'.format(**infor))
#line2 = ('Department2 name:{department2}    Manager:{depart2_m}    COURSE FEES:{COURSE_FEES_Python:.2f}   The End!'.format(**infor))

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)



##5:完成课堂作业(2)
#RE匹配IP地址，并格式化打印结果
# re.match(r'^(\w+-\w+\.\d+)\s+((?:\d{1,3}\.){3}\d{1,3})\s+\w+\s+\w+\s+(\w+)$', str1).groups()
str1 = 'Port-channel1.189    192.168.189.254    YES    CONFIG    UP'
str2 = str1.split(' ')
print(str2)
print()

while True:
    if str2.count(''):
        str2.remove('')
    else:
        break
print(str2)
print('接口\t\t:{0[0]}\nip地址\t\t:{0[1]}\n状态\t\t:{0[2]}'.format(str2))