#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019-11-21 00:27
#@Author: max liu
#@File  : PostgreSql_example.py


import pg8000

# Python字典对象，我们将把它写入PSQL外部数据库
teachers_dict = [{'姓名': '秦柯', '年龄': 37, '部门': '安全', '职位': '讲师'},
                 {'姓名': '马海波', '年龄': 33, '部门': '数据中心', '职位': '讲师'},
                 {'姓名': '周亚军', '年龄': 31, '部门': '路由交换', '职位': '讲师'}]

# 连接外部PSQL数据库
conn = pg8000.connect(host='10.1.1.60', user='qytangdbuser', password='Cisc0123', database='qytangdb')
cursor = conn.cursor()

# # 执行创建表的任务
# cursor.execute("create table qytang_teachers_info (姓名 varchar(40), 年龄 int, 部门 varchar(40), 职务 varchar(40))")
#
# # 读取Python字典数据，并逐条写入外部PSQL数据库
# for teacher in teachers_dict:
#     name = teacher['姓名']
#     age = teacher['年龄']
#     department = teacher['部门']
#     job = teacher['职位']
#     cursor.execute("insert into qytang_teachers_info values ('%s', %d, '%s', '%s')" % (name, age, department, job))
#
# # 读取整个qytang_teachers_info表的信息，并且打印
# cursor.execute("select * from qytang_teachers_info")
# yourresults = cursor.fetchall()
#
# for teacher in yourresults:
#     print(teacher)
#
# # 基于单一条件搜索数据库表
# cursor.execute("select 年龄 from qytang_teachers_info where 姓名 = '秦柯'")
# yourresults = cursor.fetchall()
#
# for age in yourresults:
#     print(age[0])
#
# # 基于多重条件搜索数据库表
# cursor.execute("select 姓名 from qytang_teachers_info where 年龄 > 32 and 职务 = '讲师'")
# yourresults = cursor.fetchall()
#
# for age in yourresults:
#     print(age[0])
#
# # 删除表
# cursor.execute("drop table qytang_teachers_info")
#
# # 严重注意一定要提交，否则数据不会实际写入数据库
# conn.commit()


# 执行创建表的任务
cursor.execute("create table config_info(id SERIAL PRIMARY KEY, config varchar(9999) not null, md5 varchar(200) unique, record_time timestamp default current_timestamp)")


cursor.execute("insert into config_info (config, md5) values ('%s', '%s')" % ('CiscoRouter', 'sdfsdfsdfsdfsdf'))
cursor.execute("insert into config_info (config, md5) values ('%s', '%s')" % ('CiscoSwitch', 'sdfsdfsdfsdfsde'))

# 读取整个qytang_teachers_info表的信息，并且打印
cursor.execute("select * from config_info")
yourresults = cursor.fetchall()

for config in yourresults:
    print(config)

from datetime import datetime
# 基于时间过滤
start = datetime(2019, 3, 31, 10, 47, 6, 395000)
end = datetime(2019, 3, 31, 11, 00, 48, 257000)

cursor.execute("select * from config_info WHERE record_time >='{0}' AND record_time < '{1}'".format(start, end))
yourresults = cursor.fetchall()

for config in yourresults:
    print(config)

# 删除表
cursor.execute("drop table config_info")

# 严重注意一定要提交，否则数据不会实际写入数据库
conn.commit()
