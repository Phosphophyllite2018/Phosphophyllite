import json
import flask
from flask import request
from ..Phos import PhosLog 
from ..Phos.common import isLogin
from ..Model import ArticleModel

def content():
    id = int(request.form['id'])
    value = {}
    value['title'] = ArticleModel.getById("title", id)
    value['content'] = ArticleModel.getById("content", id)

    return json.dumps(value,ensure_ascii=False)

def save() :
    if not isLogin() :
        return flask.redirect('/login')

    id = request.form['id']
    print(id)
    name = request.form['title']
    content = request.form['content']
    ArticleModel.save(name, content, id)

    return flask.redirect('/admin/article_list')

def delete() :
    if not isLogin() :
        return flask.redirect('/login')

    id = int(request.form['id'])
    ArticleModel.delete(id)

    return flask.redirect('/admin/article_list')