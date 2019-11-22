[https://segmentfault.com/a/1190000018812714#articleHeader0]()

##### 环境
psql (PostgreSQL) 11.6  
CentOS Linux release 7.7.1908 (Core)

##### PostgreSQL
PostgreSQL是以加州大学伯克利分校计算机系开发的 POSTGRES，现在已经更名为PostgreSQL，版本 4.2为基础的对象关系型数据库管理系统（ORDBMS）。PostgreSQL支持大部分 SQL标准并且提供了许多其他现代特性：复杂查询、外键、触发器、视图、事务完整性、MVCC。同样，PostgreSQL 可以用许多方法扩展，比如， 通过增加新的数据类型、函数、操作符、聚集函数、索引。免费使用、修改、和分发 PostgreSQL，不管是私用、商用、还是学术研究使用。
PostgreSQL从9.3版本开始内置了JSON数据类型，而9.4开始支持JSONB，标志着<span style="color: yellow;">PostgreSQL实际上已经是一个关系型数据库和NoSQL数据库的结合体</span>。虽然PostgreSQL还定位在关系型数据库，但是<span style="color: yellow;">近几次更新PostgreSQL的NoSQL性能飙升甚至超过MongoDB</span>。

##### PostgreSQL安装
下载rpm包  
yum install https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-redhat11-11-2.noarch.rpm -y  

安装  
yum -y install postgresql11 postgresql11-server postgresql11-libs  

初始化数据库  
/usr/pgsql-11/bin/postgresql-11-setup initdb  

设置开机自启动PostgreSQL和启动服务  
systemctl enable postgresql-11  
systemctl start postgresql-11  
systemctl status postgresql-11  

##### PostgreSQL连接
 登录数据库，这里切换账号postgres  
su - postgres  
psql

Navicat连接PostgreSQL 这里要修改配置文件postgresql.conf  
find / -name postgresql.conf  
vi /var/lib/pgsql/11/data/postgresql.conf

 找到listen_address那里，解开注释并修改引号内localhost的值为*  
listen_address="*"

 保存并退出，重启postgresql服务  
systemctl restart postgresql-11


 修改远程连接pg_hba.conf  
find / -name pg_hba.conf  
vi /var/lib/pgsql/11/data/pg_hba.conf  
 在文件末尾加上,如果不加上远程连接PostgreSQL会出现no pg_hba.conf...的错误  
host    all             all             0.0.0.0/0               trust

 在navicat连接，如果不修改localhost为*，navicat连接会提示错误“Connection Refuse”

 我在这里修改了postgres用户的密码，步骤如下：  
 切换用户后进入psql  
su - postgres  
psql  
修改密码  
alter user postgres password '密码'

