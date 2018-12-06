# 示例页面

from flask import render_template
from . import HeadView , HeadModel , MarkdownView , FooterView

def render() :
    demo_article = open('README.md', "r", encoding='utf-8').read()
    return render_template('template.html', 
                            css_settings=HeadView.renderCSS(HeadModel.getCSS()),
                            js_settings=HeadView.renderJS(HeadModel.getJS()),
                            title="Phosphophyllite",
                            article=MarkdownView.renderMarkdown(demo_article),
                            footer=FooterView.renderFooter())