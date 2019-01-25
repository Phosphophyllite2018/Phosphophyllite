var utility = {}

/* 页面内容切换 */
utility.load = function(html, callback, dir, label_selector)
{
    label_selector = label_selector ? label_selector : 'body'
    dir = dir ? dir : '/static/html/template/'
    url = dir + html 

    AsyncGet(url, null, function(request)
    {
        if(request.status == 200)
        {
            document.querySelector(label_selector).innerHTML = request.responseText
            callback()
        }
        else
        {
            ArticleInterface.page404()
        }
        
    })
}

/* 时区转换 */
utility.localtime = function(utc_time)
{
    let datetime = new Date(utc_time)
    datetime = new Date(Date.UTC(datetime.getFullYear(),
                                datetime.getMonth(),
                                datetime.getDate(),
                                datetime.getHours(),
                                datetime.getMinutes(),
                                datetime.getSeconds()))
    return datetime.toLocaleString()
}