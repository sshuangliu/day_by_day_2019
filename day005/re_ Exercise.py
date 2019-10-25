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

#### 2: 列表作业：冒泡排序 相连两元素 前后两个数字交换

L1 = [4, 3, 7, 8, 5, 8]
L2 = L1.copy()
for i in range(len(L2)):
    for m in range(len(L2)-1-i):
        if L2[m] > L2[m+1]:
            L2[m], L2[m+1] = L2[m+1], L2[m]

for i in range(len(L2)):
    print(L1[i], L2[i])
