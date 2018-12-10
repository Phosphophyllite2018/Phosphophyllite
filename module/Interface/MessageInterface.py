from flask import request
from ..Phos import PhosLog
from ..Model import MessageModel

def addMessage() :
    name = request.form['name']
    content = request.form['content']
    MessageModel.append(name, content)