#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/11/13 11:44
#@Author: max liu
#@File  : device_ssh_script_help.py

import paramiko


def shuang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read().decode())

if __name__ == '__main__':
    # shuang_ssh(ip='192.168.157.141', username='root', password='root123', cmd='cat /etc/redhat-release')

    from argparse import ArgumentParser

    usage_001 = 'python3 device_ssh_script_help.py -i ipadd -u username -p password -c cmdlist'
    parser = ArgumentParser(usage=usage_001)
    parser.add_argument('-i', '--ipadd', dest='ipadd', help='connect to devices', default='1.1.1.1', type=str)
    parser.add_argument('-u', '--username', dest='username', help='devices username', default='ro', type=str)
    parser.add_argument('-pwd', '--password', dest='password', help='devices password', default='ro', type=str)
    parser.add_argument('-p', '--port', dest='port', help='device connect port', default=22, type=int)
    parser.add_argument('-c', '--cmd', dest='cmd', help='device exed cmd', default='cat /etc/redhat-release', type=str)
    # parser.add_argument(nargs='?', dest='cmd_list', help='device exed cmd_list', default='ls', type=str)  # 位置参数 可以输入0个或一个参数 配合函数使用
    # parser.add_argument(nargs='*', dest='cmd_list', help='device exed cmd_list', default='ls pwd', type=str)  # 位置参数 可以输入0个或多个参数 配合函数使用

    args = parser.parse_args()
    shuang_ssh(args.ipadd, args.username, args.password, args.port, args.cmd)
    # shuang_ssh(args.ipadd, args.username, args.password, args.port, args.cmd_list)
