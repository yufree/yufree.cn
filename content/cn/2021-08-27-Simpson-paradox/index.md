---
title: 辛普森悖论
author: Miao Yu
date: '2021-08-27'
slug: Simpson-paradox
categories: []
tags: []
---

曾经有两本书伴我度过了无数漫漫长夜，毕竟每次鼓起勇气看不超过10页就会睡过去，一本是[前面](https://yufree.cn/cn/2020/09/01/metaphor/)写过的 **metaphors we live by**，另一本就是《悖论简史》。这种书的一大特色就是读的时候如果不带脑子看不懂，带脑子就头疼，但可气的是写的还挺有趣。

基础科研的很多突破都是来自于悖论或者说反例，不过这里的悖论属于理论悖论，大概率是理论本身有问题，需要新的理论来解释观察与实验。还有很多悖论属于错觉，本身不是悖论仅仅因为解释上的片面出现，其实魔术就可以化为这一类，很多魔术手法展示的现象完全是违背常理的，但了解手法后就会发现其实是利用了一些惯性思维产生的错误解释。真正的悖论是语义学上的，例如“这句话是错的”就是一个语义悖论，如果认为这句话是错的那就应该是对的，但如果认为这句话是对的其又描述了一个自己是错误的判断，这种带有自指的悖论属于无解。其实数学领域的第三次危机本质上也要通过语义学划定语义解释范围来凑合解决，这属于逻辑自身的漏洞。

辛普森悖论属于某种程度上的错觉悖论。其本质就是说存在一种分组方法，让`$\frac{A_1+B_1}{C_1+D_1} > \frac{A_2+B_2}{C_2+D_2}$`，然后`$\frac{A_1}{C_1}<\frac{A_2}{C_2}$` 并且 `$\frac{B_1}{D_1}<\frac{B_2}{D_2}$`，乍看之下会感觉莫名其妙，因为数学上找这么一组数太简单了（睡不着觉别数羊，就去构造辛普森悖论，比数羊效果好多了）。

`$\frac{1+3}{5+4} = \frac{4}{9} > \frac{4}{10} = \frac{2+2}{8+2}$`

`$\frac{1}{5}<\frac{1}{4}$` 并且 `$\frac{3}{4}<\frac{1}{1}$`

从数学角度看完全不存在悖论，因为`$\frac{A}{B}+\frac{C}{D} \neq \frac{A+B}{C+D}$`，所以`$\frac{A}{B}$`与`$\frac{C}{D}$`的数值比较关系无法传递到`$\frac{A+B}{C+D}$` 的比较里。

但我们要加个语境就完全不同了。例如，这里我们把上面的数扩大十倍，某种化学品暴露组一共90人患病40人，对照组一共100人患病40人，此时研究人员会得出暴露组发病率比对照组高的结论。然而，如果暴露组里有50名男性发病10人，对照组80名男性发病20人，我们会发现男性对照组发病率高于暴露组；而同时女性40人里发病30人，对照组里20人发病20人，还是暴露组低于对照组。

同样的数据，如果环境科学家看到会说这是一种致病污染物需要禁止而药厂则认为这是一种对不同性别都有效的预防性药物，两边成果都足以发表业内很好的杂志上也都说得通，但解读出的含义完全相反。由于人体本身就有回归到正常的现象，确实存在一些病吃药七天恢复不吃药一星期恢复，所以很多我们研究发现的效应如果不能强到药到病除而需要通过不断细分数据来发现效应，那么大概率就会存在辛普森悖论。

但问题现在的很多病的新药或常见保健品就是这个表现水平，徘徊在吃不死人的底线之上通过安慰剂效应或信仰来起效果，这就很尴尬了。保健品大多数吃了虽然没用但也不会有害，跟食物差不多效果但价钱就不一样了。而且如果一个人得了慢性病，大概率本来身体状态就是起起伏伏，此时你吃保健品就会形成一个错觉：身体状态好就会认为保健品起效了而不好则会认为没吃够或者哪天忘了吃了。保健品本身就起到了信仰的效果，功劳都是它的罪过都是自己的，有这份心什么成不了？

其实我跟安慰剂效应有很深的渊源，小学每年都有体测，那时候我跑步不行，就开始动歪脑筋，反正体测又不尿检不如用兴奋剂来提高成绩。但问题我家哪有兴奋剂啊，回去一通翻箱倒柜发现一桶咖啡，我之前也没喝过心想这玩意也算兴奋剂吧？结果冲了一碗就去体测，当时感觉甜甜的还挺好喝，效果也还不错，成绩有明显提升。这事过去快一年等到下一次体测来的时候我又想起这玩意了，这次又翻出来仔细读标签才发现是“咖啡伴侣”但伴侣两个字很不好认，也就是喝的是植脂末跟奶粉，这次成绩就崩了。好多年后我才喝到真正的咖啡，说实话，还不如咖啡伴侣好喝。

后来跟父母说起这事就奇怪，家里又没人喝咖啡为啥要搞一罐咖啡伴侣？答案也不难猜，这是过年走亲戚送来送去留下来的礼物，他们买的时候估计也当成咖啡了，包装洋气而且比真咖啡便宜多了。这里能促进成绩的其实只是服用了兴奋剂的信念而非兴奋剂，也就是当一件事决定因素心理影响更大时，药物的药效反而成了玄学了。当然重申一下，体测别动歪脑筋，人本身的潜力要远大于外界刺激，平时加强锻炼才是正道。否则，凭运气赚来的，早晚都要凭实力输出去，这就是所谓的回归现象。

接着说辛普森悖论，这里我们已经看到，数学上比较整体比值与局部比值是毫无意义的，各种情况都会出现。然而，如果我们给数字赋予含义，那么就会出现不同专业基于不同立场给出的完全相反但又都解释得通的结论。也就是说，从绝对的数学计算上，这就是个鸡同鸭讲毫无意义的比较，但赋予背景后，现实中又确实存在明确的问题，例如前面说的那种化学品究竟是应该推广还是禁用？这个问题咋解决？

此时我们就不得不进入因果推断的领域了，我们必须对化学品、性别及疾病这三者关系建模，这也算某种三体问题了，考虑方向其实一共就23种关系：

## 三者都没关系

- 化学品 性别 疾病

## 三者里只有一组两两关系

- 化学品->性别 疾病
- 化学品<-性别 疾病
- 化学品 性别->疾病
- 化学品 性别<-疾病
- 性别 化学品->疾病
- 性别 化学品<-疾病

## 三者里有两组两两关系

- 化学品->性别->疾病
- 化学品->性别<-疾病
- 化学品<-性别->疾病
- 化学品<-性别<-疾病
- 性别->化学品->疾病
- 性别->化学品<-疾病
- 性别<-化学品->疾病
- 性别<-化学品<-疾病

## 三者里有三组两两关系

- 化学品<-性别<-疾病<-化学品
- 化学品<-性别<-疾病->化学品
- 化学品<-性别->疾病<-化学品
- 化学品<-性别->疾病->化学品
- 化学品->性别<-疾病<-化学品
- 化学品->性别<-疾病->化学品
- 化学品->性别->疾病<-化学品
- 化学品->性别->疾病->化学品

我们的专业知识或者语义本身就可以缩小待检验的模型，例如性别是先天的，所以凡是有化学品决定性别的都可以排除掉，疾病也不可能决定性别跟化学品，此时我们就剩下六种模型了：

## 三者都没关系

- 化学品 性别 疾病

## 三者里只有一组两两关系

- 化学品<-性别 疾病
- 化学品 性别->疾病
- 性别 化学品->疾病

## 三者里有两组两两关系

- 化学品<-性别->疾病
- 性别->化学品->疾病

## 三者里有三组两两关系

- 化学品<-性别->疾病<-化学品

这里假如我们发现性别确实会同时影响化学品跟疾病，那么就必须考虑控制性别后的净效应。假如性别只影响化学品不影响疾病（例如女性喜欢用化妆品暴露量更大），那么那么我们则不需要控制性别可以直接考察化学品对疾病的影响。如果性别也不影响化学品，那么也可以直接考察化学品对疾病的影响。这就是三种化学品跟疾病有关系的模型。如果化学品跟疾病本就没关系，甚至性别也跟疾病没关系，例如这是一种细菌性传染病，那从一开始研究就没有因果关系支持，做出的结果就属于玄学了。但一定不要直接排除掉这些可能，不论常识还是专业知识都排除不了就需要逐一考察。

通过分析这三种模型，我们会发现要首先检验性别跟疾病是不是有关系，确定了这一条，后面就知道是不是要考虑按性别分组了。此时辛普森悖论从实际意义上就解决了，靠的其实还是我们自己赋予的实际语义与专业知识，但别忘了专业知识可能本身就是错的，实际语义可能存在二义性，这些才是搞出悖论的根基。

不过如果我们看回原始版辛普森悖论，里面的三体是性别、学院及录取率，要解决这个问题就还是要把23种可能性全列出来然后排除掉学院决定性别、录取率决定性别这些语义跟常识上不存在的可能性，然后就可以知道需要检验的是什么了，但这里可以看出辛普森原版悖论可排出的可能性要比我的例子少，因此需要检验的模型就更多，跟性别有关决定录取率的模型有关的有五个。我们来看下其中两个有三组两两关系的模型：

- 性别->学院<-录取率<-性别
- 性别->学院->录取率<-性别

学院决定录取率还是录取率决定学院这个是不太好说的，因为这两者可能并不是谁决定谁的，可能被学校同时控制，例如学校会决定学院规模与最低录取率之类，此时就不是三体问题，因为另一个变量学校又出现了：

- 性别->学院<-学校->录取率<-性别

此时因果图出现一个对撞结构，你要是需要控制学院就开了后门无法正确估计性别的作用，此时就不应控制任何变量直接看两者关系。但真实世界哪有这么简单，学校这个因素通常我们根本观察不到，所以也不好假设其与学院的关系，如果学院可以影响学校决策，此时就还是要控制学院。也就是说辛普森悖论是否有解其实完全要依赖实际存在的因果关系。

Judea Pear 曾经写过一份辛普森悖论的技术[报告](http://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf)，里面给出了一种无限层级的因果图，他起了名叫做辛普森悖论机。在那张图里，如果你顺次控制混杂因素与对撞因素，那么原因与结果就会反复出现需要控制变量与不需要控制变量的情况。也就是说，想解决悖论，重要的是解决背后的因果图，不同语境逻辑或因果图下对其他变量控制与否是可以完全不同的。我们最终只能接受一个相对语境下的正确答案，绝对语境下那个数学问题其实并没有意义。

也就是说，辛普森悖论其实暗示了我们不同自洽逻辑下可以出现不唯一的正确解，而这个正确与否取决于你对其背后因果关系模型的假设，而这种假设可以不唯一。好消息是自然科学中检验假设很大一部分可以通过实验来证实或证伪，但坏消息却是我们日常交流用的语言与语义可能天然就无法将因果关系描述清晰，能量化的数值无物理意义而有物理意义的数值无法量化，这就导致我们只能看到模型下的真实而无法验证模型本身。这部分内容在科学哲学里就涉及实在论与非实在论了，也是催眠利器。

或许我们所谓解决悖论的方法不过就是引入一套模型屏蔽掉会产生悖论的讨论，但这反而说明了悖论的无解与我们自然语义天然存在漏洞。至于说不同学科根据自己学科利益来报道结果倒也不用太担心，这类弱效应的成果最多搞出一堆保健品与智商税产品，基本上无害。