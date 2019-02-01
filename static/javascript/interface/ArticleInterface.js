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
                Page.page404()
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

    let id = parseInt(location.hash.replace("#edit/id/",""))
    params = {
        "id" : id,
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
            Page.manager()
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
ArticleInterface.showList = function(page, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
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

            elements[i].appendChild(document.createElement("hr"))

            /* 上一页 */
            if(page > 0)
            {
                let prev_page = document.createElement("a")
                prev_page.onclick = function(){ArticleInterface.showList(page - 1)}
                prev_page.href = "javascript:void(0);"
                prev_page.innerText = "上一页"
                elements[i].appendChild(prev_page)

                let space = document.createElement("span")
                space.innerText = "   "
                elements[i].appendChild(space)
            }

            /* 下一页 */
            AsyncJsonPost('/article/pages', {}, function(json)
            {
                if(json['pages'] > page + 1)
                {
                    let next_page = document.createElement("a")
                    next_page.onclick = function(){ArticleInterface.showList(page + 1)}
                    next_page.href = "javascript:void(0);"
                    next_page.innerText = "下一页"
                    elements[i].appendChild(next_page)
                }
            })
            
        }
    })
}



/* 显示文章管理列表 */
ArticleInterface.showManager = function(page, label_selector)
{
    label_selector = label_selector ? label_selector : '.article_content'
    AsyncJsonPost('/article/list', {"page" : page}, function(json)
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            elements[i].innerHTML = "" // 清空
            let table = document.createElement("table")
            elements[i].appendChild(table)
            
            let thead = document.createElement("thead")
            table.appendChild(thead)

            let thead_id = document.createElement("td")
            thead_id.innerText = "ID"
            thead.appendChild(thead_id)

            let thead_title = document.createElement("td")
            thead_title.innerText = "Title"
            thead.appendChild(thead_title)

            let thead_edit = document.createElement("td")
            thead_edit.innerText = "Edit"
            thead.appendChild(thead_edit)

            let thead_delete = document.createElement("td")
            thead_delete.innerText = "Delete"
            thead.appendChild(thead_delete)

            for(let j = 0; j < json['article'].length; j++)
            {
                let m = json['article'][j]

                let tr = document.createElement("tr")
                table.appendChild(tr)

                let td_id = document.createElement("td")
                td_id.innerText = m['id']
                table.appendChild(td_id)

                let td_title = document.createElement("td")
                td_title.innerText = m['title']
                table.appendChild(td_title)

                let td_edit = document.createElement("td")
                let a_edit = document.createElement("a")
                td_edit.appendChild(a_edit)
                a_edit.innerText = "编辑"
                a_edit.href = "javascript:void(0);"
                a_edit.onclick = function(){Page.editor(m['id'])}
                table.appendChild(td_edit)

                let td_delete = document.createElement("td")
                let a_delete = document.createElement("a")
                td_delete.appendChild(a_delete)
                a_delete.innerText = "删除"
                a_delete.href = "javascript:void(0);"
                a_delete.onclick = function()
                {
                    ArticleInterface.delete(m['id'])
                    ArticleInterface.showManager(page)
                }
                table.appendChild(td_delete)
            }

            elements[i].appendChild(document.createElement("hr"))

            /* 上一页 */
            if(page > 0)
            {
                let prev_page = document.createElement("a")
                prev_page.onclick = function(){ArticleInterface.showManager(page - 1)}
                prev_page.href = "javascript:void(0);"
                prev_page.innerText = "上一页"
                elements[i].appendChild(prev_page)

                let space = document.createElement("span")
                space.innerText = "   "
                elements[i].appendChild(space)
            }

            /* 下一页 */
            AsyncJsonPost('/article/pages', {}, function(json)
            {
                if(json['pages'] > page + 1)
                {
                    let next_page = document.createElement("a")
                    next_page.onclick = function(){ArticleInterface.showManager(page + 1)}
                    next_page.href = "javascript:void(0);"
                    next_page.innerText = "下一页"
                    elements[i].appendChild(next_page)
                }
            })
            
        }
    })
}


/* 删除文章 */
ArticleInterface.delete = function(id)
{
    params = {
        "id" : id,
        "username" : BlogInterface.user
    }
    AsyncJsonPost('/article/delete', params, function(json)
    {
        if(json['state'] == true)
        {
            alert("删除成")
        }
        else
        {
            alert(json['error'])
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

/* 显示最新的文章 */
ArticleInterface.showLatest = function()
{
    AsyncJsonPost('/article/latest', {}, function(json)
    {
        ArticleInterface.showById(json['id'])
    })
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