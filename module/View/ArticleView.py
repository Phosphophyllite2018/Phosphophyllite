from flask import render_template
from ..Phos.common import textFilter

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
        title = str(article['title'])

        recent_message_html += "<p><a href='article?id=%d'> %s </a><p>" % (id, textFilter(title))
    return recent_message_html

def renderArticleList(page, articles, total_pages) :
    prev = ("/article_list?page=%d" % (page - 1)) if page - 1 > 0 else ""
    next = ("/article_list?page=%d" % (page + 1)) if page + 1 > total_pages else ""
    return render_template("admin/article_list.html",
                            page=page+1,
                            total_pages=total_pages,
                            prev=prev,
                            next=next,
                            article_list=articles)
