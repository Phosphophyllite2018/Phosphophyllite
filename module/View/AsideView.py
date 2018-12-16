from flask import render_template

def render(**kwargs) :
    output = render_template('aside.html',
                            username=kwargs['username'],
                            running_days=kwargs['running_days'],
                            visiting_count=kwargs['visiting_count'],
                            artcile_count=kwargs['artcile_count'],
                            message_count=kwargs['message_count'],
                            recent_article=kwargs['recent_article'],
                            recent_message=kwargs['recent_message'])
    return output

def renderAdminAside(**kwargs) :
    output = render_template('admin_aside.html',
                            username=kwargs['username'],
                            running_days=kwargs['running_days'],
                            visiting_count=kwargs['visiting_count'],
                            artcile_count=kwargs['artcile_count'],
                            message_count=kwargs['message_count'])
    return output