var BlogInterface = {}

/* 显示博客标题 */
BlogInterface.setTitle = function(json) 
{
    var blog_titles = document.querySelectorAll('.blog_title');
    for(let i = 0; i < blog_titles.length; i++)
    {
        blog_titles[i].innerText = json['username']
        console.log(blog_titles[i])
    }
}

/* 显示运行天数 */
BlogInterface.setRunDays = function(json) 
{
    var blog_titles = document.querySelectorAll('.running_days');
    for(let i = 0; i < blog_titles.length; i++)
    {
        blog_titles[i].innerText = json['days']
        console.log(blog_titles[i])
    }
}


/* 显示访问总量 */
BlogInterface.setVisitingCount = function(json) 
{
    var blog_titles = document.querySelectorAll('.visiting_count');
    for(let i = 0; i < blog_titles.length; i++)
    {
        blog_titles[i].innerText = json['count']
        console.log(blog_titles[i])
    }
}


/* 全体数据刷新 */
BlogInterface.fresh = function()
{
    AsyncJsonPost('/blog/username', {}, BlogInterface.setTitle);
    AsyncJsonPost('/blog/running_days', {}, BlogInterface.setRunDays)
    AsyncJsonPost('/blog/visiting_count', {}, BlogInterface.setVisitingCount)
}