from flask import render_template

def renderNav() :
    output = render_template('owner.html',
                            name="Phosphophyllite",
                            data="2018-12-7")
    return output