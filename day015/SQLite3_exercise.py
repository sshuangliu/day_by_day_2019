#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/13 18:38
# @Author: max liu
# @File  : SQLite3_exercise.py


# https://www.runoob.com/sqlite/sqlite-python.html
# https://www.runoob.com/sqlite/sqlite-intro.html


import sqlite3
import os

if os.path.exists('sqlite3_test.db'):
    os.remove('sqlite3_test.db')

Sql_dict = [{'姓名': '学员1', 'age': 22, '作业数': 3},
            {'姓名': '学员2', 'age': 25, '作业数': 9},
            {'姓名': '学员3', 'age': 27, '作业数': 30}]

conn = sqlite3.connect('sqlite3_test.db')
c = conn.cursor()

#  创建表
c.execute(
    '''CREATE TABLE Student_homework_info
    (ID INT PRIMARY KEY     NOT NULL,
    '姓名' varchar(40)        NOT NULL,
    age    int,
    '作业数' int);
    ''')

#  插入表
id = 1

for v in Sql_dict:
    name = v.get('姓名')
    age = v.get('age')
    homework_commits = v.get('作业数')
    # insert 的内容 字符串 需要'',数字不需要
    c.execute(
        f'''INSERT INTO Student_homework_info (ID,姓名,age,作业数)
      VALUES ({id},'{name}',{age},{homework_commits})
    ''')
    id += 1
conn.commit()

#  查询表

user_notify = '''
请输入查询选项：
1 ：查询整个数据库
2 ：按姓名查询
3 ：按年龄查询
4 ：按作业数查询
0 ：退出
'''
while True:
    print(user_notify)
    option = int(input('请输入查询选项：'))
    if option == 0:
        break
    elif option == 1:
        c.execute('''SELECT * FROM Student_homework_info''')
        for i in c.fetchall():
            print(i)

    elif option == 2:
        name = input('请输入学员姓名：')
        c.execute(f'''SELECT * FROM Student_homework_info where 姓名 = \'{name}\'''')  # 字符串输入‘’ ？？？？？
        result = c.fetchall()  # c.fetchall() 结果被处理一次就为空，需要保存到中间变量，以便二次操作
        if result:
            for i in result:
                print(i)
        else:
            print('学员不存在')

    elif option == 3:
        age = input('搜索大于输入年龄的学员,请输入学员年龄：')
        c.execute(f'''SELECT * FROM Student_homework_info where age > {age}''')
        result = c.fetchall()
        if result:
            for i in result:
                print(i)
        else:
            print('不存在')
    elif option == 4:
        homework_commits = int(input('搜索大于输入作业数的学员,请输入作业数量：'))
        c.execute(f'''SELECT * FROM Student_homework_info where 作业数 > {homework_commits}''')
        result = c.fetchall()
        if result:
            for i in result:
                print(i)
        else:
            print('不存在')
    else:
        print('输入错误')

conn.commit()
c.close()
conn.close()
if __name__ == '__main__':
    pass
# #  查询表
# c.execute('''SELECT ID,姓名 FROM Student_homework_info where age > 22 and 作业数 = 30''')
# for i in c.fetchall():
#     print(i)
#
# #  update表
# c.execute('''UPDATE Student_homework_info SET 作业数 = 40 WHERE ID = 3''')
#
# #  delete 表
# c.execute('''DELETE FROM Student_homework_info WHERE ID=2;''')
# # #  drop表
# #     c.execute('''DROP TABLE Student_homework_info''')
