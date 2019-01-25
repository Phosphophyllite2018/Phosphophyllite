var BlogInterface = {}

/* 登录 */
BlogInterface.login = function(username, password)
{
    params = {
        "username" : username,
        "password" : password
    }
    AsyncJsonPost('/blog/login', params, function(json) 
    {
        if(json['state'] == true)
        {
            alert("登陆成功")
            BlogInterface.user = username
        }
        else
        {
            alert(json['error'])
        }
    })
}

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


/* 访问量加一 */
BlogInterface.addVisiting = function()
{
    AsyncJsonPost('/blog/visiting_modify', {}, function(json) 
    {
        if(json['state'] == false)
        {
            console.log("BlogInterface.addVisiting return false")
            return false
        }
    })
}