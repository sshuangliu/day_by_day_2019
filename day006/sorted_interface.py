#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/28 19:47
# @Author: max liu
# @File  : sorted_interface.py


# 1:接口排序

import re

port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34',
             'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

new_port_list = sorted(port_list, key=lambda x: (
    int(re.findall(r'\d{1,3}', x)[0]), int(re.findall(r'\d{1,3}', x)[1]), int(re.findall(r'\d{1,3}', x)[2]),
    int(re.findall(r'\d{1,3}', x)[3])))
print(new_port_list)
