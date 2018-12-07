# Phosphophyllite
`Phosphophyllite`是一个基于`Flask`开发的小型博客程序，采用`Markdown`作为文章编辑语法。

## 初始化
* 打开终端，进入`private`目录下。  
* 运行`init.py`脚本，这个脚本需要两个参数，依次是`用户名`和`密码`，如果忘记了用户名和密码，也可以运行这个脚本强制修改。  

例如：
```bash
./init.py "phos2018" "l!QQgLu&K0T66Vm*"
```

## Markdown语法
使用 GitHub API ( [https://developer.github.com/v3/markdown/](https://developer.github.com/v3/markdown/) ) 来渲染Markdown，因此支持的语法与GitHub一致。
* 请确保搭建博客所用的服务器能够正常请求GitHub API，请求GitHub API的速度会影响网站的加载速度。

## Python与依赖库
`Phosphophyllite`采用`Python3`，依赖以下库:
```python
import flask
import requests
import sqlite3
```

## 注意事项    
* 文章中如需使用`<`和`>`，必须使用对应的转义字符`&lt;`和`&gt;`。  
* 由于GitHub API的限制，文章的大小不能超过`400KB`(约10万字)。  
* 出于安全性考虑，GitHub API会过滤掉Markdown中html标签的属性，因此无法使用类似`<span style="color:red;">TEXT</span>`的方式自定义文本样式。

## TODO List
 - [x] Markdown渲染
 - [ ] aside显示用户信息
 - [ ] header显示航栏
 - [ ] footer显示Phosphophyllite
 - [ ] 文章编辑
 - [ ] 文章显示
 - [ ] 文章预览
 - [ ] 文章目录
 - [ ] 留言板
