# Phosphophyllite
`Phosphophyllite`是一个基于`Flask`开发的小型博客程序，采用`Markdown`作为文章编辑语法。

## Markdown语法
使用 GitHub API ( [https://developer.github.com/v3/markdown/](https://developer.github.com/v3/markdown/) ) 来渲染Markdown，因此支持的语法与GitHub一致。
* 请确保搭建博客所用的服务器能够正常请求GitHub API

## Python与依赖库
`Phosphophyllite`采用`Python3`，依赖以下库:
```python
import flask
import requests
import sqlite3
```

## Feature    
* 文章中如需使用`<`和`>`，必须使用对应的转义字符`&lt;`和`&gt;`  
* 由于GitHub API的限制，文章的大小不能超过`400KB`
<span class="color:red;">红色</span> 

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
