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

/* 发起Post请求 */
function AjaxPost(url, params)
{
    let http = new XMLHttpRequest();
    http.open("post", url, true)
    
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

    if(params['content'].length > 150) // 去除空格后为空
    {
        alert("内容太长了。")
        return false
    }

    httpPost("/addmessage", params)
}

/* 保存文章 */
function saveArticle()
{
    params = {}
    params['title'] = document.querySelector("#article_title").value
    params['content'] = document.querySelector("#article_content").value
    if(params['title'].replace(/^\s*|\s*$/g,"") == "") // 去除空格后为空
    {
        alter("请填写标题")
        return false
    }

    if(params['content'].replace(/^\s*|\s*$/g,"") == "") // 去除空格后为空
    {
        alter("请编辑文章")
        return false
    }

    httpPost("/saveArticle", params)
}