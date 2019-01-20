import sqlite3
import math
from ..Phos import PhosLog
from ..Phos.common import sqlFilter , sqlCheck
from . import MarkdownModel

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

# 列名，做sql语句校验
columns = ("id", "name", "markdown", "html", "date")

# 返回行数
def getCount() :
    try :
        sql = "SELECT count(*) FROM message;"
        result = cursor().execute(sql)
        output = result.fetchone()
        if output == None :
            raise RuntimeError('SELECT count(*) failed')
        else :
            return output[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

# 根据id查找
def getById(key, id) :
    try :
        sqlCheck(columns, key)
        sql = "SELECT ? FROM message where id=?;"
        params = (key, id)
        result = cursor().execute(sql, params)
        output = result.fetchone()
        if output == None :
            raise RuntimeError("SELECT %s FROM message where id=%d;" % params)
        else :
            return output[0]
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
        output = result.fetchone()
        if output == None :
            raise RuntimeError("SELECT %s FROM message where id=%d;" % params)
        else :
            return output[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 添加Message
def append(name, content) :
    try :
        if name.strip() == "" :
            name = "匿名"  

        html = MarkdownModel.renderMarkdown(content)
        sql = "INSERT INTO message VALUES(NULL, ?, ?, ?, datetime('now'));" 
        params = (name, content, html)
        cursor().execute(sql, params)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

# 删除留言
def delete(id) :
    try :
        sql = "DELETE FROM message WHERE id=%d;" % id
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

# 返回最近的start条留言
def getList(start, count) :
    recent_message = []

    if getCount() < start + count :
        count = getCount()

    for i in range(1, count + 1) :
        recent_message.append({
            "id"        : getByOrder("id", -(start+i)),
            "name"      : getByOrder("name", -(start+i)),
            "date"      : getByOrder("date", -(start+i)),
            "markdown"  : getByOrder("markdown", -(start+i)),
            "html"      : getByOrder("html", -(start+i))
        })

    return recent_message

def getPages(perpage) :
    return math.ceil(getCount() / perpage)

# 返回第n页留言
def getMessages(page, perpage=20) :
    recent_message = []
    if page == 1 :
        start = 1
    else :
        start = perpage * (page-1) + 1
    n = perpage * page 
    if getCount() < n :
        n = getCount()

    for i in range(start, n + 1) :
        recent_message.append({
            "id"        : getByOrder("id", -i),
            "name"      : getByOrder("name", -i),
            "birthday"  : getByOrder("birthday", -i),
            "content"   : getByOrder("content", -i)
        })

    return recent_message