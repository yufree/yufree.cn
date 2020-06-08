---
title: SI for ASMS 2020 Reboot Reactomics Presentation
author: ''
date: '2020-06-07'
slug: si-for-asms-2020-reboot-presentation
categories: []
tags: []
---

I will be in the Q&A session for ASMS 2020 Reboot MOB pm: Exposomics, Toxicology, and Health Outcomes tomorrow. 20 minutes might not be enough to cover all the details of "Reactomics: using mass spectrometry as chemical reaction detector". Here I list some useful resources for this presentation and I will update the Q&A after the online session in this post.

### Resources

- [Vedio](https://youtu.be/-mT3HcVygHE). If you didn't register for ASMS 2020 Reboot, here is the link to unlisted vedio on YouTube.

- [Slides](http://yufree.github.io/presentation/reactomics/pres-asms.html). This is the slides for ASMS 2020 Reboot. Press "P" and you will see the notes for each slide with details. Another full version of reactomics presentaiton for one hour presentation could be found [here](http://yufree.github.io/presentation/reactomics/pres). I will not update the conference presentation while I will add new contents for the full version of reactomics presentation whenever I have new results.

- [Reactomics Preprint on BioRxiv](https://www.biorxiv.org/content/10.1101/855148v2). This preprint contain the same contents as shown in the presentation. I will update the manuscript later in this week for some changes.

- [pmd package](https://cran.rstudio.com/web/packages/pmd/index.html). This is the software for reactomics. It's on CRAN and you could check this [site](https://yufree.github.io/pmd/) for the most updated version with new functions, updated pmd annotation database and [tutorial](https://yufree.github.io/pmd/articles/globalstd.html).

- [pmd paper](https://pubmed.ncbi.nlm.nih.gov/30661584/). This is the first paper on pmd package to introduce structure/reaction directed analysis and I developed this idea into reactomics.

- [GlobalStd Shiny App](https://yufree.shinyapps.io/pmdapp/). This is online application to reduce peaks list into independant peaks by GlobalStd algorithm. This app try to remove redundancy peaks such as co-eluted peaks, multi-chargers, adducts, neutral loss, isotopologues, and fragments ions in the peak list by pmd frequency analysis. Then you will have a smaller while independant peaks list (usually less that 20% of original peaks numbers) csv file for reactomics analysis.

- [pmd network analysis Shiny App](https://yufree.shinyapps.io/pmdnet). This is online application to perform pmd network analysis. It tries to find all the possible metabolites of certaion input mass to charge ratio and pmd values. You could reproduce the pumpkin TBBPA study results as shown in the presentation. Both online app could be run locally when you install pmd package. `runPMD()` could start the GlobalStd Shiny App and `runPMDnet()` could start the pmd network analysis Shiny App.

- [PMDDA Workflow Poster](https://docs.google.com/presentation/d/18qDbjy1PYuLZgOOlbSgzkpFBQnc3k-H5XhQPHjszfHA/edit?usp=sharing). This is the PMDDA workflow poster for ASMS 2020 Reboot. PMDDA workflow tries to produce MS1 level independant peaks (GlobalStd algorithm) for MS2 pseudo targeted analysis and make annotation based on PMD of MS2 spectra.

- [xcmsrocker image](https://hub.docker.com/r/yufree/xcmsrocker/). This is the Rocker image for metabolomics data analysis. If you are familiar with docker image, this image include the same data analysis environment with all of the R based software used in my current lab for reproducible research. It also contaion PMDDA workflow data analysis templete as part of [rmwf package](https://github.com/yufree/rmwf).

- [meta-workflow online book](https://bookdown.org/yufree/Metabolomics/). This is a online book for maintained by me. You could find answers for most of the metabolomics data analysis related questions. It's open source to anyone who wish to contribute. Any PR is welcomed.

- [Metabolomics Data Analysis Workshop Slides](https://github.com/yufree/mdaw). I have organized this Workshop in University of Waterloo and University of California, Irvine. The slides will be updated according to the most updated research. It's a good start for the beginner of meatbolimcis data analysis.

### Q&A

TO BE UPDATED
