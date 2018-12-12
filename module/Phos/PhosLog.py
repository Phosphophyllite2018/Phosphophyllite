# 记录错误日志
import time
import traceback

def log(message) :
    fp = open('./private/phosphophyllite.log.txt', 'a',encoding='utf-8')
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    text = "[PhosLog](%s) : %s \n" % (t, message)
    traceback.print_exc()
    fp.write(text)
    fp.close()