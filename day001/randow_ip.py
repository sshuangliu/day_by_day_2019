#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-10-20 20:13
#@Author: max liu
#@File  : randow_ip.py

import random

['%s' % random.randint(0, 255) for i in range(4)]
# ['100', '151', '70', '103']
a='.'.join('%s'%random.randint(0, 255) for i in range(4)) # join 接一个可迭代的对象
print(a)


