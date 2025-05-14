---
title: 'Introducing ThermoFlask: Simplifying Thermo .raw File Processing'
author: Miao Yu
date: '2025-05-14'
slug: introducing-thermoflask-simplifying-thermo-raw-file-processing
categories: []
tags: []
---
In the world of high resolution mass spectrometry, Thermo `.raw` files are a common format for storing raw data. However, processing these files into more accessible formats like mzML. To make this process easier, ThermoFlask—a Flask-based web application designed to simplify Thermo .raw file processing is developed.

## What is ThermoFlask?

ThermoFlask is a lightweight, user-friendly web application that leverages the power of the ThermoRawFileParser to process .raw files. Whether you're a researcher, data scientist, or bioinformatician, ThermoFlask provides an intuitive interface to upload, process, and download your data in just a few clicks. You can also deploy it as web service and here is a demo [website](https://fywupilibssa.us-east-1.clawcloudrun.com) using this docker image. You can also find the source code on [GitHub](https://github.com/yufree/thermoflask).

## Key Features

ThermoFlask is packed with features to make your workflow seamless:

- Batch Processing: Upload multiple .raw files at once for batch conversion.
Flexible Output Formats: Convert .raw files to mzML, indexed mzML, Parquet, MGF, or metadata-only formats.

- Custom Parameters: Add custom arguments for advanced processing with the ThermoRawFileParser.

- Debugging Support: View command output directly in the interface for troubleshooting.
Download Results: Easily download processed files through the web interface.

## How to Get Started

Getting started with ThermoFlask is easy! Here’s a quick guide:

You can pull the prebuilt Docker image from Docker Hub and run them locally using the following command:

```bash
docker run -p 5000:5000 yufree/thermoflask:latest
```

Upload and Process Files: Open the web interface, upload your .raw files, select the desired output format, and start processing. Once complete, download your results directly from the interface.

Alternatively, you can build the Docker image from the source code. Here’s how:

1. Build the Docker Image: Clone the [repository](https://github.com/yufree/thermoflask) and run the following command to build the Docker image:

```bash
docker build -t thermoflask .
```
2. Run the Application: Start the application with:

```bash
docker run -p 5000:5000 thermoflask
```

The application will be accessible at http://localhost:5000.

## Acknowledgments

ThermoFlask wouldn’t be possible without the incredible work of the ThermoRawFileParser team. I also thank the Flask community for providing a robust framework for building web applications.
