#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/28 19:44
#@Author: max liu
#@File  : sorted.py

#### 2: 列表作业：冒泡排序 相连两元素 前后两个数字交换

L1 = [4, 3, 7, 8, 5, 8]
# sorted排序函数
#sorted(L1, reverse=True)

L2 = L1.copy()
for i in range(len(L2)):
    for m in range(len(L2)-1-i):
        if L2[m] > L2[m+1]:
            L2[m], L2[m+1] = L2[m+1], L2[m]

print(L2)