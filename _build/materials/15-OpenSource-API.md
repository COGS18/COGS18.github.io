---
interact_link: content/materials/15-OpenSource-API.ipynb
download_link: assets/downloads/15-OpenSource-API.ipynb.zip
pdf_link: assets/pdf/15-OpenSource-API.pdf
layout: materials
title: '15-OpenSource-API'
prev_page:
  url: /materials/14-Documentation-Style
  title: '14-Documentation-Style'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

**Due Dates**
- **CL5** due tonight (5/13)
- **A5** due *Friday* (not Thursday) (11:59 PM) 
- **Final Exam** Friday (due Sat 11 AM)
 
**Notes**
- Fill out your CAPEs, please!
    - \>=85% response rate == +0.5% to everyone's grade
- There will also be a post-course survey (optional; EC +0.25%)

#### Clicker Question #0

What would you prefer we cover in lecture tomorrow?

- A) Advanced Python
- B) Final Exam Review
- C) No Preference

# Open Source, Scientific Computing & APIs

## Open Source

- Open Source Software, versioning & History of Python
- Tools: Jupyter, GitHub, PyPI, PIP, Conda

## Scientific Computing

- `scipy`, `numpy`, `pandas`

### APIs

- `lisc`, `tweepy`

## Open Source

<div class="alert alert-success">
Open source software is software for which the source code is openly available.
</div>

The Source Code for Python (which is actually written in C) is all available.

Open Source Software is free. (free == freedom)

Open source software is software that the user can:

- use and install the software
- view the source code of the project
- distribute the software
- change the source code of the project

Scientific research is often done in an exclusively open source environment.

## Aside: Brief History of Python

First conceptualized by **Guido van Rossum** in the late 1980s: 
- ABC is a general-pupose programming language that influenced Python
- goal: simple scripting language
    - basic syntax
    - indentation rather than cruly braces or begin-end blocks
    - developed certain data types (dictionary, list, strings, numbers)
- he was the BDFL (benevolent dictator for life) until July 2018

### Basic Timeline
- 1991: Python 0.9.0 was first released 
- 1994: Python 1.0 (lambda, map, filter, and reduce)
- 2000: Python 2.0 (list comprehensions, full garbage collector, supported unicode)
- 2008: Python 3.0 released (print function; not backwards-compatible, fulfilling the 13th law of the Zen of Python)

### For Context:

- 1842: Ada Lovelace - first published computer program
- 1940s: first high level programming language
- 1956: FORTRAN - first commercially available
- 1972: C
- 1980s: Consolidation, modules, & performance
    - 1987: Perl
- 1990s: Age of the Internet
    - 1991: **Python**
    - 1993: R
    - 1995: Java

**Fun fact**: Python is named after the British TV show Monty Python (not the snake).



## Open Source Developers

<div class="alert alert-success">
Open source software is often developed in an collaborative, public manner, through open collaboration.
</div>

Many are community-driven:
- open, public, & collaborative
- `pandas` was intially written by Wes McKinney

How open source packages are maintained and updated:
- support from foundations
- grant funding
- out of the kindness of individual's or the community's heart(s)

## Software Management & Distribution

- Jupyter
- GitHub
- PyPI
- PIP
- Conda

### Aside: Project Jupyter

- Spun off from IPython in 2014 (Fernando Perez)
- originally called "IPython Notebooks" (this is where .ipynb comes from)
- intended for use by those who program in Julia, Python, and R 
- developed to support those who use interactive computing

This document (.ipynb) IS a JSON document
- {'key' : 'value'}
- nested & hierarchical
- operating unit is the cell (Markdown, code, LaTeX, ...)

### IPython

- Interactive Python
- Initial release: 2001
- Command Shell for interactive computing in the shell

- 1991: Python 0.9.0 was first released 
- 1994: Python 1.0 (lambda, map, filter, and reduce)
- 2000: Python 2.0 (list comprehensions, full garbage collector, supported unicode)
- 2001: IPython released
- 2008: Python 3.0 released (print function; not backwards-compatible, fulfilling the 13th law of the Zen of Python)
- 2014: Jupyter notebooks spun off

### GitHub

<div class="alert alert-success">
<b>GitHub</b> is a software development platform, which is used to host and develop open source projects.
</div>

Similar to Dropbox or Google Drive...but for code.

#### Benefits of GitHub

- Share code
- Work collaboratively
- See others' code 
- Contribute to others' code

But...what if you just want to _use_ what's available to you in Python...

### PyPI: Python Package Index

<div class="alert alert-success">
The Python Package Index is a software repository for the Python programming language.
</div>

[PyPI](https://pypi.org/): Where packages are hosted. You can search and use packages from Python.

### PIP: Python Installer

<div class="alert alert-success">
PIP is a Python tool for installing Python packages. 
</div>

It searches PyPi for you and allows you to install new python packages from the terminal.

The format for this is:

`pip install package_name`

On Datahub, you have to use the `--user` flag

`pip install --user package_name`




{:.input_area}
```python
# for example 
!pip install --user nltk
```


## Licenses

<div class="alert alert-success">
The details of how an open-source project can be used are detailed in its <b>license</b>, which explicitly states its terms of use. 
</div>

- Open Source projects still have a license:
    - sometimes it says: go do whatever you want with this
    - other times it says: if you're not a company/going to make money, you can use this
    - and other times it says: you can use it but you have to attribute the original developers

## Versioning

When you make changes to the software you've released into the world, you have to change the version of that software to let people know changes have occurred.

### Versioning Schemes

The rules, if you're new to this can be [dizzying](https://www.python.org/dev/peps/pep-0440/#version-scheme), so we'll [simplify](https://www.python.org/dev/peps/pep-0396/) for now:

- `<MAJOR>.<MINOR>`
    - i.e. 1.3
    
- `<MAJOR>.<MINOR>.<MAINTENANCE>`
    - i.e. 1.3.1

- `<MAJOR>` - increase by 1 w/ incompatible API changes
- `<MINOR>` - increase by 1 w/ added functionality in a backwards-compatible manner
- `<MAINTENANCE>` - (aka patch) inrease by 1 w/  backwards-compatible bug fixes.

In Python (package) development... when `<MAJOR>` == 0, suggests a package in development



{:.input_area}
```python
# Python version
!python --version
```




{:.input_area}
```python
# see version information
!pip show nltk
```




{:.input_area}
```python
# see version information
import nltk
nltk.__version__
```


### Dependencies

<div class="alert alert-success">
Packages can have dependencies on each other, meaning they require (use) other packages to work.
</div>

### A Note on Conda

<div class="alert alert-success">
Conda is a package management and environment management system. 
</div>

`pip` manages single installs. `Conda` manages the whole system / environment and interactions between packages.

## Scientific Computing

<div class="alert alert-success">
<b>Scientific Computing</b> is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
</div>

## Scientific Python: Scipy Stack

Scipy = Scientific Python

- `scipy`
- `numpy`
- `pandas`
- Data Analysis in Python

<div class="alert alert-success">
<b><code>Scipy</code></b> is an <i>ecosystem</i>, including a collection of open-source packages for scientific computing in Python.
</div>

A 'family' of packages that all work well together to do scientific computing.

Not made by the same people who manage the standard library.

## Homogenous Data

- for example: store data of the same type (i.e. all numerics)
- recordings of values from experimental participants
- heights or quantitative information from survey data

Lists are a start, and lists of lists are possible.

But, they can get nightmareish.

So we use arrays.

### `numpy`

**`numpy`** - stands for numerical python

**arrays** - work with arrays (matrices)

Allow you to efficiently operate on arrays (linear algebra, matrix operations, etc.)



{:.input_area}
```python
import numpy as np
```




{:.input_area}
```python
# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
```




{:.input_area}
```python
arr1
```




{:.input_area}
```python
# lists of lists don't store dimensionality well
[[1, 2], [3, 4]] 
```


#### Indexing Arrays



{:.input_area}
```python
# Check out an array of data
arr1
```




{:.input_area}
```python
# Check the shape of the array
arr1.shape
```




{:.input_area}
```python
# Index into a numpy array
arr1[0, 0]
```


Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

#### Notes on Arrays



{:.input_area}
```python
# arrays are most helpful when they
# have the same length in each list
np.array([[1, 2, 3, 4], [2, 3, 4]])
```




{:.input_area}
```python
# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])
```


#### Working with Arrays

(Things you can't do with lists)



{:.input_area}
```python
# Add arrays together
arr1 + arr2
```




{:.input_area}
```python
# Matrix mutliplication
arr1 * arr2
```


#### A brief reminder: `zip()`

`zip()` takes two iterables (things you can loop over) and loop over them together.



{:.input_area}
```python
for a, b in zip([1,2], ['a','b']):
    print(a, b)
```


#### Clicker Question #1

Given the following code, what will it print out?



{:.input_area}
```python
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0,:], data[1,:]):
    output.append(d1 + d2)

print(output)
```


- A) [1, 2, 3, 4]
- B) [1, 2, 3, 4, 5, 6, 7, 8]
- C) [6, 8, 10, 12]
- D) [10, 26]
- E) [36]

Note that if you find yourself looping over arrays...there is probably a better way.



{:.input_area}
```python
data.sum()
```




{:.input_area}
```python
data.sum(axis=0)
```


## Heterogenous Data

- have continuous (numeric) and categorical (discrete) data
- different data types need to be stored
- uses a DataFrame object (think: spreadsheet)
- allows for column and row labels

### pandas



{:.input_area}
```python
import pandas as pd
```




{:.input_area}
```python
# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
```




{:.input_area}
```python
# Create a dataframe 
df = pd.DataFrame([d1, d2], [0, 1])
```




{:.input_area}
```python
# Check out the dataframe
df
```




{:.input_area}
```python
# You can index in pandas
df['condition']
```




{:.input_area}
```python
# You can index in pandas
df.loc[0,:]
```


#### Working with DataFrames



{:.input_area}
```python
df.describe()
```




{:.input_area}
```python
# Take the average of all numeric columns
df.mean()
```


#### Clicker Question #2

Comparing them to standard library Python types, which is the best mapping for these new data types?

- A) DataFrames are like lists, arrays are like tuples
- B) DataFrames and arrays are like lists
- C) DataFrames are like tuples, arrays are like lists
- D) DataFrames and arrays are like dictionaries
- E) Dataframes are like dictionaries, arrays are like lists

## Plotting



{:.input_area}
```python
%matplotlib inline

import matplotlib.pyplot as plt
```




{:.input_area}
```python
# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])
```




{:.input_area}
```python
# Plot the data
plt.plot(dat);
```


- can change plot type
- _lots_ of customizations possible

## Analysis

- `scipy` - statistical analysis
- `sklearn` - machine learning



{:.input_area}
```python
import scipy as sp
from scipy import stats
```




{:.input_area}
```python
# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)
```


### Analysis - Plotting the Data



{:.input_area}
```python
# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);
```


### Analysis - Statistical Comparisons



{:.input_area}
```python
# Statistically compare the two distributions
stats.ttest_ind(d1, d2)
```


## COGS108: Data Science in Practice

<div class="alert alert-info">
If you are interested in data science and scientific computing in Python, consider taking <b>COGS108</b> : <a>https://github.com/COGS108/</a>.
</div>

# APIs

- modules
    - review
    - module APIs
- RESTful APIs
    - LISC
    - Twitter API

## Application Programming Interface

<div class="alert alert-success">
An <b>API</b> is a programmatic interface to an application - a software to software interface, or way for programs to talk to other programs. 
</div>

If you are pointing and clicking on computer applications, that is _not_ an API.

If you are writing code to interact with software and get information, that _IS_ an API.

## Module APIs

Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

## Quick Review: Modules

<div class="alert alert-success">
A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
</div>

Modules are stored in Python files. We can import these files into our namespace, to gain access to the module within Python.



{:.input_area}
```python
# Import & use the math module
import math
math.sqrt(9)
```


### Imports: `from` & `as`



{:.input_area}
```python
# Import a specific object from a module
from random import choice

# use random.choice
magic_8_ball = ['As I see it, yes!', 'Most likely.', 
                'Ask again later.', 'Don\'t Count on it', 
                'Outlook not so good']

choice(magic_8_ball)
```




{:.input_area}
```python
# Import a specific object from a module using an alias
from random import choice as ch

# use shorter name 
ch(magic_8_ball)
```


### Importing Custom Code



{:.input_area}
```python
# Import a class class from an external module
from remote import MyNumbers
```




{:.input_area}
```python
# Define an instance of our custom class
# apply method
out = MyNumbers(2, 3).add()
out
```




{:.input_area}
```python
# remember we only imported MyNumbers
choice?
```


## Module APIs

Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

#### Clicker Question #3

What will the following code snippet print out:



{:.input_area}
```python
def foo(a, b, c=0):
    d = c
    for e in a[:b]:
        d += e
    return d

print(foo(b=2, a=[10, 10, 10, 10]))
```


- A) 10
- B) 20
- C) 30 
- D) 40
- E) None

#### Clicker Question #4

How easy did you find interpreting this code?

- A) Easy
- B) Fairly Easy
- C) Neutral
- D) Somewhat Difficult
- E) Difficult

Arguably, this function does _not_ have a good API.

### Function with Fixed Names

#### Clicker Question #5

What will the following code snippet print out:



{:.input_area}
```python
def sum_across_list(list_to_count, end_index, start_val=0):

    running_count = start_val
    
    for element in list_to_count[:end_index]:
        running_count += element
    
    return running_count

print(sum_across_list(end_index=2, list_to_count=[10, 10, 10, 10]))
```


- A) 10
- B) 20
- C) 30 
- D) 40
- E) None

#### Clicker Question #6

How easy did you find interpreting this code?

- A) Easy
- B) Fairly Easy
- C) Neutral
- D) Somewaht Difficult
- E) Difficult

This is the same function, but has a better API.

## Names Matter!

When writing an API, you are designing the user facing code that a programmer (maybe you in the future) will use.

When using an API, you are using the programmer-facing code that someone else wrote for the task. 

Taking time to have good names and clear documentation can *really help* a programmer interact with an API. 

## Web APIs

APIs are an interface to interact with an application, _designed for programmatic use_ :
- They allow systematic, controlled access to (for example) an applications database and procedures
- They can be used to request data and/or to request that the the application perform some procedure

### RESTful API

(Representational State Transfer API) 

An approach to interact with web addresses

## EUtils API

<div class="alert alert-success">
EUtils is a web accessible API for the National Center for Biotechnology Information, and the databases they curate.
</div>

### EUtils: Search

Search a database to get information we want it to return



{:.input_area}
```python
# Set the base URL for the e-utils API
# where you go to query information from this web address
base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
```


Build a URL like a Python function call...

We're just adding some additional 'parameters'.



{:.input_area}
```python
# Set the information we need for launching a search request
search = 'esearch.fcgi?'
term = 'term=' + 'brain'
```


Interacting with APIs specifies that we follow the rules specified by the API from which we're requesting information.

### EUtils: Fetch



{:.input_area}
```python
# Build the full search URL
search_url = base_url + search + term
print(search_url)
```




{:.input_area}
```python
# Set the information we need for launching a fetch request
fetch = 'efetch.fcgi?'
db = 'db=' + 'pubmed'
retmode = '&retmode=' + 'xml'
pubmed_id = '&id=' + str(30439964)
```




{:.input_area}
```python
# Build the full search URL
fetch_url = base_url + fetch + db + retmode + pubmed_id
print(fetch_url)
```


But, our goal isn't to see this information in a web browser. Web browsers are for humans. We want to use this information computationally...

## Requesting Web Pages from Python

To accomplish API interactions, we need to use HTTP requests.



{:.input_area}
```python
# The requests module allows you to send URL requests from python
import requests

# Beautiful Soup has functions to 'clean up' returned web pages into human-friendlier formats
from bs4 import BeautifulSoup
```


### EUtils Search, through Python



{:.input_area}
```python
print(search_url)
```




{:.input_area}
```python
# Request the search page, and parse
search_page = requests.get(search_url)
search_content = BeautifulSoup(search_page.content, 'xml')
```




{:.input_area}
```python
# Check out the content of the returned page
search_content
```


### EUtils Fetch, through Python



{:.input_area}
```python
print(fetch_url)
```




{:.input_area}
```python
# Request the fetch page, and parse
fetch_page = requests.get(fetch_url)
fetch_content = BeautifulSoup(fetch_page.content, 'lxml')
```




{:.input_area}
```python
# Check out the content of the page
# fetch_content
```


### BeautifulSoup Objects



{:.input_area}
```python
# Our 'fetch_content' variable is a custom BeautifulSoup object
type(fetch_content)
```




{:.input_area}
```python
# We can use some methods to access particular information
fetch_content.find('year').text
```


## Literature Scanner

But when making HTTP requests it can be difficult to figure out exactly what URL needs to be specified and how to get the contents back out.

So, often in Python we'll interact with an API indirectly. There are packages that will use methods and objects to make this easier on us.

**LISC** : Literature Scanner is a tool for automated meta-analyses of scientific literature (https://github.com/lisc-tools/lisc)



{:.input_area}
```python
# uncomment and run to have the following 
# example work in your notebook
!pip install --user git+https://github.com/lisc-tools/lisc.git
```




{:.input_area}
```python
# Import LISC - Words
from lisc import Words
```




{:.input_area}
```python
# Initialize Words object & set some search terms
words = Words()
words.add_terms(['brain']) 
```




{:.input_area}
```python
# Run words scrape
words.run_collection(retmax = '5')
```


### LISC: Words Data



{:.input_area}
```python
# Check out some information from our scraped data
for phrase in words['brain']:
    print(phrase['title'])
```


## Twitter API



{:.input_area}
```python
# to use this on your computer
# uncomment and run following line
# !pip install tweepy
```


Then, follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) for authetication of tweepy with Python.



{:.input_area}
```python
# Accessing Twitter API from Python
#  Note: to run this, you will have to fill in stw.py with your OAuth credentials.
#    You can do that here: https://apps.twitter.com/

# Import tweepy to access API
import tweepy
from tweepy import OAuthHandler

# Import my API credentials
from stw import *

# Twitter API requires Authentification with OAuth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object to access Twitter
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.user.name)
    print(status.text, '\n')
```

