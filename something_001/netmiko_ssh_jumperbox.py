# -*- coding: utf-8 -*-

import netmiko
import time
import logging

#日志记录
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#from netmiko import ConnectHandler


#跳板机登陆实例：
jumperbox = {
    "device_type":"linux",
    'host':'192.168.1.1',
    'username' : 'admin',
    'password' : 'admin',}

net_connect = netmiko.ConnectHandler(**jumperbox)
print ("SSH prompt: {}".format(net_connect.find_prompt()))
net_connect.write_channel("ssh -l admin 10.2.2.2\n") #### or a ssh 10.30.1.11
time.sleep(6)
output = net_connect.read_channel()
print(output)
if 'ssword' in output:
    net_connect.write_channel('admin\n')
output = net_connect.read_channel()

# Verify you logged in successfully
print(output)
time.sleep(1)
netmiko.redispatch(net_connect,device_type="huawei")
output2 = net_connect.send_command('dis ver')
print(output2)
config_commands = ['interface 10GE1/0/36',
                   'description netmiki_test',
                    'commit',
                  ]
output3 = net_connect.send_config_set(config_commands)
print(output3)



