#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/26 22:07
#@Author: max liu
#@File  : temp_test_001.py


import os
#a = os.popen('ip add').read()
#print(a)


#os.chdir('day007/test')
print(os.getcwd())

port_infor = os.popen('netstat -ano|findstr "80"').read().split('\n')

for i in port_infor:
    print(i)

# 测试
# 测试2
