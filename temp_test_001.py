#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/26 22:07
#@Author: max liu
#@File  : temp_test_001.py


import os
#a = os.popen('ip add').read()
#print(a)


os.chdir('day007/test')
print(os.getcwd())

for root ,dirs, files in os.walk('.',topdown=False):
    for key_wd_file in files:
        file_path = os.path.join(root,key_wd_file)
        file_obj = open(file_path,'rb')
        if 'qytang' in str(file_obj.read()):
            print(file_path)
        file_obj.close()