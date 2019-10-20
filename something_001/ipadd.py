# -*- coding: utf-8 -*-

# 转换输入ip信息到整数

def ipv4_to_int(ipv4):
    ipv4 = [int(x) for x in ipv4.split('.')]
    ipv4_int = (ipv4[0]<<24)+(ipv4[1]<<16)+(ipv4[2]<<8)+ipv4[3]
    return ipv4_int

def int_to_ipv4(ipv4_int):
    ipv4 = []
    for x in (24,16,8,0):
        ipv4.append(str(ipv4_int >> x & 0xFF))
    return '.'.join(ipv4)

start_ip = '10.1.1.252'

for x in range(4):
    new_ip = ipv4_to_int(start_ip)+x*2
    print(new_ip)
    new_ip = int_to_ipv4(new_ip)
    print(new_ip)
    print('interface 100GE2/0/%s' %(x+1))
    print('undo portswitch')
    print('ip address %s 255.255.255.254' %new_ip)
    print('undo shutdown')
    print()