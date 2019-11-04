#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/4 18:38
# @Author: max liu
# @File  : paramiko_ssh_find_gateway.py


import paramiko
import re


def connect_device(ip, username, password, port=22, cmd='ls'):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    infor = stdout.read().decode()
    return infor


def re_get_gateway(gateway_001):
    for i in gateway_001.split('\n'):
        list_001 = re.findall(r'.*default via\s((?:\d{1,3}\.){3}\d{1,3})', i)
        if list_001:
            print(f'网关为:\n{list_001[0]}')


if __name__ == '__main__':
    gateway = connect_device(ip='192.168.157.141', username='root', password='root123', cmd='ip rou show')
    print(gateway)
    re_get_gateway(gateway)
