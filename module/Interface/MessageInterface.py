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
        returnJsonData['id'] = MessageModel.getIdByOrderDesc(order)
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
        returnJsonData['name'] = MessageModel.getNameById(id)
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
        returnJsonData['date'] = MessageModel.getDateById(id)
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
        returnJsonData['markdown'] = MessageModel.getMarkdownById(id)
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
        returnJsonData['html'] = MessageModel.getHtmlById(id)
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
        returnJsonData['name'] = MessageModel.getNameById(id)
        returnJsonData['date'] = MessageModel.getDateById(id)
        returnJsonData['markdown'] = MessageModel.getMarkdownById(id)
        returnJsonData['html'] = MessageModel.getHtmlById(id)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取页数
def pages() :
    returnJsonData = {}

    try :
        returnJsonData['pages'] = MessageModel.getPageCount()
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 留言列表
def getList() :
    returnJsonData = {}

    try :
        page = request.json['page']
        
        returnJsonData['message'] = MessageModel.getMessagePage(page)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 侧边栏留言
def getAside() :
    returnJsonData = {}
    try :
        returnJsonData['message'] = MessageModel.getList(0, 10)
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