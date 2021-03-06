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


/* 异步Get请求 */
function AsyncGet(url, params, callback)
{
    let request = new XMLHttpRequest();
    request.open("get", url, true)
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
    switch(typeof(json))
    {
        case "object" : 
            json = JSON.stringify(json)
            break;

        case "string" :
            break;

        default :
            console.log("json param is invalid type (" + typeof(json) + ")")
            return false

    }
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
        
        callback(JSON.parse(request.responseText))
    }

    return true
}

/* 接口测试打印 */
function InterfacePrint(json)
{
    let p = document.createElement("p")
    p.innerText = String(JSON.stringify(json))
    document.body.appendChild(p)
}

/* 接口测试函数 */
function InterfaceTest(url, params)
{
    let json = params
    AsyncJsonPost(url, json, InterfacePrint)
}

