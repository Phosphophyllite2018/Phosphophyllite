import sqlite3
import hashlib
import time
import requests
from bs4 import BeautifulSoup
from flask import session
from ..Phos import PhosLog

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

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

def getAvatar() :
    url = "https://github.com/%s" % getGitName() 
    response = requests.get(url)
    if response.status_code != 200 :
        return None
        
    soup = BeautifulSoup(response.text, 'html.parser')
    avatar = soup.find("meta", property="og:image")
    return avatar.attrs['content']

def getUsername() :
    try :
        sql = "SELECT username FROM blog WHERE id = 0;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "Phosphophyllite"

def isLogin(username) :
    return (username in session) and (session[username] == True)

def checkPassword(user, pswd) :
    try :
        sha256 = hashlib.sha256()
        sha256.update(pswd.encode('utf-8'))
        pswd = sha256.hexdigest()
        sql = "SELECT password FROM blog WHERE username=?;"
        params = (user,)
        result = cursor().execute(sql, params)
        if pswd == result.fetchone()[0] :
            return True
        else :
            return False
    except Exception as e:
        PhosLog.log(e)
        return False

def getRunDays() :
    try :
        sql = "SELECT birthday FROM blog WHERE id = 0;"
        result = cursor().execute(sql)
        birthday = time.mktime(time.strptime(result.fetchone()[0], "%Y-%m-%d %H:%M:%S")) 
        now = time.time()
        return int((now - birthday)/(24*60*60))
    except Exception as e:
        PhosLog.log(e)
        return 0

def getVisiting() :
    try :
        sql = "SELECT visiting FROM blog WHERE id = 0;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

def addVisiting(n=1) :
    try :
        value = getVisiting() + n
        sql = "UPDATE blog SET visiting=%d WHERE id = 0;" % value
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

