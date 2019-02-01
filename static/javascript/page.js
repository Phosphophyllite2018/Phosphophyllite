var Page = {}

Page.cache = {}

Page.load = function(element, html, callback)
{
    dir = '/static/html/template/'
    url = dir + html 

    /* 如果没有改变，则不重新加载 */
    if(Page.cache[element] == html)
    {
        callback()
        return 0
    }
    Page.cache[element] = html

    AsyncGet(url, null, function(request)
    {
        if(request.status == 200)
        {
            document.querySelector(element).innerHTML = request.responseText
            callback()
        }
        else
        {
            Page.page404()
        }
        
    })
}

/* 404页面 */
Page.page404 = function()
{
    Page.load('article', 'article/404.html', function(){})
}

/* 主页 */
Page.article = function()
{
    Page.load('header', 'header/header.html', function()
    {
        BlogInterface.showTitle()
    })

    Page.load('aside', 'aside/main.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showAside()
        ArticleInterface.showAside()
    })

    Page.load('article', 'article/content.html', function()
    {
        if(location.hash == '#' || location.hash == '')
        {
            ArticleInterface.showLatest()
        }
        else
        {
            ArticleInterface.showByUrl()
        }
    })

    Page.load('footer', 'footer/footer.html', function(){})
}


/* 回到首页 */
Page.home = function()
{
    location.hash='#'
    Page.article()
}

/* 文章目录 */
Page.list = function(page)
{
    Page.load('header', 'header/header.html', function()
    {
        BlogInterface.showTitle()
    })

    Page.load('aside', 'aside/main.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showAside()
        ArticleInterface.showAside()
    })

    Page.load('article', 'article/list.html', function()
    {
        ArticleInterface.showList(page)
    })

    Page.load('footer', 'footer/footer.html', function(){})
}


/* 留言板页面 */
Page.messageBoard = function()
{
    Page.load('header', 'header/header.html', function()
    {
        BlogInterface.showTitle()
    })

    Page.load('aside', 'aside/message.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        ArticleInterface.showAside()
    })

    Page.load('article', 'article/message.html', function()
    {
        MessageInterface.showMain()
    })

    Page.load('footer', 'footer/footer.html', function(){})
}

/* 登录页面 */
Page.login = function()
{
    Page.load('header', 'header/header.html', function()
    {
        BlogInterface.showTitle()
    })

    Page.load('aside', 'aside/admin.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
    })

    Page.load('article', 'article/login.html', function(){})

    Page.load('footer', 'footer/footer.html', function(){})
}


/* 管理页面 */
Page.admin = function()
{
    BlogInterface.isLogin(function()
    {
        Page.load('header', 'header/header.html', function()
        {
            BlogInterface.showTitle()
        })

        Page.load('aside', 'aside/admin.html', function()
        {
            BlogInterface.showTitle()
            BlogInterface.showAvatar()
            BlogInterface.showDays()
            BlogInterface.showVisiting()
            ArticleInterface.showCount()
            MessageInterface.showCount()
        })

        Page.load('article', 'article/admin.html', function(){})

        Page.load('footer', 'footer/footer.html', function(){})

    }, Page.login)
}

/* 文章编辑 */
Page.editor = function(id)
{
    id = id ? id : 0
    BlogInterface.isLogin(function()
    {
        Page.load('header', 'header/header.html', function()
        {
            BlogInterface.showTitle()
        })

        Page.load('aside', 'aside/admin.html', function()
        {
            BlogInterface.showTitle()
            BlogInterface.showAvatar()
            BlogInterface.showDays()
            BlogInterface.showVisiting()
            ArticleInterface.showCount()
            MessageInterface.showCount()
        })

        Page.load('article', 'article/editor.html', function(){
            location.href = "#edit/id/" + id
            if(id != 0)
            {
                AsyncJsonPost('/article/title', {"id" : id}, function(json){
                    let title = document.querySelector("#article_title")
                    title.value = json['title']
                })

                AsyncJsonPost('/article/markdown', {"id" : id}, function(json){
                    let title = document.querySelector("#article_content")
                    title.value = json['markdown']
                })
            }
        })

        Page.load('footer', 'footer/footer.html', function(){})
        
    }, Page.login)
    
}


/* 文章管理 */
Page.manager = function()
{
    BlogInterface.isLogin(function()
    {
        Page.load('header', 'header/header.html', function()
        {
            BlogInterface.showTitle()
        })

        Page.load('aside', 'aside/admin.html', function()
        {
            BlogInterface.showTitle()
            BlogInterface.showAvatar()
            BlogInterface.showDays()
            BlogInterface.showVisiting()
            ArticleInterface.showCount()
            MessageInterface.showCount()
        })

        Page.load('article', 'article/article_manager.html', function(){
            ArticleInterface.showManager(0)
        })

        Page.load('footer', 'footer/footer.html', function(){})
        
    }, Page.login)
}


/* 文章管理 */
Page.messageManager = function()
{
    BlogInterface.isLogin(function()
    {
        Page.load('header', 'header/header.html', function()
        {
            BlogInterface.showTitle()
        })

        Page.load('aside', 'aside/admin.html', function()
        {
            BlogInterface.showTitle()
            BlogInterface.showAvatar()
            BlogInterface.showDays()
            BlogInterface.showVisiting()
            ArticleInterface.showCount()
            MessageInterface.showCount()
        })

        Page.load('article', 'article/message_manager.html', function(){
            MessageInterface.showManager(0)
        })

        Page.load('footer', 'footer/footer.html', function(){})
        
    }, Page.login)
}