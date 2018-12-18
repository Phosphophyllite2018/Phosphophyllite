import flask
from flask import render_template , session
from ..Phos.common import isLogin
from ..View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView , HeaderView
from ..Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage() :
    if not isLogin() :
        return flask.redirect('/login')

    # 侧边栏
    aside = AsideView.renderAdminAside(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages())

    editor_html = ArticleView.renderEditor()
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            header=HeaderView.renderHeader(),
                            aside=aside,
                            article=editor_html,
                            footer=FooterView.renderFooter())