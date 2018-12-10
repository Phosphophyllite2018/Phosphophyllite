import sqlite3
from ..Phos import PhosLog

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