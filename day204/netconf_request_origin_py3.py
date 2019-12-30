#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/30 16:35
#@Author: max liu
#@File  : netconf_request_origin_py2.py


# python3:
#配置 edit_config
"""

    Netconf python example by yang-explorer (https://github.com/CiscoDevNet/yang-explorer)

    Installing python dependencies:
    > pip install lxml ncclient

    Running script: (save as example.py)
    > python example.py -a 192.168.59.134 -u cisco -p Cisc0123 --port 830
"""

import lxml.etree as ET
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>4</name>
        <description>netconf_test</description>
        <ip>
          <address>
            <primary>
              <address>100.1.1.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

if __name__ == '__main__':

    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    args = parser.parse_args()

    # connect to netconf agent
    with manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        try:  # edit_config target='running'
            response = m.edit_config(target='running', config=payload).xml
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # beautify output
        print(ET.tostring(data, pretty_print=True).decode())




######################################################################

# 监控 get

"""
    Netconf python example by yang-explorer (https://github.com/CiscoDevNet/yang-explorer)

    Installing python dependencies:
    > pip install lxml ncclient

    Running script: (save as example.py)
    > python example.py -a 192.168.59.134 -u cisco -p Cisc0123 --port 830
"""

import lxml.etree as ET
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <cpu-usage xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-process-cpu-oper">
    <cpu-utilization>
      <one-minute/>
    </cpu-utilization>
  </cpu-usage>
</filter>
"""

if __name__ == '__main__':

    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    args = parser.parse_args()

    # connect to netconf agent
    with manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        try:
            response = m.get(payload).xml
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # beautify output
        print(ET.tostring(data, pretty_print=True).decode())