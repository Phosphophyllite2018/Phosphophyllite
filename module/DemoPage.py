# 示例页面

from flask import render_template
from .View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView
from .Model import HeadModel , AsideModel , MarkdownModel , MessageModel

def renderPage() :
    demo_article = open('README.md', "r", encoding='utf-8').read()

    # GitHub用户名密码
    gitname = MarkdownModel.getGitName()
    gitpass = MarkdownModel.getGitPass()

    # 文章
    article_html = ArticleView.render("示例文章", "2018-12-07", "520", 
                                    MarkdownView.renderMarkdown(demo_article, gitname, gitpass))

    # 最近文章
    recent_article = ""

    # 最近留言
    recent_message = MessageModel.getLatestMessage(10)
    recent_message_html = MessageView.renderAsideMessage(recent_message, gitname, gitpass)

    # 侧边栏
    aside = AsideView.render(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages(),
                            recent_article=recent_article,
                            recent_message=recent_message_html)

    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            aside=aside,
                            article=article_html,
                            footer=FooterView.renderFooter())