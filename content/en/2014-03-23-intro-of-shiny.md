---
title: A very brief intro of shiny
date: 2014-03-23
slug: intro of shiny
---

> If you are a starter of shiny as me, this post may help your know some principle of shiny.  

# What is shiny?

- R based
- View as webpage hosted on servers
- **give a request, show the result**

# Backgroud needed

- Almost R only

# Why shiny?

- Entirely extensible
- Display your data in an interactive way

# How shiny works?

- Reactive Programming

    When the input changes, the R code will run again to get a refresh. Shiny makes the connections among R, input and the the output on your screen by some communication tags. So you can just focused on R code and let shiny do the other things.
    
- server.R

    You need write your R code here to tell shiny run what when the inputs change. The R code need a input and output values.

- ui.R
  
    You need tell the app user where is the input/output box, which values of the input should be transfer to R code and which values of the output should be display on the webpage. You can also custome your UI of app here if you have writen some basic html pages.
    
- Render function in server.R

    Tell shiny the output values used in the app's webpage. This function need to be re-ran when the input changes, so the render function must be assighed to a output values while contains the input values.

- RUN

    When you finish your server.R and ui.R, just `runApp()` and you will get the great webpage.
    
# How to share your apps?

- Push your shiny code on the github or make a zip file, the user can run it locally use the `runUrl`,`runGitHub` or `runGist` in the shiny package.

- You can also build up a server with www connection and put your app there.

# Learn more?

- [Lessons](http://www.rstudio.com/shiny/lessons/Intro/)
- [Tutorial](http://rstudio.github.io/shiny/tutorial/)