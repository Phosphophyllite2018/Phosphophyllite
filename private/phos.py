#! /usr/bin/env python3

import sys
import os
import sqlite3
import hashlib

# 打印帮助信息
def show_help() :
	script = os.path.basename(sys.argv[0])
	print("Usage : %s <opt> <param>" % script)
	print("        %s init                : 初始化数据库" % script)
	print("        %s username <username> : 设置Blog的用户名" % script)
	print("        %s password <password> : 设置Blog的密码" % script)
	print("        %s git-name <git-name> : 设置GitHub的用户名" % script)
	print("        %s git-pass <git-pass> : 设置GitHub的密码" % script)

# 创建表
def create_table(cursor, table_name, lines) :
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
		
def init_blog_table(cursor) :	
	# 检查是否已经有字段
	sql = "select count(*) from blog"
	length = cursor.execute(sql).fetchone()[0]
	
	# 没有字段，初始化
	if length == 0 :
		
		sql = "INSERT INTO blog VALUES(0, NULL, NULL, NULL, NULL, datetime('now'), 0)"
		cursor.execute(sql)
		print("'blog'表写入初始值。")

# blog表的列
blog_table = [
	["id" , "INTEGER PRIMARY KEY"],
	["username" , "VARCHAR(512)"],
	["password" , "VARCHAR(512)"],
	["git_name" , "VARCHAR(512)"],
	["git_pass" , "VARCHAR(512)"],
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

def phos_init(cursor, argv) :
	if len(argv) != 2 or argv[1] != "init" :
		return False
		
	create_table(cursor, "blog", blog_table)
	create_table(cursor, "article", article_table)
	create_table(cursor, "message", message_table)
	init_blog_table(cursor)
	print("初始化完成")
	return True
	
def phos_setting_username(cursor, argv) :
	if len(argv) != 3 or argv[1] != "username" :
		return False
		
	sql = "UPDATE blog set username='%s' WHERE id=0" % argv[2].replace("'", "''")
	cursor.execute(sql)
	print("用户名设置成功。")
	return True
	
def phos_setting_password(cursor, argv) :
	if len(argv) != 3 or argv[1] != "password" :
		return False
		
	# 将密码加密
	sha256 = hashlib.sha256()
	sha256.update(argv[2].encode('utf-8'))
	password = sha256.hexdigest()
	
	sql = "UPDATE blog set password='%s' WHERE id=0" % password
	cursor.execute(sql)
	print("密码设置成功。")
	return True
	
def phos_setting_git_name(cursor, argv) :
	if len(argv) != 3 or argv[1] != "git-name" :
		return False
		
	sql = "UPDATE blog set git_name='%s' WHERE id=0" % argv[2].replace("'", "''")
	cursor.execute(sql)
	print("GitHub用户名设置成功。")
	return True
	
def phos_setting_git_pass(cursor, argv) :
	if len(argv) != 3 or argv[1] != "git-pass" :
		return False
		
	sql = "UPDATE blog set git_pass='%s' WHERE id=0" % argv[2].replace("'", "''")
	cursor.execute(sql)
	print("GitHub密码设置成功。")
	return True
	

# 连接数据库并创建cursor
if __name__ == "__main__" :
	try :
		db = sqlite3.connect("phosphophyllite.db")
		cursor = db.cursor()
		
		process = [phos_init, phos_setting_username, phos_setting_password,
					phos_setting_git_name, phos_setting_git_pass]
		state = False
		for func in process :
			state = state or func(cursor, sys.argv)
		
		db.commit()
		db.close()
		
		if state == False :
			show_help()
	except Exception as e :
		print(e)