---
title: Evaluation and reduction of the analytical uncertainties in GC-MS analysis using a boundary regression model
date: 2016-11-29
slug: my third paper
---

This [paper](http://www.sciencedirect.com/science/article/pii/S0039914016309298) received opposite comments from reviewers. One rejected and the other recommanded. Anyway, this is just the beginning of this kind of data analysis for mass spectrum. Also this work was the basis of one chapter in my thesis.

In this work, I wanted to access and reduce the uncertainties in the whole procedure of environmental analysis. In regular analysis, we would use pure standards to optimized the analysis method and recovery and RSD were commonly used for quality control analysis. My concerns are:

- Uncertainties were hard to be found with standards in advance. When you injected a dirty samples, you instruments would be polluted after you see the results. Furthormore, when you found your targeted compounds were influenced by something from the matrices, you have to start the analysis from the beginning with new methods. So, I wounder if we could access some common properties during the analysis before we analysis the samples. Then I used visualization methods to show the Uncertainties in the raw data from GC-MS.

- Another issue is that how to escape the influnces from the uncertainties found in the visualization methods. My solution was that building a boundary regression models to seperate the "clean" zone from the "dirty" zone in the raw data. By this model, we would get a better sensitivity by choosing right ions regardless of the matrices or pretreatment.

I am always wondering whether different pretreatments would show similar results for certain matrix and compounds. From this paper, my answer is almost yes. Certain pretreatments would remove something we do not like or harmful to the instruments. However, such influnces might be pointless and can't be detected on mass spectrum. In GC-MS, the co-elute influnces are hard to affect the your target compounds at the same retention time and the same massed. Only the rising baseline is important and we could get rid of it by the boundary model. Then the only thing we need to consider is the pollution of the instruments.

Meanwhile, I need to say such model might not be suitable for high-resolution mass spectrum. However, this idea could be used to improve the analytical methods for some compounds, especially for PBDEs. Also this paper supplied some basic data for environmental analysis. As a rule of thumb, you might know:

> When you rise 1 degrees centigrade, the 'dirty' zone's boundary would rise about 2 unit mass in the worst matrix and pretreatment. Always try to choose heavier ions for qualitative and quantitative analysis.

Here is the graphical summary for the whole methods and I think more patterns could be mined from the data of GC-MS:

![](http://yufree.cn/blogcn/figure/MorF.jpg)

Also I developed a package to perform this kind of analysis in R. Check [here](https://github.com/yufree/enviGCMS). This package has been published on [CRAN](https://cran.r-project.org/web/packages/enviGCMS/index.html) and you could install and load it by:

~~~
install.packages('enviGCMS')
library('enviGCMS')
~~~

You might find **Easter Eggs** in this package.

If you have questions about this paper, comment here and I will reply as soon as possible. 