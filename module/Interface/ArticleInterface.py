import json
import flask
from flask import request
from ..Phos import PhosLog 
from ..Phos.common import isLogin
from ..Model import ArticleModel

# 文章数量
def count() :
    returnJsonData = {}

    try :
        returnJsonData['count'] = ArticleModel.getCount()

        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章ID
def getIdByOrder() :
    returnJsonData = {}

    try :
        order = request.json['order']
        returnJsonData['count'] = ArticleModel.getByOrder('id',order)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章标题
def title() :
    returnJsonData = {}

    try :
        id = request.json['id']

        returnJsonData['title'] = ArticleModel.getById('title', id)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章日期
def date() :
    returnJsonData = {}

    try :
        id = request.json['id']

        returnJsonData['date'] = ArticleModel.getById('date', id)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章阅读量
def readingCount() : 
    returnJsonData = {}

    try :
        id = request.json['id']

        returnJsonData['reading'] = ArticleModel.getById('reading', id)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章内容
def content():
    returnJsonData = {}

    try :
        id = request.json['id']

        returnJsonData['title'] = ArticleModel.getById('title', id)
        returnJsonData['date'] = ArticleModel.getById('date', id)
        returnJsonData['reading'] = ArticleModel.getById('reading', id)
        returnJsonData['content'] = ArticleModel.getById('content', id)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章完整数据
def total():
    returnJsonData = {}

    try :
        id = request.json['id']

        returnJsonData['content'] = ArticleModel.getById('content', id)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


def save() :
    if not isLogin() :
        return flask.redirect('/login')

    id = request.form['id']
    print(id)
    name = request.form['title']
    content = request.form['content']
    ArticleModel.save(name, content, id)

    return flask.redirect('/admin/article_list')

def delete() :
    if not isLogin() :
        return flask.redirect('/login')

    id = int(request.form['id'])
    ArticleModel.delete(id)

    return flask.redirect('/admin/article_list')