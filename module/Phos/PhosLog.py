# 记录错误日志
import time
import traceback

def log(message) :
    fp = open('./private/phosphophyllite.log.txt', 'a',encoding='utf-8')
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    text = "[PhosLog](%s) : %s \n" % (t, message)
    print(text)
    fp.write(traceback.format_exc())
    fp.close()