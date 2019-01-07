import sqlite3
from ..Phos import PhosLog
from ..Phos.common import textFilter
import requests
import json

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

def loadArticle(id) :
    pass

def saveArticle(data) :
    pass

def getGitName() :
    try :
        sql = "SELECT git_name FROM blog;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

def getGitPass() :
    try :
        sql = "SELECT git_pass FROM blog;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

def renderMarkdown(md_text, timeout=15) :
    try :
        if md_text == None :
            return None
        
        # 获取用户名密码
        gitname = getGitName()
        gitpass = getGitPass()

        # 请求信息
        payload = {"text" : md_text, "mode" : "gfm", "context" : "https://github.com/Phosphophyllite2018/Phosphophyllite"}

        # 带身份验证的请求
        response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), auth=(gitname,gitpass), timeout=timeout)
        
        # 带身份验证请求失败，不带身份验证请求
        if response.status_code != 200 :
            response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), timeout=timeout)
        
        # 不带身份验证请求仍然失败
        if response.status_code != 200 :
            PhosLog.log("Render Markdown Failed.")
            return None

        # 任意一次请求成功
        else :
            output = response.text #.encode("utf-8").decode("utf-8")

        return output

    except Exception as e:
        PhosLog.log("Render Markdown Failed.")
        PhosLog.log(e)
        return None