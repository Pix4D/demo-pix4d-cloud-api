# Simple Demos of the Pix4D Cloud API

## Introduction

These code examples show a simple flow using some of the available Pix4D Engine Cloud APIs.

Behind the scenes this runs on AWS, so you will also have to use their APIs to deal with,
for example, file uploads.

For authentication, the primary way is currently through a client ID and secret. These are provided
by your Pix4D sales rep when you get your Engine Cloud license.

## Useful links

* [Pix4D Engine Cloud support documentation](https://support.pix4d.com/hc/en-us/sections/360003825371-Pix4Dengine-Cloud-API#authentication)
* [Pix4D Engine Cloud Swagger live API](http://cloud.pix4d.com/api/doc/)

## Running this demo

This demo assumes you have python3.6.

The code only uses standard publicly available libraries, and demonstrates a simple usage scenario.

**However, this code is not tested or sufficiently hardened for use in a production system.**

### Create a python virtualenv

```bash
$ virtualenv -p python3.6 venv
$ . venv/bin/activate
```

### Install the requirements

```bash
(venv)$ pip install -r requirements.txt
```

### Set your Pix4D Engine Cloud credentials

```bash
(venv)$ export PIX4D_CLIENT_ID=xxx
(venv)$ export PIX4D_CLIENT_SECRET=xxx
```

### Run the notebooks

```bash
(venv)$ jupyter notebook
```

This will start the `jupyter` server and open the notebook file browser in your web browser.

Open the `*.ipynb` and run it! 