#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/8 18:57
# @Author: max liu
# @File  : configure_router_ssh.py

import paramiko
import time


def configure_router(hostname=None, username=None, password=None, enable='', wait_time=2, verbose=True, cmd_list=None):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username=username, password=password)

    print("login to ", hostname, end='')
    cmd = ssh_client.invoke_shell()
    time.sleep(wait_time)
    if '>' in cmd.recv(65535).decode():
        # print(cmd.recv(65535).decode())  buffe 读取或调用一次就为空，不可重复，否则卡住等待新buffer内容
        if enable == '':
            enable = input('please input enable password:')
        cmd.send('enable' + '\n')
        cmd.send(enable + '\n')
    for i in cmd_list:
        cmd.send(i + '\n')
        time.sleep(1)
    if verbose:
        time.sleep(1)
        output = cmd.recv(65535).decode()
        print(output)
    ssh_client.close()


if __name__ == '__main__':
    cmd_list_001 = ['terminal length 0', 'show version', 'config t', 'router ospf 1', 'network 1.1.1.1 0.0.0.0 area 0']
    configure_router(hostname='192.168.59.132', username='cisco1', password='cisco1', cmd_list=cmd_list_001)
