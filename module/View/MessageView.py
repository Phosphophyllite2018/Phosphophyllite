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
        if not isinstance(content,str) or content.strip() == "" :
            continue

        recent_message_html += "<p><span class='visitor'>[ %s ]</span><br/></p>" % textFilter(name)
        # recent_message_html += "<em>( %s )</em>" % date
        recent_message_html += "<p>" + MarkdownView.renderMarkdown(content, gitname, gitpass) + "</p>"
    return recent_message_html

# 留言页面上的留言
def renderMessageBoard(page, total_pages, messages, gitname, gitpass) :
    recent_message_html = ""
    for message in messages :
        floor = message['id']
        name = message['name']
        date = message['birthday']
        content = message['content']

        # 如果没有内容
        if not isinstance(content,str) or content.strip() == "" :
            continue
            
        recent_message_html += "<br/><span class='floor'> #%d </span>" % floor
        recent_message_html += "<span class='visitor'>[ %s ]</span>" % textFilter(name)
        recent_message_html += "<em>( %s )</em><br/>" % date
        recent_message_html += MarkdownView.renderMarkdown(content, gitname, gitpass)

    prev = ("/message?page=%d" % (page - 1)) if page - 1 > 0 else ""
    next = ("/message?page=%d" % (page + 1)) if page + 1 <= total_pages else ""
    return render_template("message.html", 
                            recent_message=recent_message_html,
                            page=page,
                            total_pages=total_pages,
                            next=next,
                            prev=prev)

def renderAdminMessageList(page, total_pages, messages) :
    prev = ("/admin/message?page=%d" % (page - 1)) if page - 1 > 0 else ""
    next = ("/admin/message?page=%d" % (page + 1)) if page + 1 <= total_pages else ""
    return render_template("/admin/message.html", 
                            message_list=messages,
                            page=page,
                            total_pages=total_pages,
                            next=next,
                            prev=prev)