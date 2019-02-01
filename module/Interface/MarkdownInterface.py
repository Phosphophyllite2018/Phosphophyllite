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
        returnJsonData['content'] = MarkdownModel.renderMarkdown(text)
        returnJsonData['state'] = True

    except Exception as e:
        returnJsonData['state'] = False
        returnJsonData['error'] = str(e)
        PhosLog.log(e)
        
    return json.dumps(returnJsonData, ensure_ascii=False)


