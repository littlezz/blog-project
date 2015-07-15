blog project
===============

个人博客的网站， 当做是django的一个练习吧， 还在**开发中**。

mezzanine 是一个很好的博客框架， 但是却只支持一套博客系统。
我想要的时 /code/ 部分用markdown编辑器， 是关于技术的。 /blog/用富文本编辑器。

所以我的想法很简单， 把他们拆分成两个应用， 但是， 后果是不可避免的有一些非常冗余的代码。

~~另外， 把他们放在一个应用里面， 然后修改admin widget来支持两个编辑器也是可以的， 但是就没有那么清晰了。~~

我目前还是选择前者， 开发都在separator 分支下。


Requirements
----------------
- django >= 1.8
- markdown2
- django-markdown
- django-bootstrap3
- bleach
- grappelli
- django-wysiwyg-redactor
- slugify

TO DO
------
- 搜索
- 侧边栏
- 阻止重复提交相同评论
- 前端重做
- 后台tag标签可选显示
- 后台图片管理
- 照片墙

完成
----
- 评论模块 2015年07月11日21:21:21
- 日期归档 2015年07月15日15:48:13
