#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/8 11:34
# @Author: max liu
# @File  : device_ssh_get_config.py


import paramiko



class Device_ssh_001(object):

    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    def ssh_get_config(self, cmd='show run'):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.ip, username=self.username, password=self.password, port=self.port)
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        return stdout.read().decode()


if __name__ == '__main__':
    shuang_ssh = Device_ssh_001(ip='192.168.59.132', username='cisco', password='Cisc0123')
    print(shuang_ssh.ssh_get_config())
