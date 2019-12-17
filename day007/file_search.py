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
maxliu1 = open('maxliu1', 'w')
maxliu1.write('test file\n')
maxliu1.write('this is maxliu\n')
maxliu1.close()

maxliu2 = open('maxliu2', 'w')
maxliu2.write('test file\n')
maxliu2.write('maxliu python\n')
maxliu2.close()

maxliu3 = open('maxliu3', 'w')
maxliu3.write('test file\n')
maxliu3.write('this is python\n')
maxliu3.close()

os.mkdir('maxliu4')
os.mkdir('maxliu5')

print(os.getcwd())
print('文件夹中包含\'maxliu\'关键字为：')

for root, dirs, files in os.walk('.', topdown=False):
    for key_wd_file in files:
        file_path = os.path.join(root, key_wd_file)
        file_obj = open(file_path, 'rb')
        if 'maxliu' in str(file_obj.read()):
            print(file_path)
        file_obj.close()

if __name__ == '__main__':
    pass
#
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#     for name in files:
#         print(os.path.join(root, name))
#     for name in dirs:
#         print(os.path.join(root, name))

os.path.exists(test_file.txt)
os.path.isfile("test-data")
os.path.isdir(x)
os.access(path, mode)
if os.access("/file/path/foo.txt", os.F_OK):
    print "Given file path is exist."

if os.access("/file/path/foo.txt", os.R_OK):
    print "File is accessible to read"

if os.access("/file/path/foo.txt", os.W_OK):
    print "File is accessible to write"

if os.access("/file/path/foo.txt", os.X_OK):
    print "File is accessible to execute"

>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

# 文件内容替换
import os
import re

# 遍历方式为以文件夹为主线遍历 root:当前遍历的文件夹绝对路径，dirs:当前遍历路径下文件夹的列表 files：当前遍历路径下文件的列表
for root, dirs, files in os.walk("D:\T1", topdown=True):
    for item in dirs:
        for root1, dirs1, files1 in os.walk(os.path.join(root, item), topdown=True):
            for i in files1:
                if '.vmx' == os.path.splitext(i)[1]:
                    with open(os.path.join(root1, i), 'r+') as f: # + 以seek（teel）位置逐行覆盖写; w/w+:先清空，慎用
                        if re.findall(r'vmci0.present = "True"', f.read(10240)):
                            f.seek(0)
                            new_data = re.sub(r'vmci0.present = "True"', 'vmci0.present = "false"', f.read(10240),
                                              count=1)
                            f.seek(0)
                            f.write(new_data)
                            print('已修改:', os.path.join(root1, i))
                        else:
                            print('无需修改:', os.path.join(root1, i))
                    break
            break
    break