from flask import render_template

def render(title, date, reading, content):
    output = render_template("article.html",
                            arcicle_title=title,
                            arcicle_date=date,
                            arcicle_reading=reading,
                            article_content=content)
    return output