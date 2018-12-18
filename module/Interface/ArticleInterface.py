import flask
from flask import request
from ..Phos import PhosLog 
from ..Phos.common import isLogin
from ..Model import ArticleModel

def save() :
    if not isLogin() :
        return flask.redirect('/login')

    name = request.form['title']
    content = request.form['content']
    ArticleModel.save(name, content)

    return flask.redirect('/admin/article_list')

def delete() :
    if not isLogin() :
        return flask.redirect('/login')

    id = int(request.form['id'])
    ArticleModel.delete(id)

    return flask.redirect('/admin/article_list')