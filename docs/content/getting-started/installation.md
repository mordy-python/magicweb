---
title: "Installation"
weight: 1
date: 2021-09-02T11:41:28-04:00
draft: false
---

## Installation

### Create a virtual environment

To install Magicweb, you need to have python and pip installed.

First create a virtual environment: `python -m venv venv`. Then activate it: `source venv/bin/activate` on Mac and Linux, or `venv\Scripts\activate` on Windows.

### Install with pip

To install with pip you can use the following command:

`pip install magicweb` or `python -m pip install magicweb`.

If neither of those work, try: `pip3 install magicweb` or `python3 -m pip install magicweb`.

### Install from source

To install from source, clone the repo from github and install it with setup.py like so:

```shell
git clone https://github.com/mordy-python/magicweb.git
cd magicweb
python setup.py install
```
