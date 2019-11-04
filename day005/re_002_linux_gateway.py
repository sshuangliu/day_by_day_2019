import re
import os

#### 1: 匹配Linux路由表的网关
# infor = os.popen('route -n').read()
infor = '''

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.168.1   0.0.0.0         UG    0      0        0 eth0
169.254.0.0     0.0.0.0         255.255.0.0     U     1002   0        0 eth0
192.168.168.0   0.0.0.0         255.255.255.0   U     0      0        0 eth0

'''


# ()的嵌套 非捕获
# 定义def 多次re匹配,路由表为空的用try抛出

def re_gateway(infor01):
    route_list = re.findall(r'(?:(?:\d{1,3}\.){3}\d{1,3}\s+){3}UG', infor01)[0]
    route_list = re.findall(r'\d+\.\d+\.\d+\.\d+\s+(\d+\.\d+\.\d+\.\d+)', route_list)[0]
    return route_list


print('网关为：%s' % re_gateway(infor))


