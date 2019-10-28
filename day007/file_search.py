#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/27 13:51
# @Author: max liu
# @File  : file_search.py

import os

print(os.getcwd())
# new_path = os.path.join(os.getcwd(), 'test_001')
# os.mkdir(new_path)

os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1', 'w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()

qytang2 = open('qytang2', 'w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()

qytang3 = open('qytang3', 'w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()

os.mkdir('qytang4')
os.mkdir('qytang5')

print(os.getcwd())
print('文件夹中包含\'qytang\'关键字为：')

for root ,dirs, files in os.walk('.',topdown=False):
    for key_wd_file in files:
        file_path = os.path.join(root,key_wd_file)
        file_obj = open(file_path,'rb')
        if 'qytang' in str(file_obj.read()):
            print(file_path)
        file_obj.close()




if __name__ == '__main__':
    pass
