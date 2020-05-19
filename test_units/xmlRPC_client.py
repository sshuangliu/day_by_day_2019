#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 21:36
# @Author: max liu
# @File  : xmlRPC_client.py

from xmlrpc.client import ServerProxy

if __name__ == '__main__':
    server = ServerProxy("http://localhost:8888")
    print(server.sum(1, 2))  # 调用函数1并传参
    print(server.add(2, 2))  # 调用函数2并传参
