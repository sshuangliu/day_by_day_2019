# Lesson01 什么是PostgreSql？

小马视频:http://komavideo.com/

gitee:https://gitee.com/komavideo/LearnPostgreSql
## 知识点

* 面向关系的数据库
  + Oracle
  + MySql
  + SQLServer
  + PostgreSql
* NoSql
  + MongoDB
  + Redis

### 数据库排名

https://db-engines.com/en/ranking



# Lesson02 初来乍到数据库

~~~bash
$ sudo su postgres
$ psql --version
$ psql -l
$ createdb komablog
$ psql -l
$ psql komablog
> help
> \h
> \?
> \l
> \q
$ psql komablog
> select now();
> select version();
> \q
$ dropdb komablog
$ psql -l
~~~

# Lesson03 操作数据表

~~~bash
$ sudo su postgres
$ createdb komablog
$ psql -l
$ psql komablog
> create table posts (title varchar(255), content text);
> \dt
> \d posts
> alter table posts rename to komaposts;
> \dt
> drop table komaposts;
> \dt
> \q
$ nano db.sql
...
create table posts (title varchar(255), content text);
...
$ psql komablog
> \i db.sql
> \dt
~~~

# Lesson04 字段类型

* 数值型：
  + integer(int)
  + real
  + serial
* 文字型：
  + char
  + varchar
  + text
* 布尔型：
  + boolean
* 日期型：
  + date
  + time
  + timestamp
* 特色类型：
  + Array
  + 网络地址型(inet)
  + JSON型
  + XML型

参考网站：

https://www.postgresql.org/docs/9.5/static/datatype.html
# Lesson05 添加表约束

~~~sql
create table posts (
    id serial primary key,
    title varchar(255) not null,
    content text check(length(content) > 8),
    is_draft boolean default TRUE,
    is_del boolean default FALSE,
    created_date timestamp default 'now'
);

-- 说明
/*
约束条件：

not null:不能为空,''也是有值,但不能为'NULL'值
unique:在所有数据中值必须唯一
check:字段设置条件  自定义函数
default:字段默认值
primary key(not null, unique):主键,不能为空,且不能重复
*/
~~~
# Lesson06 INSERT语句

~~~sql
 每一句语句后面加'；'代表语句的结束
> insert into posts (title, content) values ('', '');
> insert into posts (title, content) values (NULL, '');
> insert into posts (title, content) values ('title1', 'content11');
> select * from posts;
> insert into posts (title, content) values ('title2', 'content22');
> insert into posts (title, content) values ('title3', 'content33');
> select * from posts;
~~~
# Lesson07 SELECT语句

~~~sql
create table users (
    id serial primary key,
    player varchar(255) not null,
    score real,
    team varchar(255)
);

insert into users (player, score, team) values
('库里', 28.3, '勇士'),
('哈登', 30.2, '火箭'),
('阿杜', 25.6, '勇士'),
('阿詹', 27.8, '骑士'),
('神龟', 31.3, '雷霆'),
('白边', 19.8, '热火'),
('阿12', 22.6, '勇士'),
('1阿', 20.6, '勇士'),
('阿', 30.6, '勇士');
~~~

 SQL实战

~~~bash
$ psql komablog
> \i init.sql
> \dt
> \d users
> select * from users;
> \x 改为纵向显示,默认横向显示
> select * from users;
> \x
> select * from users;
> select player, score from users;
~~~
# Lesson08 WHERE语句

~~~sql
> select * from users;
> select * from users where score > 20;
> select * from users where score < 30;
> select * from users where score > 20 and score < 30;
> select * from users where team = '勇士';
> select * from users where team != '勇士';
> select * from users where player like '阿%';  以'啊'字符开头,以任意位数(包括0个)的字符结尾的player
> select * from users where player like '阿_';  以'啊'字符开头,以任意**一个**位数的字符结尾的player
~~~
# Lesson09 数据抽出选项
* order by
* limit
* offset
~~~sql
> select * from users order by score asc; 升序 默认升序
> select * from users order by score desc; 降序
> select * from users order by team; 同一个team的会在一起
> select * from users order by team, score; 相同team内部二次按照score升序排序,不同team之间不比较score
> select * from users order by team, score desc;
> select * from users order by team desc, score desc; ???
> select * from users order by score desc limit 3;
> select * from users order by score desc limit 3 offset 1;
> select * from users order by score desc limit 3 offset 2;
> select * from users order by score desc limit 3 offset 3;
~~~
# Lesson10 统计抽出数据
* distinct
* sum
* max/min
* group by/having
~~~sql
> select distinct team from users; 重复元素算一个统计,统计并打印team列
> select sum(score) from users; 返回处理后的 一个结果,新sum列,一个结果
> select max(score) from users;
> select min(score) from users;
> select * from users where score = (select max(score) from users); 二次查询
> select * from users where score = (select min(score) from users);
> select team, max(score) from users group by team; 分组统计,返回每组的最终结果并汇总,影响组内有多个元素的结果
> select team, max(score) from users group by team having max(score) >= 25; 分组,符合have条件的组才会去参与统计
> select team, max(score) from users group by team having max(score) >= 25 order by max(score); 最终按照新max列排序
~~~
# Lesson11 方便的函数

* length
* concat
* alias
* substring
* random
~~~sql
> select player, length(player) from users; 新列默认为函数名：length
> select player, concat(player, '/', team) from users;
> select player, concat(player, '/', team) as "球员信息" from users; 对列起别名
> select substring(team, 1, 1) as "球队首文字" from users; 从team第一个字符起始,切一个长度
> select concat('我', substring(team, 1, 1)) as "球队首文字" from users; 
> select random(); 生产一个0-1的随机数 0.0452571660280228
> select * from users order by random(); 随机排序
> select * from users order by random() limit 1; 随机抽取一个
~~~
# Lesson12 更新和删除

~~~sql
> update users set score = 29.1 where player = '阿詹';
> update users set score = score + 1 where team = '勇士';
> update users set score = score + 100 where team IN ('勇士', '骑士');
> delete from users where score > 30;
~~~
# Lesson13 变更表结构

* alter table [tablename] ...
* create index ...
* drop index ...
~~~sql
> \d users;
> alter table users add fullname varchar(255); 新建列
> \d users;
> alter table users drop fullname; 删除列 有数据也可以删
> \d users;
> alter table users rename player to nba_player; 更改列名
> \d users;
> alter table users alter nba_player type varchar(100); 更改列名 数据类型
> \d users;
> create index nba_player_index on users(nba_player); 创建某些列的索引(单列索引 或多列复合索引),提升查询效率
> \d users;
> drop index nba_player_index; 删除索引
> \d users;
~~~
# Lesson14 操作多个表

~~~sql
create table users (
    id serial primary key,
    player varchar(255) not null,
    score real,
    team varchar(255)
);
insert into users (player, score, team) values
('库里', 28.3, '勇士'),
('哈登', 30.2, '火箭'),
('阿杜', 25.6, '勇士'),
('阿詹', 27.8, '骑士'),
('神龟', 31.3, '雷霆'),
('白边', 19.8, '热火');

create table twitters (
    id serial primary key,
    user_id integer,
    content varchar(255) not null
);
insert into twitters (user_id, content) values
(1, '今天又是大胜,克莱打的真好!'),
(2, '今晚我得了60分,哈哈!'),
(3, '获胜咱不怕,缺谁谁尴尬.'),
(4, '明年我也可能转会西部'),
(5, '我都双20+了，怎么球队就是不胜呢?'),
(1, '明年听说有条大鱼要来,谁呀?');
~~~

 SQL实行

~~~sql
$ dropdb komablog;
$ createdb komablog;
$ psql komablog;
> \i renew.sql
> select * from users;
> select * from twitters;
> select users.player, twitters.content from users, twitters where users.id = twitters.user_id; 外键关联,取出user每个人说的所有话
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id; 对表起别名
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1;
~~~
# Lesson15 使用视图

###### 视图概念

视图（View）是从一个或多个表导出的对象。视图与表不同，视图是一个虚表，即视图所对应的数据不进行实际存储，数据库中只存储视图的定义，在对视图的数据进行操作时，系统根据视图的定义去操作与视图相关联的基本表。

###### 解释

视图就是一个SELECT语句，把业务系统中常用的SELECT语句简化成一个类似于表的对象，便于简单读取和开发。

###### 知识点

* 使用数据库视图(view)
  + create view ...
  + drop view ...


~~~sql
> select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1; 多表操作,外键关联查询
> create view curry_twitters as select u.player, t.content from users as u, twitters as t where u.id = t.user_id and u.id = 1; 视图  逻辑表
> \dv
> \d curry_twitters
> select * from curry_twitters;
> drop view curry_twitters;
> \dv
~~~

###### 建议

在自己项目中，为了提高数据查询速度，可在表中加入索引index。同时对于经常需要查询的语句，可以提前建立视图view，方便于编码和管理。
# Lesson16 使用事务

###### 事务概念

数据库事务(Database Transaction) ，是指作为单个逻辑工作单元执行的一系列操作，要么完全地执行，要么完全地不执行。 事务处理可以确保除非事务性单元内的所有操作都成功完成，否则不会永久更新面向数据的资源。通过将一组相关操作组合为一个要么全部成功要么全部失败的单元，可以简化错误恢复并使应用程序更加可靠。一个逻辑工作单元要成为事务，必须满足所谓的ACID（原子性、一致性、隔离性和持久性）属性。事务是数据库运行中的逻辑工作单位，由DBMS中的事务管理子系统负责事务的处理。

###### 知识点

* PostgreSql数据库事务使用
  + begin
  + commit
  + rollback


~~~sql
> select * from users;
> begin;
> update users set score = 50 where player = '库里';
> update users set score = 60 where player = '哈登';
> commit;
> select * from users;
> begin;
> update users set score = 0 where player = '库里'; select查询结果已经生效
> update users set score = 0 where player = '哈登';
> rollback;
> select * from users;
~~~
