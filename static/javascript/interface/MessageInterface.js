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
                elements[i].innerText = json['html']
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
    AsyncJsonPost('/message/list', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['html']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}