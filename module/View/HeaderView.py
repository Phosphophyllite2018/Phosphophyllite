# <header>块的View

from flask import render_template
from ..Model import BlogModel

def renderHeader() :
    return render_template("header.html", name=BlogModel.getUsername())