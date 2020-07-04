#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/7/4 10:24
#@Author: max liu
#@File  : collector_v9.py

import struct
import os
import sqlite3


field_types = {
    0: 'UNKNOWN_FIELD_TYPE',  # fallback for unknown field types

    # Cisco specs for NetFlow v9
    # https://tools.ietf.org/html/rfc3954
    # https://www.cisco.com/en/US/technologies/tk648/tk362/technologies_white_paper09186a00800a3db9.html
    1: 'IN_BYTES',
    2: 'IN_PKTS',
    3: 'FLOWS',
    4: 'PROTOCOL',
    5: 'IP_TOS',  # SRC_TOS
    6: 'TCP_FLAGS',
    7: 'L4_SRC_PORT',
    8: 'IPV4_SRC_ADDR',
    9: 'SRC_MASK',
    10: 'INPUT_INTERFACE_ID',
    11: 'L4_DST_PORT',
    12: 'IPV4_DST_ADDR',
    13: 'DST_MASK',
    14: 'OUTPUT_INTERFACE_ID',
    15: 'IPV4_NEXT_HOP',
    16: 'SRC_AS',
    17: 'DST_AS',
    18: 'BGP_IPV4_NEXT_HOP',
    19: 'MUL_DST_PKTS',
    20: 'MUL_DST_BYTES',
    21: 'LAST_SWITCHED',
    22: 'FIRST_SWITCHED',
    23: 'OUT_BYTES',
    24: 'OUT_PKTS',
    25: 'MIN_PKT_LNGTH',
    26: 'MAX_PKT_LNGTH',
    27: 'IPV6_SRC_ADDR',
    28: 'IPV6_DST_ADDR',
    29: 'IPV6_SRC_MASK',
    30: 'IPV6_DST_MASK',
    31: 'IPV6_FLOW_LABEL',
    32: 'ICMP_TYPE',
    33: 'MUL_IGMP_TYPE',
    34: 'SAMPLING_INTERVAL',
    35: 'SAMPLING_ALGORITHM',
    36: 'FLOW_ACTIVE_TIMEOUT',
    37: 'FLOW_INACTIVE_TIMEOUT',
    38: 'ENGINE_TYPE',
    39: 'ENGINE_ID',
    40: 'TOTAL_BYTES_EXP',
    41: 'TOTAL_PKTS_EXP',
    42: 'TOTAL_FLOWS_EXP',
    # Cisco Connection_ID
    45010: 'CONNECTION_ID',
    # 43 vendor proprietary
    44: 'IPV4_SRC_PREFIX',
    45: 'IPV4_DST_PREFIX',
    46: 'MPLS_TOP_LABEL_TYPE',
    47: 'MPLS_TOP_LABEL_IP_ADDR',
    48: 'FLOW_SAMPLER_ID',
    49: 'FLOW_SAMPLER_MODE',
    50: 'NTERVAL',
    # 51 vendor proprietary
    52: 'MIN_TTL',
    53: 'MAX_TTL',
    54: 'IPV4_IDENT',
    55: 'DST_TOS',
    56: 'IN_SRC_MAC',
    57: 'OUT_DST_MAC',
    58: 'SRC_VLAN',
    59: 'DST_VLAN',
    60: 'IP_PROTOCOL_VERSION',
    61: 'DIRECTION',
    62: 'IPV6_NEXT_HOP',
    63: 'BPG_IPV6_NEXT_HOP',
    64: 'IPV6_OPTION_HEADERS',
    # 65-69 vendor proprietary
    70: 'MPLS_LABEL_1',
    71: 'MPLS_LABEL_2',
    72: 'MPLS_LABEL_3',
    73: 'MPLS_LABEL_4',
    74: 'MPLS_LABEL_5',
    75: 'MPLS_LABEL_6',
    76: 'MPLS_LABEL_7',
    77: 'MPLS_LABEL_8',
    78: 'MPLS_LABEL_9',
    79: 'MPLS_LABEL_10',
    80: 'IN_DST_MAC',
    81: 'OUT_SRC_MAC',
    82: 'IF_NAME',
    83: 'IF_DESC',
    84: 'SAMPLER_NAME',
    85: 'IN_PERMANENT_BYTES',
    86: 'IN_PERMANENT_PKTS',
    # 87 vendor property
    88: 'FRAGMENT_OFFSET',
    89: 'FORWARDING_STATUS',
    90: 'MPLS_PAL_RD',
    91: 'MPLS_PREFIX_LEN',  # Number of consecutive bits in the MPLS prefix length.
    92: 'SRC_TRAFFIC_INDEX',  # BGP Policy Accounting Source Traffic Index
    93: 'DST_TRAFFIC_INDEX',  # BGP Policy Accounting Destination Traffic Index
    94: 'APPLICATION_DESCRIPTION',  # Application description
    95: 'APPLICATION_TAG',  # 8 bits of engine ID, followed by n bits of classification
    96: 'APPLICATION_NAME',  # Name associated with a classification
    98: 'postipDiffServCodePoint',  # The value of a Differentiated Services Code Point (DSCP) encoded in the Differentiated Services Field, after modification
    99: 'replication_factor',  # Multicast replication factor
    100: 'DEPRECATED',  # DEPRECATED
    102: 'layer2packetSectionOffset',  # Layer 2 packet section offset. Potentially a generic offset
    103: 'layer2packetSectionSize',  # Layer 2 packet section size. Potentially a generic size
    104: 'layer2packetSectionData',  # Layer 2 packet section data

    195: 'IP_DSCP',  # for wireshark


    # 105-127 reserved for future use by Cisco

    # ASA extensions
    # https://www.cisco.com/c/en/us/td/docs/security/asa/special/netflow/guide/asa_netflow.html
    148: 'NF_F_CONN_ID',  # An identifier of a unique flow for the device
    176: 'NF_F_ICMP_TYPE',  # ICMP type value
    177: 'NF_F_ICMP_CODE',  # ICMP code value
    178: 'NF_F_ICMP_TYPE_IPV6',  # ICMP IPv6 type value
    179: 'NF_F_ICMP_CODE_IPV6',  # ICMP IPv6 code value
    225: 'NF_F_XLATE_SRC_ADDR_IPV4',  # Post NAT Source IPv4 Address
    226: 'NF_F_XLATE_DST_ADDR_IPV4',  # Post NAT Destination IPv4 Address
    227: 'NF_F_XLATE_SRC_PORT',  # Post NATT Source Transport Port
    228: 'NF_F_XLATE_DST_PORT',  # Post NATT Destination Transport Port
    281: 'NF_F_XLATE_SRC_ADDR_IPV6',  # Post NAT Source IPv6 Address
    282: 'NF_F_XLATE_DST_ADDR_IPV6',  # Post NAT Destination IPv6 Address
    233: 'NF_F_FW_EVENT',  # High-level event code
    33002: 'NF_F_FW_EXT_EVENT',  # Extended event code
    323: 'NF_F_EVENT_TIME_MSEC',  # The time that the event occurred, which comes from IPFIX
    152: 'NF_F_FLOW_CREATE_TIME_MSEC',
    231: 'NF_F_FWD_FLOW_DELTA_BYTES',  # The delta number of bytes from source to destination
    232: 'NF_F_REV_FLOW_DELTA_BYTES',  # The delta number of bytes from destination to source
    33000: 'NF_F_INGRESS_ACL_ID',  # The input ACL that permitted or denied the flow
    33001: 'NF_F_EGRESS_ACL_ID',  # The output ACL that permitted or denied a flow
    40000: 'NF_F_USERNAME',  # AAA username

    # PaloAlto PAN-OS 8.0
    # https://www.paloaltonetworks.com/documentation/80/pan-os/pan-os/monitoring/netflow-monitoring/netflow-templates
    346: 'PANOS_privateEnterpriseNumber',
    56701: 'PANOS_APPID',
    56702: 'PANOS_USERID',
}


def createdb():
    """
    创建数据库表,推荐未来改进为MongoDB
    """
    # 判断是否存在数据库,如果存在就删除
    if os.path.exists('netflow.sqlite'):
        os.remove('netflow.sqlite')

    # 连接SQLite数据库
    conn = sqlite3.connect('netflow.sqlite')
    cursor = conn.cursor()

    # 执行创建表的任务
    cursor.execute("create table netflowdb (源地址 varchar(40), 目的地址 varchar(40), 协议 int, 源端口 int, 目的端口 int, 入接口ID int, 入向字节数 int)")

    conn.commit()


def netflowdb(netflow_dict):
    """
    写入数据库,推荐未来改进为MongoDB
    """
    # 连接SQLite数据库
    conn = sqlite3.connect('netflow.sqlite')
    cursor = conn.cursor()

    # 读取Python字典数据，并逐条写入SQLite数据库
    cursor.execute("insert into netflowdb values ('%s', '%s', %d, %d, %d, %d, %d)" % (netflow_dict['IPV4_SRC_ADDR'],
                                                                                      netflow_dict['IPV4_DST_ADDR'],
                                                                                      netflow_dict['PROTOCOL'],
                                                                                      netflow_dict['L4_SRC_PORT'],
                                                                                      netflow_dict['L4_DST_PORT'],
                                                                                      netflow_dict['INPUT_INTERFACE_ID'],
                                                                                      netflow_dict['IN_BYTES']))
    # 提交数据
    conn.commit()


class IP:
    """
    读取数据,并且转换为字符串格式的IP地址
    """
    def __init__(self, data):
        self.IP_LIST = []
        self.IP_LIST.append(str(data >> 24 & 0xff))
        self.IP_LIST.append(str(data >> 16 & 0xff))
        self.IP_LIST.append(str(data >> 8 & 0xff))
        self.IP_LIST.append(str(data & 0xff))
        self.ip_addr = '.'.join(self.IP_LIST)


class DataFlowSet:
    """
    分析DataFlowSet内的字段和值
    """
    def __init__(self, data, templates):
        pack = struct.unpack('!HH', data[:4])
        # 前四个字节分别为,FlowSet ID(需要与模板ID匹配)和DataFlowSet长度
        self.template_id = pack[0]
        self.length = pack[1]
        # 初始化流列表flows为空列表
        self.flows = []

        # 略过已经分析的DataFlowSet头部
        offset = 4
        # 提取传入templates中,对应的模板(通过模板ID)
        template = templates[self.template_id]

        # v9 DataFlowSet长度必须被4字节整除,如果不够4字节边界,需要填充数据,下面在计算填充数据长度
        padding_size = 4 - (self.length % 4)  # 4 Byte

        while offset <= (self.length - padding_size):
            # 开始提取记录,初始化new_record为空字典
            new_record = {}

            for field in template.fields:  # 提取模板中的每一个字段
                # 提取字段长度
                flen = field.field_length
                # 提取字段类型
                fkey = field_types[field.field_type]
                # fdata = None

                # 截取相应的数据长度,进行分析
                dataslice = data[offset:offset+flen]

                # 对于可变长度字段下面的方法可能比struct.unpack更加有效
                fdata = 0
                # enumerate使用实例
                # >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
                # >>> list(enumerate(seasons))
                # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

                # reversed()用于反向排序

                # >>> dataslice = b'\x01\x02\x03'
                # >>> bytearray(dataslice)
                # bytearray(b'\x01\x02\x03')
                # >>> reversed(bytearray(dataslice))
                # <reversed object at 0x000001192C620438>
                # >>> enumerate(reversed(bytearray(dataslice)))
                # <enumerate object at 0x000001192C61D7E0>
                # >>> for idx, bytes in enumerate(reversed(bytearray(dataslice))):
                # ...   print(idx, bytes)
                # ...
                # 0 3
                # 1 2
                # 2 1

                # 提取数据部分,使用reversed主要是计算机字节序与网络字节序的关系
                for idx, byte in enumerate(reversed(bytearray(dataslice))):
                    fdata += byte << (idx * 8)
                if fkey == 'APPLICATION_TAG': # 前8bit是nbar engines_id,后n bit为 AppID
                    application_engines_id = fdata >> (flen*8-8)
                    application_classification_id = fdata & int(('0x'+'f'*(flen-1)), 16)
                    new_record[fkey] = [application_engines_id, application_classification_id]
                elif fkey == 'IP_TOS':  # 如果是源IP_TOS,转为为16进制的字符串
                    new_record[fkey] = hex(fdata)
                elif fkey == 'DIRECTION' and fdata == 0:  # 如果是DIRECTION,转为为DIRECTION 对应的值进制的字符串
                    new_record[fkey] = 'Ingress'
                elif fkey == 'DIRECTION' and fdata == 1:  # 如果是DIRECTION,转为为DIRECTION 对应的值进制的字符串
                    new_record[fkey] = 'Egress'
                elif fkey == 'IPV4_SRC_PREFIX':  # 如果是源IPV4_SRC_PREFIX地址,转为IPV4_SRC_PREFIX地址的字符串
                    new_record[fkey] = IP(fdata).ip_addr
                elif fkey == 'IPV4_NEXT_HOP':  # 如果是源IPV4_NEXT_HOP地址,转为IPV4_NEXT_HOP地址的字符串
                    new_record[fkey] = IP(fdata).ip_addr
                elif fkey == 'IPV4_SRC_ADDR':  # 如果是源IP地址,转为为IP地址的字符串
                    new_record[fkey] = IP(fdata).ip_addr
                elif fkey == 'IPV4_DST_ADDR':  # 如果是目的IP地址,转为为IP地址的字符串
                    new_record[fkey] = IP(fdata).ip_addr
                else:
                    new_record[fkey] = fdata

                offset += flen
            # 把提取的内容直接写入数据库,这个代码的问题是,传统数据库灵活性有限,需要固定字段,推荐使用MongoDB
            # 由于本次试验数据源仅仅来自于一个路由器,所以并没有考虑写入模板ID的情况
            # 处理ICMP 目的端口问题
            if new_record.get('PROTOCOL') == 1:
                new_record['L4_DST_PORT'] = 0
            self.flows.append(new_record)
            # print(new_record)
            # print(self.flows)
            # netflowdb(new_record)

    def __repr__(self):  # 格式化打印类时的显示字符串
        return "<DataFlowSet with template {} of length {} holding {} flows>"\
            .format(self.template_id, self.length, len(self.flows))


class TemplateField:
    """
    仅仅用于记录模板中字段的类型和长度数据
    """
    def __init__(self, field_type, field_length):
        self.field_type = field_type  # integer
        self.field_length = field_length  # bytes

    def __repr__(self): # 格式化打印类时的显示字符串
        return "<TemplateField type {}:{}, length {}>".format(
            self.field_type, field_types[self.field_type], self.field_length)


class TemplateRecord:
    """
    仅仅用来记录模板内容,包括ID,数量和字段
    """
    def __init__(self, template_id, field_count, fields):
        self.template_id = template_id
        self.field_count = field_count
        self.fields = fields

    def __repr__(self): # 格式化打印类时的显示字符串
        return "<TemplateRecord {} with {} fields: {}>".format(
            self.template_id, self.field_count,
            ' '.join([field_types[field.field_type] for field in self.fields]))


class TemplateFlowSet:
    """
    分析Template FlowSet,分析模板,便于后续分析Data FlowSet
    """
    def __init__(self, data):
        # 分析数据的前四个字节,分别为FlowSet ID和Template FlowSet的长度
        pack = struct.unpack('!HH', data[:4])
        # FlowSet ID,注意ID为0时为模板
        self.flowset_id = pack[0]
        # Template FlowSet的长度
        self.length = pack[1]
        # 初始化模板为空字典
        self.templates = {}

        # 略过已经分析的前四个字节
        offset = 4

        # 逐个分析在这个template flowset中的template record
        while offset != self.length:
            # 分析第4-8个字节,分别为模板ID,和字段数量
            pack = struct.unpack('!HH', data[offset:offset+4])
            template_id = pack[0]
            field_count = pack[1]
            # 初始化字段列表为空列表
            fields = []
            for field in range(field_count):  # 按照字段数量逐个分析字段内容
                # 每个字段4个字节,分别为类型和长度,offset += 4,用来略过上一个字段
                offset += 4
                # 提取字段类型和字段长度
                field_type, field_length = struct.unpack('!HH', data[offset:offset+4])
                # 如果字段类型不在field_types中,就设置为0,表示位置字段类型UNKNOWN_FIELD_TYPE
                if field_type not in field_types:
                    field_type = 0
                # 使用类TemplateField产生实例field,其实只是换了一个存储数据的方式
                field = TemplateField(field_type, field_length)
                # 把记录字段数据的实例field放入fields列表中
                fields.append(field)

            # 把前期获取的模板ID,字段数量,字段内容,通过类TemplateRecord产生实例来进行存储
            template = TemplateRecord(template_id, field_count, fields)

            # 把模板内容,放入以模板ID为键值的templates字典中
            self.templates[template.template_id] = template

            # 分析下一个模板,略过最后一个分析的字段 分析完毕后，让offset== length 跳出while循环
            offset += 4

    def __repr__(self): # 格式化打印类时的显示字符串
        return "<TemplateFlowSet with id {} of length {} containing templates: {}>"\
            .format(self.flowset_id, self.length, self.templates.keys())


class Header:
    """
    解析Netflow的头部
    """
    def __init__(self, data):
        pack = struct.unpack('!HHIIII', data[:20])

        self.version = pack[0]  # The version of NetFlow records exported in this packet; for Version 9, this value is 0x0009
        self.count = pack[1]  # Number of FlowSet records (both template and data) contained within this packet
        self.uptime = pack[2]  # Number of FlowSet records (both template and data) contained within this packet
        self.timestamp = pack[3]  # Time in milliseconds since this device was first booted
        # Incremental sequence counter of all export packets sent by this export device; this value is
        # cumulative, and it can be used to identify whether any export packets have been missed
        self.sequence = pack[4]
        # The Source ID field is a 32-bit value that is used to guarantee uniqueness for all flows exported from a particular device.
        self.source_id = pack[5]


class ExportPacket:
    """
    这个类是整个解析的开头
    最开始传入的templates为空字典{}
    """
    def __init__(self, data, templates):
        # 解析netflow头部
        self.header = Header(data)
        # 把传入的空字典{},写入属性templates
        self.templates = templates

        self.flows = []
        # 偏移量调整到20,略过已经分析过的头部(netflow头部20个字节)
        offset = 20

        while offset != len(data):
            # 提取flowset_id,它一共2两个字节
            flowset_id = struct.unpack('!H', data[offset:offset+2])[0]
            # flowset_id == 0 非常重要,因为Template FlowSet会在这里发送,如果没有模板就没法对后续Data FlowSet进行分析
            if flowset_id == 0:
                # 使用类TemplateFlowSet分析数据,返回实例tfs(类TemplateFlowSet)
                tfs = TemplateFlowSet(data[offset:])
                # print(tfs)
                # 把实例tfs(类TemplateFlowSet)中的属性templates,
                # 更新到类ExportPacket属性templates中
                self.templates.update(tfs.templates)
                # 去除TemplateFlowSet头部,便于后续DataFlowSet的分析  让offset== length 跳出while循环
                offset += tfs.length
            else:
                # 使用类DataFlowSet分析数据,返回实例dfs(类DataFlowSet)
                dfs = DataFlowSet(data[offset:], self.templates)
                # print(dfs)
                self.flows += dfs.flows
                offset += dfs.length

    def __repr__(self):
        # 对类的打印输出结果进行格式化,显示版本和,记录数量
        return "<ExportPacket version {} counting {} records>".format(
            self.header.version, self.header.count)
