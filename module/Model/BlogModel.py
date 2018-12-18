import sqlite3
import hashlib
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

def checkPassword(pswd) :
    try :
        sha256 = hashlib.sha256()
        sha256.update(pswd.encode('utf-8'))
        pswd = sha256.hexdigest()
        sql = "SELECT password FROM blog WHERE id = 0;"
        result = cursor().execute(sql)
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

def addVisiting() :
    try :
        value = getVisiting() + 1
        sql = "UPDATE blog SET visiting=%d WHERE id = 0;" % value
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

