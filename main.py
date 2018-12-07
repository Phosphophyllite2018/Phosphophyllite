#! /usr/bin/env python3

import flask
from module import DemoPage , HomePage , ArticleModel
app = flask.Flask(__name__, template_folder="./static/html")

@app.route('/')
def index() :
	if ArticleModel.getArticleCount() == 0 :
		return DemoPage.renderPage()
	else :
		return HomePage.renderPage()

# @app.route('/private')
# def private() :
# 	flask.abort(404)
	
if __name__ == "__main__" :
	app.run(port=80)