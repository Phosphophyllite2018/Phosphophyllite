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

@app.route('/blog/is_login', methods=["POST"])
def isLogin() :
    return BlogInterface.isLogin() 

@app.route('/blog/login', methods=["POST"])
def login() :
    return BlogInterface.login() 

@app.route('/blog/username', methods=["POST"])
def username() :
    return BlogInterface.getUsername() 

@app.route('/blog/running_days', methods=["POST"])
def getRunDays() :
    return BlogInterface.getRunDays() 

@app.route('/blog/visiting_count', methods=["POST"])
def getVisitingCount() :
    return BlogInterface.getVisitingCount() 

@app.route('/blog/visiting_modify', methods=["POST"])
def addVisitingCount() :
    return BlogInterface.addVisitingCount() 



    
if __name__ == "__main__" :
    app.run(port=8102)