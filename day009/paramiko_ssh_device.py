#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/4 18:03
# @Author: max liu
# @File  : paramiko_ssh_device.py

# 1:安装paramiko,并创建SSH登录设备执行命令的函数

import paramiko


def shuang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    # print(stdout.read().decode())
    return stdout.read().decode()

if __name__ == '__main__':
    print(shuang_ssh(ip='192.168.157.37', username='root', password='root123', cmd='cat /etc/redhat-release'))
