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
ArticleInterface.showTitle = function(id, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_title'
    AsyncJsonPost('/article/title', {"id" : id}, function(json)
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
ArticleInterface.showDate = function(id, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_date'
    AsyncJsonPost('/article/date', {"id" : id}, function(json)
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
ArticleInterface.showReading = function(id, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_reading'
    AsyncJsonPost('/article/reading_count', {"id" : id}, function(json)
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
ArticleInterface.showHTML = function(id, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/html', {"id" : id}, function(json)
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
                ArticleInterface.showMarkdown(id)
            }
        }
    })
}


/* 显示文章正文内容Markdown */
ArticleInterface.showMarkdown = function(id, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/markdown', {"id" : id}, function(json)
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
                Page.load('article', 'article/404.html', function(){})
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




/* 显示侧边栏列表 */
ArticleInterface.showAside = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.recent_article'
    AsyncJsonPost('/article/aside', {}, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            elements[i].innerHTML = "" // 清空
            for(let j = 0; j < json['article'].length; j++)
            {
                let m = json['article'][j]

                let p = document.createElement("p")

                let link = document.createElement("a")
                link.className = 'article_link'
                link.href =  "#article/id/" + m['id'] 
                link.innerText = m['title']
                link.onclick = ArticleInterface.goto(link.href)
                p.appendChild(link)

                // let date = document.createElement("span")
                // date.innerText = "(" + m['date'] + ")"
                // p.appendChild(date)
                
                elements[i].appendChild(p)
            }
        }
    })
}


/* 显示目录列表 */
ArticleInterface.showIndex = function(page, label_selector)
{
    label_selector = label_selector ? label_selector : 'article'
    AsyncJsonPost('/article/list', {"page" : page}, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            elements[i].innerHTML = "" // 清空
            for(let j = 0; j < json['article'].length; j++)
            {
                let m = json['article'][j]

                let h1 = document.createElement("h1")

                let link = document.createElement("a")
                link.className = 'article_link'
                link.href =  "#article/id/" + m['id'] 
                link.innerText = m['title']
                link.onclick = ArticleInterface.goto(link.href)
                h1.appendChild(link)



                let p = document.createElement("p")
                p.innerText = "日期 : " + utility.localtime(m['date']) + " 阅读量 : " + m['reading']
                
                
                elements[i].appendChild(h1)
                elements[i].appendChild(p)
            }
        }
    })
}


/* 显示文章 */
ArticleInterface.showById = function(id)
{
    Page.load('article', 'article/content.html', function()
    {
        // BlogInterface.showTitle()
        // BlogInterface.showAvatar()
        // BlogInterface.showDays()
        // BlogInterface.showVisiting()
        // ArticleInterface.showCount()
        // MessageInterface.showCount()
        // MessageInterface.showAside()
        // ArticleInterface.showAside()
        ArticleInterface.showTitle(id)
        ArticleInterface.showDate(id)
        ArticleInterface.showReading(id)
        ArticleInterface.showHTML(id)
    })
}

/* 显示文章 */
ArticleInterface.showByUrl = function()
{
    let id = parseInt(location.hash.replace("#article/id/",""))
    ArticleInterface.showById(id)
}


/* 打开文章 */
ArticleInterface.goto = function(url)
{
    return function(){
        location.href = url;
        ArticleInterface.showByUrl()
        return true
    }
    
}