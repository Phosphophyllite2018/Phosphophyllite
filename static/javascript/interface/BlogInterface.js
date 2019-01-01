var BlogInterface = {}

/* 显示博客标题 */
BlogInterface.refreshTitle = function(json) 
{
    var elements = document.querySelectorAll('.blog_title');
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
}

/* 显示运行天数 */
BlogInterface.refreshRunDays = function(json) 
{
    var elements = document.querySelectorAll('.running_days');
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
}


/* 显示访问总量 */
BlogInterface.refreshVisitingCount = function(json) 
{
    var elements = document.querySelectorAll('.visiting_count');
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
}


/* 刷新全部数据 */
BlogInterface.refresh = function()
{
    AsyncJsonPost('/blog/username', {}, BlogInterface.refreshTitle);
    AsyncJsonPost('/blog/running_days', {}, BlogInterface.refreshRunDays)
    AsyncJsonPost('/blog/visiting_count', {}, BlogInterface.refreshVisitingCount)
}