import json
import flask
from flask import request , session
from ..Phos import PhosLog 
from ..Model import BlogModel

# 是否登录
def isLogin() :
    returnJsonData = {}

    try :
        username = request.json['username']
        returnJsonData['state'] = BlogModel.isLogin(username)

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 进行登录
def login() :
    returnJsonData = {}

    try :
        username = request.json['username']
        password = request.json['password']
        if(BlogModel.checkPassword(password)) :
            session[username] = True
            returnJsonData['state'] = True
        else :
            session[username] = False
            returnJsonData['state'] = False
            returnJsonData['error'] = "error password"

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取头像
def getAvatar() :
    returnJsonData = {}
    try :

        returnJsonData['avatar'] = BlogModel.getAvatar()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)


# 获取用户名
def getUsername() :
    returnJsonData = {}

    try :

        returnJsonData['username'] = BlogModel.getUsername()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取运行天数
def getRunDays() :
    returnJsonData = {}

    try :

        returnJsonData['days'] = BlogModel.getRunDays()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取访问量
def getVisitingCount() :
    returnJsonData = {}

    try :

        returnJsonData['count'] = BlogModel.getVisiting()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 增加访问量
def addVisitingCount() :
    returnJsonData = {}

    try :

        BlogModel.addVisiting()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)

    return json.dumps(returnJsonData, ensure_ascii=False)