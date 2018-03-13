---
title: Downverse workflow for research
author: ''
date: '2018-03-13'
slug: workflow-for-r-based-research-environment
categories: []
tags:
  - R
---

Firstly, I really appreciate Yihui's [post](https://yihui.name/en/2018/03/miao-yu-postdoc/) about me. 

Today I want to share some tips with people in academia about how to reduce repeated works in research. You might treat this as an extension for [Jeek Leek](http://jtleek.com/)'s excellent book: [How to be a mordern scientist](https://leanpub.com/modernscientist).

## What?

Which kind of works could be treated as repeated works in research? A lot! However, unless you experiments are all *in silico*, I just want to focused on the parts after you finished your experiment. Repeated works in data analysis, writing and presentation should be considered. 

## Why?

Doing the same thing multiple times would waste your time. Also such behavior would introduce variances to reproduce your results. If we could not find a robot, a better choice is using codes. An important principle in research is that what you could do should be totally reproducible by other people, and yourself. When you do something related to research, make sure other people could always repeat your operation from the recipe you left. You should always treat yourself as 'other people' and such codes or text files would help you reduce the future energy.

## How?

- Use Graphical User Interface(GUI)?

Nooooooooo! No one would remember whether certain buttons have been clicked or not. However, you could also use macro to track your operations if possible. Make sure such macro could be shared without certain requirements about expensive software. If you have to use GUI, try to avoid the interactive operations which could affect your results.

- Version control?

Yes! Always use version control for your files and add comments about changes. Use words which could be understood by human beings. Otherwise prepare a code book for yourself. Trust me, you need such code book rather than any other people. [Git](https://git-scm.com/) and [github](https://github.com/) would be a good start.

- RSS?

Yes! Try to create your own rss list and keep track of new papers in passive way. Always start with abstract and end with a note links to original paper. Organize the notes as a book related to your research topic. When a new paper appeared as a note in your knowledge system or books, you could finally use such paper. Avoid guiding by the authors and keep your own system updated as I did for metabolomics [here](https://bookdown.org/yufree/Metabolomics/).

- Plot/Process similar data with the same setting? 

Try to organize scripts in one function and use [rmarkdown](https://rmarkdown.rstudio.com/) to make reproducible reports about it. Next time you only need to call that functions as I did [here](https://github.com/yufree/democode).

- Make it clear? 

Use [tidyverse](https://www.tidyverse.org/) style or verse with [tinytex](https://yihui.name/tinytex/) support. Try to keep style stable and other people with similar style would figure out what you said from your codes in one second.

- Market your ideas? 

Write journal papers with [rticles](https://github.com/rstudio/rticles) and show them at conferences with [xaringan](https://github.com/yihui/xaringan) and/or [shiny](https://shiny.rstudio.com/). All you need to learn is [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) and you could graduate in five minutes at most. 

Try to share source files about your ideas as a github repo and this would help you spread your ideas as [meme](https://en.wikipedia.org/wiki/Meme). Also you should consider pre-print sever such as [arxiv](https://arxiv.org/), [bioRxiv](https://www.biorxiv.org/) and [chemrxiv](https://chemrxiv.org/) to share your ideas in Physics, Life science and Chemistry, respectively.

- SNS your ideas? 

Write blog posts with [blogdown](https://bookdown.org/yihui/blogdown/) in plain text and share them on twitter/linkedin/researchgate. Actually, one of the purposes of my [website](https://yufree.cn) is share my ideas.

- Similar topic of a bunch of functions? 

Pack the functions into a package and make detailed documents and publish with [pkgdown](https://github.com/r-lib/pkgdown) as I did in [enviGCMS](https://cran.rstudio.com/web/packages/enviGCMS/index.html) package.

- Similar topic of your ideas? 

Write a book online with [bookdown](https://bookdown.org/yihui/bookdown/) as I did for metabolomics [here](https://bookdown.org/yufree/Metabolomics/)

- Reproduce the whole environment for data analysis? 

Use [docker](https://www.docker.com/) or [rocker](https://hub.docker.com/u/rocker/) image to pack all but least dependence or software in a Linux image and share them on [dockerhub](https://hub.docker.com). You could also distribute your raw data and scripts with your docker image and show the links on your publications. In this case, anyone could validate your results with the same setting. I also did [one](https://hub.docker.com/r/yufree/xcmsrocker/) for metabolomics study.

- Share the data?

Try [figshare](https://figshare.com/) or [Open Science Framework](https://osf.io) to share your data or projects. I still suggested to use docker image to avoid potential issues.

- Literature management? 

[Zotero](https://www.zotero.org/) or [fulltext](https://github.com/ropensci/fulltext). However, as I shown [here](https://yufree.cn/en/2018/01/12/get-rid-of-bibliography/), all you need for literature management is [DOI](https://www.doi.org/). Just build your own knowledge system and organize literature according to your topic. You would benefit from such system by reducing a lot of time to align literature into the sections of your papers since you have already done this at the very beginning.

- I can't remember those tips

Well, I prepare a `downverse` rocker [image](https://hub.docker.com/r/yufree/downverse/) with those software installed and you could try. Other websites where you could always find excellent tools for research is [rOpenSci](https://ropensci.org/) and [Rstudio](https://www.rstudio.com/).

Thanks again, Yihui! Actually you developed most of the packages. 