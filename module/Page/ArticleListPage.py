import flask
from flask import render_template , session
from ..Phos.common import isLogin
from ..View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView , HeaderView
from ..Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage(page) : 

    if not isinstance(page, int) :
        page = 1

    # GitHub用户名密码
    gitname = MarkdownModel.getGitName()
    gitpass = MarkdownModel.getGitPass()

    # 最近文章
    recent_article = ArticleModel.getRecentArticle(10)
    recent_article_html = ArticleView.renderAsideArticleList(recent_article, gitname, gitpass)

    # 最近留言
    recent_message = MessageModel.getRecentMessage(10)
    recent_message_html = MessageView.renderAsideMessage(recent_message, gitname, gitpass)

    # 侧边栏
    aside = AsideView.render(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages(),
                            recent_article=recent_article_html,
                            recent_message=recent_message_html)
    
    # 目录
    article_number_per_page = 20
    articles = ArticleModel.getArticleListPage(page, article_number_per_page)
    pages = ArticleModel.getPages(article_number_per_page)
    article_list = ArticleView.renderArticleList(page, articles, pages)

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            header=HeaderView.renderHeader(),
                            aside=aside,
                            article=article_list,
                            footer=FooterView.renderFooter())

