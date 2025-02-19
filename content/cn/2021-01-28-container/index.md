---
title: jupyter与容器技术
author: Miao Yu
date: '2021-01-28'
slug: container
categories: []
tags:
  - tech
  - data
---

我们现在评价科研成果，经常喜欢用当前的共识这个表述，但前沿领域的共识不见得是对的。更严格说，所有涉及观点站队问题的讨论都不属于科学讨论，面对质疑经过合格训练的科学家都不会简单采信某一方观点而是要去看原始数据或在自己的实验室重现，让事实说话要比空对空有意义的多。不过重复实验在现代社会能不能拿到经费是存疑的，在当前经费获取的方式下，重复研究别人的成果是费力不讨好的，更多人重复他人实验是为了基于此进行进一步研究，如果重复不出有些课题组会尝试其他路径，有些就去联系原作者询问实验细节。

我博士阶段末期就收到过关于一组植物愈伤组织实验重复的询问，当时我特意去重复了实验还发了操作过程照片过去，结果那边还是重复不出来。我到现在也搞不清楚是哪里的问题，因为我重复后结果跟发表的论文是一样的，但对方咋做的就不知道了，而且他那边其实对我的体系进行了本地化修改，暴露物也换掉了，但在我看来应该不影响结果。因为这段往事让我意识到可重复性里面可能包含了质疑者与原作者都没意识到但很重要的步骤，而这个步骤直接导致了重现性不好，这就是真实科研或者说实验学科会遇到的问题。好比一份菜谱给出来，两个厨子炒出了两份口味不同的菜，如果菜谱符合要求，那么一定是存在菜谱外的东西影响了结果。这种情况在化学实验里不常见，因为化学实验体系通常比较简单，但生物实验就非常常见了，同样成分的培养基经常一个能养活细胞，另一个养啥死啥，这也是为什么生物论文实验里用的材料是要标注厂家信息的，因为很多实验对材料的要求只能用厂家品控来保证重复性。

实验的可重复性眼下可控性里操作空间还是有的，但眼下实验完成后的数据处理与共享部分如果透明化，那么会极大挤压学术不端的空间。虽然同样一组数据在不同的分析方法或统计模型下可能得到完全不同的结论，但只要你能把数据如何分析的过程及原始数据共享出来，那么也是可接受的。打比方要做一组高维数据的机理与预测模型，你用随机森林选出一组重要变量并基于此构建了逻辑通顺的机理模型，隔天用同样的数据别人用线性混合模型又选出一组变量也构建了逻辑通顺的机理模型，但这两个模型降维上用了完全不同的策略与假设，导致两组模型虽然都说得通但都可能只解释了真相的一部分，这个也属于常见现象。

当前期刊一般都会要求上传原始数据，但这是不够的，博士阶段我读了一篇论文看到了里面一种计算方法很有意思，但他们给的是数学公式，我是在matlab上重现后才能去验证。这个操作对于实验学科的人而言门槛过高，绝大多数实验学科研究人员的数据分析水平不会超过调用别人写好函数处理数据的阶段，指望自己写需要自学很多东西，这虽然应该是合格研究人员应具备的素质，但难度还是有的。我现在读很多论文可以感到明显的割裂感，就是实验部分与数据分析是分工来做的，这就导致很多描述非常不准，例如简单利用p值来说明结果而意识不到p值本身的问题，很多数据分析方法描述非常奇怪，明明一两句就能说清楚但却自己定义了一大堆东西来绕弯，很明显对分析方法原理没搞清楚。

这属于无效协作，实验方与数据分析方想按照分工原理来提高效率，但最后展示出来的则是一团乱麻。一篇论文一定要有一个人能同时理顺实验与数据分析的所有步骤，这看上去很不合理但没办法，从我跟单位里所谓专业统计分析人员打交道的体验来看，那种强调要把数据做成他们那种行是样品列是特征的标准格式的要求是荒谬的，真实数据要转化到那种标准格式是要进行大量假设的，这部分实验方通常不了解，数据处理方又不管，最后给出的结果常常导致实验方无法验证而数据处理方又对数据中普遍存在的异常值与确实值大为恼火。在我看来根本就不能割裂开实验与数据分析，这两步需要同一个人来做，而且职业做实验的一定会被自动化仪器取代而职业处理标准数据分析的也一定会被自动化软件取代，唯独互相连接的人是无法被技术取代的。

当前的解决方案对于实验人员而言就是保留完整的数据分析脚本，这个本来很正常的需求因为图形化商业软件的流行而被认为很不友好。说句不好听的，这就是被图形界面给惯坏了而忘了科研中对重复性的要求，而且大多数专业图形界面的数据分析软件其实也会记录操作步骤，你的每一步点击都会在一份记录中被保留，所以数据分析步骤与图形界面并不矛盾。不过从实际数据分析角度，如何给出脚本确实是个技术问题而jupyter项目则在一定程度上解决了这个问题。

在介绍Jupyter项目之前，我想说如果你的数据分析完全依赖 R 与 Python，那么自带 RStudio 服务器版的 Rocker 镜像配合 Rmarkdown 文档就已经可以实现数据分析的完全可重现性了，甚至 Rmarkdown 文档本身就可以作为完整数据分析步骤的良好载体而附加在论文附件里来保证可重复性。当然如果你懂一点R包开发，把分析方法作为模版嵌到一个R包里也是没问题的。今天想说 jupyter 项目，纯粹是因为我最近考古发现现在 jupyter 已经从 Python 的轻量级在线开发环境成长为多语言支持的平台了，其部署上也非常容易。当然，其对学术写作生态的支持对比 Rmarkdown 的生态还是弱了非常多，更偏探索，当然依赖pandoc的核心都可以互相转换，但感觉学术界，特别是实验学科目前对R的接受度更高，毕竟学术数据分析所需要的统计工具 R 基本都有现成的，Python 在这方面虽然机器学习的包更全，但实际研究里需要的工具就不完整。R 包的社区里存在大量即懂专业知识又懂统计分析的人，会给出很多研究人员直接用的函数，当然很多开发者并不太在意效率问题。Python的社区里也有科研人员，但实验学科的不多，整体社区偏软件工程偏通用计算问题。不过理想状态是两种语言都掌握，一种做到开发级，另一种做到应用级对于绝大多数科研数据分析问题就都能处理了。

Jupyter 项目最开始就是专门为 python 设计的，后来逐渐发展壮大，可以支持更多的语言，前提是你要把对应的核装上保证交互通信畅通。这里顺道也捋一捋 Python 的安装问题，现在人装软件都是全家桶，你单装一个 Python后面一样有大量的依赖问题，因此大多数都是去装一个anaconda，这是基于Python的数据处理和科学计算平台发行版，但其实也支持R。可以把 anaconda 理解为 TeX Live 之于 TeX 排版系统的关系，作为发行版，基本要囊括编程语言本身、集成开发环境（IDE）、常用包及包的管理器。例如，TeX live里就会打包排版引擎、参考文献处理引擎、文档格式转换、字体、常用宏包、包管理器 tlmgr、文档编辑器 TeXworks 等几乎所有你可能用到的工具与文档。anaconda 里你可以装 Jupyter notebook作为IDE，也可以装PyCharm作为IDE，甚至可以装RStudio，其包管理用的是 conda，用法上类似 Python 的 pip 安装，但 conda 不仅仅支持python，你是可以用 conda 来装 R 包的，而且其解决依赖问题也比较智能（pip其实也可以做到）。不过，因为 anaconda 本身也是个公司，有付费产品，免费产品界面也有点花哨，所以很多有洁癖的人会选 miniconda 这种精简版。

Jupyter 经典版就是交互式笔记本，也是最早得以流行的核心功能，用户可以在代码块里写代码，然后运行代码块直接看到结果。熟悉 R 的会发现这跟 knitr 的功能类似，不同点在于 knitr 对于代码块的控制更多，侧重一次编译出带结果的成品文档，而Jupyter notebook 侧重实时输出结果或再现结果，更接近 REPL 但不算是个好的开发工具。在实际写文档时，相信多数人会选择调用包里的函数而不是现写一个，所以 Jupyter notebook 在交互要求高时也还算不错。虽然大多数人用 ipython 作为解释器，但通过 IRkernel 这个R包并初始化后其代码块也可以执行 R。在 RStudio 里，也可以创建类似的 R Notebook，并用 reticulate 包来使用 python。Jupyter 笔记本是完全采用网页界面形式进行交互（其实 RStudio 也是），笔记本的下一代产品是 JupyterLab ，这个界面更接近一个全功能的IDE了，也是基于 notebook的，可以装各种插件来提高效率，所以现在上手可以直接从 JupyterLab 开始。

Jupyter项目中最吸引我的是Jupyter hub，前面的在线笔记本是一个人用的，Jupyter hub可以将笔记本发布到网上供多人使用。在R里面我们做网络应用一般用Shiny，后台跑的是R，如果借助Jupyter hub，我们也可以把一个交互式应用放到网上，这里可以用带有Jupyter hub的docker镜像进行快速部署，也可以借助k8s部署到集群上。如果你只打算在一台服务器上做一个轻量级的在线应用或分享一个笔记本，用户不超过100人，可以直接用The Littlest JupyterHub 来部署，这个应该是个很好的教学工具平台，不过R里也有learnr包作为对比。

另一个值得关注的项目是binder，在这个项目里你可以直接分享一个笔记本，在这个[网站](https://mybinder.org/)，只需要告诉binder你的 Github 库地址就可以，当然这个库里得有笔记本。这个项目相当于给了公共计算资源，你的GitHub笔记本会被生成一个 docker 镜像，然后借助dockerhub展示给用户，这个项目目前是免费的，也支持R，请不要滥用。

有了jupyter项目与容器技术，科研数据分析的流程就可以实现在线化与可重复性，其实如前所述单纯R的生态也可以做到。这样研究成果发表时应该同时附带对应的数据分析流程报告且最好这份报告也支持在线验证，这样就很容易从技术上堵掉图片误用这类说不清道不明的漏洞。上传原始数据并同时上传数据处理脚本，所有处理过程都让电脑来完成，这样审稿只需要关注处理方法是否合理就可以了，因为这里面从数据到结果没有可以人为干涉的空间。我相信重要的发现一定是可重复的，那么起码要保证数据到结果之间100%的重现性。

在验证学术问题上，实验数据比专家口水更管用，代码自动化重现要比手动点击靠谱。
