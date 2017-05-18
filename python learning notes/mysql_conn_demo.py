#!/usr/bin/env python
#coding:utf-8
#data:200170420
#Author:1975

import MySQLdb

conn = MySQLdb.connect(user='',passwd='',host='127.0.0.1')  #连接
cur = connect.cursor()  #保存连接
conn.select_db('mysql') #选择数据库
cur.execute('select host,user,password from user')  #查询数据，返回数据条数
cur.fetchone()  #取出一条数据
#('localhost', 'root', '')
cur.fetchmany(5)    #返回多条数据
cur.fetchmany(cur.execute('select host,user,password from user'))   #一步查询
cur.scroll(0,'absolute')    #将数据指针移到第一行

#sqli = "insert into userinfo(name,age,gender) value(%s,%s,%s)"
#cur.execute(sqli,('csvt',5,'s'))

sqlim = "insert into userinfo(name,age,gender) values(%s,%s,%s)"
cur.executemany(slqi,[('cs',5,'s'),('c',1,'s'),('s',2,'m')])    #多条数据插入

cur.close()     #先关闭游标
conn.close()       #再关闭连接