from flask import render_template

def render(username, runtime, visiting, articles, messages) :
    output = render_template('nav.html',
                            name=username,
                            running_time=runtime,
                            visiting_count=visiting,
                            artcile_count=articles,
                            message_count=messages)
    return output