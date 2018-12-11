import sqlite3
from ..Phos import PhosLog

def cursor() :
    db = sqlite3.connect("./private/phosphophyllite.db", isolation_level=None)
    cursor = db.cursor()
    return cursor

# 返回行数
def getCount() :
    try :
        sql = "SELECT count(*) FROM article;"
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return 0

# 列名，做sql语句校验
columns = ("id", "title", "content", "birthday", "visiting")
# 检查key
def sqlCheck(key, id) :
    if key not in columns :
        raise Exception("Key %s is invalid." % key)
    elif not isinstance(id, int) :
        raise Exception("Id %d is invalid." % id)

# 将'替换为''
def sqlFilter(text) :
    text = text.replace("'", "''")
    return text

# 根据id查找
def getById(key, id) :
    try :
        sqlCheck(key, id)
        sql = "SELECT %s FROM article where id=%d;" % (key, id)
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查找
# 整数正序，负数逆序
def getByOrder(key, num) :
    try :
        sqlCheck(key, num)
        sql = ""
        if num > 0 :
            sql = "SELECT %s FROM article ORDER BY id LIMIT %d,1;" % (key, num-1)
        else :
            sql = "SELECT %s FROM article ORDER BY id DESC LIMIT %d,1;" % (key, abs(num)-1)
            
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 检查文章id是否存在
def isExist(id) :
    try :
        rId = getById("id", id)
        if rId == None :
            return False
        else :
            return True
    except Exception as e:
        PhosLog.log(e)
        return None

# 保存文章
def save(title, content, id=None) :
    try :
        title = sqlFilter(title)
        content = sqlFilter(content)
        sql = ""
        if id == None or isExist(id):
            sql = "INSERT INTO article VALUES(NULL, '%s', '%s', datetime('now'), 0);" % (title, content)
        else :
            sql = "UPDATE article SET title='%s',content='%s' WHERE id=%d;" % (title, content, id) 
            
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

# def getLatestTitle() :
#     try :
#         sql = "SELECT title FROM article ORDER BY id DESC LIMIT 1;"
#         result = cursor().execute(sql)
#         return result.fetchone()[0]
#     except Exception as e:
#         PhosLog.log(e)
#         return "Title"

# def getLatestContent() :
#     try :
#         sql = "SELECT content FROM article ORDER BY id DESC LIMIT 1;"
#         result = cursor().execute(sql)
#         return result.fetchone()[0]
#     except Exception as e:
#         PhosLog.log(e)
#         return "Content"

# def getLatestBirthday() :
#     try :
#         sql = "SELECT birthday FROM article ORDER BY id DESC LIMIT 1;"
#         result = cursor().execute(sql)
#         return result.fetchone()[0]
#     except Exception as e:
#         PhosLog.log(e)
#         return "birthday"
# def getLatestVisiting() :
#     try :
#         sql = "SELECT visiting FROM article ORDER BY id DESC LIMIT 1;"
#         result = cursor().execute(sql)
#         return result.fetchone()[0]
#     except Exception as e:
#         PhosLog.log(e)
#         return "visiting"