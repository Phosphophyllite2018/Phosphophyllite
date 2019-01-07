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


/* 刷新全部数据 */
MessageInterface.refresh = function()
{
    AsyncJsonPost('/message/count', {}, MessageInterface.refreshCount);
}