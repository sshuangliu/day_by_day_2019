# -*- coding: utf-8 -*-
import netmiko
import time
import logging

#日志记录
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

CE6810 = {
    "device_type":"huawei_vrpv8",
    'host':'10.191.147.190',
    'username': 'uCDrw',
    'password': 'uCDrw@ucloud.cn',
    'global_delay_factor': 2,
}
net_connect = netmiko.ConnectHandler(**CE6810)
print ("SSH prompt: {}".format(net_connect.find_prompt()))

with open('interface .conf') as f:
    lines = f.read().split('/n')
lines_001 = lines.append('commit')
print(lines_001)
output5 = net_connect.send_config_set(lines)
print(output5)
