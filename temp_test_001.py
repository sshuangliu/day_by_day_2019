#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/26 22:07
#@Author: max liu
#@File  : temp_test_001.py


import re

port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34',
             'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']


par = re.match(r'eth \d{1,3}/\d{1,3}/\d{1,3}/(\d{1,3})', port_list[0]).group(1)
print(par)
