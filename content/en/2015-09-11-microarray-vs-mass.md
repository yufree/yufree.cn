---
title: The Data Analysis Similarity between Microarray and GC-MS
date: 2015-09-11
slug: microarry vs ms
---

I have finished [Data Analysis for Genomics(HarvardX-PH525x)](https://courses.edx.org/courses/HarvardX/PH525x/1T2014/info) by Prof. Rafael A Irizarry and Dr. Michael I Love for more than a year until recently I realised the data analysis similarity between microarray and Gas chromatography–mass spectrometry(GC-MS).

When we talked about data analysis of microarray, we use different genes or probes as the rows and different samples as the columns. The responses are fluorescence signals.

When we talked about data analysis of microarray, we use different m/z as the rows and different retention times as the columns. The responses are count signals.

Interesting, the Total Ion Chromatorgraphy(TIC) is widely used in GC-MS while heatmap in microarray. How about show the heatmap of GC-MS and TIC of heatmap.

Wait, we couldn't do a thing without meanings. Why use TIC in GC-MS? Because we always think one compound would show at certain retention time. However, under EI source or hard ionization, one compound could show many m/z responses. In environmental analysis, the matrix effect might also show responses. Then we got the meanings: the heatmap of GC-MS would show a visualization of matrix effect.

How about TIC in microarray? I don't think such plot has meanings because there is no time dependences in the samples of microarray.

But when the data could be shown in heatmap, we might employ some noise reduction methods to ease the matrix effect. The following two heatmaps were a native "before and after" results processed by some microarray data analysis methods. Yeah, now I think it is OK to use such method to reduce the matrix effect in environmental samples.

![](http://yufree.cn/blogcn/figure/h2585bg.png)

![](http://yufree.cn/blogcn/figure/h2585diffgcms.png)

Wait, my paper is writing. And I will show the details of such method soon(maybe or might be).
