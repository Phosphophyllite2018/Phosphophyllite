import flask
from flask import render_template , session
from ..Phos.common import isLogin
from ..View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView , HeaderView
from ..Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage() :
    if not isLogin() :
        return flask.redirect('/login')
    else :
        return flask.redirect('/admin/edit')