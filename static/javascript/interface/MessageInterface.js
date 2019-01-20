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
    AsyncJsonPost('/message/list', {count : 10}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                for(let j = 0; j < json['message'].length; j++)
                {
                    let m = json['message'][j]

                    let div = document.createElement("div")

                    let name = document.createElement("span")
                    name.className = 'visitor_name'
                    name.innerText = '[' + m['name'] + ']'
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


/* 留言板显示最近1024条留言 */
MessageInterface.showMain = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.message_board'
    AsyncJsonPost('/message/list', {count : 1024}, function(json) 
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

                    let name = document.createElement("span")
                    name.className = 'visitor_name'
                    name.innerText = '[' + m['name'] + ']'
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

/* 跳转到留言板页面 */
MessageInterface.jump = function()
{
    utility.load('message.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showMain()
    })
}


/* 添加留言 */
MessageInterface.save = function()
{
    name_inpiut = document.querySelector('#message_name')
    content_input = document.querySelector('#message_content')

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
    name_inpiut.value = ""
    content_input.value = ""
    AsyncJsonPost('/message/save', params, function(json) 
    {
        if(json['state'] == true)
        {
            // 刷新
            MessageInterface.showCount()
            MessageInterface.showMain()
        }
        else
        {
            alert(json['error'])
        }
        
    })

    return true
}