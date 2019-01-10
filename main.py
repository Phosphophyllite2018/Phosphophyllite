#! /usr/bin/env python3

import os
from datetime import timedelta
import flask
from module.Interface import *

app = flask.Flask(__name__, template_folder="./static/html")
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.route('/', methods=["GET", "POST"])
def index() :
    return flask.redirect('/static/html/index.html')

@app.route('/test', methods=["GET", "POST"])
def test() :
    return flask.redirect('/static/test/index.html')

# 博客数据接口
blogInterfaceList = [
    ['/blog/is_login',          BlogInterface.isLogin],
    ['/blog/login',             BlogInterface.login],
    ['/blog/username',          BlogInterface.getUsername],
    ['/blog/running_days',      BlogInterface.getRunDays],
    ['/blog/visiting_count',    BlogInterface.getVisitingCount],
    ['/blog/visiting_modify',   BlogInterface.addVisitingCount],
]

for route in blogInterfaceList :
    app.add_url_rule(route[0], endpoint=route[0], view_func=route[1], methods=['POST'])




# 文章数据接口
articleInterfaceList = [
    ['/article/count',                  ArticleInterface.count],
    ['/article/get_id_by_order',        ArticleInterface.getIdByOrder],
    ['/article/title',                  ArticleInterface.title],
    ['/article/date',                   ArticleInterface.date],
    ['/article/reading_count',          ArticleInterface.readingCount],
    ['/article/markdown',               ArticleInterface.markdown],
    ['/article/html',                   ArticleInterface.html],
    ['/article/total',                  ArticleInterface.total],
    ['/article/modify/reading_count',   ArticleInterface.modifyReadingCount],
    ['/article/save',                   ArticleInterface.save],
    ['/article/delete',                 ArticleInterface.delete],
]

for route in articleInterfaceList :
    app.add_url_rule(route[0], endpoint=route[0], view_func=route[1], methods=['POST'])




# 留言数据接口
messageInterfaceList = [
    ['/message/count',                  MessageInterface.count],
    ['/message/get_id_by_order',        MessageInterface.getIdByOrder],
    ['/message/visitor_name',           MessageInterface.visitorName],
    ['/message/date',                   MessageInterface.date],
    ['/message/markdown',               MessageInterface.markdown],
    ['/message/html',                   MessageInterface.html],
    ['/message/total',                  MessageInterface.total],
    ['/message/list',                   MessageInterface.list],
    ['/message/save',                   MessageInterface.save],
    ['/message/delete',                 MessageInterface.delete], 
]

for route in messageInterfaceList :
    app.add_url_rule(route[0], endpoint=route[0], view_func=route[1], methods=['POST'])


# Markdown接口
markdownInterfaceList = [
    ['/markdown/render',                MarkdownInterface.render],
]

for route in markdownInterfaceList :
    app.add_url_rule(route[0], endpoint=route[0], view_func=route[1], methods=['POST'])

    
if __name__ == "__main__" :
    app.run(port=8102)