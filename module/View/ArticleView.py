from flask import render_template

def render(title, date, reading, content):
    output = render_template("article.html",
                            arcicle_title=title,
                            arcicle_date=date,
                            arcicle_reading=reading,
                            article_content=content)
    return output

def renderEditor() :
    output = render_template("editor.html")
    return output

def renderAsideArticle(recent_article, gitname, gitpass) :
    recent_message_html = ""
    for article in recent_article :
        id = article['id']
        title = article['title']

        recent_message_html += "<p><a href='article?id=%d'>[ %s ]</a><p>" % (id, title)
    return recent_message_html
