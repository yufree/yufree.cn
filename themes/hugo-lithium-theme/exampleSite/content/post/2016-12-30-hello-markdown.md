---
title: "A Plain Markdown Post"
date: "2016-12-30T21:49:57-07:00"
---

This is a post written in plain Markdown (`*.md`) instead of R Markdown (`*.Rmd`). The major differences are:

1. You cannot run any R code in a plain Markdown document, whereas in an R Markdown document, you can embed R code chunks (```` ```{r} ````);
2. A plain Markdown post is rendered through [Blackfriday](https://gohugo.io/overview/configuration/), and an R Markdown document is compiled by [**rmarkdown**](http://rmarkdown.rstudio.com) and [Pandoc](http://pandoc.org).

There are many differences in syntax between Blackfriday's Markdown and Pandoc's Markdown. For example, you can write a task list with Blackfriday but not with Pandoc:

- [x] Write an R package.
- [ ] Write a book.
- [ ] ...
- [ ] Profit!

Similarly, Blackfriday does not support LaTeX math and Pandoc does. I have added the MathJax support to this theme ([hugo-lithium-theme](https://github.com/yihui/hugo-lithium-theme)) but there is a caveat for plain Markdown posts: you have to include inline math expressions in  a pair of escaped parentheses `\( \)` instead of dollar signs `$ $`, e.g. `\(S_n = \sum_{i=1}^n X_i\)`. For R Markdown posts, you can use `$ $` to write inline math expressions.

When creating a new post, you have to decide whether the post format is Markdown or R Markdown, and this can be done via the `rmd` argument of the function `blogdown::new_post()`, e.g.

```r
blogdown::new_post("Post Title", rmd = FALSE)
```
