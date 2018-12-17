import flask
from flask import render_template , session
from .View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView
from .Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage() :
    if 'login' not in session or session['login'] != True :
        return flask.redirect('/login')

    # GitHub用户名密码
    gitname = MarkdownModel.getGitName()
    gitpass = MarkdownModel.getGitPass()

    # 最近文章
    recent_article = ArticleModel.getRecentArticle(10)
    recent_article_html = ArticleView.renderAsideArticle(recent_article, gitname, gitpass)

    # 最近留言
    recent_message = MessageModel.getRecentMessage(10)
    recent_message_html = MessageView.renderAsideMessage(recent_message, gitname, gitpass)

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
                            aside=aside,
                            article=editor_html,
                            footer=FooterView.renderFooter())