# shuimu_user
获取水木用户信息的爬虫脚本。

## 依赖

+ lxml
+ BeautifulSoup
+ pymongo

## 使用

+ 打开shuimu_user.py文件。设置cookie变量为你当前登录用户的cookie值。(你懂的)
+ python shuimu_user.py

## 问题

+ 访问在线用户列表页面需要登录。所以这里需要设置cookie。但是设置cookie之后，如果访问太快。会被禁止访问。后续可以从帖子列表中获取用户名，这样就不会受到这样的限制，但是爬取的工作量会大很多。
