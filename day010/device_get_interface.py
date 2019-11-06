#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/6 18:28
# @Author: max liu
# @File  : device_get_interface.py

import re
import pprint
from day010 import device_ping
from day010 import device_ssh

# print = pprint.pprint


def device_get_interface(*ipadd, username=None, password=None, cmd_001=None):
    dict_001 = {}
    device_if_dict = {}
    for ip in ipadd:
        if device_ping.ping_pro(ip):
            device_ssh_infor = device_ssh.shuang_ssh(ip, username, password, cmd=cmd_001)
            print(device_ssh_infor)
            for i in device_ssh_infor.strip().split('\n')[1:]:
                values_001 = re.findall(r'(.*?)\s+', i.strip())
                print(values_001)
                dict_001[values_001[0]] = values_001[1]
            device_if_dict[ip] = dict_001
        else:
            device_if_dict[ip] = {}
    return device_if_dict


if __name__ == '__main__':
    ipadd_list = ['192.168.59.130', '192.168.59.131', '192.168.59.132']
    pprint.pprint(device_get_interface(*ipadd_list, username='cisco', password='Cisc0123', cmd_001='show ip int bri'), indent=4)
