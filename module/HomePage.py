from flask import render_template
from .View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView
from .Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage() :
    # 文章
    title = ArticleModel.getLatestTitle()
    birthday = ArticleModel.getLatestBirthday()
    visiting = ArticleModel.getLatestVisiting()
    content = ArticleModel.getLatestContent()

    # GitHub用户名密码
    gitname = MarkdownModel.getGitName()
    gitpass = MarkdownModel.getGitPass()

    # 最近文章
    recent_article = ""

    # 最近留言
    recent_message = MessageModel.getLatestMessage(10)
    recent_message_html = MessageView.renderAsideMessage(recent_message, gitname, gitpass)

    # 侧边栏
    aside = AsideView.render(AsideModel.getUsername(), 
                            AsideModel.getRuntime(), 
                            AsideModel.getVisiting(), 
                            AsideModel.getArticles(), 
                            AsideModel.getMessages(),
                            recent_article,
                            recent_message_html)

    article_html = ArticleView.render(title, birthday, visiting, MarkdownView.renderMarkdown(content))
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            aside=aside,
                            article=article_html,
                            footer=FooterView.renderFooter())