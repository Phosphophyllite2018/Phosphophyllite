import sqlite3
from ..Phos import PhosLog
from ..Phos.common import sqlFilter , sqlCheck

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

# 列名，做sql语句校验
columns = ("id", "name", "content", "birthday")

# 返回行数
def getCount() :
    try :
        sql = "SELECT count(*) FROM message;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

# 根据id查找
def getById(key, id) :
    try :
        sqlCheck(columns, key)
        sql = "SELECT %s FROM message where id=%d;" % (key, id)
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查找
# 整数正序，负数逆序
def getByOrder(key, num) :
    try :
        sqlCheck(columns, key)
        sql = ""
        if num > 0 :
            sql = "SELECT %s FROM message ORDER BY id LIMIT %d,1;" % (key, num-1)
        else :
            sql = "SELECT %s FROM message ORDER BY id DESC LIMIT %d,1;" % (key, abs(num)-1)
            
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 添加Message
def append(name, content) :
    try :
        if name.strip() == "" :
            name = "匿名"  
        name = sqlFilter(name)
        content = sqlFilter(content)
        sql = "INSERT INTO message VALUES(NULL,'%s','%s', datetime('now'));" % (name, content)
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

# 返回最近的n条留言
def getRecentMessage(n) :
    recent_message = []

    if getCount() < n :
        n = getCount()

    for i in range(1, n + 1) :
        recent_message.append({
            "id"        : getByOrder("id", -i),
            "name"      : getByOrder("name", -i),
            "birthday"  : getByOrder("birthday", -i),
            "content"   : getByOrder("content", -i)
        })

    return recent_message