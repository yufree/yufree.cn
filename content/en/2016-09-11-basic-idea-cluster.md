---
title: Basic idea behind cluster analysis
date: 2016-09-11
slug: basic idea cluster
---

After we got a lot of samples and analyzed the concentrations of many compounds in them, we may ask about the relationship between the samples. You might have the sampling information such as the date and the position and you could use boxplot or violin plot to explore the relationships among those categorical variables. However, you could also use the data to find some potential relationship.

But how? if two samples' data were almost the same, we might think those samples were from the same potential group. On the other hand, how do we define the "same" in the data?

Cluster analysis told us that just define a "distances" to measure the similarity between samples. Mathematically, such distances would be shown in many different manners such as the sum of the absolute values of the differences between samples. 

For example, we analyzed the amounts of compound A, B and C in two samples and get the results:

| Compounds(ng) | A | B | C |
| ------------- |---|---|---|
| Sample 1      | 10| 13| 21|
| Sample 2      | 54| 23| 16|

The distance could be:

$$
distance = |10-54|+|13-23|+|21-16| = 59
$$

Also you could use the sum of squares or other way to stand for the similarity. After you defined a "distance", you could get the distances between all of pairs for your samples. If two samples' distance was the smallest, put them together as one group. Then calculate the distances again to combine the small group into big group until all of the samples were include in one group. Then draw a dendrogram for those process.

The following issue is that how to cluster samples? You might set a cut-off and directly get the group from the dendrogram. However, sometimes you were ordered to cluster the samples into certain numbers of groups such as three. In such situation, you need K means cluster analysis.

The basic idea behind the K means is that generate three virtual samples and calculate the distances between those three virtual samples and all of the other samples. There would be three values for each samples. Choose the smallest values and class that sample into this group. Then your samples were classified into three groups. You need to calculate the center of those three groups and get three new virtual samples. Repeat such process until the group members unchanged and you get your samples classified.

OK, the basic idea behind the cluster analysis could be summarized as define the distances, set your cut-off and find the group. By this way, you might show potential relationships among samples.