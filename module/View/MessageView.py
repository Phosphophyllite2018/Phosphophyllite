from flask import render_template
from . import MarkdownView
from ..Phos import PhosLog
from ..Phos.common import textFilter

# 侧边栏的最近留言
def renderAsideMessage(recent_message, gitname, gitpass) :
    recent_message_html = ""
    for message in recent_message :
        name = message['name']
        date = message['birthday']
        content = message['content']

        # 如果没有内容
        if content.strip() == "" :
            continue

        recent_message_html += "<span class='visitor'>[ %s ]</span><br/>" % textFilter(name)
        # recent_message_html += "<em>( %s )</em>" % date
        recent_message_html += MarkdownView.renderMarkdown(content, gitname, gitpass)
    return recent_message_html

# 留言页面上的留言
def renderPageMessage(recent_message, gitname, gitpass) :
    recent_message_html = ""
    for message in recent_message :
        floor = message['id']
        name = message['name']
        date = message['birthday']
        content = message['content']

       # 如果没有内容
        if content.strip() == "" :
            continue
            
        recent_message_html += "<hr/>"
        recent_message_html += "<span class='floor'> #%d </span>" % floor
        recent_message_html += "<span class='visitor'>[ %s ]</span>" % textFilter(name)
        recent_message_html += "<em>( %s )</em><br/>" % date
        recent_message_html += MarkdownView.renderMarkdown(content, gitname, gitpass)
    return render_template("message.html", recent_message=recent_message_html)