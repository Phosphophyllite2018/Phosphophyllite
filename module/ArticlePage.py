from flask import render_template
from .View import HeadView , MarkdownView , FooterView , AsideView , ArticleView , MessageView
from .Model import HeadModel , AsideModel , ArticleModel , MessageModel , MarkdownModel

def renderPage(id=None) :
    # 文章
    if id == None :
        title = ArticleModel.getByOrder("title",-1)
        birthday = ArticleModel.getByOrder("birthday",-1)
        visiting = ArticleModel.getByOrder("visiting",-1)
        content = ArticleModel.getByOrder("content",-1)
    else :
        title = ArticleModel.getById("title",id)
        birthday = ArticleModel.getById("birthday",id)
        visiting = ArticleModel.getById("visiting",id)
        content = ArticleModel.getById("content",id)

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
    aside = AsideView.render(username=AsideModel.getUsername(), 
                            running_days=AsideModel.getRunDays(), 
                            visiting_count=AsideModel.getVisiting(), 
                            artcile_count=AsideModel.getArticles(), 
                            message_count=AsideModel.getMessages(),
                            recent_article=recent_article_html,
                            recent_message=recent_message_html)

    article_html = ArticleView.render(title, birthday, visiting, MarkdownView.renderMarkdown(content))
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            aside=aside,
                            article=article_html,
                            footer=FooterView.renderFooter())