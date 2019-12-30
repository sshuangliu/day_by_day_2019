#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/30 19:01
# @Author: max liu
# @File  : netconf_get_xml_analyse.py

xml_response = '''
<rpc-reply message-id="urn:uuid:98281a8f-ec6e-4a37-9a46-e13aacd878f5" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <data>
    <cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
      <cpu-utilization>
        <one-minute>6</one-minute>
      </cpu-utilization>
    </cpu-usage>
  </data>
</rpc-reply>
'''

import xmltodict
from pprint import pprint

xmldict = xmltodict.parse(xml_response)
pprint(xmldict)
'''
OrderedDict([('rpc-reply',
              OrderedDict([('@message-id',
                            'urn:uuid:98281a8f-ec6e-4a37-9a46-e13aacd878f5'),
                           ('@xmlns',
                            'urn:ietf:params:xml:ns:netconf:base:1.0'),
                           ('@xmlns:nc',
                            'urn:ietf:params:xml:ns:netconf:base:1.0'),
                           ('data',
                            OrderedDict([('cpu-usage',
                                          OrderedDict([('@xmlns',
                                                        'http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper'),
                                                       ('cpu-utilization',
                                                        OrderedDict([('one-minute',
                                                                      '6')]))]))]))]))])
'''
pprint(xmldict['rpc-reply']['data']['cpu-usage']['cpu-utilization']['one-minute'], indent=4)
