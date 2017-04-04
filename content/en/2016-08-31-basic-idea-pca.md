---
title: Basic idea behind principal components analysis
date: 2016-08-31
slug: basic idea pca
---

For environmental scientist, data analysis might be the only way to show your ability when you get the data from observation. I found many students even researcher showed their data in a bad way and many data analysis pattern just came from certain one paper. However, data analysis methods always have their scopes and some methods might just not suit your cases. 

Thanks to data analysis software, you need not to calculate some values by hand. But to make their usage clear, you need to know the basic idea. I will show some basic ideas behind certain method in a few posts. The first one is principal components analysis(PCA).

In most cases, PCA is used as an exploratory data analysis(EDA) method. In most of those most cases, PCA is just served as visualization method. I mean, when I need to visualize some high-dimension data, I would use PCA.

So, the basic idea behind PCA is compression. When you have 100 samples with concentrations of certain compound, you could plot the concentrations with samples' ID. However, if you have 100 compounds to be analyzed, it would by hard to show the relationship between the samples. Actually, you need to show a matrix with sample and compounds (100 * 100 with the concentrations filled into the matrix) in an informal way.

The PCA would say: OK, guys, I could convert your data into only 100 * 2 matrix with the loss of information minimized. Yeah, that is what the mathematical guys or computer programmer do. You just run the command of PCA. The new two "compounds" might have the cor-relationship between the original 100 compounds and retain the variances between them. After such projection, you would see the compressed relationship between the 100 samples. If some samples' data are similar, they would be projected together in new two "compounds" plot. That is why PCA could be used for cluster and the new "compounds" could be referred as principal components(PCs).

However, you might ask why only two new compounds could finished such task. I have to say, two PCs are just good for visualization. In most cases, we need to collect PCs standing for more than 80% variances in our data if you want to recovery the data with PCs. If each compound have no relationship between each other, the PCs are still those 100 compounds. So you have found a property of the PCs: PCs are orthogonal between each other.

Another issue is how to find the relationship between the compounds. We could use PCA to find the relationship between samples. However, we could also extract the influences of the compounds on certain PCs. You might find many compounds showed the same loading on the first PC. That means the concentrations pattern between the compounds are looked similar. So PCA could also be used to explore the relationship between the compounds.

OK, next time you might recall PCA when you need it instead of other paper showed them.