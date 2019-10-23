
# 正则表达式测试 1
# 字符串为MAC地址表内容: '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
#
# 使用正则表达式匹配，并且格式化打印后结果:
import re
mac_add_table = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
obj_001 = re.match(r'^(\d+)\s+([0-9a-f]{4}.[0-9a-f]{4}.[0-9a-f]{4})\s+([A-Z]+)\s+(.*)', mac_add_table)
tuple_001 = obj_001.groups()
print(tuple_001)
print('{0:<10}:{1}'.format('VLAN ID', obj_001.group(1)))
print('{0:<10}:{1}'.format('MAC', obj_001.group(2)))
print('{0:<10}:{1}'.format('Type', obj_001.group(3)))
print('{0:<10}:{1}'.format('Interface', obj_001.group(4)))



# 正则表达式测试 2
# 字符串为ASA防火墙show conn（查看连接内容):
# 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# 使用正则表达式匹配，并且格式化打印后结果:

firewall_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
obj_002 = re.match(r'^(\w+)\s+[a-z]+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+)\s+[a-z]+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+),\s+[a-z]+\s+([0-9:]+),\s+[a-z]+\s+(\d+),\s+\w+\s+(.*)', firewall_conn)
# obj_002 = re.match(r'^(.*)\s+.*\s+(.*)\s+.*\s+(.*),\s+.*\s+(.*),\s+.*\s+(.*),\s+.*\s+(.*)', firewall_conn)
tuple_002 = obj_002.groups()
time_001 = re.match(r'^(\d+):(\d+):(\d+)', tuple_002[3]).groups()
print(tuple_002)
print(time_001)

print('{0:<20}:{1}'.format('protocol', obj_002.group(1)))
print('{0:<20}:{1}'.format('server', obj_002.group(2)))
print('{0:<20}:{1}'.format('localserver', obj_002.group(3)))
print('{0:<20}:{1[0]} 小时 {1[1]}分钟 {1[2]}秒'.format('idle', time_001))
print('{0:<20}:{1}'.format('bytes', obj_002.group(5)))
print('{0:<20}:{1}'.format('flags', obj_002.group(6)))
