# 一些多出使用的基本函数

# 检查SQL语句的key值是否合法
def sqlCheck(columns, key) :
    if key not in columns :
        raise Exception("Key %s is invalid." % key)

# 过滤SQL语句
def sqlFilter(text) :
    text = text.replace("'", "''")  # 将'替换为''
    return text

# 过滤要显示的文本内容
def textFilter(text) :
    text = text.replace("\n", "<br/>")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    
    return text