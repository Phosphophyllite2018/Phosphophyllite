from flask import render_template
from .View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView
from .Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage() :
    # GitHub用户名密码
    gitname = MarkdownModel.getGitName()
    gitpass = MarkdownModel.getGitPass()

    # 最近文章
    recent_article = ""

    # 最近留言
    recent_message = MessageModel.getLatestMessage(10)
    recent_message_html = MessageView.renderNavMessage(recent_message, gitname, gitpass)

    # 导航栏
    nav = AsideView.render(AsideModel.getUsername(), 
                            AsideModel.getRuntime(), 
                            AsideModel.getVisiting(), 
                            AsideModel.getArticles(), 
                            AsideModel.getMessages(),
                            recent_article,
                            "")

    # article块
    article_html = MessageView.renderMessagePage(recent_message, gitname, gitpass)

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            navigation=nav,
                            article=article_html,
                            footer=FooterView.renderFooter())