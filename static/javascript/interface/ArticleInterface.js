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


/* 显示文章正文内容HTML */
ArticleInterface.showHTML = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/html', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true && json['html'] != null)
            {
                elements[i].innerHTML = json['html']
            }
            else
            {
                ArticleInterface.showMarkdown(params)
            }
        }
    })
}


/* 显示文章正文内容Markdown */
showMarkdown = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/markdown', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['markdown']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}

/* 主页 */
ArticleInterface.homepage = function()
{
    utility.load('article.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        ArticleInterface.showTitle({'order' : -1})
        ArticleInterface.showDate({'order' : -1})
        ArticleInterface.showReading({'order' : -1})
        ArticleInterface.showHTML({'order' : -1})
        MessageInterface.showCount()
        MessageInterface.showAside()
    })
}