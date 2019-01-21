var BlogInterface = {}

/* 显示博客标题 */
BlogInterface.showTitle = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.blog_title'
    AsyncJsonPost('/blog/username', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['username']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}

/* 显示博客头像 */
BlogInterface.showAvatar = function(label_selector)
{
    label_selector = label_selector ? label_selector : '#avatar'
    var element = document.querySelector(label_selector);
    if(BlogInterface.avatar)
    {
        element.src = BlogInterface.avatar
        return true
    }
    AsyncJsonPost('/blog/avatar', {}, function(json) 
    {
        if(json['state'] == true)
        {
            element.src = json['avatar']
            BlogInterface.avatar = json['avatar']
        }
        else
        {
            alert(json['error'])
        }
    })
}

/* 显示运行天数 */
BlogInterface.showDays = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.running_days'
    AsyncJsonPost('/blog/running_days', {}, function(json) 
    {
        var elements = document.querySelectorAll(label_selector);
        for(let i = 0; i < elements.length; i++)
        {
            if(json['state'] == true)
            {
                elements[i].innerText = json['days']
            }
            else
            {
                alert(json['error'])
            }
        }
    })
}


/* 显示访问总量 */
BlogInterface.showVisiting = function(label_selector)
{
    label_selector = label_selector ? label_selector : '.visiting_count'
    AsyncJsonPost('/blog/visiting_count', {}, function(json) 
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


/* 刷新全部数据 */
BlogInterface.refresh = function()
{
    AsyncJsonPost('/blog/username', {}, BlogInterface.refreshTitle);
    AsyncJsonPost('/blog/running_days', {}, BlogInterface.refreshRunDays)
    AsyncJsonPost('/blog/visiting_count', {}, BlogInterface.refreshVisitingCount)
}