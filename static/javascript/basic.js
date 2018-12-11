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

/* 添加留言 */
function addMessage(pre)
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