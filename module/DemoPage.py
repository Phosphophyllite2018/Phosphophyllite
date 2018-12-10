# 示例页面

from flask import render_template
from .View import HeadView , MarkdownView , FooterView , NavView , ArticleView
from .Model import HeadModel , NavModel , MarkdownModel , MessageModel

def renderPage() :
    demo_article = open('README.md', "r", encoding='utf-8').read()

    

    # 文章
    article_html = ArticleView.render("示例文章", "2018-12-07", "520", 
                                    MarkdownView.renderMarkdown(demo_article, 
                                                                MarkdownModel.getGitName(),
                                                                MarkdownModel.getGitPass()))

    # 最近文章
    recent_article = ""

    # 最近留言
    recent_message = MessageModel.getLatestMessage(10)
    recent_message_html = ""
    for message in recent_message :
        recent_message_html += "<p> %s </p>" % message

    # 导航栏
    nav = NavView.render(NavModel.getUsername(), 
                            NavModel.getRuntime(), 
                            NavModel.getVisiting(), 
                            NavModel.getArticles(), 
                            NavModel.getMessages(),
                            recent_article,
                            recent_message_html)

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            navigation=nav,
                            article=article_html,
                            footer=FooterView.renderFooter())