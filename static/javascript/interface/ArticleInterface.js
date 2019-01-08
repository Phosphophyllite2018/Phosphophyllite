var ArticleInterface = {}

/* 显示文章总数 */
ArticleInterface.showCount = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.artcile_count'
    AsyncJsonPost('/article/count', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['count']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 显示文章标题 */
ArticleInterface.showTitle = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_title'
    AsyncJsonPost('/article/title', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['title']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 显示文章日期 */
ArticleInterface.showDate = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_date'
    AsyncJsonPost('/article/date', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['date']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 显示文章阅读量 */
ArticleInterface.showReading = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_reading'
    AsyncJsonPost('/article/reading_count', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['reading']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 显示文章正文内容 */
ArticleInterface.showContent = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/html', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerHTML = json['html']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}