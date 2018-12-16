from flask import request
from ..Phos import PhosLog
from ..Model import ArticleModel

def save() :
    name = request.form['title']
    content = request.form['content']
    ArticleModel.save(name, content)