---
title: 理解基因组数据分析之结果注释与通路分析篇
date: 2015-08-29
slug: genomewide data 4
---

上面三篇费了半天口舌的最终目的就是找出靠谱的差异基因，但到这里只算是研究的开始，下一步我们要为这些差异基因寻找意义。

分子生物学的研究方法一般就是围着中心法则转圈并找出同一层次的上下游变化。举例而言，如果我们实际发现一个突变性状想找到调控基因，那么你最好能纯化出这个蛋白或者根据相似性原理找一组同源蛋白，拿到序列后想办法搞出抗体来，然后活体或质粒去验证下有没有高表达，找出功能与目标蛋白的联系。当你确定找对了蛋白，剩下要做的就是反推序列合探针找基因，找到了基因也要做下功能验证。验证完了发现对不上可以考虑下RNA了，这种调控就比较麻烦了。等基因找到了，就该讨论基因上下游调控了，如果不用基因芯片，那就通过类似通路去推理，然后围着中心法则转一圈去寻找出现共同变化的基因。这里面实验上的奇技淫巧特别多，传统老派的研究人员也比较认可这类基于免疫分析的套路。

组学技术基本就把上面的思路反过来了，我们直接通过基因芯片或基因组测序拿到差异基因或序列，然后沿着中心法则一路走下去做验证，最后自上而下给出调控机理。组学技术不仅仅体现在基因层，灵活使用基因芯片是可以找出转录因子，对于信号转导的研究也没什么问题。不同于传统方法通过假设去验证，组学带来的信息不是太少而是太多，没有假设就给了一堆验证，这时候就有必要通过数据库的检索与信息挖掘来给出我们想发现的假设或有意思的现象。

因为前面大都基于基因芯片做的讨论，在讨论注释之前有必要介绍下测序研究的工作流程：

- 命令行下`wget`得到公用服务器测序数据的FASTQ文件文件或从仪器端`scp`过来
- 用fastqc检查下测序质量
- 将FASTQ文件对应到基因组里生成BAM文件，`bowtie`常用来映射 DNA测序而`tophat`来映射RNA测序，因为全局比对就不用`BLAST`这种比较局部的算法了
- 用`Rsamtools`包在R中创建BamFile对象
- 用`GenomicAlignments`包进行序列比对计数
- 用`DeSeq2`包对数据进行与基因芯片类似的降噪，用于有实验设计的基因组研究
- 可视化

我们可以看到，在测序研究中同样也是为了发现不同，而这个不同多半来自与公布出的基因组比对。那么首先考虑的是原始数据如何存储？在Bioconductor中，存储与序列相关的对象为`IRanges`与`Grange`。`IRanges`结构比较简单，就是起点长度终点，常见操作如下：


~~~
source("http://bioconductor.org/biocLite.R")
biocLite()
library(IRanges)
# 单个范围，有起点终点也有宽度
(ir <- IRanges(5,10))
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     5  10     6
~~~

~~~
# 可对范围进行平移
shift(ir, -2)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     3   8     6
~~~

~~~
# 也可缩小范围
narrow(ir, start=2)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     6  10     5
~~~

~~~
# 还可以展示范围一侧的序列
flank(ir, width=3, start=TRUE, both=FALSE)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     2   4     3
~~~

~~~
# 从开头重新定义长度
resize(ir, 1)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     5   5     1
~~~

~~~
# 下面包括多个范围
(irs <- IRanges(start=c(3,5,17), end=c(10,8,20)))
~~~

~~~
## IRanges of length 3
##     start end width
## [1]     3  10     8
## [2]     5   8     4
## [3]    17  20     4
~~~

~~~
# 总覆盖范围
range(irs)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]     3  20    18
~~~

~~~
# 实际覆盖范围
reduce(irs)
~~~

~~~
## IRanges of length 2
##     start end width
## [1]     3  10     8
## [2]    17  20     4
~~~

~~~
# 总范围内没覆盖到的部分
gaps(irs)
~~~

~~~
## IRanges of length 1
##     start end width
## [1]    11  16     6
~~~

~~~
# 所有范围片段化
disjoin(irs)
~~~

~~~
## IRanges of length 4
##     start end width
## [1]     3   4     2
## [2]     5   8     4
## [3]     9  10     2
## [4]    17  20     4
~~~

`Grange`就是范围加上链、染色体、基因组的信息，见下面


~~~
library(GenomicRanges)
# 构件一个GRange对象
(gr <- GRanges("chrZ", IRanges(start=c(5,10),end=c(35,45)),
              strand="+", seqlengths=c(chrZ=100L)))
~~~

~~~
## GRanges object with 2 ranges and 0 metadata columns:
##       seqnames    ranges strand
##          <Rle> <IRanges>  <Rle>
##   [1]     chrZ  [ 5, 35]      +
##   [2]     chrZ  [10, 45]      +
##   -------
##   seqinfo: 1 sequence from an unspecified genome
~~~

~~~
# 添加基因组信息
genome(gr) <- "hg19"
# 也可进行类似IRange的操作
shift(gr, 10)
~~~

~~~
## GRanges object with 2 ranges and 0 metadata columns:
##       seqnames    ranges strand
##          <Rle> <IRanges>  <Rle>
##   [1]     chrZ  [15, 45]      +
##   [2]     chrZ  [20, 55]      +
##   -------
##   seqinfo: 1 sequence from hg19 genome
~~~

~~~
# 可以增加序列信息列，例如分组等
mcols(gr)$value <- c(-1,4)
# 可以保存多个序列
(gr2 <- GRanges("chrZ",IRanges(c(19,33),c(38,35)),strand="*"))
~~~

~~~
## GRanges object with 2 ranges and 0 metadata columns:
##       seqnames    ranges strand
##          <Rle> <IRanges>  <Rle>
##   [1]     chrZ  [19, 38]      *
##   [2]     chrZ  [33, 35]      *
##   -------
##   seqinfo: 1 sequence from an unspecified genome; no seqlengths
~~~

~~~
# 可以对多个序列比对找出重复的，第一个范围对应第二个范围的位置
fo <- findOverlaps(gr, gr2)
queryHits(fo)
~~~

~~~
## [1] 1 1 2 2
~~~

~~~
subjectHits(fo)
~~~

~~~
## [1] 1 2 1 2
~~~

~~~
# 可以直接截取范围
gr %over% gr2
~~~

~~~
## [1] TRUE TRUE
~~~

~~~
gr[gr %over% gr2]
~~~

~~~
## GRanges object with 2 ranges and 1 metadata column:
##       seqnames    ranges strand |     value
##          <Rle> <IRanges>  <Rle> | <numeric>
##   [1]     chrZ  [ 5, 35]      + |        -1
##   [2]     chrZ  [10, 45]      + |         4
##   -------
##   seqinfo: 1 sequence from hg19 genome
~~~

另外有一种`Rle`数据类型也可使用，更节省空间。

从上面我们可以看到R中构建一个序列对象与进行序列比对的底层操作，这也是很多基于R的比对可视化基础。当我们得到BamFile对象时其比对的基础就是一组范围。基因组级别的比对属于多对多，用`GenomicAlignmets`包提供的比对函数比较方便。如果你对比的基因组有新版本，这时候可用`rtracklayer`包中liftOver功能来重新比对。此外，也可以包含对应序列用来后续的突变研究。

终于到了注释这一段了，首先要确定比对的是序列还是基因基因组，前面对应测序研究，后面对应基因芯片。通过序列中给出的参考基因组信息与芯片对应的基因组信息，我们可以从Bioconductor中很方便的找到比对基因组。序列层基因组测序就可以直接可视化去探索下基因功能了，基因芯片则可通过系统生物学给出的一些包对接网络进行通路分析例如GO跟KEGG。值得注意的是不同数据库对同样的序列或基因有着不同的提法，这时候调用对应物种的注释地图包就可以利用键值任意转换，进而实现不同目的的分析。

下面还是用基因芯片数据来进行一个演示，从数据导入到通路分析。


~~~
# 从GEO上下载某个实验编号为GSE34313的实验数据，该网站也托管了很多实验数据方便他人重复
library(GEOquery)
# 该实验考察了一种激素对平滑肌基因表达的影响
g <- getGEO("GSE34313")
# 表达数据
e <- g[[1]]
# 提取分组数据
e$condition <- e$characteristics_ch1.2
levels(e$condition) <- c("dex24","dex4","control")
# 观察数据是否需要正则化
boxplot(exprs(e), range=0)
~~~

![](http://yufree.github.io/blogcn/figure/genome7.png) 

~~~
# 选取两个分组进行对比
lvls <- c("control", "dex4")
es <- e[,e$condition %in% lvls]
es$condition <- factor(es$condition, levels=lvls)
# 寻找差异基因
library(limma)
design <- model.matrix(~ es$condition)
fit <- lmFit(es, design=design)
fit <- eBayes(fit)
tt <- topTable(fit, coef=2, genelist=fData(es)$GENE_SYMBOL)
# 用GO号选取某个基因组进行差异比较
idx <- grep("GO:0006955", fData(es)$GO_ID)
(r1 <- roast(es, idx, design))
~~~

~~~
##          Active.Prop    P.Value
## Down      0.16269841 0.01350675
## Up        0.09325397 0.98699350
## UpOrDown  0.16269841 0.02700000
## Mixed     0.25595238 0.00800000
~~~

~~~
# 测试多个基因组
# 读取人类基因组数据库
library(org.Hs.eg.db)
# 提取基因组定义
go2eg <- as.list(org.Hs.egGO2EG)
golengths <- sapply(go2eg, length)
govector <- unlist(go2eg)
# 基因匹配
idxvector <- match(govector, fData(es)$GENE)
table(is.na(idxvector))
~~~

~~~
## 
##  FALSE   TRUE 
## 239596   8306
~~~

~~~
# 获得改变基因
idx <- split(idxvector, rep(names(go2eg), golengths))
# 筛选基因数大于10的基因组
idxclean <- lapply(idx, function(x) x[!is.na(x)])
idxlengths <- sapply(idxclean, length)
idxsub <- idxclean[idxlengths > 10]
# 计算基因组表达差异谱
r2 <- mroast(es, idxsub, design)
head(r2)
~~~

~~~
##            NGenes  PropDown     PropUp Direction PValue        FDR
## GO:0005125    174 0.2758621 0.04597701      Down  0.001 0.01043919
## GO:0008083    167 0.2874251 0.07784431      Down  0.001 0.01043919
## GO:0070098     65 0.2461538 0.06153846      Down  0.001 0.01043919
## GO:0043433     63 0.2698413 0.12698413      Down  0.001 0.01043919
## GO:0042102     54 0.1666667 0.09259259      Down  0.001 0.01043919
## GO:0006959     53 0.2452830 0.09433962      Down  0.001 0.01043919
##            PValue.Mixed   FDR.Mixed
## GO:0005125        0.001 0.002596639
## GO:0008083        0.001 0.002596639
## GO:0070098        0.001 0.002596639
## GO:0043433        0.001 0.002596639
## GO:0042102        0.001 0.002596639
## GO:0006959        0.001 0.002596639
~~~

~~~
# 提取受影响大的基因组
r2 <- mroast(es, idxsub, design)
# 注释上GO数据库里的功能
library(GO.db)
# 提取受影响大的基因组功能
r2tab <- select(GO.db, keys=rownames(r2)[1:10],
                columns=c("GOID","TERM","DEFINITION"), 
                keytype="GOID")
# 展示数据
r2tab[,1:2]
~~~

~~~
##          GOID
## 1  GO:0005125
## 2  GO:0008083
## 3  GO:0007623
## 4  GO:0071222
## 5  GO:0070098
## 6  GO:0043433
## 7  GO:0042102
## 8  GO:0006959
## 9  GO:0048661
## 10 GO:0030593
##                                                                                  TERM
## 1                                                                   cytokine activity
## 2                                                              growth factor activity
## 3                                                                    circadian rhythm
## 4                                             cellular response to lipopolysaccharide
## 5                                                chemokine-mediated signaling pathway
## 6  negative regulation of sequence-specific DNA binding transcription factor activity
## 7                                         positive regulation of T cell proliferation
## 8                                                             humoral immune response
## 9                             positive regulation of smooth muscle cell proliferation
## 10                                                              neutrophil chemotaxis
~~~

OK，这一系列四篇文章只算是一个基因组数据分析的入门，先形成类比思想工作就好展开一些。下面给出一些链接，可深入学习。

- [Bioconductor上各种数据分析的流程图](http://bioconductor.org/help/workflows/)

- [Raff教授公开课的开源教材](http://genomicsclass.github.io/book/)

- [糗世界 中文教程比较多 实战经验丰富](http://blog.qiuworld.com:8080/)
