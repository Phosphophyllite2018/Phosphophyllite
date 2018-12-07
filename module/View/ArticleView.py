from flask import render_template

def render(title, date, reading, content):
    output = render_template("article.html",
                            arcicle_title=title,
                            arcicle_info="日期 : %s  阅读量 : %s" % (date, reading),
                            article_content=content)
    return output