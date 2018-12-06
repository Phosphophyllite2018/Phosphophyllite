from flask import Flask
from module import DemoView 
app = Flask(__name__, template_folder="./static/html")

@app.route('/')
def index() :
	return DemoView.render()
	
if __name__ == "__main__" :
	app.run(port=80)