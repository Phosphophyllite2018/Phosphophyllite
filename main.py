#! /usr/bin/env python3

import os
from datetime import timedelta
import flask
from module import Page , AdminPage
from module.Model import ArticleModel
from module.Interface import MessageInterface , AuthInterface , ArticleInterface

app = flask.Flask(__name__, template_folder="./static/html")
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)



# 基本页面

@app.route('/')
def index() :
    if ArticleModel.getCount() == 0 :
        return Page.DemoPage.renderPage()
    else :
        return Page.ArticlePage.renderPage()

@app.route('/message')
def message() :
    page = flask.request.args.get('page', type=int)
    return Page.MessagePage.renderPage(page)

@app.route('/readme')
def readme() :
    return Page.DemoPage.renderPage()

@app.route('/login')
def login() :
    return Page.LoginPage.renderPage()

@app.route('/article')
def article() :
    id = flask.request.args.get('id', type=int)
    return Page.ArticlePage.renderPage(id)

@app.route('/article_list')
def articleList() :
    page = flask.request.args.get('page', type=int)
    return Page.ArticleListPage.renderPage(page)




# 后台页面 

@app.route('/admin')
def admin():
    return AdminPage.AdminPage.renderPage()
    
@app.route('/admin/edit')
def edit():
    return AdminPage.EditorPage.renderPage()

@app.route('/admin/article_list')
def admin_article_list() :
    page = flask.request.args.get('page', type=int)
    return AdminPage.ArticleListPage.renderPage(page)

@app.route('/admin/message')
def admin_message() :
    page = flask.request.args.get('page', type=int)
    return AdminPage.MessagePage.renderPage(page)




# 接口

@app.route('/interface/add_message', methods=["POST"])
def addMessage() :
    return MessageInterface.addMessage() 

@app.route('/interface/delete_message', methods=["POST"])
def deleteMessage() :
    return MessageInterface.deleteMessage() 

@app.route('/interface/save_article', methods=["POST"])
def saveArticle() :
    return ArticleInterface.save() 

@app.route('/interface/delete_article', methods=["POST"])
def deleteArticle() :
    return ArticleInterface.delete() 

@app.route('/interface/auth', methods=["POST"])
def auth() :
    if AuthInterface.checkPassword() :
        return flask.redirect('/admin')
    else :
        return flask.redirect('/login')

@app.route('/interface/article_json', methods=["POST"])
def articleJson() :
    return ArticleInterface.content() 


    
if __name__ == "__main__" :
    app.run(port=8102)