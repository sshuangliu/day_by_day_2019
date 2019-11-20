#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-11-19 22:40
#@Author: max liu
#@File  : socket_udp_server.py


import struct
import socket


def udp_server(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((ip,port))
    print('udp server done')
    data, add = s.recvfrom(1024)







if __name__ == '__main__':
    pass
    