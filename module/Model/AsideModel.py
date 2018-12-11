import sqlite3
import time
from ..Phos import PhosLog

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

def getUsername() :
    try :
        sql = "SELECT username FROM blog WHERE id = 0;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "Phosphophyllite"

def getRuntime() :
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

def getArticles() :
    try :
        sql = "SELECT count(*) FROM article;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

def getMessages() :
    try :
        sql = "SELECT count(*) FROM message;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0