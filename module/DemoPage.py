# 示例页面

from flask import render_template
from .View import HeadView , MarkdownView , FooterView , NavView , ArticleView
from .Model import HeadModel , NavModel

def renderPage() :
    demo_article = open('README.md', "r", encoding='utf-8').read()
    nav = NavView.render(NavModel.getUsername(), 
                            NavModel.getRuntime(), 
                            NavModel.getVisiting(), 
                            NavModel.getArticles(), 
                            NavModel.getMessages())
    article_html = ArticleView.render("示例文章", "2018-12-07", "520", MarkdownView.renderMarkdown(demo_article))
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            navigation=nav,
                            article=article_html,
                            footer=FooterView.renderFooter())