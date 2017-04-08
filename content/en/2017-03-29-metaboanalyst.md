---
title: Tips for local installation of MetaboAnalyst on Windows
date: 2017-03-29
slug: metaboanalyst
---

I am running Windows 7 to perform metabolomics data analysis(mainly for mscovert). Recently I found MetaboAnalyst could be installed locally. Since some group members really care about their data safety, I just installed MetaboAnalyst on one of group computers. Here is some tips for it:

- Windows 7 is currently not supported by Metaboanalyst, so I use virtualbox to install a 64-bit Ubuntu 16.10.

- For Ubuntu, you need to install a few packages to support both the R and Java environment, also some packages. You might follow the script in bash:

```
sudo apt-get install libnetcdf-dev graphviz libxml2-dev libcairo2-dev default-jdk r-base-dev 
```

- You also need to install some packages from either CRAN or Bioconductor

    - Install Rserver in bash to get rid of configure of R

```
sudo apt-get isntall r-cran-rserve
R
```

``` r
# Use the following code to install packages in R:
install.packages(c("ellipse", "scatterplot3d","pls", "caret", "lattice", "Cairo", "randomForest", "e1071","gplots", "som", "xtable", "RColorBrewer", "pheatmap", "igraph", "RJSONIO", "caTools", "ROCR", "pROC"))
source("https://bioconductor.org/biocLite.R")
biocLite()
biocLite(c("xcms", "impute", "pcaMethods", "siggenes", "globaltest", "GlobalAncova", "Rgraphviz", "KEGGgraph", "preprocessCore", "genefilter", "SSPA", "sva"))
```

- If you want to install Rstudio on 64-bit Ubuntu, you need the following steps:
    - Download "libgstreamer plugin" from [here](https://packages.debian.org/jessie/amd64/libgstreamer-plugins-base0.10-0/download) 
    - Download "libgstreamer" from [here](https://packages.debian.org/jessie/amd64/libgstreamer0.10-0/download) 
    - Install two packages above
    - Install the following packages
    
```
sudo apt-get install libjpeg62
```

- MetaboAnalyst is actually a java-based web application (also, R based). You need java environment and use Tomcat or Glassfish to host the *.war file on server (Linux or Mac OS). Then you only need to access it by browser, just like what you did online.

- Install Glassfish. I tried Tomcat and the deploy always failed and I suggest to use Glassfish following the guide(you might need to set up user and password) and upload the *.war file by a web interface at http://localhost:4848

```
wget download.java.net/glassfish/4.1.1/release/glassfish-4.1.1.zip
apt-get install unzip
unzip glassfish-4.0.zip -d /opt
cd /opt/glassfish/bin
./asadmin start-domain
./asadmin enable-secure-admin
./asadmin restart-domain
```

![](https://yufree.github.io/blogcn/figure/war.PNG)

- Run the Rserve in bash:

```
R CMD Rserve
```

- After the installation of MetaboAnalyst on Glassfish, make a port transfer to ensure you could access the MetaboAnalyst on browsers of windows. You need to know the local IP address of both your host and virtual machine(VM).

    - Your host address is the IP for the connection between host and VM. Use `ipconfig /all` to get it
    
    ![](https://yufree.github.io/blogcn/figure/hostip.PNG)
    
    - Your VM address could be found by `connection information`
    
    ![](https://yufree.github.io/blogcn/figure/vmip.PNG)
    
    - Set up the NAT port transfer to ensure you could access MetaboAnalyst on VM from host browser
    
    ![](https://yufree.github.io/blogcn/figure/porttrans.PNG)
    
    - Save a bookmark for the url(in my case: http://192.168.56.1:8080/MetaboAnalyst/ ) Open the virtualbox all the time at the background
    
    ![](https://yufree.github.io/blogcn/figure/ip.PNG)
    
    - Enjoy local access (while not updated) to MetaboAnalyst

- Every time you restart your computer, input this in bash to start the MetaboAnalyst:

```
R CMD Rserve
cd /opt/glassfish/bin
./asadmin start-domain
```

- For the other thing, just follow the official guide [here](http://www.metaboanalyst.ca/faces/home.xhtml)