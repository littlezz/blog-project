blog project
===============

个人博客的网站， 当做是django的一个练习吧， 还在**开发中**。

mezzanine 是一个很好的博客框架， 但是却只支持一套博客系统。
我想要的时 /code/ 部分用markdown编辑器， 是关于技术的。 /blog/用富文本编辑器。

所以我的想法很简单， 把他们拆分成两个应用， 但是， 后果是不可避免的有一些非常冗余的代码。

另外， 把他们放在一个应用里面， 然后修改admin widget来支持两个编辑器也是可以的， 但是就没有那么清晰了。

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
