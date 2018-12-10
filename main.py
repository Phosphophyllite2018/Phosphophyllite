#! /usr/bin/env python3

import flask
from module import DemoPage , HomePage
from module.Model import ArticleModel
from module.Interface import MessageInterface
app = flask.Flask(__name__, template_folder="./static/html")

@app.route('/')
def index() :
	if ArticleModel.getCount() == 0 :
		return DemoPage.renderPage()
	else :
		return HomePage.renderPage()

@app.route('/readme')
def reame() :
	return DemoPage.renderPage()

@app.route('/addmessage', methods=["POST"])
def message() :
	MessageInterface.addMessage() 
	return flask.redirect(flask.url_for('index'))

# @app.route('/private')
# def private() :
# 	flask.abort(404)
	
if __name__ == "__main__" :
	app.run(port=80)