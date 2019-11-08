#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/8 11:35
# @Author: max liu
# @File  : device_config_comparison.py

import re
import hashlib
import time
from day011.device_ssh_get_config import Device_ssh_001


class Config_comparison(Device_ssh_001):

    # def __init__(self, ip, username, password, cmd='show run'):  # dis cur
    #     super().__init__(ip, username, password)
    #     self.cmd = cmd

    def monitor_config_change(self):
        m = hashlib.md5()
        cisco_return_values = re.search(r'hostname(.*)end', Device_ssh_001.ssh_get_config(self), re.DOTALL).group(1)
        m.update(cisco_return_values.encode('utf-8'))
        cisco_md5_init_values = m.hexdigest()

        while True:
            m = hashlib.md5()
            cisco_return_values = re.search(r'hostname(.*)end', Device_ssh_001.ssh_get_config(self), re.DOTALL).group(1)
            m.update(cisco_return_values.encode())
            cisco_md5_values = m.hexdigest()
            if cisco_md5_init_values == cisco_md5_values:
                print(cisco_md5_values)
                cisco_md5_init_values = cisco_md5_values
                time.sleep(5)
            else:
                print(cisco_md5_values)
                print('MD5 values change')
                break


if __name__ == '__main__':
    test_change = Config_comparison(ip='192.168.59.132', username='cisco', password='Cisc0123')
    # print(test_change.ssh_get_config())
    test_change.monitor_config_change()
