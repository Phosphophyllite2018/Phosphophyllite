# 示例页面

from flask import render_template
from . import HeadView , HeadModel , MarkdownView

demo_article = '''
# Phosphophillite
Phosphophillite是一个简单的Blog程序，支持使用Markdown编辑文章。这个示例文章就是使用Markdown编辑的，采用GitHub API进行渲染。可以用和GitHub一样的方式插入代码，例如：
```Python
#! /usr/bin/env python3

import time
import colorama

if __name__ == "__main__" :
	# 初始化colorame
	colorama.init()
 
	# 日历头部
	print(time.strftime("     %Y-%m-%d %H:%M:%S"))
	print(" Sun Mon Tue Wed Thu Fri Sat ")
	
	# 保存今天的日期并回到月初第一天
	timestamp = time.time()
	time_tuple = time.localtime(timestamp)
	month = time_tuple.tm_mon
	today = time_tuple.tm_mday
	timestamp -= (today - 1) * 24 * 60 * 60 
	time_tuple = time.localtime(timestamp)
	
	# 打印月初前的空白
	for i in range(0,time_tuple.tm_wday+1) : 
		print("    ", end="")
		
	# 打印日历
	while time_tuple.tm_mon == month :
		if time_tuple.tm_mday == today :
			print(colorama.Style.BRIGHT, end="")
			print(colorama.Fore.GREEN, end="")
		print(" %2d " % (time_tuple.tm_mday), end="")
		print(colorama.Style.RESET_ALL, end="")
			
		if time_tuple.tm_wday == 5 :
			print("")
		timestamp += 24 * 60 * 60
		time_tuple = time.localtime(timestamp)
	print("")
```
'''

def render() :
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophillite",
                            article=MarkdownView.renderMarkdown(demo_article))