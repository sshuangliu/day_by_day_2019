#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/1/10 18:23
# @Author: max liu
# @File  : download_homework.py


import requests
import urllib3
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://qytsystem.qytang.com/accounts/login/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

client = requests.session()
r = client.get(url=url, headers=headers, verify=False)
print(r.headers)
soup = BeautifulSoup(r.content, 'lxml')
csrftoken1 = soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
csrftoken2 = r
print(csrftoken1)
print(csrftoken2)

login_data = {'username': 'pye_lius', 'password': '9Hn.IOP', "csrfmiddlewaretoken": csrftoken1}
r = client.post(url=url, headers=headers, data=login_data, verify=False)
print(r.request.headers)
print(r.text)
# r = client.get(url='https://qytsystem.qytang.com/python_enhance/python_enhance_homework_a', verify=False)
# print(r.text)

if __name__ == '__main__':
    pass
