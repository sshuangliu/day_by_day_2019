## snmpwalk snmpget 安装 使用
~~~
yum install -y net-snmp-perl net-snmp-utils
~~~

## 针对一个OID探测: snmpget
~~~
[root@linux-node2 ~]# snmpget -v2c -c admin 192.168.56.12 .1.3.6.1.4.1.2021.10.1.3.1   
UCD-SNMP-MIB::laLoad.1 = STRING: 0.03   # 获取到1分钟的系统负载
~~~
### 针对一组OID探测：snmpwalk
~~~
[root@linux-node2 ~]# snmpwalk -v2c -c admin 192.168.56.12 .1.3.6.1.4.1.2021.10.1.3   # 获取到1，5，15分钟的系统负载
UCD-SNMP-MIB::laLoad.1 = STRING: 0.00
UCD-SNMP-MIB::laLoad.2 = STRING: 0.01
UCD-SNMP-MIB::laLoad.3 = STRING: 0.05
~~~
