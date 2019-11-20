#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/15 21:45
# @Author: max liu
# @File  : IP_sorted.py


from socket import inet_aton
import struct
import ipaddress

#  https://docs.python.org/zh-cn/3/howto/ipaddress.html 神库

IP_LIST = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23',
           ]


def sort_ip(ips):
    # inet_aton(ip) 转换IP到直接字符串
    # >>> inet_aton("172.16.1.1")
    # b'\xac\x10\x01\x01'
    # 了解struct https://docs.python.org/zh-cn/3.8/library/struct.html  按照一定的格式编码字符串：

    # >> > from struct import *
    # >> > pack('hhl', 1, 2, 3)
    # b'\x00\x01\x00\x02\x00\x00\x00\x03'
    # >> > unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
    # (1, 2, 3)
    # >> > calcsize('hhl')
    # 8

    # struct.unpack("!L", inet_aton(ip))[0] 把直接字符串转换为整数
    # >>> struct.unpack("!L", inet_aton("172.16.1.1"))
    # (2886729985,)
    # >>> struct.unpack("!L", inet_aton("172.16.1.1"))[0]
    # 2886729985
    # 根据整数排序,然后返回排序后的ips列表
    # return sorted(ips, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
    return sorted(ips, key=lambda ip: ipaddress.ip_address(ip))  # ipadd 对象可以直接比较大小 也可以直接加减运算


if __name__ == "__main__":
    print(sort_ip(IP_LIST))


