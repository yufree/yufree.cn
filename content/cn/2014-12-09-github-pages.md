---
title: 基于Github Pages快速建站指南
date: 2014-12-09
slug: github pages
---

最近整理了公开课笔记，开始是打算生成html扔到rpubs上，后来发现latex公式显示有问题，是可忍孰不可忍，就花了点时间整理出一个[网站](yufree.github.io/notes/)。做完了发现实际连半个小时都没用上，但就显示效果而言还过得去。进而想到科研人员给自己的项目搭建一个极简的网站其实是很实用的，但如果让每个科研人员去学前端后端估计不现实，但我们可以站在别人的肩上去工作的。

## Git & Github

首先你可以在[在线模拟器](https://try.github.io/levels/1/challenges/1)上试一下。要点是Git是本地仓，Github是远程仓，你在本地仓的操作commit后可以push到远程仓更新。换句话讲，你在本地仓里写静态文本，然后推送到远程仓，远程仓通过`Github Pages`这个Github提供的服务将你的文本转化为网页展示出去。所以具备这条前置知识后你应该至少在本地端安装了[Git](http://git-scm.com/)并注册有[Github](https://github.com/)账号，之后具备在本地Git端与服务器Github端仓库的交互能力。例如在本地名为test仓的a.txt文件可以推送到远程仓。学习基本语法加安装最多半小时左右就可以。

如果你之前写过博客，这就相当于把Github作为博客的空间与域名提供商，你在本地提供内容就可以了。那么问题来了，什么样的内容可以转化成为网页？按说浏览器解析的是html语言，这样你应该先去学html语言… 等等，html语言，对，就是你在浏览器上右键查看源代码看到的那一坨，强烈不建议学习，我们需要一种更简单的语言，这就是markdown语言。

## markdown 语法

这个语法更简单，查看[这里](https://help.github.com/articles/markdown-basics/)就可以，如果你打算实现高级点的功能例如表格或代码高亮什么的，可以看Github对markdown语法的[增强](https://help.github.com/articles/github-flavored-markdown/)。这个学习过程可能就是几分钟的事。我在[博客](http://yufree.github.io/blogcn/2014/10/25/kramdown.html)中对markdown语法的一种方言进行了介绍，由于科研人员对数学公式的输出有要求，这种方言的学习很有必要。

## Github Pages

好了，现在你应该有个本地仓test，远端用testwebpage注册了github账号，里面有个按照markdown语法写好的文本文件例如a.md。把这个文档推送到远端就可以了，那么网址是什么呢？按照github规定，这个网址应该是：http://testwebpage.github.io/test/a.html。但你直接访问是打不开的，因为你得让github知道这是个需要生成网页的项目，按照规定github默认的网页必须放的一个名为gh-pages的git分支中，这样你手工新建一个这样的分支push到远端就可以了。但这仅仅是实现了网页而你还需要一个主页来整合网页，这时我们写一个index.md的文档把网页整合好放到根目录下就OK了。这样你访问http://testwebpage.github.io/test就能看到主页了。其实还有更简单的方法，你可以按照[这里](https://pages.github.com/)的介绍可视化生成网页。

## 定制

按照前面的方法你大概可以做出一个能看的网页，但要做出好看有个性的网页仅仅依赖默认方法就不好办了。这里建议拿出一点时间来到[w3school](http://www.w3school.com.cn/)上面学下网页前端的基本概念，然后如果你选择一款有开发者模式的浏览器例如[chrome](https://www.google.com/chrome/)，打开我的[博客](http://yufree.github.io/blogcn)，对上面每个元素进行审查，看一下样式如何嵌套并修改观察效果。在试错中成长是最快的，如果不断实践，很快就可以摸索出修改方法，然后按自己的习惯定制就可以了。对于科研人员，这类网站不要花哨，简单明了重点在内容就可以了。阮一峰的一篇[介绍](http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html)也很有价值，值得参考。