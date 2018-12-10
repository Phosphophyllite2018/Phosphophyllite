import requests
import json

def renderMarkdown(md_text, gitname=None, gitpass=None) :
    try :
        payload = {"text" : md_text, "mode" : "gfm", "context" : "https://github.com/hubenchang0515/Phosphophyllite"}
        response = ""
        if gitname != None and gitpass != None :
            response = requests.post("https://api.github.com/markdown", data=json.dumps(payload), auth=(gitname,gitpass))
        else :
            response = requests.post("https://api.github.com/markdown", data=json.dumps(payload))
        output = response.text #.encode("utf-8").decode("utf-8")
        return output
    except Exception as e:
        return "<h1>Exception</h1>\n<p>%s</p>\n<p>%s</p>" % (e, md_text)