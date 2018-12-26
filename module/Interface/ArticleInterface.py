import json
import flask
from flask import request
from ..Phos import PhosLog 
from ..Model import ArticleModel , BlogModel

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
        returnJsonData['id'] = ArticleModel.getByOrder('id',order)
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
        returnJsonData['state'] = True

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
        returnJsonData['state'] = True

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
        returnJsonData['state'] = True

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
        returnJsonData['content'] = ArticleModel.getById('content', id)
        returnJsonData['state'] = True

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
        returnJsonData['title'] = ArticleModel.getById('title', id)
        returnJsonData['date'] = ArticleModel.getById('date', id)
        returnJsonData['reading'] = ArticleModel.getById('reading', id)
        returnJsonData['content'] = ArticleModel.getById('content', id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 修改文章标题
def modifyTitle():
    returnJsonData = {}

    try :
        id = request.json['id']
        title = request.json['title']

        if ArticleModel.setById('title', id, title) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)



# 修改文章内容
def save():
    returnJsonData = {}

    try :
        id = request.json['id']
        title = request.json['title']
        content = request.json['content']
        username =request.json['username']
        if not BlogModel.isLogin(username) :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'please-login'
        elif ArticleModel.save(title, content, id) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 删除文章
def delete() :
    returnJsonData = {}

    try :
        id = request.json['id']
        username =request.json['username']
        if not BlogModel.isLogin(username) :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'please-login'
        elif ArticleModel.delete(id) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)