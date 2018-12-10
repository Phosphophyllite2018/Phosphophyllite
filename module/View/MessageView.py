from flask import render_template
from . import MarkdownView
from ..Phos import PhosLog

# 导航栏上的最近留言
def renderNavMessage(recent_message, gitname, gitpass) :
    recent_message_html = ""
    for message in recent_message :
        name = message['name']
        date = message['birthday']
        content = message['content']
        recent_message_html += "<span class='visitor'>[ %s ]</span>" % name
        # recent_message_html += "<em>( %s )</em>" % date
        recent_message_html += MarkdownView.renderMarkdown(content, gitname, gitpass)
    return recent_message_html

# 留言页面上的留言
def renderMessagePage(recent_message, gitname, gitpass) :
    recent_message_html = ""
    for message in recent_message :
        name = message['name']
        date = message['birthday']
        content = message['content']
        recent_message_html += "<hr/>"
        recent_message_html += "<span class='visitor'>[ %s ]</span>" % name
        recent_message_html += "<em>( %s )</em>" % date
        recent_message_html += MarkdownView.renderMarkdown(content, gitname, gitpass)
    return render_template("message.html", recent_message=recent_message_html)