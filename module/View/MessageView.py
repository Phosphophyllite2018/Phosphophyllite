from flask import render_template
from . import MarkdownView
from ..Phos import PhosLog

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