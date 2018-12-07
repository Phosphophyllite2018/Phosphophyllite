# 示例页面

from flask import render_template
from . import HeadView , HeadModel , MarkdownView , FooterView , NavView , ArticleView

def render() :
    demo_article = open('README.md', "r", encoding='utf-8').read()
    article_html = ArticleView.render("示例文章", "2018-12-07", "520", MarkdownView.renderMarkdown(demo_article))
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            navigation=NavView.renderNav(),
                            article=article_html,
                            footer=FooterView.renderFooter())