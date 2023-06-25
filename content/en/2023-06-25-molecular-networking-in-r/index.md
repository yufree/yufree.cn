---
title: Molecular networking in R
author: Miao Yu
date: '2023-06-25'
slug: molecular-networking-in-r
categories: []
tags:
  - metabolomics
---

I found lots of research using molecular networking in this year's ASMS annual meeting. However, I didn't find R code or package for molecular networking. It seems most people using molecular networking are using GNPS and don't talk too much about the algorithm behind molecular networking. In this post, I will make a brief introduction about molecular networking and show some dirty code to perform molecular networking in R.

## What is molecular networking?

Molecular networking is more about molecular network linked by MS2 similarity. In the network, nodes represent compounds with different MS2 spectra and edges represent the similarity of their MS2 spectra. When two compounds are connected by edge, they should have structure similarity and potential biological functional similarity.

From this definition, we know the precursors of connected compounds should be different. This is the major difference between molecular networking and MS2 spectra matching. In MS2 spectra matching, the purpose is identification of unknown MS2 spectra. In molecular networking, the purpose is classification of similar compounds. If one node in the molecular networking is known compound, we could infer the other nodes connected with this compound should also be compounds similar to this known compound such as metabolites or congeners. Though most of the users of GNPS using molecular networking as annotation tools, the most unique feature of molecular networking is to interpret the network for biological purpose. In the [original publication](https://www.pnas.org/doi/10.1073/pnas.1203689109) of molecualr networking, such tool is designed to find new nature products, which is not for identification purpose only. This post is also not focused on identification and care more about the relation network among molecular.

## How to define MS2 similairy?

If you are familiar with MS2 spectra matching, you might realize the precursors of matching two spectra should be the same or has isotopologue shift. However, molecular networking will consider the spectra similarity with different precursors, which is called modified cosine similarity in their original paper.

Before we discuss the modified cosine similarity, let's review cosine similarity. Cosine similarity is very straightforward. If we have two vectors like [1,10,1] and [10,100,10], the cosine similarity is to calculate the normalized dot product, which can also be interpreted as the cosine of the angle between two vector. For vector [1,10,1] and [10,100,10], the value should be:

`$$
cos(\theta) = \frac{(1*10 + 10*100 + 1*10}/{\sqrt(1*1+10*10+1*1) * \sqrt(10*10+100*100+10*10)} = 1
$$`

In this case, the cosine value is 1 and angle should be 0. Those two vectors are similar in terms of cosine similarity.

For MS2 spectra matching, such two vectors should be the intensities with same m/z. In this case, you need to define the tolerance of m/z shifts to align two MS2 spectra before the calculation of cosine similarity.

OK, I hope you understand the regular way to compare two MS2 spectra now. Now we need to modify this algorithm for molecular networking: 

- Step 1: calculate paired mass distance between precursors

- Step 2: Apply this mass distance to all the query MS2 spectra to generate a shift version of MS2 spectra with the same intensities profile

- Step 3: Align the m/z between query MS2 spectra (both the original and shifted version of target MS2 spectra) and target MS2 spectra

- Step 4: Calculate the cosine similarity between the aligned intensity as modified cosine similarity

I know you still confuse about the algorithm. I will give an example. Compound A has m/z 300 as precursor and m/z [100,200,250] as fragment ions with intensity [100,200,300]. Compound B had m/z 215.995 as precursor and m/z [100, 200, 265.995] as fragment ions with intensity [10,20,30]. 

- Step 1: the paired mass distance of precursors is 15.995
- Step 2: we generate a shift version of spectra A with m/z [115.995, 215.995, 265.995] with intensity [100,200,300]
- Step 3: Align both the original and shifted spectra A with spectra B. We got aligned m/z[100,200,265.995] with intensity[100,200,300] for A and [10,20,30] for B
- Step 4: the cosine similarity of between A and B is 1, which means A and B are structure similar to each other

In the above example, compound B is the oxidized metabolite of compound A. One fragment ions show the mass shift of oxidation while the smaller ions will not contain the fragment with oxidized parts. Such scenario is highly true for real world compounds. Now we can infer compound B should be a metabolite of compound by modified cosine similarity.

## Different between molecular networking and PMD network

I also [published](https://www.nature.com/articles/s42004-020-00403-z) tools to construct paired mass distance(PMD) network by MS1 only data. You might ask the differences between molecular networking and PMD network. Here is the similarity and difference:

In both PMD network and molecular networking, node are different compounds and the connection could be displayed as paired mass distance or mass shift. Both of them could be used to interpret relation among the compounds found in certain samples.

In PMD network, the paired mass distance is defined by paired mass distance of two MS1 ions. To perform PMD network analysis, you need to remove the redundant peaks from the same compounds by GlobalStd algorithm. Only the predefined PMDs will be used for connection. Such PMDs list could be generated based on domain knowledge or purely based on the frequency of PMDs among ions. When some PMDs always be found, such reaction should be considered as important relations.

In molecular networking, the paired mass distance is calculated between two precursors of two MS2 spectra. Modified cosine similarity is used to define the connection, which can also be interpreted by mass shifts. Here, you don't need to tell the mass shifts of precursors and the algorithm will do this job. The only issue is that you need high quality MS2 data. In my experience, MS2 data collected for certain projects are always 'identify' the similar compounds profile and DDA mode usually only cover 10-20% of the MS1 ions found in corresponding MS1 full scan data. 

In my opinion, if you preferred a high coverage of compounds in the samples, try PMD network on MS1 data first and then collected pseudotargeted MS2 data based on you PMD network results with modified cosine similarity matching. On the other hand, if you preferred a high confidence of identification at the very beginning, try molecular networking directly.

## R code for molecuar networking

Here are two functions for molecular networking and I read the [python code](https://matchms.readthedocs.io/en/latest/api/matchms.similarity.ModifiedCosine.html) of matchms package to write those R functions. 

`find_matches` is used to align the m/z of two MS2 spectra and `mnmatch` is used to perform molecular networking for certain MS2 spectra files. This function will only calculate the modified cosine similarity for all the MS2 spectra in one file and return a list object with two elements: one is the data table for network and another is also list object with matched spectra for detailed check.

```r
find_matches <- function(spec1_mz, spec2_mz, tolerance, shift = 0) {
        matches <- data.frame()
        for (peak1_idx in seq_along(spec1_mz)) {
                mz <- spec1_mz[peak1_idx]
                low_bound <- mz - tolerance
                high_bound <- mz + tolerance
                for (peak2_idx in c(1:length(spec2_mz))) {
                        mz2 <- spec2_mz[peak2_idx] + shift
                        if (mz2 < high_bound & mz2 > low_bound) {
                                matches <- rbind.data.frame(matches,
                                                            c(peak1_idx, peak2_idx))
                        }
                }
        }
        if (nrow(matches) > 0) {
                colnames(matches) <- c('query', 'query2')
                return(matches)
        } else{
                return(NULL)
        }
}
mnmatch <- function(spectra,
                    binstep,
                    cf,
                    npeaks) {
        matches <- list()
        intersected_indices <- c()
        for (i in 1:(length(spectra) - 1)) {
                for (j in (i + 1):length(spectra)) {
                        ins <- intensity(spectra)[[i]]
                        ins <- ins / sum(ins)
                        pmz <- precursorMz(spectra[i])
                        pmz2 <- precursorMz(spectra[j])
                        diff <- pmz - pmz2
                        rt <- rtime(spectra[i])
                        rt2 <- rtime(spectra[j])
                        diffrt <- rt - rt2
                        insx1 <- insx2 <- insnx1 <- insnx2 <- c()
                        if (abs(diffrt) > 10) {
                                if (abs(diff) < binstep) {
                                        query <- mz(spectra)[[i]]
                                        query2 <- mz(spectra)[[j]]
                                        re <- find_matches(query,
                                                           query2,
                                                           binstep,
                                                           shift = 0)
                                        if (!is.null(re)) {
                                                insn <- intensity(spectra)[[j]]
                                                insn <- insn / sum(insn)
                                                insnx1 <- insn[re$query2]
                                                insx1 <- ins[re$query]
                                        }
                                        if (length(insnx1) > npeaks) {
                                                cos <-
                                                        crossprod(insx1,
                                                                  insnx1) / sqrt(
                                                                          crossprod(insx1) * crossprod(insnx1)
                                                                  )
                                                if (c(cos) > cf) {
                                                        intersected_indices <-
                                                                rbind(
                                                                        intersected_indices,
                                                                        c(
                                                                                i,
                                                                                j,
                                                                                as.numeric(
                                                                                        cos
                                                                                ),
                                                                                diff
                                                                        )
                                                                )
                                                        ms1 <- query[re$query]
                                                        ms2 <- query2[re$query2]
                                                        query <- cbind.data.frame(
                                                                mz = ms1,
                                                                ins = insx1
                                                        )
                                                        query2 <- cbind.data.frame(
                                                                mz = ms2,
                                                                ins = insnx1
                                                        )
                                                        queryraw <-
                                                                cbind.data.frame(
                                                                        mz = mz(
                                                                                spectra
                                                                        )[[i]],
                                                                        ins = ins
                                                                )
                                                        query2raw <-
                                                                cbind.data.frame(
                                                                        mz = mz(
                                                                                spectra
                                                                        )[[j]],
                                                                        ins = insn
                                                                )
                                                        diff <- diff
                                                        matcht <- list(
                                                                query,
                                                                query2,
                                                                queryraw,
                                                                query2raw,
                                                                diff
                                                        )
                                                        matches <- append(matches,
                                                                          list(
                                                                                  matcht
                                                                          ))
                                                }
                                        }
                                } else{
                                        query <- mz(spectra)[[i]]
                                        query2 <- mz(spectra)[[j]]
                                        re <- find_matches(query,
                                                           query2,
                                                           binstep,
                                                           shift = 0)
                                        if (!is.null(re)) {
                                                insn <- intensity(spectra)[[j]]
                                                insn <- insn / sum(insn)
                                                insnx1 <- insn[re$query2]
                                                insx1 <- ins[re$query]
                                        }
                                        re2 <- find_matches(query,
                                                            query2,
                                                            binstep,
                                                            shift = diff)
                                        if (!is.null(re2)) {
                                                insn <- intensity(spectra)[[j]]
                                                insn <- insn / sum(insn)
                                                insnx2 <- insn[re2$query2]
                                                insx2 <- ins[re2$query]
                                        }
                                        insx <- c(insx1, insx2)
                                        insnx <- c(insnx1, insnx2)
                                        if (length(insx) > npeaks) {
                                                cos <-
                                                        crossprod(insx, insnx) / sqrt(
                                                                crossprod(insx) * crossprod(insnx)
                                                        )
                                                if (c(cos) > cf) {
                                                        intersected_indices <-
                                                                rbind(
                                                                        intersected_indices,
                                                                        c(
                                                                                i,
                                                                                j,
                                                                                as.numeric(
                                                                                        cos
                                                                                ),
                                                                                diff
                                                                        )
                                                                )
                                                        ms1 <- c(query[re$query],
                                                                 query[re2$query])
                                                        ms2 <- c(query2[re$query2],
                                                                 query2[re2$query2])
                                                        query <-
                                                                cbind.data.frame(
                                                                        mz = ms1[order(ms1)],
                                                                        ins = insx[order(ms1)]
                                                                )
                                                        query2 <-
                                                                cbind.data.frame(
                                                                        mz = ms2[order(ms2)],
                                                                        ins = insnx[order(ms2)]
                                                                )
                                                        queryraw <-
                                                                cbind.data.frame(
                                                                        mz = mz(
                                                                                spectra
                                                                        )[[i]],
                                                                        ins = ins
                                                                )
                                                        query2raw <-
                                                                cbind.data.frame(
                                                                        mz = mz(
                                                                                spectra
                                                                        )[[j]],
                                                                        ins = insn
                                                                )
                                                        diff <- diff
                                                        matcht <- list(
                                                                query,
                                                                query2,
                                                                queryraw,
                                                                query2raw,
                                                                diff
                                                        )
                                                        matches <- append(matches,
                                                                          list(
                                                                                  matcht
                                                                          ))
                                                }
                                        }
                                }
                        }
                }
        }
        if (nrow(intersected_indices) > 0) {
                colnames(intersected_indices) <- c('query', 'query2', 'cos', 'diff')
                intersected_indices <- as.data.frame(intersected_indices)
        } else {
                intersected_indices <- NULL
        }
        return(list(intersected_indices, matches))
}
```

The usage is simple. You need to prepare mgf file for MS2 spectra. Here we also use binstep for 0.001Da to align two m/z, minimal 5 peaks for matching, and cutoff of 0.6 for cosine similarity:

```r
library(Spectra)
specs <- Spectra('YOUFILE.msp', source = MsBackendMsp::MsBackendMsp())
result <- mnmatch(specs,binstep=0.001,cf=0.6,npeaks=5)
table <- result[[1]]
library(igragh)
net <- igraph::from_data_frame(table,directed = F)
# display molecular networking
plot(net)
```
