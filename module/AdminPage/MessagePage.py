import flask
from flask import render_template , session
from ..Phos.common import isLogin
from ..View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView , HeaderView
from ..Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage(page) : 
    if not isLogin() :
        return flask.redirect('/login')

    if not isinstance(page, int) :
        page = 1

    # 侧边栏
    aside = AsideView.renderAdminAside(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages())
    
    # 目录
    message_number_per_page = 20
    messages = MessageModel.getMessages(page, message_number_per_page) 
    pages = MessageModel.getPages(message_number_per_page)
    message_list = MessageView.renderAdminMessageList(page, pages, messages) 

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            header=HeaderView.renderHeader(),
                            aside=aside,
                            article=message_list,
                            footer=FooterView.renderFooter())

