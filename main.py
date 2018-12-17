#! /usr/bin/env python3

import os
from datetime import timedelta
import flask
from module import DemoPage , ArticlePage , MessagePage , LoginPage , EditorPage , AdminPage
from module.Model import ArticleModel
from module.Interface import MessageInterface , AuthInterface , ArticleInterface

app = flask.Flask(__name__, template_folder="./static/html")
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.route('/')
def index() :
	if ArticleModel.getCount() == 0 :
		return DemoPage.renderPage()
	else :
		return ArticlePage.renderPage()

# 页面

@app.route('/message')
def message() :
	return MessagePage.renderPage()

@app.route('/readme')
def readme() :
	return DemoPage.renderPage()

@app.route('/login')
def login() :
	return LoginPage.renderPage()

@app.route('/article')
def article() :
	id = flask.request.args.get('id', type=int)
	return ArticlePage.renderPage(id)


# 后台页面

@app.route('/admin_edit')
def edit():
	return EditorPage.renderPage()

@app.route('/admin')
def admin():
	return AdminPage.renderPage()


# 接口

@app.route('/addmessage', methods=["POST"])
def addmessage() :
	MessageInterface.addMessage() 
	return flask.redirect('/message')

@app.route('/saveArticle', methods=["POST"])
def saveArticle() :
	ArticleInterface.save() 
	return flask.redirect('/')

@app.route('/auth', methods=["POST"])
def auth() :
	if AuthInterface.checkPassword() :
		return flask.redirect('/admin')
	else :
		return flask.redirect('/login')

# @app.route('/private')
# def private() :
# 	flask.abort(404)
	
if __name__ == "__main__" :
	app.run(port=8102)