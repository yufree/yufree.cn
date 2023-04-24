---
title: Use msconvert in Linux or Mac
author: ''
date: '2019-10-15'
slug: use-msconvert-in-linux-or-mac
categories: []
tags:
  - metabolomics
---

One of the major issue for metabolomics data analysis is that user have to use Window to convert vendor data into open source format like mzML or mzXML. Though msConvert could be run under Linux or Mac, it will not support vendor format. It's really annoying to set up virtual machine for data format issue. Another software supporting vendor format is [Abf Converter](https://www.reifycs.com/AbfConverter/index.html), which also only support Windows and their output is for MS-DIAL.

Recently I noticed that a docker [image](https://hub.docker.com/r/chambm/pwiz-skyline-i-agree-to-the-vendor-licenses) is created to covert vendor data by [ProteoWizard](http://proteowizard.sourceforge.net/download.html). It only has 3.9GB, which is much easier to use under Linux. Just pull it from DockerHub:

```bash
docker pull chambm/pwiz-skyline-i-agree-to-the-vendor-licenses
```

The usage is quite clear  You could use the following code to convert all the files in a folder:

```bash
docker run -it --rm -e WINEDEBUG=-all -v /your/data/path/:/data chambm/pwiz-skyline-i-agree-to-the-vendor-licenses wine msconvert /data/*.RAW
```

There is small problem for Agilent files: `.d` format is actually a folder. If you use previous code, you will get Then a `for` trick could solve this issue:

```bash
for f in $(basename /your/path/*.*)
do
  docker run -it --rm -e WINEDEBUG=-all -v /your/path:/data chambm/pwiz-skyline-i-agree-to-the-vendor-licenses wine msconvert /data/$f
done
```

Then you will see the converted mzML in the same directory of your raw data folder.

There are three vendor formats not supporting by this image: ABI T2D, Bruker FID/YEP and Waters UNIFI.

-----

Updates on 2023-04-23

- Errors for Thermos Fisher Raw files

Try [ThermoRawFileParser](https://github.com/compomics/ThermoRawFileParser) and they also shared a docker image:

```
docker run -i -t -v /home/user/raw:/data_input quay.io/biocontainers/thermorawfileparser:<tag> ThermoRawFileParser.sh --help
```

The <tag> could be *1.4.2--ha8f3691_0* and you could check here for [details](https://quay.io/repository/biocontainers/thermorawfileparser?tab=tags).

- Singularity

For msconvert, you need to build the singularity image through Dockerhub:

```
singularity pull docker://chambm/pwiz-skyline-i-agree-to-the-vendor-licenses
```

Then use the following code to convert the file:

```
singularity exec --cleanenv -B ~:/mywineprefix --writable-tmpfs pwiz-skyline-i-agree-to-the-vendor-licenses_latest.sif mywine msconvert --32 --zlib --filter "peakPicking true 1-" --filter "zeroSamples removeExtra" 'test.RAW'
```

Or you might choose ThermoRawFileParser:

```
singularity pull docker://globusgenomics/thermorawfileparser
```

Then use the following code to convert files in certain folder:

```
singularity exec --cleanenv thermorawfileparser_latest.sif ThermoRawFileParser.sh -d PATH_OF_RAW_FILES
```
