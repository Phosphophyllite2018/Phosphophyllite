import json
import flask
from flask import request
from ..Phos import PhosLog 
from ..Model import ArticleModel , BlogModel

# 文章数量
def count() :
    returnJsonData = {}

    try :
        returnJsonData['count'] = ArticleModel.getCount()

        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章ID
def getIdByOrder() :
    returnJsonData = {}

    try :
        order = request.json['order']
        returnJsonData['id'] = ArticleModel.getIdByOrder(order)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章标题
def title() :
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['title'] = ArticleModel.getTitleById( id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['title'] = ArticleModel.getTitleByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章日期
def date() :
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['date'] = ArticleModel.getDateById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['date'] = ArticleModel.getDateByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章分类
def category() :
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['category'] = ArticleModel.getCategoryById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['category'] = ArticleModel.getCategoryByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章阅读量
def readingCount() : 
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['reading'] = ArticleModel.getReadingById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['reading'] = ArticleModel.getReadingByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章内容Markdown
def markdown():
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['markdown'] = ArticleModel.getMarkdownById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['markdown'] = ArticleModel.getMarkdownByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 文章内容HTML
def html():
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['html'] = ArticleModel.getHtmlById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['html'] = ArticleModel.getHtmlByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 文章完整数据
def total():
    returnJsonData = {}

    try :
        if 'id' in request.json :
            id = request.json['id']
            returnJsonData['id'] = id
            returnJsonData['title'] = ArticleModel.getTitleById(id)
            returnJsonData['date'] = ArticleModel.getDateById(id)
            returnJsonData['category'] = ArticleModel.getCategoryById(id)
            returnJsonData['reading'] = ArticleModel.getReadingById(id)
            returnJsonData['markdown'] = ArticleModel.getMarkdownById(id)
            returnJsonData['html'] = ArticleModel.getHtmlById(id)
            returnJsonData['state'] = True
        elif 'order' in request.json :
            order = request.json['order']
            returnJsonData['id'] = ArticleModel.getIdByOrder(order)
            returnJsonData['title'] = ArticleModel.getTitleByOrder(order)
            returnJsonData['date'] = ArticleModel.getDateByOrder(order)
            returnJsonData['category'] = ArticleModel.getCategoryByOrder(order)
            returnJsonData['reading'] = ArticleModel.getReadingByOrder(order)
            returnJsonData['markdown'] = ArticleModel.getMarkdownByOrder(order)
            returnJsonData['html'] = ArticleModel.getHtmlByOrder(order)
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'no id or order'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 修改文章阅读量
def modifyReadingCount():
    returnJsonData = {}

    try :
        id = request.json['id']
        reading = request.json['reading']

        if ArticleModel.setById('reading', id, reading) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)



# 保存
def save():
    returnJsonData = {}

    try :
        id = request.json['id']
        title = request.json['title']
        content = request.json['content']
        username =request.json['username']
        if not BlogModel.isLogin(username) :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'please-login'
        elif ArticleModel.save(title, content, id) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 删除文章
def delete() :
    returnJsonData = {}

    try :
        id = request.json['id']
        username = request.json['username']
        if not BlogModel.isLogin(username) :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'please-login'
        elif ArticleModel.delete(id) == True :
            returnJsonData['state'] = True
        else :
            returnJsonData['state'] = False
            returnJsonData['error'] = 'update database failed'

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


# 获取最近文章列表显示到侧边栏
def aside() :
    returnJsonData = {}

    try :
        returnJsonData['article'] = ArticleModel.getRecentArticle()
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

# 获取文章列表显示到目录
def list() : 
    returnJsonData = {}

    try :
        page = request.json['page']
        returnJsonData['article'] = ArticleModel.getPage(page)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

def pages() :
    returnJsonData = {}

    try :
        returnJsonData['pages'] = ArticleModel.getPages()
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)

def latest() :
    returnJsonData = {}

    try :
        returnJsonData['id'] = ArticleModel.getIdByOrder(0)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)