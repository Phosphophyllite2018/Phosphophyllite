from flask import render_template
from . import HeadView , MarkdownView , FooterView , NavView , ArticleView
from . import HeadModel , NavModel , ArticleModel

def renderPage() :
    title = ArticleModel.getLatestTitle()
    birthday = ArticleModel.getLatestBirthday()
    visiting = ArticleModel.getLatestVisiting()
    content = ArticleModel.getLatestContent()
    nav = NavView.render(NavModel.getUsername(), 
                            NavModel.getRuntime(), 
                            NavModel.getVisiting(), 
                            NavModel.getArticles(), 
                            NavModel.getMessages())
    article_html = ArticleView.render(title, birthday, visiting, MarkdownView.renderMarkdown(content))
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            navigation=nav,
                            article=article_html,
                            footer=FooterView.renderFooter())