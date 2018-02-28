---
title: Pittcon 2018
author: ''
date: '2018-02-27'
slug: see-you-pittcon-2018
categories: []
tags:
  - conf
---

This is the first time I attend Pittcon. The past two days I saw a lot of old friends and some big fish on analytical chemistry. However, this post is mainly for my two presentations on Feb. 28th, 2018 in case someone miss the take-home message either by the early presentaion time or my communication skills.

## Online batch correction and interactive data visualization for GC/LC-MS data

This oral presentaiton are mainly focused on the online application [XcmsPlus](https://yufreecas.shinyapps.io/xcmsplus/). This app is powered by [R](https://www.r-project.org/) and [shiny](https://shiny.rstudio.com/). The first part about batch correction methods are actually surpassed by [NOREVA](http://idrb.zju.edu.cn/noreva/), which have more methods to be used. However, I am not intended to add more correction methods but focused on the simulation of batch effects and the evaluation of correction methods based on statistical properties about GC/LC-MS data.

By simulation with real data, I found most of the batch correction methods are fine in most cases. However, not so much improvement before and after correction. Acutally, batch correction would add false positive while keep more true positive. Such effects should be considered before applying any batch correction methods.

As for methods selection, I found in most cases, surrogated variable analysis or independant surrogated variable analysis outperform other correction methods. Also we could use quantitative analysis to show the influences from experimental design and batch effects.

Another topic about this presentaiton is about the visulization of peak list data. Such feature is powered by [DT](https://rstudio.github.io/DT/) package. You could always select, scale and download part of your peak list data through your eyes. This function is simple while useful for most of the metabolomics starters.

My slides could be found via [google doc](https://docs.google.com/presentation/d/11nEtnaYR5KGE2uufv5sgw0Qw70G7ZAYd7AnCdMUKZa4/edit?usp=sharing) and the source code of XcmsPlus could be found via [github](https://github.com/yufree/xcmsplus)

See you at 205C between 8:50 am and 9:10 am tomorrow!

## Tissue storage affects global metabolic: Profiling in comparision to in vivo microsampling approach

This poster presentation are works done by Anna and me. The original experiment is done by Vincent, Anna and me. We found the tissue storage would strongly change the pathway analysis results for in vivo study and hydrolysis process should be considered. Solid phase microextration could capture more lipophilic and short live compounds in in vivo studies. 

This is a fundamental research for non-targeted analyticla methods and the results might give us a hint about the complex during in vivo metabolomics studies.

See you at poster zone between 1:00pm and 3:00pm.

## Flyer about SPME courses

Our SPME courses are canceled just before this conference. So Prof. Pawliszyn asked all the group members to present the flyer about two days SPME course in Waterloo between April 26th and 27th. Here is the flyer and you could contact Nikita for more infomation.

![](https://yufree.cn/images/pittcon2018flyer.jpg)

## Hire me

My PostDoc contract would end at the end of July, 2018. I want to find a new PostDoc or research scientist position in U.S. because my girlfriend is here and travels between U.S. and Canada are really not so convenient for me. If you are interested in me or my research, you could find everything including referee and cv on this website and contact me [here](mailto:42@yufree.cn).