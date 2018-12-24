import json
import flask
from flask import request , session
from ..Model import BlogModel

# 是否登录
def isLogin() :
    returnJsonData = {}

    try :
        jsonStr  = request.form['json']
        jsonData = json.loads(jsonStr, ensure_ascii=False)

        username = jsonData['username']
        if username in session and session[username] == True :
            returnJsonData['login'] = True
        else :
            returnJsonData['login'] = False

        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 进行登录
def login() :
    returnJsonData = {}

    try :
        jsonStr  = request.form['json']
        jsonData = json.loads(jsonStr, ensure_ascii=False)

        username = jsonData['username']
        password = jsonData['password']
        if(BlogModel.checkPassword(password)) :
            session[username] = True
            returnJsonData['state'] = True
        else :
            session[username] = False
            returnJsonData['state'] = False
            returnJsonData['error'] = "error password"

        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取用户名
def getUsername() :
    returnJsonData = {}

    try :
        # jsonStr  = request.form['json']
        # jsonData = json.loads(jsonStr, ensure_ascii=False)

        returnJsonData['username'] = BlogModel.getUsername()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取运行天数
def getRunDays() :
    returnJsonData = {}

    try :
        # jsonStr  = request.form['json']
        # jsonData = json.loads(jsonStr, ensure_ascii=False)

        returnJsonData['days'] = BlogModel.getRunDays()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取访问量
def getVisitingCount() :
    returnJsonData = {}

    try :
        # jsonStr  = request.form['json']
        # jsonData = json.loads(jsonStr, ensure_ascii=False)

        returnJsonData['count'] = BlogModel.getVisiting()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)

# 增加访问量
def addVisitingCount() :
    returnJsonData = {}

    try :
        # jsonStr  = request.form['json']
        # jsonData = json.loads(jsonStr, ensure_ascii=False)

        BlogModel.addVisiting()
        returnJsonData['state'] = True


    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)

    return json.dumps(returnJsonData, ensure_ascii=False)