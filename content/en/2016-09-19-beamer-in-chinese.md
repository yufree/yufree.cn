---
title: Use Chinese in RStudio Beamer Slides
date: 2016-09-19
slug: beamer in chinese
---

**RStudio** is an excellent IDE for R. However, using Chinese in default setting of Rmd to output a PDF document is always annoying. Well, the source is **tex**.

**RStudio** uses **knitr** to covert the Rmd document into md document. Then it uses **Pandoc** to convert the md document into tex document. Then they actually use **tex** engine such as pdflatex or xelatex to get PDF document. 

Why Chinese would not display? This issue happens at the last step. By default, some templates such as beamer in **RStudio** use pdflatex. However, you might need CJK package. However you would need to use CJK environment to display Chinese. I don't think it is a good way and you need to write ugly documents.

xeCJK package would be preferred because you only need to set up the font for your Chinese and you will get the output. However, such configuration need you use xelatex to compile you documents.

For the beamer template in **RStudio**, they use pdflatex. So the first way to show Chinese is telling **Pandoc** to use xelatex other than pdflatex. You could set up such command in the yaml.

The second issue is the font. When you use xelatex(actually xeCJK package), you need to set the font for CJK charactors such as Chinese. Maybe you could try the following yaml to use a font without sources.

~~~
---
title: "中文测试"
author: "Yufree"
date: "2016年9月19日"
CJKmainfont: FandolFang
output:
  beamer_presentation:
    latex_engine: xelatex
---
~~~

Not everyone knows how to find the right name of a font. However, the updated ctex package solved such problem. They use some default setting to avoid the font issue. All you need to do is use the ctex package for your tex template.

We might also use yaml:

~~~
---
title: "中文测试"
author: "Yufree"
date: "2016年9月19日"
header-includes:
  - \usepackage{ctex}
output: 
  beamer_presentation:
    latex_engine: xelatex
---
~~~

OK, now you would see Chinese in your Beamer PDF slides.

## Summary

Three solutions:

- Use CJK packages along with pdflatex (Not recommanded, only for Guru from 20 century)

or

- Set you font yourself in the yaml with xelatex (for Geek)

or

- Use the ctex package in your yaml (for everyone)

For Chinese in the figure and pdf, check [here](http://yufree.cn/blog/2014/07/21/rmd-to-pdf.html).