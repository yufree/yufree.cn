---
title: 打造一个新组学
author: ''
date: '2019-11-26'
slug: reactomics
categories: []
tags:
  - paper
---

今年ASMS我提出了一个新的概念，叫做反应组学（reactomics），这将会是我接下来一段时间工作的主题。现在我梳理下这个概念提出的过程。

首先是科学问题，生命过程的核心是中心法则，基因在分子层面上就是四种碱基DNA的排列组合，当然现在我们知道DNA的种类与修饰比想象的多。基因转录为RNA，分子层面也还是个位数种类。等到RNA合成蛋白质，基础分子种类一下增长到了20种基本氨基酸。我们先不去讨论表观遗传与各类RNA调控，蛋白质往下一层就是底物与代谢物。那么我们如何研究过程呢？DNA/RNA可以测序，蛋白可以用免疫荧光，当然现在最热的蛋白解析方法还是结晶、冷镜与质谱。但说来说去这些大分子都是小分子搭建出来的，分子骨架来来回回不超过五十种，但到了代谢物上分子骨架一下子就爆炸了，HMDB里存了十几万小分子代谢物而chemspider里有几十万化合物，ACS里有注册号的物质1.4个亿，这时候别说排列组合了，穷举一遍都是时间上不可能完成的任务。搞代谢组学的课题组大都卡在这个未知代谢物鉴定上了。搞不清楚小分子是什么，如何谈相互作用呢？

那么我们现在如何分析小分子呢？基本上是依赖质谱。简单说就是先让分子电离，然后加一个电场，不同荷质比物质在磁场中跑的距离不一样或轨迹不一样这样我们就得到这个物质了。但分子是有可能具有同分异构体的，所以就有了多级质谱或硬电离技术，核心思想就是把分子搞成碎片，因为碎片跟结构是有关系的，所以可以用来定性。现实样品通常是混合物，除了单纯依赖质谱进行分离，另一个思路就是耦合其他分离手段，最常见的就是接一个色谱柱，色谱柱可以理解成一个灌木丛，有的分子不与灌木丛作用很快就过去进质谱了，有的则被灌木丛阻挡，这样同时进样不同时间出峰也可以用来定性。现在的离子淌度质谱则是在电离后接了个迁移板，不同离子淌度物质会在这里实现第三次分离。当然，配合紫外荧光等方法，这个多维度检测的游戏还有很多玩法，但这些玩法要么灵敏度不够，要么有点贵，常见的还是色谱质谱方法进行定性定量，这样我们实际上有三维数据，保留时间、荷质比与响应。最后面那个一般不能拿来定性而更多用来定量，前面两个维度其实就是小分子分析的核心。

上亿种物质是没有人指望两维能分开的，那么为什么实际应用中大家又一窝蜂用色谱质谱联用呢？这其实是一个思维盲点，也就是那种习以为常而不觉得奇怪的东西。作为研究者，我们关心的物质标准品出现在这个两维矩阵上，那么样品里同样发现这个点有信号，我们会认为这是个真信号，潜台词就是随机过程不会在这里出现信号或概率可以忽略。那么问题来了，随机过程究竟是怎么样的？我知道一个石油样品里会出几千个峰，但这些峰实际上是有规律可循的，原因很简单，这些物质都是通过反应一步步生成的而不是等待随机结合。这种一步步的过程有没有很熟悉？对于一个原子，我们知道是存在电子轨道跃迁的，也就是电子不会随机分布在原子核周围而是存在轨道，当然后来发现这个东西测不准所以用电子云来描述，但轨道上出现电子的概率是高于非轨道空间的，这是量子效应，也就是不连续的。那么分子生成是否存在“轨道”呢？

答案显而易见，分子生成没有轨道，但会遵守化学反应，只要条件合适两个分子就会反应生成其他产物。这里我们回忆一下为什么基因组蛋白组可以做，原因在于其关注的分子间的相互关系是固定的，对于基因就是碱基配对，对于蛋白就是肽键，对于广义上的小分子就是化学反应。从这个角度看，我们现在在做的是无疑就是本末倒置了，因为通常我们是通过鉴定物质之后根据物质相关性来推测反应的存在，但是我们的质谱事实上已经监测到了反应。这就是反应组学的核心概念：质量差。我们如果得到几千个物质，在没有先验知识条件下单纯依赖高分辨质谱与保留时间进行鉴定怎么看都是不靠谱的穷举，但如果这些物质同时出现，那就一定不是随机过程，这里面至少有这个地球物质的一个特性，那就是他们都是通过反应来的，因此质量差是可能会富集到一些反应特异的区间，例如2.02Da就是一个很常见的双键打开过程，15.99Da则是一个氧化过程，也就是说质量差是量子化不连续的，会特异性富集在一些这个星球物理化学法则允许的最常见的差异段上。当我们无法搞清楚差异段上每一个分子时，直接对质量差进行定性定量就是最简单的方法。在这里质量差所保存的信息就是反应组学所要研究的目标，之所以是组学是因为质量差填补了蛋白组与代谢组之间的空档，但严格来说蛋白组与基因组都是反应组的特例。

有了核心概念，我们就需要构建对这个概念的测量方法，也就是定性定量方法。对于质量差定性而言，我们需要搞清楚两件事：质量差与化学反应的特异性怎么样，准确性又怎么样。这个就需要对已知的数据库进行数据挖掘，我从网上搞到了KEGG的反应数据库，然后对每一个反应进行了质量差的计算。在这里有个问题，我们的质量差是数学上的，但数据库里是生物意义上的，同样质量差会出现在不同反应里，不过我们深入想的话会发现同样的质量差可能是因为反应所需要的酶或蛋白是一样的。也就是说，质量差可以用来定性一组反应。事实上，频率前20的质量差覆盖了70%以上的已知反应。同时，有意思的是，单个反应里可以产生多个质量差，有的质量差是对应一组反应而有的质量差则会特异性对应单一反应。这样我们通过设计一个反应质量差的算法就可以同时定义出反应类型的定性质量差与特定反应的质量差。那么准确性呢？我们知道质谱有高分辨有低分辨，那么分辨率放到什么合适呢？对于单一物质，一般用ppm来设定，但质量差就不好用ppm来设定，因为存在质量差的物质在测定上准确率就不一样。对此我进行了针对HMDB的计算，发现小数点后三位的质量差基本可以实现质量差与分子式差的一一对应，小数点后两位大概有一半假阳性也可以接受，但小数点一位与单位质量数的准确率不到10%。这样的话如果想对质量差定性，我们需要小数点后至少两位，也就是时间飞行质谱是底线，四级杆离子阱就别来凑热闹了。想做反应组学，高分辨质谱是必须品。解决了定性我们需要定量方法，质量差至少要涉及一对以上的物质，而且说到定量，做过质谱分析的都知道单一物质有定量离子与定性离子，那么所有符合质量差的物质对也是需要定量质量差的。什么是定量质量差，简单说就是这一对物质在不同样品里的响应比例要稳定，例如rsd%在30以内。有了定量质量差，我们就可以直接定量一个特定的质量差了。

有了是什么（质量差）与怎么测量（定性定量），我们就要看下这个所谓的反应组有什么应用。第一个应用自然是代谢物的寻找与筛选。我们目前找一个物质的代谢产物时通常的思路是根据可能的反应预测产物的结构与二级质谱，然而我们并不知道产物的产物是什么样，有些计算工具可以预测两到三层，但此时计算空间已经非常大了。采用质量差就不那么费事了，我们在预设一组质量差与母体化合物后可以设计算法自动寻找数据里符合质量差的产物，然后以此为起点继续搜索直到找不到。这样我们的结果就不受计算性能的限制，数据有多少我们就搜多少。根据我对之前发表文章数据的重新分析，我发现了不仅仅二级，甚至三级、四级与五级产物都可以通过质量差网络找出来，且不用服务器，个人电脑就可以做。第二个应用则是对化合物的溯源。我们分析一个样品，通常并不知道哪些是内源产物，哪些是外源产物。然而，前面对反应数据库的研究发现生物反应是会富集在二十几个质量差上的，如果我们对所有物质构建质量差网络，生物来源的物质就会被连接到一个大网络里，而外源化合物则因为没有对应的酶来催化反应，其就会以低概率出现在大网络里。有了这种拓扑特征，我们就可以用每个峰的度来判断是否是外源化合物。这个结果我用 T3DB 数据库做了验证，结果符合预期。第三个应用就更具备实际意义，通常我们做代谢组学是为了找生物标记物，一般都会认为生物标记物需要是一个物质，但有了质量差定量方法后，我们就可以找生物标记反应或生物标记质量差了。我在一组公开的肺癌数据集里发现质量差 2.02 Da 可以作为正常人与病人的生物标记反应，因此具备诊断潜力。

构建概念，设计测量方法与应用，这个“反应组学”就打造出来了。反应作为比碱基对与肽键更基础的概念对于分子层面的研究应该有不错的前景。至于是否合理，我已经把论文放到了[预印本](https://www.biorxiv.org/content/10.1101/855148v1)服务器上，欢迎大家批评指正。