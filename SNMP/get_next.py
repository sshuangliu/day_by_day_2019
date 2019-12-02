#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/1 17:55
#@Author: max liu
#@File  : get_next.py

from pysnmp.entity.rfc3413.oneliner import cmdgen

#  类似snmpwalk,如果给定的OID不是主节点，是唯一节点，则会自动调用snmpget
def snmpv2_getnext(ip, community, oid, port=161):
    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorindex, varBindTable = cmdGen.nextCmd(
        cmdgen.CommunityData(community),  # 设置community
        cmdgen.UdpTransportTarget((ip, port)),  # 设置IP地址和端口号
        oid,  # 设置OID
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )

    result = []
    # varBindTable是个list，元素的个数可能有好多个。它的元素也是list，这个list里的元素是ObjectType，个数只有1个。
    for varBindTableRow in varBindTable:
        for item in varBindTableRow:
            result.append((item.prettyPrint().split("=")[0].strip(), item.prettyPrint().split("=")[1].strip()))
    return result


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    # 1.3.6.1.2.1.2.2 接口所有信息，包含为接口分配的索引号，与后面接口其他属性（出入带宽等）对应
    # IF-MIB::ifIndex.1 = INTEGER: 1
    # IF-MIB::ifIndex.2 = INTEGER: 2
    # IF-MIB::ifIndex.3 = INTEGER: 3
    # IF-MIB::ifIndex.4 = INTEGER: 4
    # IF-MIB::ifIndex.5 = INTEGER: 5
    # IF-MIB::ifIndex.6 = INTEGER: 6

    # 显示接口描述信息，查询ifDescr oid为：1.3.6.1.2.1.2.2.1.2，接口类oid加上接口索引即为具体接口描述oid
    # IF-MIB::ifDescr.1 = STRING: GigabitEthernet5
    # IF-MIB::ifDescr.2 = STRING: GigabitEthernet6
    # IF-MIB::ifDescr.3 = STRING: GigabitEthernet7
    # IF-MIB::ifDescr.4 = STRING: GigabitEthernet8
    # IF-MIB::ifDescr.5 = STRING: VoIP-Null0
    # IF-MIB::ifDescr.6 = STRING: Null0
    print(snmpv2_getnext("192.168.59.140", "public", "1.3.6.1.2.1.2.2.1.2", port=161))
    for x, y in snmpv2_getnext("192.168.59.140", "public", "1.3.6.1.2.1.2.2.1.2", port=161):
        print(x, y)
    # 接口速率
    print(snmpv2_getnext("192.168.59.140", "public", "1.3.6.1.2.1.2.2.1.5", port=161))

    # 进接口字节数
    print(snmpv2_getnext("192.168.59.140", "public", "1.3.6.1.2.1.2.2.1.10", port=161))

    # 出接口字节数
    print(snmpv2_getnext("192.168.59.140", "public", "1.3.6.1.2.1.2.2.1.16", port=161))