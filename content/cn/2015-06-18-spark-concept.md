---
title: Spark中关键概念的理解
date: 2015-06-18
slug: spark concept
---

其实我自己对spark的应用场景是没什么需求的，但几个月前不知道怎么想的在edx上选了一门伯克利的[spark课](https://courses.edx.org/courses/BerkeleyX/CS100.1x/1T2015/info)，所以就入了坑。一共五周，现在开到第三周，因为对python不熟加上记性也不好，先把其中比较干货的东西捡出来，此外剩下两周的课可能由于外出开会耽误。我没有计算机科学背景，所以仅按照自己理解与讲义来写，疏漏之处见谅。

## Spark简介

Spark是用来解决大量数据处理问题的一个工具。由于现在数据产生非常快，单机在收集、储存与处理数据上是性能不足的。如果我们用集群的话收集与存储是没问题了，但如何快速处理数据让数据变成知识也是需要工具的。此外，集群出于成本考虑多采用分布式的结构，所以这个工具要做的就是从这些分布式集群中快速准确的提取信息，而这也是spark的设计初衷。

我们来理解一个分布计算场景：这里有一大段文本，我们把它们分成N份去储存，现在我打算计算词频，该如何做？

- 方案一：每个储存单元作为一个处理单元，进行分词后各自计算自己分到文本的词频，然后汇总发送到另一个独立处理单元单独作汇总。这个方案是分层的，高层汇总单元（比较贵）挂了也就挂了，而同时响应并发数据很容易把这个单元搞宕机。

- 方案二：既然两层会挂掉，那我就在中间继续添加独立汇总层，例如在进行最终汇总前面加两个处理单元，每个处理单元只处理下层有限个储存单元的数据然后汇总。这样由于存在缓冲层甚至多个缓冲层，我们的处理单元成本可以相对一致，整体处理的稳定性会好一些。但这仍然是分层逻辑，高层挂了还是全挂。

- 方案三：还是分层，但是这次是逻辑分层，在词频问题上就是我们的处理层不是一台中枢而是多个处理单元。每个处理单元只收集处理逻辑上的一部分，例如处理中心A只响应词频高于100的，B只响应50～100的…这样出现宕机只会损失一部分运算。

在这里前面负责分词那一部分可理解为数据的map，也就是映射成可独自处理的小部分，而后面根据词频分别汇总可理解为reduce，也就是处理为想要的部分。整个流程就是先map到想要处理的东西，然后reduce为处理后的东西，不断循环。类似R里面从原始数据中提取想要的数据后进行处理，只是应用场景换成比较高大上的集群，而规模一大就需要有工具来把底层分发处理工作高效化，这样看spark实际提供了一个处理对象，底层的黑活（例如某个处理单元挂了重启）通过spark完成，我们只管用熟悉的数据处理方式来处理spark对象就可以了。

其实这个问题不是spark首先发现解决的，Hadoop也是来处理这个问题的，但由于Hadoop都是硬盘读写操作，大量的I/O会降低处理速度，spark的一大高明之处在于把硬盘读写省了，都在内存里玩，如果中间处理品需要，可以另外cache。

## Resilient Distributed Datasets(RDD)

RDD是spark的核心概念，所有要处理的数据都以RDD形式存储或使用。RDD可以直接生成或通过其他格式转化，这个处理对象从硬盘数据生成后运行在内存里，然后你就可以用熟悉的编程语言来处理这个对象了，目前支持Scala，Java，R与Python，同时Spark也提供了不少自带的函数来进行数据分析，前提是你得学下Scala。

## Driver and Workers

Spark里一个程序是由两部分组成：Driver与Workers。Workers工作在集群节点或线程中，而上面说的RDD是分布在这些Workers中。Driver就是你的应用需求了，把需求提给Workers就完成编程了。

## RDD的创建与操作

以下讨论我使用的是PySpark中的术语，也就是使用Spark的Python接口包。

首先是RDD的创建，RDD可以来自python的list对象，也可以来自RDD的转化与直接从硬盘读取。在RDD创建时，你可以指定RDD的分区，例如指定为5就是说会分发到5个集群节点去处理。这里是可以精细化配置的，当然你得对集群有概念，反正我没概念。

然后是RDD的操作，有两种类型，一种是transformations，另一种是actions。当你指定transformations时操作不会立即执行，属于lazy loading，当指派了actions后，操作才会执行。此外如前所述，RDD可以缓存到内存或硬盘上，对于使用者而言只要缓存了就ok，底层工作让spark来做就够了。

filter及与Hadoop类似的map功能是属于transformations的，也就是说我可以先写一大段transformations，但只要没有actions的功能例如计数（count）或收集（collect），这些语句是不被执行的。举个例子，我打算从集群的数据里map某个条目，然后filter其中符合某些特征的条目，最后计数。只有最后这个是actions，如果没有这个命令，前面那一套都不执行。

## Spark程序生命周期

- 从外部数据中建立RDD
- 通过transform变成新的RDD
- cache()一些关键RDD为了复用
- 执行actions来进行计算并输出结果

## Broadcast Variables

当某些变量需要只读的分发给所有workers，spark可以通过广播这些变量到所有workers。举例而言，当你需要反复利用同一个数据表做查询，如果每个workers都计算一遍就不如把这个表先生成广播到所有workers里来的高效。

## Accumulators

聚合所有workers结果回driver而workers之间不需要传送时，spark提供accumulators来汇总，提高性能。举例而言，当我做求和时需要汇总各个workers的数值到driver，我并不需要workers去读取driver上的数值，这时accumulators就可以在全局上进行汇总。

## PySpark实例

### RDD的建立

~~~python
# 从python list里构建
data = [1,2,3,4,5]
# 这个构建行为不是actions，只是指定构建方式，包括分发数
RDD = sc.parallelize(data,4)
# 从Hadoop输入格式建立
distFile = sc.textFile("README.md", 4)
~~~

### RDD的transformation与lambda函数

~~~python
# 构建RDD
rdd = sc.parallelize([1,2,2,4])
# 用python的lambda函数来构建映射
rdd.map(lambda x: x * 2)
# RDD:	[1,2,2,4] → [2,4,4,8]	
rdd.filter(lambda x: x % 2 == 0)
# RDD: [1,2,2,4] → [2,2,4]
rdd.distinct()	
# RDD: [1,2,2,4] → [1,2,4]
~~~

从这里我们可以看出这个操作非常类似R中对数据框的操作，但因为是lazy的，没有action命令它们不会实际被执行。

### RDD的action与lambda函数

~~~python
rdd = sc.parallelize([1,2,3])
rdd.reduce(lambda a,b: a*b)	
# Value: 6
rdd.take(2)
# Value: [1,2]	
rdd.collect()	
# Value: [1,2,3]	
~~~
Spark的一大优点在于比Hadoop提供了更多的操作，这一点需要详查文档体会。

### Broadcast Variables

~~~python
# driver端	
broadcastVar = sc.broadcast([1,2,3])	
# worker端
broadcastVar.value
# [1,2,3]
~~~

### Accumulators

~~~python
accum = sc.accumulator(0)	
rdd = sc.parallelize([1,2,3,4])	
def f(x):	
 global accum
 accum += x			
rdd.foreach(f)	
accum.value
# Value: 10	
~~~