---
title: Local Metabolites-diseases database based on HMDB
author: ''
date: '2020-12-01'
slug: metabolites-diseases-database-based-on-hmdb
categories: []
tags: []
---

Human Metabolites Database(HMDB) is a great tool to access human related metabolites or small molecular. You could access metabolites' information about disease, which is important for public health related studies. However, it's not easy to search multiple metabolites at the same time. Here I will show a demo to locally access multiple metabolites' disease information.

## Step 1: Annotate the m/z with HMDB ID


```r
library(rmwf)
library(enviGCMS)
data("mzrt")
data("hr")
re <- enviGCMS::getms1anno(pmd = c('Na-H','H','Na'), mz = mzrt$mz[1:10], ppm = 5, db=hr)
```

```
## No retention time information!
## No retention time information!
## No retention time information!
```

```r
# Only check [M+H]+
name <- unique(re[[2]]$name)
# from name to HMDB ID
HMDBID <- webchem::cts_convert(name,'name','human metabolome database')
```

```
## Querying Diethanolamine.
```

```
## OK (HTTP 200).
## Querying 2-Piperidinone. OK (HTTP 200).
## Querying S-Ethyl thioacetate. OK (HTTP 200).
##  Not found. Returning NA.
## Querying S-Methyl propanethioate. OK (HTTP 200).
##  Not found. Returning NA.
## Querying N-Nitroso-pyrrolidine. OK (HTTP 200).
##  Not found. Returning NA.
## Querying 3-(Methylthio)propanal. OK (HTTP 200).
## Querying 3-Mercapto-2-butanone. OK (HTTP 200).
## Querying Gyromitrin. OK (HTTP 200).
## Querying 1-Pyrrolidinecarboxaldehyde. OK (HTTP 200).
## Querying (Methylthio)acetone. OK (HTTP 200).
## Querying 2,5-Dihydro-2,4-dimethyloxazole. OK (HTTP 200).
##  Not found. Returning NA.
## Querying 4-Mercapto-2-butanone. OK (HTTP 200).
## Querying (2R)-2-Hydroxy-2-methylbutanenitrile. OK (HTTP 200).
##  Not found. Returning NA.
## Querying cis-3-Chloroacrylic acid. OK (HTTP 200).
##  Not found. Returning NA.
## Querying trans-3-Chloroacrylic acid. OK (HTTP 200).
##  Not found. Returning NA.
## Querying Allyl methyl sulfoxide. OK (HTTP 200).
##  Not found. Returning NA.
## Querying Neurine. OK (HTTP 200).
##  Not found. Returning NA.
## Querying 2-Hydroxy-2-methylbutanenitrile. OK (HTTP 200).
## Querying N-Methylpyrrolidin-2-one. OK (HTTP 200).
##  Not found. Returning NA.
## Querying Tetrahydrothiophene-1-oxide. OK (HTTP 200).
##  Not found. Returning NA.
```

```r
HID <- unlist(HMDBID)[!is.na(unlist(HMDBID))]
# Check the results
HID
```

```
##                  Diethanolamine                  2-Piperidinone 
##                   "HMDB0004437"                   "HMDB0011749" 
##          3-(Methylthio)propanal           3-Mercapto-2-butanone 
##                   "HMDB0031857"                   "HMDB0031982" 
##                      Gyromitrin     1-Pyrrolidinecarboxaldehyde 
##                   "HMDB0033952"                   "HMDB0034587" 
##             (Methylthio)acetone           4-Mercapto-2-butanone 
##                   "HMDB0040170"                   "HMDB0041015" 
## 2-Hydroxy-2-methylbutanenitrile 
##                   "HMDB0060309"
```

## Step 2: Build local HMDB disease database and search ID

Here is the python code to extract disease related information:


```python
from io import StringIO
from lxml import etree
import csv
def hmdbpextract(name, file):
  ns = {'hmdb': 'http://www.hmdb.ca'}
  context = etree.iterparse(name, tag='{http://www.hmdb.ca}metabolite')
  csvfile = open(file, 'w')
  fieldnames = ['accession', 'dname']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  for event, elem in context:

    accession = elem.xpath('hmdb:accession/text()', namespaces=ns)[0]
    try:
        dname = elem.xpath('hmdb:diseases/hmdb:disease/hmdb:name/text()', namespaces=ns)
    except:
        dname = 'NA'
    writer.writerow({'accession': accession, 'dname': dname})
    # It's safe to call clear() here because no descendants will be
    # accessed
    elem.clear()
# Also eliminate now-empty references from the root node to elem
    for ancestor in elem.xpath('ancestor-or-self::*'):
        while ancestor.getprevious() is not None:
            del ancestor.getparent()[0]
  del context
  return;
hmdbpextract('hmdb_metabolites.xml','hmdbd.csv')
```

If you download HMDB xml file, you could get csv file with disease related information with above code.

However, we need to make this csv file friendly for batch search.


```r
hmdb <- read.csv('hmdbd.csv')
hmdb2 <- t(apply(hmdb,1,function(x) gsub( "^\\[|]$", "", as.character(x))))
hmdb2 <- as.data.frame(hmdb2)
colnames(hmdb2) <- colnames(hmdb)

disease <- hmdb2[,c("accession","dname")]

g <- strsplit(as.character(hmdb2$dname), ",")
dname <- data.frame(accession = rep(hmdb2$accession, lapply(g, length)), dname = unlist(g))
dname$dname <- gsub( '^ ', "", as.character(dname$dname))
dname$dname <- gsub( "^'|'$", "", as.character(dname$dname))
dname$dname <- gsub( '^"|"$', "", as.character(dname$dname))

write.csv(dname,'hmdbdname.csv')
```

This part need to download HMDB database and extract the disease information. I know it's too much for user and I already did this for you.


```r
# download HMDB disease database
db <- read.csv('https://raw.githubusercontent.com/yufree/expodb/master/hmdb/hmdbdname.csv')
alld <- db[db$accession%in%HID,]
```


## Step 3: Search HMDB ID for disease information


```r
alld
```

```
##         X   accession                            dname
## 6908 6908 HMDB0011749                   Ovarian cancer
## 6909 6909 HMDB0011749                  Crohn's disease
## 6910 6910 HMDB0011749               Ulcerative colitis
## 6911 6911 HMDB0011749                Colorectal cancer
## 7625 7625 HMDB0031857 Nonalcoholic fatty liver disease
```

Then we could find two compounds might relate to five disease.

This is a very simple example from m/z to disease and you could hack the code to find new world.
