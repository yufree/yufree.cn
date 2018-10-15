---
title: Online tools for chemical research
author: ''
date: '2018-10-14'
slug: online-tools-for-chemical-research
categories: []
tags: []
---

I am tired of searching compounds online. So far, more than 140 Millons substances have been registered for CAS registry number. However, it doesn't mean CAS has covered all the compounds. In fact, at least three identifiers have been used to let someone find the compounds' information online.

The first one is CAS registry number. This number is quiet useful to buy standards. However, it's not free to get access to the full list of CAS registry number. Furthormore, this number is for substance, which is different from compounds. For example,  [PubChem](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4702940/) show the SID and CID for the same compounds. Since substances' names or numbers have been used for a long time, some mistakes might happen when we could not tell apart different compounds from the same substances.

The second identifier is Simplified Molecular-Input Line-Entry System (SMILES). This identifier could contain the structure information. However, since the standards are not well established, one compound could be linked to multiple SMILES. Such property has been improved by so-called canonical SMILES. However, this identifier still could not be trusted when you want to use them to get other identifier. SMILES is good to generate the molecular structure. However, we all knew 2D structure could not reflact the 3D structure and some software like MOPAC could be used to find the best structure if you want to do some Quantitative structure–activity relationship based prediction.

The third one is from IUPAC. Of course, it's not IUPAC name because the name has same issue like SMILES. However, IUPAC has trying to generate InChI for compounds with structure information. They also developed InChIKey by hashes on InChI. InChIKey didn't cover all of the chemical substances and user could generate the InChIKey themselves when they have InChI. So the problem is that if such key could be generated locally, some mistakes or missing of layers in InChI would still give different keys to the same compounds.

Those three indentifers are not perfect. This is the major issue when you use convertor for them such as [Chemical Translation Services from UCDavis](http://cts.fiehnlab.ucdavis.edu/batch). You could always find multiple hits from single entry. I know there are lots of indentifers such as PubChem CID and ChemSpider ID. However, they all have own coverages. Some conversions have no U turn.

Anyway this post is not about those issues. I just want to list some databases which might be helpful for researchers doing non-targeted annotation analysis.

## Compounds database

- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) is an open chemistry database at the National Institutes of Health (NIH).

- [Chemspider](http://www.chemspider.com/) is a free chemical structure database providing fast text and structure search access to over 67 million structures from hundreds of data sources.

- [ChEBI](https://www.ebi.ac.uk/chebi/) is a freely available dictionary of molecular entities focused on ‘small’ chemical compounds.

- [CAS numbers](https://www.cas.org/support/documentation/chemical-substances/faqs)

- [eChemPortal](https://www.echemportal.org/echemportal/substancesearch/substancesearchlink.action)  provides free public access to information on properties of chemicals. You could find physical chemical Properties, ecotoxicity, environmental fate and behaviour
toxicity for certain compounds

## Compounds database on certain topic

- [CompTox](https://comptox.epa.gov/dashboard) compounds, exposure and toxicity database. [Here](https://www.epa.gov/chemical-research/downloadable-computational-toxicology-data) is related data. This is for environmental study.

- [T3DB](http://www.t3db.ca/) is a unique bioinformatics resource that combines detailed toxin data with comprehensive toxin target information.

- [HMDB](http://www.hmdb.ca/) is a freely available electronic database containing detailed information about small molecule metabolites found in the human body.

- [Lipid Maps](http://www.lipidmaps.org/)

- [KEGG](https://www.genome.jp/kegg/compound/) is a collection of small molecules, biopolymers, and other chemical substances that are relevant to biological systems.

- [Drugbank](https://www.drugbank.ca/releases/latest) is a unique bioinformatics and cheminformatics resource that combines detailed drug data with comprehensive drug target information.

- [FooDB](http://foodb.ca/) is the world’s largest and most comprehensive resource on food constituents, chemistry and biology.

- [LMDB](http://lmdb.ca) is a freely available electronic database containing detailed information about small molecule metabolites found in different livestock species.

- [Zinc](http://zinc15.docking.org/) is a free database of commercially-available compounds for virtual screening. You could use this database to search commercial information for certain compound's standards.

- [chemexper](http://mastersearch.chemexper.com/) is a commercial website for commercially-available compounds.

## MS Database with annotation

### MS/MS

- [MoNA](http://mona.fiehnlab.ucdavis.edu/) Platform to collect all other open source database

- [MassBank](http://www.massbank.jp/?lang=en)

- [GNPS](https://gnps.ucsd.edu/ProteoSAFe/static/gnps-splash.jsp)

- [ReSpect](http://spectra.psc.riken.jp/): phytochemicals

- [Metlin](https://metlin.scripps.edu/)

- [LipidBlast](http://fiehnlab.ucdavis.edu/projects/LipidBlast): in silico prediction

- [MZcloud](https://www.mzcloud.org/)

- [NIST](https://www.nist.gov/srd/nist-standard-reference-database-1a-v17): Not free

### MS

- [Fiehn Lab](http://fiehnlab.ucdavis.edu/projects/binbase-setup)

- [NIST](https://www.nist.gov/srd/nist-standard-reference-database-1a-v17): No free


## Online tools

- [Molview](http://molview.org) to show a 3D structure from 2D structure. The 3D structure source is from [PubChem](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-3-4) or [Corina](https://www.mn-am.com/products/corina).

- [mol2chemfig](http://chimpsky.uwaterloo.ca/mol2chemfig/) could convert the smiles string into a figure using in LaTeX.

- [molgen](http://molgen.de) generating all structures (connectivity isomers, constitutions) that correspond to a given molecular formula, with optional further restrictions, e.g. presence or absence of particular substructures.

- [QSPR MD tools list](http://www.moleculardescriptors.eu/resources/resources.htm)

- [Isotope](https://www.envipat.eawag.ch/index.php) pattern prediction

- [mfFinder](http://www.chemcalc.org/mf_finder/mfFinder_em_new) predict formula based on accurate mass

I will appreciate it if you could comment with other useful while available online tools related to non-targeted analysis in this post.
