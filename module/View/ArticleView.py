from flask import render_template
from ..Phos.common import textFilter

# 渲染一篇文章
def render(title, date, reading, content):
    output = render_template("article.html",
                            arcicle_title=title,
                            arcicle_date=date,
                            arcicle_reading=reading,
                            article_content=content)
    return output

# 渲染文章编辑器
def renderEditor(id=0) :
    output = render_template("admin/editor.html", article_id=id)
    return output

# 渲染侧边栏文章列表
def renderAsideArticleList(recent_article, gitname, gitpass) :
    recent_message_html = ""
    for article in recent_article :
        id = article['id']
        title = str(article['title'])

        recent_message_html += "<p><a href='/article?id=%d'> %s </a><p>" % (id, textFilter(title))
    return recent_message_html

# 渲染管理页面文章列表
def renderAdminArticleList(page, articles, total_pages) :
    prev = ("/admin/article_list?page=%d" % (page - 1)) if page - 1 > 0 else ""
    next = ("/admin/article_list?page=%d" % (page + 1)) if page + 1 <= total_pages else ""
    return render_template("admin/article_list.html",
                            page=page,
                            total_pages=total_pages,
                            prev=prev,
                            next=next,
                            article_list=articles)

# 渲染文章列表
def renderArticleList(page, articles, total_pages) :
    prev = ("/article_list?page=%d" % (page - 1)) if page - 1 > 0 else ""
    next = ("/article_list?page=%d" % (page + 1)) if page + 1 <= total_pages else ""
    return render_template("article_list.html",
                            page=page,
                            total_pages=total_pages,
                            prev=prev,
                            next=next,
                            article_list=articles)
