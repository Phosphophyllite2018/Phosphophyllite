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
ArticleInterface.showMarkdown = function(params, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/markdown', params, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true && json['markdown'] != null)
            {
                elements[i].innerText = json['markdown']
            }
            else
            {
                utility.load('404.html', null, '/static/html/template/', 'article')
            }
        }
    })
}

/* 保存文章 */
ArticleInterface.save = function()
{
    title_inpiut = document.querySelector('#article_title')
    content_input = document.querySelector('#article_content')
    commit = document.querySelector("#article_commit")

    if(title_inpiut.value.replace(/\s+/g,"").length == 0 || content_input.value.replace(/\s+/g,"").length == 0)
    {
        alert("文章标题和内容不能为空")
        return false
    }

    params = {
        "id" : 0,
        "username" : BlogInterface.user,
        "title" : title_inpiut.value,
        "category-id" : 0,
        "content" : content_input.value 
    }

    AsyncJsonPost('/article/save', params, function(json) 
    {
        if(json['state'] == true)
        {
            // 刷新
            ArticleInterface.showCount()
            alert("文章保存成功")
        }
        else
        {
            alert(json['error'])
        }

        commit.disabled = false;
        commit.value = "提交"
    })

    commit.disabled = true;
    commit.value = "提交中"
    return true
}

/* 主页 */
ArticleInterface.homepage = function()
{
    utility.load('article.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
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


/* 404 */
ArticleInterface.page404 = function()
{
    utility.load('article.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showAside()
        utility.load('404.html', null, '/static/html/template/', 'article')
    })
}