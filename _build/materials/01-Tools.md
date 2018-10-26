---
download_link: assets/downloads/materials/01-Tools.ipynb.zip
pdf_link: assets/pdf/01-Tools.pdf
layout: materials
title: '01-Tools'
prev_page:
  url: /materials/00-Introduction
  title: 'Materials'
next_page:
  url: /materials/02-JupyterNotebooks
  title: '02-JupyterNotebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Tools

This notebook will guide through the tools you will need for class materials and assignments, and how to get them. 

## Prerequisites

This course and associated materials do not presume any prior knowledge of Python, or programming in general. 

To work with the course materials, you will need make sure the tools described here are installed on the computer you will be using. 

None of the materials are computationally heavy. 

## What software you need?

- Python: Working install of python3.6
    - We will be using the anaconda distribution
- Jupyter Notebooks

<center><img src="img/python.png" width="450px"></center>

<div class="alert alert-success">
Python is a programming language, whos development is led by the Python Software Foundation (PSF). 
</div>

<div class="alert alert-info">
The official Python organization website is available <a href="https://www.python.org" class="alert-link">here</a>.
</div>

## Python

- Versions: there are different versions of Python.
    - We will be using 3.6.
- Packages: Python includes a "base set" of code (the standard library), and an extensive ecosystem of third party packages
    - In this course, we will largely focus on the standard library
    - For access to other packages when we need them, we will use Anaconda

<center><img src="img/anaconda.png" width="450px"></center>

<div class="alert alert-success">
Anaconda is an open-source distribution of Python, focused on scientific computing in Python. 
</div>

<div class="alert alert-info">
The anaconda website is 
<a href="https://www.anaconda.com" class="alert-link">here</a>. 
</div>

<center><img src="img/conda.png" width="450px"></center>

<div class="alert alert-success">
Conda is a package management tool, that comes with anaconda. 
</div>

<div class="alert alert-info">
Conda documentation is available
<a href="https://conda.io/docs/" class="alert-link">here</a>.
</div>

## The Anaconda Ecosystem

- Anaconda itself is a distribution, that is, a copy of the Python standard library, included a curated collection of external packages.
- Conda is a package manager, allowing you to download, install, and manage other packages. 



<center><img src="img/jupyter.png" width="300px"></center>

<div class="alert alert-success">
Jupyter notebooks are a way to intermix code, outputs and plain text. 
They run in a web browser, and connect to a kernel to be able to execute code. 
</div>

<div class="alert alert-info">
The official Jupyter website is available 
<a href="http://jupyter.org" class="alert-link">here</a>.
</div>

<hr>

## Installation

You only need to download one thing: anaconda, which comes complete with conda, and Jupyter notebooks.

<div class="alert alert-info">
Download anaconda from
<a href="https://www.anaconda.com/download/" class="alert-link">here</a>.
</div>

Notes
-----
- If you are on Mac, you have a native installation of python. This native installation of Python may be older, will not include the extra packages that you will need for this class, and is best left untouched. 
    - Downloading anaconda will install a separate, independent install of Python, leaving your native install untouched. 
- Windows does not require Python natively and so it is not typically pre-installed. 



{:.input_area}
```python
# You can check which python you are using, and what version it is.
#  Once you have installed anaconda, you should see you are using Python in your anaconda folder
#  Make sure that the version you have is 3.6 (or at least 3.X)
#  Note: these are command-line functions that may not work on windows
!which python
!python --version
```


{:.output_stream}
```
/Users/tom/anaconda/envs/present/bin/python
Python 3.6.3 :: Anaconda custom (64-bit)

```
