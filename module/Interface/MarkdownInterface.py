import requests
import json
from flask import request
from ..Phos import PhosLog 
from ..Phos.common import textFilter
from ..Model import MarkdownModel

# Markdown渲染接口
def render() :
    returnJsonData = {}

    try :
        text = request.json['content']
        gitname = MarkdownModel.getGitName()
        gitpass = MarkdownModel.getGitPass()
        returnJsonData['content'] = renderMarkdown(text, gitname, gitpass)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


def renderMarkdown(md_text, gitname=None, gitpass=None, timeout=15) :
    try :
        if md_text == None :
            return "context is null"
        
        # 请求信息
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
            output += "<p><em>Error Message : </em><br/> %s </p>\n" % textFilter(response.text)
            output += "<p><em>Markdown Text : </em><br/> %s </p>\n" % textFilter(md_text)

        # 任意一次请求成功
        else :
            output = response.text #.encode("utf-8").decode("utf-8")

        return output

    except Exception as e:
        PhosLog.log(e)
        output = "<p><em><strong>Render Markdown Unsuccessfully</strong></em></p>\n"
        output += "<p><em>Error Message : </em><br/> %s </p>\n" % textFilter(e)
        output += "<p><em>Markdown Text : </em><br/> %s </p>\n" % textFilter(md_text)
        return output