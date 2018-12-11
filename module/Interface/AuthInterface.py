from flask import request , session
from ..Phos import PhosLog
from ..Model import BlogModel

def checkPassword() :
    password = request.form['password']
    if BlogModel.checkPassword(password) :
        session['login'] = True
        return True
    else :
        session['login'] = False
        return False