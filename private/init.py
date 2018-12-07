#! /usr/bin/env python3

import sqlite3
import hashlib

# 创建表
def create_table(cursor, table_name, lines) :
	try :
		# 检查表是否已经存在
		result = cursor.execute("select * from sqlite_master  where type = 'table' and name = '%s'" % table_name)
		
		# 表不存在则创建
		if result.fetchone() == None :
			sql = "CREATE TABLE '%s'(" % table_name
			for line in lines :
				sql += line[0] + " " + line[1] + ","
			sql = sql[:-1] + ");"
			cursor.execute(sql)
			print("创建表 '%s' 成功。" % table_name)
		else :
			pass
	except Exception as e :
		print(e)
		
def init_blog_table(cursor, username, password) :
	try :
		# 将密码加密
		sha256 = hashlib.sha256()
		sha256.update(password.encode('utf-8'))
		password = sha256.hexdigest()
		
		# 检查是否已经有字段
		sql = "select count(*) from blog"
		length = cursor.execute(sql).fetchone()[0]
		
		# 没有字段，初始化
		if length == 0 :
			
			sql = "INSERT INTO blog VALUES(0, '%s','%s',datetime('now'),0)" % (username,password)
			cursor.execute(sql)
			print("设置用户名密码完成。")
			print("初始化成功。")
		# 有字段，修改密码
		else :
			sql = "UPDATE blog set username='%s',password='%s' WHERE id=0" % (username,password)
			cursor.execute(sql)
			print("强制修改用户名密码成功。")
	except Exception as e :
		print(e)

# blog表的列
blog_table = [
	["id" , "INTEGER PRIMARY KEY"],
	["username" , "VARCHAR(512)"],
	["password" , "VARCHAR(512)"],
	["birthday" , "DATETIME"],
	["visiting" , "INT"],
]

# article表的列
article_table = [
	["id" , "INTEGER PRIMARY KEY AUTOINCREMENT"],
	["title" , "VARCHAR(512)"],
	["content" , "TEXT"],
	["birthday" , "DATETIME"],
	["visiting" , "INT"],
]

# message表的列
message_table = [
	["id" , "INTEGER PRIMARY KEY AUTOINCREMENT"],
	["name" , "VARCHAR(512)"],
	["content" , "TEXT"],
	["birthday" , "DATETIME"],
	["visiting" , "INT"],
]


# 连接数据库并创建cursor
if __name__ == "__main__" :
	import sys
	import os
	if len(sys.argv) < 2 or len(sys.argv) > 3 :
		script = os.path.basename(sys.argv[0])
		print("Usage : %s <用户名> <密码>" % script)
		print("        用于初始化数据库，或者修改用户名密码。")
		quit(1)

	db = sqlite3.connect("phosphophyllite.db")
	cursor = db.cursor()
	create_table(cursor, "blog", blog_table)
	create_table(cursor, "article", article_table)
	create_table(cursor, "message", message_table)
	init_blog_table(cursor, sys.argv[1], sys.argv[2])
	db.commit()
	db.close()