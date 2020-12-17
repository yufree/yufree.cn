---
title: Retention time alignment for peaks list
author: ''
date: '2020-12-16'
slug: retention-time-alignment-for-peaks-list
categories: []
tags: []
---

A regular open source metabolomics workflow could start from the open source format of RAW data. For xcms or other software, algorithm like obiwarp could be used to align the peaks into features. However, some workflows will start from the exported csv files from the instruments. The major issue is that peaks list is not features table and multiple samples should be aligned. Here I will show a native method to align peaks across samples in R considering the mass accuracy and pre-defined retention time shift.

Firstly, the input object should be a list with elements as peaks list from single samples. It should be a data.frame with retention time, mass to charge ratio and intensities.

Then we need to assign a sample as the template for alignment. The output of the alignment function should use m/z and rt data from this sample as the features property.

Now we could align the peaks across samples.  All the samples' peaks list should be aligned with the peaks list of template sample one by one. Here the alignment should consider the ppm of m/z and delta retention time. Each alignment will decrease the numbers of featuers when no peaks could be aligned to certain peaks in the template samples. This is a recursive process considering the aligned features' intensities would be saved and reduced for the next paired alignment. 

When one peak from template sample could be aligned to multiple peaks in other peaks list, you need to define a function to deal with the intensity of feature in other samples. For example, you could use mean/median/sum to generate the features' intensities for the other samples. Since our inputs are peaks lists, no peaks properties such as peak width, peak shape could be checked. It's better to control this when you output the peaks list for single samples.

If you are familiar with minifrac in xcms, you might find such alignment will actually set the minifrac as 1. In this case, you should perform this alignment on samples from the same group and you should not use this alignment for samples without group information.

The final output should show the feature' m/z, retention time and intensity across samples. However, this is alignment instead of correction. Such alignment will not correct the shift of retention time larger than certain cutoff, for example, 5s. The advantage of this alignment is that the concept is clear and easy to explain. The aligned peaks should be of high quality. This method could also be used to find the common ions across samples for quality control puporse.

Here is the code (I will put this function in enviGCMS package later):

```R
# check input to make sure the each peaks list contain 'mz', 'rt' and 'ins' as m/z, retetion time in seconds and intensity of certain peaks.
data1 <- read.csv('sample1.csv')
data2 <- read.csv('sample2.csv')
data3 <- read.csv('sample3.csv')
# generate the list as input
li <- list(data1,data2,data3)
# define the function to align peaks list
getretcor <- function(list,cs=1,ppm=10,deltart=5, FUN){
  nli <- list[-cs]
  csd <- list[[cs]]
  i=1
  df1 <- csd
  ins <- df1$ins
  while(i<=length(nli)){
    df2 <- list[[i]]
    df <- enviGCMS::getalign(df1$mz,df2$mz,df1$rt,df2$rt,ppm=ppm,deltart=deltart)
  mr2 <- paste0(df2$mz,'@',df2$rt)
  mrx <- paste0(df$mz2,'@',df$rt2)
  
  df$ins2 <- df2$ins[match(mrx,mr2)]
  dfx <- df[!duplicated(df$xid),]
  dfx$ins2 <- aggregate(df$ins2,by=list(df$xid),FUN)[,2]
  df1 <- cbind.data.frame(mz=dfx$mz1,rt=dfx$rt1)
  if(length(dim(ins))>1){
    insn <- ins[df$xid,]
    ins <- cbind.data.frame(insn[!duplicated(df$xid),],dfx$ins2)
  }else{
    insn <- ins[df$xid]
    ins <- cbind.data.frame(ins1=insn[!duplicated(df$xid)],dfx$ins2)
  }
  i=i+1
  }
  re <- cbind.data.frame(df1,ins)
  colnames(re) <- c('mz','rt',paste0('ins',1:length(list)))
  return(re)
}
# usage
re <- getretcor(list,FUN=mean)
```


