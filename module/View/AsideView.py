from flask import render_template

def render(username, runtime, visiting, articles, messages,recent_article,recent_message) :
    output = render_template('aside.html',
                            name=username,
                            running_time=runtime,
                            visiting_count=visiting,
                            artcile_count=articles,
                            message_count=messages,
                            recent_article=recent_article,
                            recent_message=recent_message)
    return output