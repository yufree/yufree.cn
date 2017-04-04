---
title: PLOS ONE 别叠被子了
date: 2014-03-16
slug: plos one quilt
---

传说有一种机制叫做同行评议，经过了这关发表的文章都有一定学术价值。又传说有一种同行评议的开放获取的期刊，只要你给钱就能发表（夸张，真的是夸张）。不不，不是影射plos one，相反，我个人非常看好plos one或scientific reports这类开放获取的同行评议期刊，拿国家的钱做科研，结果不涉密当然应该让公众看到，不然总是自家圈子捧丑脚也没什么意思。但不能因为受众更广泛就降低标准，今年1月，plos one上这篇文章实在让人大跌眼镜，这就是多少土鳖魂牵梦绕的s(tupid)-c(hinese)-i(ndex)。

[PLOS ONE: Quilt Plots: A Simple Tool for the Visualisation of Large Epidemiological Data](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0085047#pone-0085047-t001)

简单说，作者说我发现一种不错的数据可视化方法，原来我们搞流行病学，都是列联表，太不直观，应该用颜色深浅来表示列联表的频率数据，还为此起了个很形象的名字：被子图。为了高大上，还写了个R包，里面就一个函数quilt().这个包连r-core都没搭理，却过了plos one审稿人跟编辑的审核。

但想法还是很好的，不过怎么如此眼熟？心中弱弱的问下：这货跟heatmap有区别吗？好，来看下discussion：

> “Quilt plots” can be considered as a simple formulation of “heat maps”. They produce a similar graphical display to “heat maps” when the “clustering” and “dendrogram” options are turned off. In addition, “quilt plots” have several advantages over “heat maps”. Firstly, unlike “heat maps”, “quilt plots” come with easily understood R-functions (i.e. plot, legend and color). In addition, R is freely available software and supported by leading statistical experts around the world, and it is important to promote the use of this software among epidemiological researchers. In addition it is difficult to learn to use R compared to other statistical packages. For example, “heat maps” require the specification of 21 arguments including hierarchical clustering, weights for re-ordering the row and columns dendrogram, which are not always easily understood unless one has an extensive programming knowledge and skills. One of the aims of our paper is to present “quilt plots” as a useful tool with simply formulated R-functions that can be easily understood by researchers from different scientific backgrounds without high-level programming skills.

不翻译了，太直白了。作者说的很清楚：绝对不是heatmap，是heatmap的简化版。等等，有点不对劲，heatmap也是R写的，被子图也是R写的，哪里简化了？前面说被子图适合科研人员使用不反对，怎么后面又说R很难学？被子图不就是R写的吗？运行也要在R里敲代码的！这篇文章的逻辑实在太强大了，重新发明阉割版轮子不说，还说完整版轮子不好用，作为开车的，有那学阉割版的工夫，完整版早搞明白了。

问：如何把一个期刊搞臭？

答：拿被子捂捂就可以了。

参考文献

A mathematical model for the determination of total area under glucose tolerance and other metabolic curves. M.M. Tai. Diabetes Care, Vol 17, Issue 2 152-154