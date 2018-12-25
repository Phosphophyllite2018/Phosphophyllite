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
    app.add_url_rule(route[0], view_func=route[1], methods=['POST'])




# 文章数据接口
articleInterfaceList = [
    ['/article/count',           ArticleInterface.count],
    ['/article/get_id_by_order', ArticleInterface.getIdByOrder],
    ['/article/title',           ArticleInterface.title],
    ['/article/date',            ArticleInterface.date],
    ['/article/reading_count',   ArticleInterface.readingCount],
    ['/article/content',         ArticleInterface.content],
    ['/article/total',           ArticleInterface.total],
]

for route in articleInterfaceList :
    app.add_url_rule(route[0], view_func=route[1], methods=['POST'])

    
if __name__ == "__main__" :
    app.run(port=8102)