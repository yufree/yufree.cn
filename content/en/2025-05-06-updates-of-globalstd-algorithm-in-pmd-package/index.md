---
title: Updates of GlobalStd algorithm in pmd package
author: Miao Yu
date: '2025-05-06'
slug: updates-of-globalstd-algorithm-in-pmd-package
categories: []
tags:
  - metabolomics
---

Recently, I updated the GlobalStd algorithm in the pmd package. The new version includes several improvements and bug fixes. Here are the details:

- `getpaired` function was re-written to improve the detection of redundant peaks. The paired mass distances (PMDs) are calculated for each retention time clusters. Then redundant peaks will be found in each cluster. For isotopougue pairs, the new version can detect them using network clusters of isotopologues and the lowest mass peak is retained for the following analysis. I also added a feature to detect multiple charged isotopologues clusters and those ions will be removed from the following analysis. Then I updated the multiple charged ions detection to remove all the paired ions for further analysis. The left paired ions will be used to calculate the frequency of PMDs within the cluster and each PMD will only be count once for each cluster. After the detection of high frequency PMDs within retention time clusters or potential "common in source reactions", this function will return the PMDs for those redundant peaks, as well as the label for isotopougue, multiple charged ions and multiple charged isotopologues. Here, the ions retained in the high frequency PMDs will not be treated as multiple charged ions. 

Compared with previous version, new function added the feature to detect multiple charged isotopougue and improved the detection of redundant peaks. The code is easy to read with isolation of inner functions. The output of this version will be similar while more accurate compared with the previous version. I removed the `pmd2` column in the output data frame and user can always calculate those values from `pmd` and corresponding plot function has added `digits` parameters to control the visualization.

- `getstd` function was also re-written to retain independent peaks. The new function didn't change the original workflow while make it easy to maintain and read. The `corcutoff` parameter was moved to `getpaired` function as correlation cutoff was used to filter paired ions instead of standard ions. 

- `globalstd` function is a wrapper function for `getpaired` and `getstd` functions and has been updated accordingly.

- I changed the name of `getcluster` function to `getpseudospectrum` function and also be rewritten to focused on the recover of pseudo spectrum from MS1 feature table. This function will no longer use `getstd` function and will directly use `getpaired` function to generate the pseudo spectrum. If the independent peaks were used, extra merge process will be involved as previous version and the pseudo spectrum numbers will always be less than the independent peaks number. It will still output a vector `stdmassindex2` to find base peaks for each pseudo spectrum. It will also tell you the coverage of explainable ions coverage (~70%) in the data. We treated the ions within cluster while without passing PMD relation correlation cutoff as one pseudo spectrum, which might introduce a false positive for data using correlation cutoff while keep the opportunity to check them later.

- `getcorcluster` function has been changed to `getcorspeudospectrum` function. The new version will use the same logic as previous version to detect psudo spectrum based on correlation of ion's intensity and will also output the independent peaks with the largest m/z peaks and the base peaks with the largest intensity in their corresponding pseudo spectrum. User can use both `getpseudospectrum` and `getcorpseudospectrum` functions to generate pseudo spectrum and the latter functions will have less numbers of pseudo spectrum. I would recommend to use `getpseudospectrum` function to generate pseudo spectrum with a better explanation of the ions. The return object will contain a `pseudo` table instead of `clusters` table for further investigation. 

- `globalstd` vignettes has been updated.

If you are using the previous version, it's recommended to update the package to the latest version on GitHub. The new version is more robust and easier to use/maintain. If your code failed after the updates, it might come from the removal of `pmd2` column and you can always generate this column by `round(pmd,digits)`. If you have any questions or feedback, please feel free to reach out to me.