import requests
import json
from ..Phos import PhosLog 

def renderMarkdown(md_text, gitname=None, gitpass=None) :
    try :
        payload = {"text" : md_text, "mode" : "gfm", "context" : "https://github.com/hubenchang0515/Phosphophyllite"}

        # 带身份验证的请求
        response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), auth=(gitname,gitpass))

        # 带身份验证请求失败，不带身份验证请求
        if response.status_code != 200 :
            PhosLog.log("GitHub API failed authenticaion , retry without authenticaion.")
            response = requests.post("https://api.github.com/markdown", data=json.dumps(payload))
        
        # 不带身份验证请求仍然失败
        if response.status_code != 200 :
            output = "<h1>Render Markdown Unsuccessfully</h1>\n"
            output += "<em>Error Message : </em><br/> %s <hr/>\n" % response.text
            output += "<em>Markdown Text : </em><br/> %s <hr/>\n" % md_text.replace("\n", "<br/>")

        # 任意一次请求成功
        else :
            output = response.text #.encode("utf-8").decode("utf-8")

        return output
    except Exception as e:
        PhosLog.log(e)
        output = "<h1>Render Markdown Unsuccessfully</h1>\n"
        output += "<em>Error Message : </em><br/> %s <hr/>\n" % e
        output += "<em>Markdown Text : </em><br/> %s <hr/>\n" % md_text.replace("\n", "<br/>")
        return output