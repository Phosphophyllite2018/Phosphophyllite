import flask
from flask import render_template , session
from ..View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView , HeaderView
from ..Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage(page) : 
    if 'login' not in session or session['login'] != True :
        return flask.redirect('/login')

    if not isinstance(page, int) :
        page = 0

    # 侧边栏
    aside = AsideView.renderAdminAside(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages())
    
    # 目录
    articles = ArticleModel.getArticleListPage(page, 10)
    pages = ArticleModel.getPages(10)
    article_list = ArticleView.renderArticleList(page, articles, pages)

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            header=HeaderView.renderHeader(),
                            aside=aside,
                            article=article_list,
                            footer=FooterView.renderFooter())

