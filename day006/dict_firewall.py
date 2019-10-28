
# 1:把防火墙状态信息表存为字典!

import re

asa_conn ='''TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'''
keys = []
values = []
# ()括号的嵌套及非捕获
asa_conn_list = asa_conn.split('\n')
print(asa_conn_list)

# 生成keys values 的list
for keys_002 in asa_conn_list:
    keys.append(re.search(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)\s\w+\s((?:\d{1,3}\.){3}\d{1,3}):(\d+)', keys_002).groups())

for values_002 in asa_conn_list:
    values.append(re.search(r'bytes (\d+), flags (\w+)', values_002).groups())

print(keys)
print(values)

# 两个list 压缩对应组合为dict
asa_dict = dict(zip(keys, values))
print('打印分析后的字典：')
print(asa_dict)

print('格式化打印输出:')

src = 'src'
src_p = 'src_p'
dst = 'dst'
dst_p = 'dst_p'
bytes_name = 'bytes'
flags = 'flags'
format_str001 = 'format_str001'
format_str002 = 'format_str002'

for key, value in asa_dict.items():
    print('{:^6}:{}|\t'.format(src, key[0]), end='')
    print('{:^6}:{:^10}|'.format(src_p, key[1]), end='')
    print('{:^6}:{:^15}|'.format(dst, key[2]), end='')
    print('{:^8}:{:^10}|'.format(dst_p, key[3]))
    print('{:^6}:{:^15}|'.format(bytes_name, value[0]), end='')
    print('{:^7}:{:^10}|'.format(flags, value[1]), end='')
    print()
    print('#' * 100)



