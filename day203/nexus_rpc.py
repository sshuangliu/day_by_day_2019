#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/20 19:57
# @Author: max liu
# @File  : nexus_rpc.py
from requests.auth import HTTPBasicAuth

from day203.auth_infor import username, password, url_rpc, headers
import requests
from pprint import pprint


def json_config(*cmd_list):  # 可变参数
    # print(cmd_list)
    json_data = []
    id = 1
    for cmd in cmd_list:
        json_data.append(
            {
                "jsonrpc": "2.0",
                "method": "cli",
                "params": {
                    "cmd": cmd,
                    "version": 1
                },
                "id": id
            }
        )
        id += 1
    # print(json_data)
    return json_data


def post_config(*cmd_list):
    # print(cmd_list)
    data = json_config(*cmd_list)
    client = requests.session()
    r = client.post(url=url_rpc, json=data, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    return r.json(), r.status_code


if __name__ == '__main__':
    cmd_list = ['vlan 2', 'name t1', 'show vlan', 'show ip route']
    # pprint(post_config(*cmd_list), indent=4)
    results = \
        post_config(*cmd_list)[0][3]['result']['body']['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf'][
            'TABLE_prefix'][
            'ROW_prefix']
    print('%-20s%-20s%-20s%-20s' % ('ipprefix', 'ipnexthop', 'ifname', 'clientname'))  # 左对齐
    for item in results:
        # print(type(item["ucast-nhops"]))
        if item["ucast-nhops"] == 1:  # 当某条前缀有负载路径时，数据格式不同
            ipprefix = item["ipprefix"]
            ipnexthop = item["TABLE_path"]["ROW_path"]["ipnexthop"]
            ifname = item["TABLE_path"]["ROW_path"]["ifname"]
            clientname = item["TABLE_path"]["ROW_path"]["clientname"]
        else:
            ipprefix = item["ipprefix"]
            ipnexthop = item["TABLE_path"]["ROW_path"][0]["ipnexthop"]
            ifname = item["TABLE_path"]["ROW_path"][0]["ifname"]
            clientname = item["TABLE_path"]["ROW_path"][0]["clientname"]

        print('%-20s%-20s%-20s%-20s' % (ipprefix, ipnexthop, ifname, clientname))
