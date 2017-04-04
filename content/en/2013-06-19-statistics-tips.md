---
title: The Log Transformation of Concentration Data
date: 2013-06-19
slug: statistics tips
---

Recently, I read Part I of Song S. Qian's book - *Environmental and Ecological Statistics with R* and find some interesting tips about statistics in environmental science. Here I will discuss the log transformation of concentration.

In this book, the author said that the statistical distribution of concentration data of certain compounds need a log transformation to show a bell curve. I don't know if this conclusion comes from certain theory or just depends on the observation. But usually, when we sample from a certain place for the concentration of POPs, most of the sample will show n.d. and most of time we will use half of the MDL as the concentration in case the N.A. make some troubles. So at a lower concentration, namely the MDL, you will get a lot of samples with the same values. We all know that this situation means an overlay of log-normal distribution and a uniform distribution. So when we have such samples, we need to use our knowledge to find out the right way to summary the data. Also the author said the independence is much more important than the distribution. We need to take care of any factor when we perform sampling.
