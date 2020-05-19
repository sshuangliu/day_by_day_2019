#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/3/9 21:33
# @Author: max liu
# @File  : xmlRPC_server.py

# https://www.jianshu.com/p/9987913cf734

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


def sum1(a, b):
    return a + b


def add1(x, y):
    return x + y


if __name__ == '__main__':
    server = ThreadXMLRPCServer(('localhost', 8888))
    server.register_function(sum1, "sum")  # 注册函数1
    server.register_function(add1, 'add')  # 注册函数2
    print("Listening for Client")
    server.serve_forever()  # 保持等待调用状态
