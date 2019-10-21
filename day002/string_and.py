#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-10-21 08:59
#@Author: max liu
#@File  : string_and.py

##1:字符串拼接
a='QYTANG\'day'
b=' 2014-9-28'
print(a+b)


##2:通过切片创建子字符串
word = " scallywag"
sub_word_begin_index = word.find('allydd')
print(sub_word_begin_index)
if word.find('ally')!=-1: ##如果包含返回开始的索引值，否则返回-1
    sub_word_begin_index = word.find('ally') ##获取sub_word 在word中的初始索引值
    sub_word = word[sub_word_begin_index:sub_word_begin_index+len('ally')] ##sub_word在word中的索引区间
    print(sub_word)
else:
    print('None')

##3:创造自己的语言 我们将在英语的基础上创建自己的语言：在单词的最后加上-，
# 然后将单词的第一个字母拿出来放到单词的最后，然后在单词的最后加上y，例如，Python，就变成了ython-Py
init_str = 'Python'
init_str_01 = init_str+'-'
init_str_02 = init_str_01[1:]+init_str_01[0]
init_str_03 = init_str_02+'y'
print(init_str_03)

##4:完成课堂作业(1)
#补齐被删除的代码
department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'shuang_liu'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456



