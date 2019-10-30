#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/10/30 23:08
# @Author: max liu
# @File  : list_same_def.py


# 2:找到两个清单中相同的内容
import operator

l1 = ['aaa', 111, (4, 5), 2.01]
l2 = ['bbb', 333, 111, 3.14, (4, 5)]


def compare_same(list1, list2):
    for i in list1:
        if i in list1 and i in list2:
            print('%s in L1 and L2' % str(i))
        else:
            print('%s  only in L1' % str(i))
    for m in list2:
        if operator.eq(i, m):
            pass
        else:
            print('%s  only in L2' % str(m))


if __name__ == '__main__':
    print(compare_same(l1, l2))
