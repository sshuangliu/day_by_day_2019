#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/20 21:32
#@Author: max liu
#@File  : cdp.py

from cli import *
from cisco.interface import *
import json
import re

# https://developer.cisco.com/docs/nx-os/

def getupintlist():
    # 查看接口摘要
    intflist = json.loads(clid('show interface brief'))
    i = 0
    upintflist = []
    # 通过while循环找到那些状态处于up的以太网接口
    while i < len(intflist['TABLE_interface']['ROW_interface']):
        intf = intflist['TABLE_interface']['ROW_interface'][i]
        i = i + 1
        if intf['state'] == 'up':
            if re.match('.*Ether.*', intf['interface']):
                # 把状态处于up的以太网接口的名字放入upintflist清单
                upintflist.append(intf['interface'])
    # 返回状态处于up的以太网接口名字的清单upintflist
    return upintflist


def getneiname(ifname):
    try:
        # 查询特定接口的CDP邻居信息
        neidetail = json.loads(clid('show cdp neighbors interface %s' % ifname))
        # 提取CDP邻居的device_id信息,并返回
        return neidetail['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']['device_id']
    except:
        return None


def config_description(ifname):
    # 产生接口实例
    if_config = Interface(ifname)
    # 配置接口描述
    if_config.set_description('description link to %s' % getneiname(ifname))


if __name__ == '__main__':
    # print getupintlist()
    # print(getneiname('ethernet1/3'))
    # config_description('ethernet1/1')

    up_interfaces = getupintlist()
    for x in up_interfaces:
        if getneiname(x):
            config_description(x)
