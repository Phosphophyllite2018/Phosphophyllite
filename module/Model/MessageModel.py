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

# 根据id查询name属性
def getNameById(id) :
    sql = "SELECT name FROM message WHERE id=?;"
    params = (id,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据id查询date属性
def getDateById(id) :
    sql = "SELECT date FROM message WHERE id=?;"
    params = (id,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据id查询markdown属性
def getMarkdownById(id) :
    sql = "SELECT markdown FROM message WHERE id=?;"
    params = (id,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据id查询html属性
def getHtmlById(id) :
    sql = "SELECT html FROM message WHERE id=?;"
    params = (id,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据排序查询id属性
def getIdByOrderDesc(order) :
    sql = "SELECT id FROM message ORDER BY id DESC LIMIT ?,1;"
    params = (order,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据排序查询name属性
def getNameByOrderDesc(order) :
    sql = "SELECT name FROM message ORDER BY id DESC LIMIT ?,1;"
    params = (order,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据排序查询date属性
def getDateByOrderDesc(order) :
    sql = "SELECT date FROM message ORDER BY id DESC LIMIT ?,1;"
    params = (order,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据排序查询markdown属性
def getMarkdownByOrderDesc(order) :
    sql = "SELECT markdown FROM message ORDER BY id DESC LIMIT ?,1;"
    params = (order,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

# 根据排序查询html属性
def getHtmlByOrderDesc(order) :
    sql = "SELECT html FROM message ORDER BY id DESC LIMIT ?,1;"
    params = (order,)
    result = cursor().execute(sql, params)
    output = result.fetchone()
    return output[0]

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

# 刷新渲染HTML
def represhHtml(id) :
    try:
        pass
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

    for i in range(count) :
        recent_message.append({
            "id"        : getIdByOrderDesc(start + i),
            "name"      : getNameByOrderDesc(start + i),
            "date"      : getDateByOrderDesc(start + i),
            "markdown"  : getMarkdownByOrderDesc(start + i),
            "html"      : getHtmlByOrderDesc(start + i)
        })

    return recent_message

def getPageCount(perpage=40) :
    return math.ceil(getCount() / perpage)

# 返回第n页留言
def getMessagePage(page, perpage=40) :
    recent_message = []
    if page == 1 :
        start = 0
    else :
        start = perpage * page + 1
    n = perpage * page 
    if getCount() < n :
        n = getCount()

    return getList(start, n)