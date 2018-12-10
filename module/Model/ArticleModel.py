import sqlite3
from ..Phos import PhosLog

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

def getCount() :
    try :
        sql = "SELECT count(*) FROM article;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

def getLatestTitle() :
    try :
        sql = "SELECT title FROM article ORDER BY id DESC LIMIT 1;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "Title"

def getLatestContent() :
    try :
        sql = "SELECT content FROM article ORDER BY id DESC LIMIT 1;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "Content"

def getLatestBirthday() :
    try :
        sql = "SELECT birthday FROM article ORDER BY id DESC LIMIT 1;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "birthday"
def getLatestVisiting() :
    try :
        sql = "SELECT visiting FROM article ORDER BY id DESC LIMIT 1;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return "visiting"