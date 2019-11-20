#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/11/20 13:47
#@Author: max liu
#@File  : socket_tcp_server.py

import pickle
from io import BytesIO
from socket import *


def Server_PIC(ip, port):
    # 创建TCP Socket, AF_INET为IPv4，SOCK_STREAM为TCP
    sockobj = socket(AF_INET, SOCK_STREAM)
    # 绑定套接字到地址，地址为（host，port）的元组
    sockobj.bind((ip, port))
    # 在拒绝连接前，操作系统可以挂起的最大连接数量，一般配置为5
    sockobj.listen(5)

    while True:  # 一直接受请求，直到ctl+c终止程序
        # 接受TCP连接，并且返回（conn,address）的元组，conn为新的套接字对象，可以用来接收和发送数据，address是连接客户端的地址
        connection, address = sockobj.accept()
        # 打印连接客户端的IP地址
        print('Server Connected by', address)
        recieved_message = b''  # 预先定义接收信息变量
        recieved_message_fragment = connection.recv(1024)  # 读取接收到的信息，写入到接收到信息分片
        while recieved_message_fragment:
            recieved_message = recieved_message + recieved_message_fragment  # 把所有接收到信息分片重组装
            recieved_message_fragment = connection.recv(1024)
        obj = pickle.loads(recieved_message)  # 把接收到信息pickle回正常的obj
        if isinstance(obj, dict):
            print("收到字典数据!!!")
            print(obj)  # 打印obj，当然也可以选择写入文件或者数据库
        elif isinstance(obj, bytes):
            myfile = open('NewLogo.jpg', 'wb')
            myfile.write(obj)
            myfile.close()
            print("收到二进制数据,并写入到文件!!!")
        connection.close()


if __name__ == '__main__':
    # 使用Linux解释器 & WIN解释器
    Server_IP = '0.0.0.0'
    Server_Port = 6666
    Server_PIC(Server_IP, Server_Port)