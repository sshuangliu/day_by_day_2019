#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/21 11:41
# @Author: max liu
# @File  : auth_infor.py

import requests
import urllib3
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = 'admin'
password = 'admin'
ipadd = '192.168.59.90'

url_rpc = 'https://' + ipadd + '/ins'
url_rest = 'https://' + ipadd + '/api/aaaLogin.json'
data_rest = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
headers = {'content-type': 'application/json-rpc',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def rest_session():
    client = requests.session()
    client.post(url=url_rest, headers=headers, json=data_rest, verify=False)
    # print(r.request.headers)
    # print(r.headers)
    # print(r.json())
    return client  # 返回有状态话的会话


def get_token():
    post_response = requests.post(url=url_rest, headers=headers, json=data_rest, verify=False)

    # 从响应的JSON数据中提取Token的值
    auth = post_response.json()

    auth_token = auth['imdata'][0]['aaaLogin']['attributes']['token']
    # 返回Token的值
    return auth_token


if __name__ == '__main__':
    # print(rest_session())
    print(get_token())