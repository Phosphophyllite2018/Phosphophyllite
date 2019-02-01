var MessageInterface = {}

/* 显示留言总数 */
MessageInterface.showCount = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_count'
    AsyncJsonPost('/message/count', {}, function(json) 
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


/* 显示留言访客名 */
MessageInterface.showVisitorName = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_visitor'
    AsyncJsonPost('/message/visitor_name', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['name']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}

/* 显示留言日期 */
MessageInterface.showDate = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_date'
    AsyncJsonPost('/message/date', {}, function(json) 
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


/* 显示留言内容Markdown */
MessageInterface.showMarkdown = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_content'
    AsyncJsonPost('/message/markdown', {}, function(json) 
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


/* 显示留言内容HTML */
MessageInterface.showHTML = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_content'
    AsyncJsonPost('/message/html', {}, function(json) 
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


/* 侧边栏显示最近10条留言 */
MessageInterface.showAside = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.recent_message'
    AsyncJsonPost('/message/aside', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerHTML = "" // 清空
                for(let j = 0; j < json['message'].length; j++)
                {
                    let m = json['message'][j]

                    let div = document.createElement("div")
                    div.className = 'message_block'

                    let name = document.createElement("span")
                    name.className = 'visitor_name'
                    name.innerText = ' [ ' + m['name'] + ' ] '
                    div.appendChild(name)

                    let date = document.createElement("span")
                    date.className = 'message_date'
                    date.innerText = '(' + utility.localtime(m['date']) + ')'
                    div.appendChild(date)

                    let content = document.createElement('p')
                    content.className = 'message_content'
                    if(m['html'] != null)
                    {
                        content.innerHTML = m['html']
                    }
                    else
                    {
                        content.innerText = m['markdown']
                    } 
                    div.appendChild(content)
                    
                    elements[i].appendChild(div)
                }
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 留言板显示最近40条留言 */
MessageInterface.showMain = function(page, label_selector)
{
    label_selector = label_selector ? label_selector : '.message_board'
    page = page ? page : 0

    AsyncJsonPost('/message/list', {'page' : page}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerHTML = ""
                for(let j = 0; j < json['message'].length; j++)
                {
                    let m = json['message'][j]

                    let div = document.createElement("div")
                    div.className = 'message_block'

                    let floor = document.createElement("span")
                    floor.className = "message_floor"
                    floor.innerText = "#" + m['id']
                    div.appendChild(floor)

                    let name = document.createElement("span")
                    name.className = 'visitor_name'
                    name.innerText = ' [ ' + m['name'] + ' ] '
                    div.appendChild(name)

                    let date = document.createElement("span")
                    date.className = 'message_date'
                    date.innerText = '(' + utility.localtime(m['date']) + ')'
                    div.appendChild(date)

                    let content = document.createElement('div')
                    content.className = 'message_content'
                    if(m['html'] != null)
                    {
                        content.innerHTML = m['html']
                    }
                    else
                    {
                        content.innerText = m['markdown']
                    } 
                    div.appendChild(content)

                    let hr = document.createElement('hr')
                    div.appendChild(hr)
                    
                    elements[i].appendChild(div)
                }

                /* 上一页 */
                if(page > 0)
                {
                    let prev_page = document.createElement("a")
                    prev_page.onclick = function(){MessageInterface.showMain(page - 1)}
                    prev_page.href = "javascript:void(0);"
                    prev_page.innerText = "上一页"
                    elements[i].appendChild(prev_page)

                    let space = document.createElement("span")
                    space.innerText = "   "
                    elements[i].appendChild(space)
                }

                /* 下一页 */
                AsyncJsonPost('/message/pages', {}, function(json)
                {
                    if(json['pages'] > page + 1)
                    {
                        let next_page = document.createElement("a")
                        next_page.onclick = function(){MessageInterface.showMain(page + 1)}
                        next_page.href = "javascript:void(0);"
                        next_page.innerText = "下一页"
                        elements[i].appendChild(next_page)
                    }
                })
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}




/* 添加留言 */
MessageInterface.save = function(showAside, showMain)
{
    name_inpiut = document.querySelector('#message_name')
    content_input = document.querySelector('#message_content')
    commit = document.querySelector("#message_commit")

    // 留言内容去除空格内容为空
    if(content_input.value.replace(/\s+/g,"").length == 0)
    {
        alert("留言内容不能为空")
        return false
    }

    params = {
        name : name_inpiut.value,
        content : content_input.value 
    }

    AsyncJsonPost('/message/save', params, function(json) 
    {
        if(json['state'] == true)
        {
            // 刷新
            MessageInterface.showCount()
            if(showAside)
            {
                MessageInterface.showAside()
            }

            if(showMain)
            {
                MessageInterface.showMain()
            }
            
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
    name_inpiut.value = ""
    content_input.value = ""
    return true
}