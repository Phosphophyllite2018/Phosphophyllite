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