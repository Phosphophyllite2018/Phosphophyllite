var ArticleInterface = {}

/* 显示文章总数 */
ArticleInterface.refreshCount = function(json) 
{
    var elements = document.querySelectorAll('.artcile_count');
    for(let i = 0; i < elements.length; i++)
    {
        elements[i].innerText = json['count']
    }
}


/* 刷新全部数据 */
ArticleInterface.refresh = function()
{
    AsyncJsonPost('/article/count', {}, ArticleInterface.refreshCount);
}