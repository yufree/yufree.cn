---
title: 多重比较从原理到应用
date: 2013-12-16
slug: rgabriel package
tags:
  - data
---
# 多重比较概论

方差分析解决的是分类变量对响应变量的影响问题，通常是用分类变量所解释的变异比上分类变量以外的变异去进行F检验。换句话讲，如果分类变量可以解释大部分响应变量的变异，我们就说这种分类变量对响应变量的解释有意义。例如下面这组数据：

> 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3

总变异为10, 如果我们分组为按照相同的数放到一起，那么组内变异就是0，组间变异为10，这时我们就说这种分组有效的解释了响应变量，F值趋向正无穷。如果我们完全随机分组，组内与组间的变异差不多，那么这种分类方法并不解释响应变量，反映到F值上就是1。

但是仅仅知道是否受影响是不够的，如同上面的例子，我们知道的仅仅是存在一种分类方法可以解释响应的全部变化，其内部也是均匀的，但不同分类水平间的差异我们并不知道，这就是多重比较的起源。实际生活中如果差异很明显往往统计学工具不用出场，所以你应该预想到多重比较或仅仅是均值比较适用的场景往往差异我们不能直观感受，需要统计学工具来帮忙。

同时要注意，如果我们对两组数据做置信度0.05的t检验，我们遇到假阳性的概率为5%。但如果面对多组数据例如3组，进行两两比较的话就有$$choose(3,2)$$也就是3组对比，那么我们遇到假阳性的概率就为$$1-(1-0.05)^3$$，也就是14.3%，远高于0.05的置信度。组越多，两两对比就越多，整体上假阳性的概率就越来越大，到最后就是两组数据去对比，无论如何你都会检验出差异。

那么多重比较如何应对这个问题呢？有两种思路，一种思路是我依旧采取两两对比，进行t检验，但p值的选取方法要修改，例如Bonferroni方法中就把p的阈值调整为进行多重比较的次数乘以计算得到的p值。如果我们关心的因素为2，那么计算得到的p值都要乘2来跟0.05或0.01的边界置信度进行比较；另一种思路则是修改两两比较所用的统计量，给出一个更保守的分布，那么得到p值就会更大。不论怎样，我们这样做都是为了降低假阳性，但同时功效不可避免的降低了。

# 多重比较的可重复性

我们设计一个实验考察一个因素对响应变量的影响，结论无过于有影响，没影响。多重比较的前提是有影响，给出的答案是对影响的估计：影响有多大。那我们重复这个实验所要考虑的问题就是能否重现影响，影响的方向与大小是否与文献报道一致。

就方向而样，虽然我们都不承认0假设（要不然还做什么实验），但当我们默认设定为双尾检验时，假阳性就被默认发生在两个方向上了，这样的多重比较必然导致在其中一个方向上的错误率被夸大了。

就影响大小而言，如果我们每次重复都选择效应最强的那一组，重复越多，预设的偏态就越重，换言之，我们的零假设因为重复实验的选择偏好而发生了改变。

# 三种错误

- type I 假阳性
  - per-comparison error rate (PCER) 进行多次对比得到的假阳性的概率
  - familywise error rate (FWER) 将多组比较看作一个大组，这时造成的错误率
  - false discovery rate (FDR) 控制假阳性与总拒绝率的比例 
  - 一般而言 PCER ≤ FDR ≤ FWER FWER更容易不拒绝空假设，更保守
- type II 假阴性
- type III 有差异 方向错误

# 类型

- Single-step procedures 单步法 只考虑对H0的影响，不考虑其他影响
- Stepwise procedures 逐步法 考虑其他假设检验对单一检验的影响
  - Step-down procedures 排序后先对比第一个，有差异对比下一个，当出现无差异时停止对比
  - Step-up procedures 排序后对比，有差异时停止对比，之后均认为有差异
- 两两比较 不同组之间进行均值比较，最常见
- 对比 除了考虑不同组间均值比较，还考虑均值间线性组合的新均值的差异性，F检验有时是因为对比而不是两两比较产生的显著性

## 单步法等方差

### Tukey's HSD(两两比较)

- 基于t范围分布
- 等方差同数目，如果数目不同则使用Tukey-Kranmer方法
- 两两比较最佳，数目相同功效弱于下降法

### Bonferroni(两两比较)

- 切割α，如果进行了c次推断，整个错误率为cα
- 通用方法，应用在任一个推断
- 方法简单，但十分保守
- 只对比部分的话可自定义c值
- 适用于指定对比数情况，此时功效高于Tukey

### DST(两两比较)

- 对Boneferroni方法的改进，功效更高

### GT2 test(两两比较)

- 功效高于Dunn-Sidak方法

### Gabriel(两两比较)

- 分组数目相同等同于GT2，不同时功效高，但不保证α
- 易于可视化

### Scheffe test(两两比较)

- 两两比较中功效最弱

### Tukey's HSD(对比)

- 涉及2～3个均值时功效最高

### Bonferroni(对比)

- 指定对比数

### DST(对比)

- 指定对比数，功效高于Bonferroni

### Scheffe test(对比)

- 保证α，两两比较功效最高

## 单步法异方差(对比与两两比较)

### GH procedure

- 不保证整体错误率，有时会超过，保守但功效高

### C

- 保证整体错误率

### T3

- 保证整体错误率

### Brown-Forsythe-Scheffe

- 功效最高

## 单步法空白对比

### Dunnett

- 用于对比controls的变化
- 其他组对比不考虑

### Hsu's MCB

- 对比均值与其他最好（自定义，可最大，亦可最小）
- 目的寻找比其他好的而不是不同的
- 对比次数最少，功效强，但低于Dunnett

## Stepdown procedures

- 基于Tukey法
- 先比较最大最小，q值取分组数
- 比较最大第二小，q取分组数-1
- 继续直到出现无差异停止
- 当不需要置信区间且样本数相同时使用
- 不推荐SNK与Duncan，推荐REGWF或REGWQ方法

### SNK

- 不保证α

### Duncan

- 不保证α

### Ryan-Einot-Gabriel-Welsch-Fisher(REGWF)

- F检验加强版，保证α

### Ryan-Einot-Gabriel-Welsch-Q(REGWQ)

- q值法加强版，保证α

## step-up procedures

- Welsch 
- Hochberg 
- Dunnett and Tamhane 

# 简略选择指南

## 总体控制错误率

- 两两比较用Tukey法
- 对比用Scheffe test
- 指定对比数考虑 Gabriel > GT2 > DST > Bonferroni
- 跟control比较用Dunnett
- 方差不相等用GH，C，T3等方法

## 错误率

- 保证α用Tukey Scheffe Dunnett
- 不保证用其他的

## 探索与确认

- 事前分析确定对比数用 Gabriel GT2或Scheffe
- 事后确定对比用Tukey或各种stepwise方法

# 其他

写这篇文章是为了理清多重比较的一些基本概念，同时我自己也写了一个R包叫做[rgabriel](http://cran.r-project.org/web/packages/rgabriel/index.html)，这个包可用在指定对比数的多重比较与可视化中。此外，特别感谢[谢益辉](yihui.name)对其中SMM分布的指导与帮助。如有时间精力，我会将同样基于该分布的GT2与T3方法写入包中。

# 参考资料

- Rafter, J.A., Abell, M.L., Braselton, J.P., 2002. Multiple comparison methods for means. Siam Review 44, 259–278.
- Bretz, F., Hothorn, T., Westfall, P., 2010. Multiple Comparisons Using R. CRC Press.
- http://cos.name/cn/topic/142002

