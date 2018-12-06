import requests
import json

def renderMarkdown(md_text) :
    payload = {"text" : md_text, "mode" : "markdown"}
    response = requests.post("https://api.github.com/markdown", data=json.dumps(payload))
    output = response.text #.encode("utf-8").decode("utf-8")
    return output