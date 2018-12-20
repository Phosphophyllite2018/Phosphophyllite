import flask
from flask import request
from ..Phos import PhosLog
from ..Model import MessageModel

def addMessage() :
    name = request.form['name']
    content = request.form['content']
    MessageModel.append(name, content)

    return flask.redirect('/message')


def deleteMessage() :
    id = request.form['id']
    MessageModel.delete(int(id))

    return flask.redirect('/admin/message')