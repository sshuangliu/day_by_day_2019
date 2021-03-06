#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/1 18:46
# @Author: max liu
# @File  : trap.py

from day101.GET_IP_netifaces import get_ip_address
from pysnmp.carrier.asynsock.dispatch import AsynsockDispatcher
from pysnmp.carrier.asynsock.dgram import udp, udp6
from pyasn1.codec.ber import decoder
from pysnmp.proto import api
from pprint import pprint


def analysis(info):
    # 分析Trap信息字典函数
    # 下面是这个大字典的键值与嵌套的小字典
    # 1.3.6.1.2.1.1.3.0 {'value': 'ObjectSyntax', 'application-wide': 'ApplicationSyntax', 'timeticks-value': '103170310'}
    # 1.3.6.1.6.3.1.1.4.1.0 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'objectID-value': '1.3.6.1.6.3.1.1.5.4'}
    # 1.3.6.1.2.1.2.2.1.1.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'integer-value': '2'}
    # 1.3.6.1.2.1.2.2.1.2.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'string-value': 'GigabitEthernet2'}
    # 1.3.6.1.2.1.2.2.1.3.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'integer-value': '6'}

    pprint(info, indent=4)  # 打印字典信息

    #  不同类型使用不同类别的oid来描述这些信息，按trap类型区别oid，相同类型trap里面的oid值相同
    if '1.3.6.1.6.3.1.1.4.1.0' in info.keys():  # link-up/down类的trap信息，此oid用来描述link状态
        if info["1.3.6.1.6.3.1.1.4.1.0"][
            'objectID-value'] == '1.3.6.1.6.3.1.1.5.4':  # link-up/down类的trap信息下，此oid用来描述link up
            print(info["1.3.6.1.2.1.2.2.1.2.2"]['string-value'], "UP")  # link-up/down类的trap信息下，此oid用来描述link description
        elif info["1.3.6.1.6.3.1.1.4.1.0"][
            'objectID-value'] == '1.3.6.1.6.3.1.1.5.3':  # link-up/down类的trap信息下，此oid用来描述link down
            print(info["1.3.6.1.2.1.2.2.1.2.2"]['string-value'], "Down")

    # http://cric.grenoble.cnrs.fr/Administrateurs/Outils/MIBS/?oid=1.3.6.1.2.1.14.10.1
    # 此为ospf邻居由down到up的变化信息的oid
    ospfNbrState_dict = {'1': 'down', '2': 'attempt', '3': 'init', '4': '2-way', '5': 'exchangeStart', '6': 'exchange',
                         '7': 'loading', '8': 'full'}
    if '1.3.6.1.2.1.14.10.1.6' in info.keys():
        if info['1.3.6.1.2.1.14.10.1.6']['integer-value'] != '8':
            ospfNbrIpAddr = info['1.3.6.1.2.1.14.10.1.1']['ipAddress-value']
            ospfNbrRtrId = info['1.3.6.1.2.1.14.10.1.3']['ipAddress-value']
            ospfRouterId = info['1.3.6.1.2.1.14.1.1']['ipAddress-value']
            ospfNbrState = ospfNbrState_dict[info['1.3.6.1.2.1.14.10.1.6']['integer-value']]
            print(
                f'{ospfRouterId} neighbor change:ospfNbrIpAddr:{ospfNbrIpAddr} ospfNbrRtrId:{ospfNbrRtrId} ospfNbrState:{ospfNbrState}')


def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):  # 处理Trap信息的函数
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))  # 提取版本信息
        if msgVer in api.protoModules:  # 如果版本兼容
            pMod = api.protoModules[msgVer]
        else:  # 如果版本不兼容，就打印错误
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),  # 对信息进行解码

        )
        print('Notification message from %s:%s: ' % (
            transportDomain, transportAddress  # 打印发送TRAP的源信息
        )
              )
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:  # SNMPv1的特殊处理方法,可以提取更加详细的信息
                print('Enterprise: %s' % (
                    pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                )
                      )
                print('Agent Address: %s' % (
                    pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                )
                      )
                print('Generic Trap: %s' % (
                    pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                )
                      )
                print('Specific Trap: %s' % (
                    pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                )
                      )
                print('Uptime: %s' % (
                    pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                )
                      )
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:  # SNMPv2c的处理方法
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)

            result_dict = {}  # 每一个Trap信息,都会整理返回一个字典
            # 下面是这个大字典的键值与嵌套的小字典
            # 1.3.6.1.2.1.1.3.0 {'value': 'ObjectSyntax', 'application-wide': 'ApplicationSyntax', 'timeticks-value': '103170310'}
            # 1.3.6.1.6.3.1.1.4.1.0 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'objectID-value': '1.3.6.1.6.3.1.1.5.4'}
            # 1.3.6.1.2.1.2.2.1.1.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'integer-value': '2'}
            # 1.3.6.1.2.1.2.2.1.2.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'string-value': 'GigabitEthernet2'}
            # 1.3.6.1.2.1.2.2.1.3.2 {'value': 'ObjectSyntax', 'simple': 'SimpleSyntax', 'integer-value': '6'}
            for x in varBinds:  # 打印详细Trap信息
                result = {}
                for x, y in x.items():
                    # print(x, y.prettyPrint())  # 最原始信息打印
                    # 处理信息到字典
                    if x == "name":
                        id = y.prettyPrint()  # 把name写入字典的键
                    else:
                        bind_v = [x.strip() for x in y.prettyPrint().split(":")]
                        for v in bind_v:
                            if v == '_BindValue':
                                next
                            else:
                                result[v.split('=')[0]] = v.split('=')[1]
                result_dict[id] = result
            # 把字典传到分析模块进行分析
            analysis(result_dict)

    return wholeMsg


def snmp_trap_receiver(ifname, port=162):
    if_ip = get_ip_address(ifname)
    transportDispatcher = AsynsockDispatcher()  # 创建实例

    transportDispatcher.registerRecvCbFun(cbFun)  # 调用处理Trap信息的函数

    # UDP/IPv4
    transportDispatcher.registerTransport(
        udp.domainName, udp.UdpSocketTransport().openServerMode((if_ip, port))  # 绑定到本地地址与UDP/162号端口
    )

    transportDispatcher.jobStarted(1)  # 开始工作
    print("SNMP Trap Receiver Started!!!")
    try:
        # Dispatcher will never finish as job#1 never reaches zero
        transportDispatcher.runDispatcher()  # 运行
    except:
        transportDispatcher.closeDispatcher()
        raise


if __name__ == "__main__":
    # 使用Linux解释器 & WIN解释器
    snmp_trap_receiver("ens37")
