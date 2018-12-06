# HeadModel
# 得到<head>中需要用到的CSS样式表和JavaScript脚本文件的路径

# CSS
css_path = 'static/css/'
css_files = [
    'frameworks.css',
    'github.css',
    'basic.css',
]

def getCSS():
    return [css_path + css_file for css_file in css_files]

# JS
js_path= 'static/javascript/'
js_files = [

]

def getJS():
    return [js_path + js_file for js_file in js_files]