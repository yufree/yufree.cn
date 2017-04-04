---
title: Introduction to SP-ICP-MS
date: 2015-01-03
slug: intro SP ICP MS
---

Single particle Inductively coupled plasma mass spectrometry(SP-ICP-MS) is a novol method for detect, quantify, and characterize nanoparticles. Its theoretical basis was founded by Dr. Degueldre et al. at 2004. Here I would like to show a much more simplified version of this theory and show you how to perform a SP-ICP-MS analysis.

## Single Particle

The core concept in SP-ICP-MS is single particle. How to understand single particle? Single means every scan time on MS would get no more than one particle's signals. So how to get such signal? two ways: limit the amounts in certain scan time(dwell time) get into the MS or limit the dwell time to cut the particle flows into real pieces. We could write them in the following equation:

$$\frac{F \cdot C \cdot V \cdot t}{m} \leq 1$$

C stands for the concentration of certain particles, V stands for the flow rate of the injection, t stands for the dwell time and m stand for the mass of one particles. F means the measurable fraction of the injected particles. When the instrument could satisfy the equation, the collected data could be used for SP-ICP-MS. When you scan the real data, you might see a lot of low signals which is the same with blank data. Those signals could be used as a background and when such signals occupy a large percentage of your data, you data could certainly be used for SP-ICP-MS and you might need a long time to collect enough data for a distribution. 

## Get the diameter distribution of certain standard particles

OK, when you know the source of such data for SP-ICP-MS, we should prepare some standards of nano particles, for example, NIST 60nm silver nano particles. We should treat such diameter as an average of the whole particles and get the mass of single particles by the following equations:

$$m = \frac{4}{3} \pi (\frac{d}{2})^3 \rho $$

When we fixed the F(typically 0.01~0.05), the dwell time and the flow rate, we could get a max concentration of your standards for SP-ICP-MS analysis by the first equation. In most of the litratures, the ICP-MS currently used could not get the signals when the sliver nano particle's diameter less than about 20nm. In such state, the data look like the data collected from blank. You must know for different element the detection limit of diameter is different. Generally speaking, when the atomic weight is heavior, we could get a lower detectable diameter of such pure element. However, for such nano particles have more than one elements, you need a correction.

OK, with a proper concentration for SP-ICP-MS, we could get a standard data for SP-ICP-MS analysis(fixed time such as 1 min) and a blank data for noise. Then we could do the following analysis:

- subset the singal bigger than the average noise as partical signal data
- the signal data should minus the average noise
- treat the average signal data as the average diameter of nano particle and get the relationship(r) between the signal data(S) and the particle mass(M) as S = r(M)
- use such relationship to convert each signal into particle mass and now you could get the mass distribution of nano particle
- use the second equation to change the mass into diameter and you will get the diameter distribution of standard nano particle.
- Since you could fix the dwell time and flow rate, you could also get the F for your analysis

Here when you perform a SP-ICP-MS analysis for standards, the most important parameters you get is the relationship between the signal and the mass. Also the F could be helpful when you want to perform a quantitative analysis.

## Get the diameter distribution of certain particles in samples

When you get a samples, I suggest you perform a normal quantitative analysis for your target element to get the concertration. Then calculate according to the first equation and dilute your sample to meet the requirment for SP-ICP-MS. When you get the sample data, perform the following analysis:

- subset the singal bigger than the average noise as partical signal data
- the signal data should minus the average noise
- use the relationship between the signal and the mass to get the mass and diameter distribution of the partical in your sample

OK, if you want to get the partical number concertration, treat each signal bigger than the average noise as one particle and count the numbers of signal in certain time you will get the partical number concertration with the help of F.

## Some issues

- the distribution of particles are often log-normal while the ions show poisson distribution which could be used to find if the samples have nano particles

- try to use a larger particles to get the relationship between the signal and the mass because small particles show no signal

- TEM could be used to confirm the distribution of your result from SP-ICP-MS

## Application

I wrote a web application for SP-ICP-MS, you could upload your standard and sample data and then get the diameter distribution of the samples. Click [here](https://yufree.shinyapps.io/spicpms/demo.Rmd).

## References

- Degueldre, C., P. -Y. Favarger, and C. Bitea. “Zirconia Colloid Analysis by Single Particle Inductively Coupled Plasma–mass Spectrometry.” Analytica Chimica Acta 518, no. 1–2 (August 2, 2004): 137–42. doi:10.1016/j.aca.2004.04.015.
- Kiss, L. B., J. Söderlund, G. A. Niklasson, and C. G. Granqvist. “New Approach to the Origin of Lognormal Size Distributions of Nanoparticles.” Nanotechnology 10, no. 1 (March 1, 1999): 25. doi:10.1088/0957-4484/10/1/006.
- Laborda, Francisco, Javier Jiménez-Lamana, Eduardo Bolea, and Juan R. Castillo. “Selective Identification, Characterization and Determination of Dissolved silver(I) and Silver Nanoparticles Based on Single Particle Detection by Inductively Coupled Plasma Mass Spectrometry.” Journal of Analytical Atomic Spectrometry 26, no. 7 (July 1, 2011): 1362–71. doi:10.1039/C0JA00098A.
- Lee, Sungyun, Xiangyu Bi, Robert B. Reed, James F. Ranville, Pierre Herckes, and Paul Westerhoff. “Nanoparticle Size Detection Limits by Single Particle ICP-MS for 40 Elements.” Environmental Science & Technology 48, no. 17 (2014): 10291–300. doi:10.1021/es502422v.
- Mitrano, Denise M., Emily K. Lesher, Anthony Bednar, Jon Monserud, Christopher P. Higgins, and James F. Ranville. “Detecting Nanoparticulate Silver Using Single-Particle Inductively Coupled Plasma–mass Spectrometry.” Environmental Toxicology and Chemistry 31, no. 1 (2012): 115–21. doi:10.1002/etc.719.


