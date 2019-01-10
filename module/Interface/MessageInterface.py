import flask
import json
from flask import request
from ..Phos import PhosLog
from ..Model import MessageModel , BlogModel

# 留言数量
def count() :
    returnJsonData = {}

    try :
        returnJsonData['count'] = MessageModel.getCount()

        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 留言ID
def getIdByOrder() :
    returnJsonData = {}

    try :
        order = request.json['order']
        returnJsonData['id'] = MessageModel.getByOrder('id',order)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 留言访客名
def visitorName() :
    returnJsonData = {}

    try :
        id = request.json['id']
        returnJsonData['name'] = MessageModel.getByOrder('name',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 留言日期
def date() :
    returnJsonData = {}

    try :
        id = request.json['id']
        returnJsonData['date'] = MessageModel.getByOrder('date',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 留言内容
def markdown() :
    returnJsonData = {}

    try :
        id = request.json['id']
        returnJsonData['markdown'] = MessageModel.getByOrder('markdown',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 留言内容
def html() :
    returnJsonData = {}

    try :
        id = request.json['id']
        returnJsonData['html'] = MessageModel.getByOrder('html',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 留言全部数据
def total() :
    returnJsonData = {}

    try :
        id = request.json['id']
        returnJsonData['name'] = MessageModel.getByOrder('name',id)
        returnJsonData['date'] = MessageModel.getByOrder('date',id)
        returnJsonData['markdown'] = MessageModel.getByOrder('markdown',id)
        returnJsonData['html'] = MessageModel.getByOrder('html',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 留言列表
def list() :
    returnJsonData = {}

    try :
        start = request.json['start'] or 1
        count = request.json['count']
        
        returnJsonData['name'] = MessageModel.getByOrder('name',id)
        returnJsonData['date'] = MessageModel.getByOrder('date',id)
        returnJsonData['markdown'] = MessageModel.getByOrder('markdown',id)
        returnJsonData['html'] = MessageModel.getByOrder('html',id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 留言保存
def save() :
    returnJsonData = {}

    try :
        name = request.json['name']
        content = request.json['content']
        if MessageModel.append(name, content) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
        returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 留言删除
def delete() :
    returnJsonData = {}

    try :
        id = request.json['id']
        username =request.json['username']
        if not BlogModel.isLogin(username) :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'please-login'
        elif MessageModel.delete(id) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)