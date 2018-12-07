#! /usr/bin/env python3

import flask
from module import DemoPage 
app = flask.Flask(__name__, template_folder="./static/html")

@app.route('/')
def index() :
	return DemoPage.renderPage()

# @app.route('/private')
# def private() :
# 	flask.abort(404)
	
if __name__ == "__main__" :
	app.run(port=80)