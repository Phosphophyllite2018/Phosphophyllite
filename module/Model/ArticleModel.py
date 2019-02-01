import math
import sqlite3
from ..Phos import PhosLog 
from ..Phos.common import sqlCheck , sqlFilter
from . import MarkdownModel

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
columns = ("id", "title", "markdown", "html", "date", "reading", "category")


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

# 根据id查标题
def getTitleById(id) :
    try :
        sql = "SELECT title FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id查Markdown
def getMarkdownById(id) :
    try :
        sql = "SELECT markdown FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id查HTML
def getHtmlById(id) :
    try :
        sql = "SELECT html FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        output = result.fetchone()
        if output[0] == None :
            return refreshHtml(id)
        else:
            return output[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id查日期
def getDateById(id) :
    try :
        sql = "SELECT date FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id查阅读量
def getReadingById(id) :
    try :
        sql = "SELECT reading FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据id查分类
def getCategoryById(id) :
    try :
        sql = "SELECT category FROM article where id=?;" 
        params = (id,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查ID
def getIdByOrder(order) :
    try :
        sql = "SELECT id FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查标题
def getTitleByOrder(order) :
    try :
        sql = "SELECT title FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查Markdown
def getMarkdownByOrder(order) :
    try :
        sql = "SELECT markdown FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查HTML
def getHtmlByOrder(order) :
    try :
        sql = "SELECT html FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        output = result.fetchone()
        if output[0] == None :
            return refreshHtml(getIdByOrder(order))
        else:
            return output[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查日期
def getDateByOrder(order) :
    try :
        sql = "SELECT date FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查阅读量
def getReadingByOrder(order) :
    try :
        sql = "SELECT reading FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 根据排序查分类
def getCategoryByOrder(order) :
    try :
        sql = "SELECT category FROM article ORDER BY id DESC LIMIT ?,1;" 
        params = (order,)
        result = cursor().execute(sql, params)
        return result.fetchone()[0]
    except Exception as e:
        PhosLog.log(e)
        return None

# 修改HTML
def setHtmlById(id, html) :
    sql = "UPDATE article SET html=? WHERE id=?;"
    params = (html,id)
    cursor().execute(sql, params)
    print('setHtmlById')

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


# 获取文章数据
def get(key, id_or_order, method='id') :
    try :
        if method == 'id' :
            return getById(key, id_or_order)
        elif method == 'order' :
            return getByOrder(key, id_or_order)
        else :
            PhosLog.log('Invalid method')
            return None
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
        markdown = sqlFilter(content)
        html = MarkdownModel.renderMarkdown(markdown)

        if id == None or not isExist(int(id)):
            sql = "INSERT INTO article VALUES(NULL, ?, ?, ?, datetime('now'), 0, 0);"
            params = (title, markdown, html)
        else :
            sql = "UPDATE article SET title=?, markdown=?, html=? WHERE id=?;" 
            params = (title, markdown, html, id) 

        cursor().execute(sql, params)
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
def getRecentArticle(n = 10) :
    recent_article = []

    if getCount() < n :
        n = getCount()
        
    for i in range(0, n) :
        recent_article.append({
            "id"         : getIdByOrder(i),
            "title"      : getTitleByOrder(i),
            # "date"       : getDateByOrder(i),
            # "reading"    : getReadingByOrder(i),
            # "category"   : getCategoryByOrder(i)
            # "markdown"   : getMarkdownByOrder(i),
            # "html"       : getHtmlByOrder(i)
        })

    return recent_article

# 获取最近第num_start到第num_end篇文章
def getArticleList(num_start, num_end) :
    article_list = []
    if getCount() < num_start :
        num_start = getCount()
    if getCount() < num_end :
        num_end = getCount()
    for i in range(num_start, num_end) :
        article_list.append({
            "id"         : getIdByOrder(i),
            "title"      : getTitleByOrder(i),
            "date"       : getDateByOrder(i),
            "reading"    : getReadingByOrder(i),
            # "category"   : getCategoryByOrder(i)
            # "markdown"   : getMarkdownByOrder(i),
            # "html"       : getHtmlByOrder(i)
        })
        
    return article_list

# 按页获取文章列表， page从1开始
def getPage(page, perpage=20) :
    num_start = (perpage * page)
    num_end   = (perpage * (page+1))

    return getArticleList(num_start, num_end)


# 获取总页数
def getPages(perpage=20) : 
    return math.ceil(getCount() / perpage)

# 刷新html
def refreshHtml(id) :
    try:
        md = getMarkdownById(id)
        html = MarkdownModel.renderMarkdown(md)
        if html != None :
            setHtmlById(id, html)
            return html
    except Exception as e:
        PhosLog.log(e)
        return None