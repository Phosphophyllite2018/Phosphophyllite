from flask import render_template
from .View import LoginView
from .Model import BlogModel

def renderPage() :
    return LoginView.render()