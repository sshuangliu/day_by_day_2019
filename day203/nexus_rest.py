#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/23 12:33
# @Author: max liu
# @File  : nexus_rest.py

# 参考文档
# https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-3x/#!configuring-svis/creating-and-configuring-an-svi-interface

from day203.auth_infor import rest_session, get_token, ipadd, headers
import requests


def svi_cnofig_session(*, vlanid, adminSt='up', descr='python_test', **cmdlist):  # 可以update cmdlist字典里面的扩展字段到json date
    svi_url = f'https://{ipadd}/api/node/mo/sys/intf/svi-[{vlanid}].json'
    new_headers = headers.copy()
    new_headers['content-type'] = 'application/json'
    # mtu=None,如果json data有该属性字段 ，则值不能为none，必须明确
    data = {
        "sviIf": {
            "attributes": {
                "id": vlanid,
                "adminSt": adminSt,
                "descr": descr,
            }
        }
    }
    print(data)
    print(new_headers)
    client = rest_session()
    r = client.post(url=svi_url, json=data, headers=new_headers, verify=False)
    return r.json()


def svi_cnofig_cookie(*, vlanid, adminSt='up', descr='python_test', **cmdlist):  # 可以update cmdlist字典里面的扩展字段到json date
    svi_url = f'https://{ipadd}/api/node/mo/sys/intf/svi-[{vlanid}].json'
    new_headers = headers.copy()
    new_headers['content-type'] = 'application/json'
    new_headers['Cookie'] = "APIC-Cookie=" + get_token()
    # mtu=None,如果json data有该属性字段 ，则值不能为none，必须明确
    data = {
        "sviIf": {
            "attributes": {
                "id": vlanid,
                "adminSt": adminSt,
                "descr": descr,
            }
        }
    }
    print(data)
    r = requests.post(url=svi_url, json=data, headers=new_headers, verify=False)
    print(r.request.headers)
    return r.json()


if __name__ == '__main__':
    # print(svi_cnofig_session(vlanid='vlan998'))
    print(svi_cnofig_cookie(vlanid='vlan998', descr='python_tttttt'))
