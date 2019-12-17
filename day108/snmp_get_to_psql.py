#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/2 12:32
# @Author: max liu
# @File  : snmp_get_to_psql.py

from pysnmp.hlapi import *
import pg8000
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import logging
from datetime import datetime,timedelta

#  2019-11-28 15:44:11 base.py[line:440] INFO Adding job tentatively -- it will be properly scheduled when the scheduler starts
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='snmp_get_to_psql.log',
                    filemode='a')


#  类似snmpget
def snmpv2_get(ip, community, oid, port=161):
    # varBinds是列表，列表中的每个元素的类型是ObjectType（该类型的对象表示MIB variable）
    errorIndication, errorStatus, errorindex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),  # 配置community
               UdpTransportTarget((ip, port)),  # 配置目的地址和端口号
               ContextData(),
               ObjectType(ObjectIdentity(oid))  # 读取的OID
               )
    )
    # 错误处理
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus,
            errorindex and varBinds[int(errorindex) - 1][0] or '?'
        )
              )
    # 如果返回结果有多行,需要拼接后返回
    result = ""

    for varBind in varBinds:
        result = result + varBind.prettyPrint()  # 返回结果！
    # 返回的为一个元组,OID与字符串结果
    return result.split("=")[0].strip(), result.split("=")[1].strip()


def to_psql():
    cpu_utilization = int(snmpv2_get("192.168.59.140", "public", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1])
    memory_free = int(snmpv2_get("192.168.59.140", "public", "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1])
    memory_used = int(snmpv2_get("192.168.59.140", "public", "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1])
    memory_utilization = int((memory_used / (memory_free + memory_used)) * 100)
    device_name = snmpv2_get("192.168.59.140", "public", "1.3.6.1.4.1.9.2.1.3.0", port=161)[1]
    device_ipadd = '192.168.59.140/24'

    conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                          database='shuangdb_001')
    c = conn.cursor()

    #  插入表 字符值需要加‘’，数字不需要！！！！！！
    sql = f'''INSERT INTO device_cpu_memory_utilization(device_name,device_ipadd,cpu_utilization,memory_utilization) VALUES ('{device_name}','{device_ipadd}', {cpu_utilization}, {memory_utilization}) '''  # 参数需要''  ！！！！！！！！！
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def create_tab_for_snmp():
    """
 https://www.postgresql.org/docs/9.6/functions-net.html
 PSQL inet 网络数据类型，可以带上掩码信息，不写为/32掩码，后续可以根据网络属性过滤 过滤方法：
 1：过滤相同网络的主机
 SELECT * FROM temp001 where network(ipadd) = network('2.2.2.2/24')
 2：过滤大于某个ip地址的主机
 SELECT * FROM temp001 where ipadd > inet '2.2.2.3/24'
 3：过滤下一个ip地址的主机
 SELECT * FROM temp001 where ipadd = inet '2.2.2.3/24' + 1
 4：过滤范围内的主机：
 SELECT * FROM temp001 where ipadd > inet '2.2.2.2/24'  and ipadd < inet '2.2.2.5/24'
 5：插入网络类型的数据：
 INSERT INTO temp001 (ipadd, name) VALUES ('22.2.2.200/24', '3')
 6：插入不符合网络数据类型会报错：
 INSERT INTO temp001 (ipadd, name) VALUES ('22.2.2.256/24', '3')；

    """
    conn = pg8000.connect(host='192.168.59.100', user='shuangliu007', password='shuangliu001',
                          database='shuangdb_001')
    c = conn.cursor()
    #  创建表
    sql = '''
                    CREATE TABLE device_cpu_memory_utilization(
                    ID SERIAL PRIMARY KEY,
                    device_name varchar(50) not null ,
                    device_ipadd inet not null ,
        			tdate timestamp default current_timestamp,
                    cpu_utilization smallint not null ,
        			memory_utilization smallint not null )
                    '''

    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()


def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行:周期性监控设备配置变化...6秒一次')


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(func=create_tab_for_snmp, args=[], trigger='date', run_date='2019-12-02 16:38:00',
                      id='once_task')  # 被调度函数参数由args传入，列表 元组都可
    scheduler.add_job(func=to_psql, args=[], trigger='interval', seconds=6,
                      start_date=datetime.now()+timedelta(seconds=10), id='interval_task')
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler._logger = logging

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        exit()


