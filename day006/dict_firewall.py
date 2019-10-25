
import re

asa_conn = '''TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
              TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO
            '''
keys = []
values = []
# ()括号的嵌套及非捕获
keys_001 = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}:\d+\s\w+\s(?:\d{1,3}\.){3}\d{1,3}:\d+', asa_conn)
values_001 = re.findall(r'bytes \d+, flags \w+', asa_conn)
print(keys_001)
print(values_001)

# 生成keys values 的list
for keys_002 in keys_001:
    keys.append(re.match(r'((?:\d{1,3}\.){3}\d{1,3}):(\d+)\s\w+\s((?:\d{1,3}\.){3}\d{1,3}):(\d+)', keys_002).groups())

for values_002 in values_001:
    values.append(re.match(r'bytes (\d+), flags (\w+)', values_002).groups())

print(keys)
print(values)

# 两个list 压缩对应组合为dict
print(dict(zip(keys, values)))
