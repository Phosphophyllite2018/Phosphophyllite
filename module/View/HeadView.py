# HeadView
# 渲染<head>中需要用到的CSS样式表和JavaScript脚本文件的标签
# 注意不是header

def renderCSS(css_files):
    html = ""
    for href in css_files :
        html += '<link href="%s" rel="stylesheet" type="text/css" />\n' % href
    return html

def renderJS(js_files):
    html = ""
    for src in js_files :
        html += '<script src="%s" type="text/javascript"></script>\n' % src
    return html