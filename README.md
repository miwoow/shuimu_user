# shuimu_user
获取水木用户信息的爬虫脚本。并将结果保存到本地mongodb中。

## 依赖

+ lxml
+ BeautifulSoup
+ pymongo

## 使用

+ 打开shuimu_user.py文件。设置cookie变量为你当前登录用户的cookie值。(你懂的)
+ python shuimu_user.py
+ 会将结果保存在本机上的mongodb中。（mongodb配置写在代码中。如需修改，可以修改代码）

## 基本原理

+ 登录用户可以看到一个在线用户列表页面。地址：http://www.newsmth.net/nForum/online?ajax&p=1
+ 在已知用户名的情况下，可以通过这个地址查看用户基本信息。地址：http://www.newsmth.net/nForum/user/query/用户名.json

## 问题

+ 访问在线用户列表页面需要登录。所以这里需要设置cookie。但是设置cookie之后，如果访问太快。会被禁止访问。后续可以从帖子列表中获取用户名，这样就不会受到这样的限制，但是爬取的工作量会大很多。
