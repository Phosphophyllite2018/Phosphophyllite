/* img标签源文件加载失败时绘制一张图片 */
function imageLoadError(img)
{
    img.onerror = null;
    let canvas = document.createElement("canvas");
    img.src = canvas.toDataURL("canvas");
}


/* 发起post请求 */
function httpPost(url, params)
{
    let virtualForm = document.createElement("form");
    virtualForm.action = url;
    virtualForm.method = "post";
    virtualForm.style.height = 0;
    virtualForm.style.width = 0;
    virtualForm.style.overflow = "hidden";
    for(let key in params)
    {
        let input = document.createElement("textarea");
        input.name = key;
        input.value = params[key];
        virtualForm.appendChild(input);
    }
    document.body.appendChild(virtualForm);
    virtualForm.submit();
}


/* 发起get请求 */
function httpGet(url, params)
{
    let virtualForm = document.createElement("form");
    virtualForm.action = url;
    virtualForm.method = "get";
    virtualForm.style.height = 0;
    virtualForm.style.width = 0;
    virtualForm.style.overflow = "hidden";
    for(let key in params)
    {
        let input = document.createElement("textarea");
        input.name = key;
        input.value = params[key];
        virtualForm.appendChild(input);
    }
    document.body.appendChild(virtualForm);
    virtualForm.submit();
}

/* 异步Post请求 */
function AsyncPost(url, params, callback)
{
    let request = new XMLHttpRequest();
    request.open("post", url, true)
    let data = ""
    for(let key in params)
    {
        data += key + "=" + params[key] + "&"
    }
    request.setRequestHeader("Content-Type","application/x-www-form-urlencoded;");
    request.send(data)
    
    /* 设置回调 */
    request.onreadystatechange = function() {
        if(request.readyState != 4)
        {
            return false
        }
        
        callback(request)
    }
}


/* 异步Post发送JSON */
function AsyncJsonPost(url, json, callback)
{
    let request = new XMLHttpRequest();
    request.open("post", url, true)
    request.setRequestHeader("Content-Type","application/json;");
    request.send(json)
    
    /* 设置回调 */
    request.onreadystatechange = function() {
        if(request.readyState != 4)
        {
            return false
        }
        
        callback(request)
    }
}

/* 接口测试打印 */
function InterfacePrint(request)
{
    let p = document.createElement("p")
    p.innerText = request.responseText
    document.body.appendChild(p)
}

/* 接口测试函数 */
function InterfaceTest(url, params)
{
    let json = JSON.stringify(params)
    AsyncJsonPost(url, json, InterfacePrint)
}

/* 添加留言 */
function addMessage()
{
    params = {}
    params['name'] = document.querySelector("#message_name").value
    params['content'] = document.querySelector("#message_content").value
    if(params['content'].replace(/^\s*|\s*$/g,"") == "") // 去除空格后为空
    {
        alert("请写点什么。")
        return false
    }

    if(params['name'].length > 15) // 去除空格后为空
    {
        alert("名字太长了。")
        return false
    }

    if(params['content'].length > 150) // 去除空格后为空
    {
        alert("留言内容太长了。")
        return false
    }

    httpPost("/interface/add_message", params)
}

/* 保存文章 */
function saveArticle(button)
{
    params = {}
    id = button.getAttribute("article-id")
    if(Number.isInteger(Number(id)))
    {
        params['id'] = id
    }
    else
    {
        params['id'] = 0
    }
    params['title'] = document.querySelector("#article_title").value
    params['content'] = document.querySelector("#article_content").value
    if(params['title'].replace(/^\s*|\s*$/g,"") == "") // 去除空格后为空
    {
        alert("请填写标题")
        return false
    }

    if(params['content'].replace(/^\s*|\s*$/g,"") == "") // 去除空格后为空
    {
        alert("请编辑文章")
        return false
    }

    httpPost("/interface/save_article", params)
}

/* 删除文章 */
function deleteArticle(link)
{
    params = {}
    params['id'] = link.getAttribute("article-id")
    httpPost("/interface/delete_article", params)
}

/* 删除留言 */
function deleteMessage(link)
{
    params = {}
    params['id'] = link.getAttribute("message-id")
    httpPost("/interface/delete_message", params)
}