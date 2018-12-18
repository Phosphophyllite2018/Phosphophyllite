import math
import sqlite3
from ..Phos import PhosLog 
from ..Phos.common import sqlCheck , sqlFilter

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


# 根据id查找
def getById(key, id) :
    try :
        sqlCheck(columns, key)
        sql = "SELECT %s FROM article where id=%d;" % (key, id)
        result = cursor().execute(sql)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id设置
def setById(key, id, value) :
    try :
        sqlCheck(columns, key)
        if isinstance(value, str) :
            value = sqlFilter(value)
        sql = "UPDATE article SET %s='%s' where id=%d;" % (key, value, id)
        cursor().execute(sql)
        return True
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

# 删除文章
def delete(id) :
    try:
        sql = "DELETE FROM article WHERE id=%d" % id
        
        cursor().execute(sql)
        return True
    except Exception as e:
        PhosLog.log(e)
        return False

# 访问量增加
def addVisiting(id, n=1) :
    try :
        visiting = getById('visiting', id)
        setById('visiting', id, visiting+1)
    except Exception as e:
        PhosLog.log(e)
        return False

# 返回最近的n篇文章
def getRecentArticle(n) :
    recent_article = []

    if getCount() < n :
        n = getCount()
        
    for i in range(1, n + 1) :
        recent_article.append({
            "id"         : getByOrder("id", -i),
            "title"      : getByOrder("title", -i),
            "birthday"   : getByOrder("birthday", -i),
            "content"    : getByOrder("content", -i),
            "visiting"   : getByOrder("visiting", -i)
        })

    return recent_article

# 获取最近第num_start到第num_end篇文章
def getArticleList(num_start, num_end) :
    article_list = []
    if getCount() < num_start :
        num_start = getCount()
    if getCount() < num_end :
        num_end = getCount() + 1
    for i in range(num_start, num_end) :
        article_list.append({
            "id"         : getByOrder("id", -i),
            "title"      : getByOrder("title", -i),
            "birthday"   : getByOrder("birthday", -i),
            "visiting"   : getByOrder("visiting", -i)
        })
        
    return article_list

# 按页获取文章列表， page从0开始
def getArticleListPage(page, perpage) :
    num_start = (perpage * page + 1)
    num_end   = (perpage * (page + 1) + 1)

    return getArticleList(num_start, num_end)


# 获取总页数
def getPages(perpage) : 
    return math.ceil(getCount() / perpage)