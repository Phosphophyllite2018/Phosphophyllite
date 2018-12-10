# Phosphophyllite
`Phosphophyllite`是一个基于`Flask`开发的小型博客程序，采用`Markdown`作为文章编辑语法。

## 初始化
* 打开终端，进入`private`目录下。  
* 运行`phos.py`脚本，进行初始化 : 
```bash
./phos.py init
```
* 运行`phos.py`脚本，设置用户名和密码 : 
```bash
./phos.py username "Phos2018"
./phos.py password "l!Q'gLu&K0T66Vm*"
```

* 运行`phos.py`脚本，绑定GitHub(由于使用GitHub API渲染Markdown，需要进行身份验证，否则每小时只能请求60次。建议注册一个不使用的GitHub账号以免密码泄露。) :
```bash
./phos.py git-name "gituser2018"
./phos.py git-pass "!k'GLu4^%0V86xY*q"
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

## Markdown测试  
行内代码`code` 

一级强调 *em*

二级强调 **string**

三级强调 ***em strong***  

代码块
```
https://github.com/hubenchang0515/Phosphophyllite.git
```

语法高亮代码块
```C
#include <stdio.h>

int main() 
{
    printf("Hello World\n");
    return 0;
}
```

表格(元素右对齐)  

 序号 | 单价 | 数量 | 总价 
 -:   | -:  | -:   | -:
  1   |5    |100   | 500  
  2   |2    |10    | 20   
  3   |4    |50    | 200  
  4   |1    |100   | 100  
  5   |7    |10    | 70   
合计  |     |      | 890  

