var MessageInterface = {}

/* 显示留言总数 */
MessageInterface.refreshCount = function(json) 
{
    var elements = document.querySelectorAll('.message_count');
    for(let i = 0; i < elements.length; i++)
    {
        elements[i].innerText = json['count']
    }
}


/* 刷新全部数据 */
MessageInterface.refresh = function()
{
    AsyncJsonPost('/message/count', {}, MessageInterface.refreshCount);
}