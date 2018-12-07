# 错误日志
import time

def log(message) :
    fp = open('./private/phosphophyllite.log.txt', 'a',encoding='utf-8')
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    fp.write("[Log](%s) : %s \n" , (t, message))
    fp.close()