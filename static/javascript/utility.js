var utility = {}

/* 页面内容切换 */
utility.load = function(html, callback, dir)
{
    dir = dir ? dir : '/static/html/template/'
    url = dir + html 

    AsyncGet(url, null, function(request)
    {
        document.querySelector('body').innerHTML = request.responseText
        callback()
    })
}