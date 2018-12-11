import requests
import json
from ..Phos import PhosLog 

def renderMarkdown(md_text, gitname=None, gitpass=None, timeout=0.5) :
    try :
        payload = {"text" : md_text, "mode" : "gfm", "context" : "https://github.com/Phosphophyllite2018/Phosphophyllite"}

        # 带身份验证的请求
        response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), auth=(gitname,gitpass), timeout=timeout)
        
        # 带身份验证请求失败，不带身份验证请求
        if response.status_code != 200 :
            PhosLog.log("GitHub API failed authenticaion , retry without authenticaion.")
            response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), timeout=timeout)
        
        # 不带身份验证请求仍然失败
        if response.status_code != 200 :
            output = "<p><em><strong>Render Markdown Unsuccessfully</strong></em></p>\n"
            output += "<p><em>Error Message : </em><br/> %s </p>\n" % response.text
            output += "<p><em>Markdown Text : </em><br/> %s </p>\n" % md_text.replace("\n", "<br/>")

        # 任意一次请求成功
        else :
            output = response.text #.encode("utf-8").decode("utf-8")

        return output

    except Exception as e:
        PhosLog.log(e)
        output = "<p><em><strong>Render Markdown Unsuccessfully</strong></em></p>\n"
        output += "<p><em>Error Message : </em><br/> %s </p>\n" % e
        output += "<p><em>Markdown Text : </em><br/> %s </p>\n" % md_text.replace("\n", "<br/>")
        return output