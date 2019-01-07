var utility = {}

/* 页面内容切换 */
utility.load = function(html, dir)
{
    dir = dir ? dir : '/static/html/template/'
    url = dir + html 
    AsyncGet(url, null, function(request)
    {
        document.querySelector('body').innerHTML = request.responseText
        BlogInterface.refresh()
        ArticleInterface.showCount()
        ArticleInterface.showTitle(8)
        ArticleInterface.showDate(8)
        ArticleInterface.showReading(8)
        ArticleInterface.showContent(8)
        MessageInterface.refresh()
    })
}