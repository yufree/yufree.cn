---
title: Quantum effect for chemical reaction
author: ''
date: '2019-03-10'
slug: quantum-effect-for-paired-mass-distances
categories: []
tags: 
  - metabolomics
---

Due to mass defect, the high resolution mass spectrum could be used for qualitative analysis. However, I am curious about the distribution of the decimal part of real compounds' exact mass. If compounds are generated randomly, the decimal part of exact mass should be uniform distributed between 0 and 1. However, we all know compounds should follow chemical property to form new compounds. In this case, let's see what happened for certain compounds database.

Again, we use HMDB to make a demo. This is the decimal part of real compounds' exact mass for 13251 unique exact mass in HMDB.

![](/en/2019-03-10-quantum-effect-for-paired-mass-distances_files/hmdbmzr.png)

As you could see, the distribution is not uniform distribution. However, it's kind of continuous between 0 and 1. Then I wonder what happened if I checked the paired mass distances(PMD) among those unique exact mass and check the distribution of the decimal part of PMD. After one cup of tea, my 2014 laptop give me this result:

![](/en/2019-03-10-quantum-effect-for-paired-mass-distances_files/hmdbpmd.png)

Well. Compared with compounds, pmd's distribution show a much clear pattern with incontinuity around 0.7. It seems that pmd could be used to check if certain reactions are real or unknown. Furthermore, pmd could stand for chemical reaction, such distribution imply a selection of reaction.

Well, let's zoom in the distribution between 0 and 0.1:

![](/en/2019-03-10-quantum-effect-for-paired-mass-distances_files/comp.png)

Hmmmm...it seems kind of quantum effect could be found in both compound and reaction level. Such quantum effect might be used for qualitative analysis or outlier detection. 

I hope you could still follow this interesting phenomenon. Anyway, if not, I will attend ASMS 2019 this summer. Unfortunately I didn't get the opportunity for oral presentation but poster presentation. 

My topic would be **Reacomics for LC-MS based untargeted analysis**. I will show more interesting results there. 

See you in Atlanta!