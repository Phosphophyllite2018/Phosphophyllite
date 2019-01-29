var Page = {}

/* 主页 */
Page.home = function()
{
    utility.load('article.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showAside()
        ArticleInterface.showAside()
        ArticleInterface.showByUrl()
    })
}


/* 留言板页面 */
Page.messageBoard = function()
{
    utility.load('message.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
        MessageInterface.showMain()
    })
}


/* 管理页面 */
Page.admin = function()
{
    utility.load('admin/admin.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
    })
}

/* 文章编辑 */
Page.editor = function()
{
    utility.load('admin/editor.html', function()
    {
        BlogInterface.showTitle()
        BlogInterface.showAvatar()
        BlogInterface.showDays()
        BlogInterface.showVisiting()
        ArticleInterface.showCount()
        MessageInterface.showCount()
    })
}