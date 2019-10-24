import re

ens160 = '''flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
              inet 172.16.66.166 netmask 255.255.255.0 broadcast 172.16.66.255
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link>
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet)
              RX packets 174598769 bytes 1795658527217 (1.6 TiB)
              RX errors 1 dropped 24662 overruns 0 frame 0
              TX packets 51706604 bytes 41788673420 (38.9 GiB)
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0   
                  '''
# 字符串重复---小括号
# ?: 非捕获分组
# ?<= 非捕获 匹配后面表达式 且该字符串前面字符匹配前面匹配表达式
pattern1 = re.compile(r'(?<=inet\s)\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')
pattern2 = re.compile(r'(?<=netmask\s)\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')
pattern3 = re.compile(r'(?<=broadcast\s)\b(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')
pattern4 = re.compile(r'(?<=ether\s)\b(?:[0-9a-f]{2}:){5}(?:[0-9a-f]{2})\b')

ipv4add = pattern1.findall(ens160)[0]
netmask = pattern2.findall(ens160)[0]
broadcast = pattern3.findall(ens160)[0]
macadd = pattern4.findall(ens160)[0]

print(ipv4add)
print(netmask)
print(broadcast)
print(macadd)
