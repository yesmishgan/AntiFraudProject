
[![Build Status](https://travis-ci.com/yesmishgan/AntiFraudProject.svg?branch=main)](https://travis-ci.com/yesmishgan/AntiFraudProject)

# FraudPredictSystem(FPS)

<img src="https://media.giphy.com/media/lJNoBCvQYp7nq/giphy.gif" width="300" >

# Contents

- [Overview](#overview)
- [Installing dependencies](#installing-dependencies)
    * [Debian](#debian)
    * [macOS](#macos)
- [Usage](#usage)
- [License](#license)

# Overview

This project consists of components as described below.

- Maintaining the transaction database

- Display information from the database

- Dynamic search transactions by ID

- Display statistics on data

- Generation of input data and processing with the trained model

- Handling POST requests containing a json object and adding a record to the database

# Installing dependencies

This project needs [python v3.6+](https://www.python.org) to work. Other objects will be install when you first start.

## Debian

```bash
$ sudo apt-get update
$ sudo apt-get install python3
```

## macOS

Use [brew](https://brew.sh/):
```bash
$ brew install python
```

# Usage

First make sure that you have followed all steps presented in [installing dependencies](#installing-dependencies) topic.

If you want to add application in your library of apps, please follow the commands

```bash
$ git clone https://github.com/yesmishgan/AntiFraudProject.git
$ cd AntiFraudProject/

# if you have macOS
$ mv FraudPredict.app /System/Application
# Run application in your Doc after that command

# if you have other System (without Windows)
$ sudo chmod +x app.sh
$ ./app.sh
```

After the install you can use application in one step. Just click on the icon of the app.

# License

This software is distibuted under MIT License. For more details see [LICENSE.txt](LICENSE.txt).

# Further development

- [ ] Wavelet module
- [ ] JPEG module
