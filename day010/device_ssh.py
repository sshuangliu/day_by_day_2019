#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/6 18:29
# @Author: max liu
# @File  : device_ssh.py

import paramiko


def shuang_ssh(ip, username, password, port=22, cmd=None):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    return stdout.read().decode()


if __name__ == '__main__':
    print(shuang_ssh(ip='192.168.157.141', username='root', password='root123', cmd='cat /etc/redhat-release'))
    print(shuang_ssh(ip='192.168.157.141', username='root', password='root123', cmd='ip add'))
    print(shuang_ssh(ip='192.168.59.131', username='cisco', password='Cisc0123', cmd='show ip int bri'))
