#! /usr/bin/env python3

import flask
from module import DemoPage , HomePage , MessagePage
from module.Model import ArticleModel
from module.Interface import MessageInterface
app = flask.Flask(__name__, template_folder="./static/html")

@app.route('/')
def index() :
	if ArticleModel.getCount() == 0 :
		return DemoPage.renderPage()
	else :
		return HomePage.renderPage()

@app.route('/message')
def message() :
	return MessagePage.renderPage()


@app.route('/readme')
def readme() :
	return DemoPage.renderPage()

@app.route('/addmessage', methods=["POST"])
def addmessage() :
	MessageInterface.addMessage() 
	return flask.redirect('/message')

# @app.route('/private')
# def private() :
# 	flask.abort(404)
	
if __name__ == "__main__" :
	app.run(port=80)