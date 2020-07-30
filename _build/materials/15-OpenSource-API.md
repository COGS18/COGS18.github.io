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
  url: /materials/16-AdvancedPython
  title: '16-AdvancedPython'
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


{:.output_stream}
```
Python 3.7.0

```



{:.input_area}
```python
# see version information
!pip show nltk
```


{:.output_stream}
```
Name: nltk
Version: 3.3
Summary: Natural Language Toolkit
Home-page: http://nltk.org/
Author: Steven Bird
Author-email: stevenbird1@gmail.com
License: Apache License, Version 2.0
Location: /anaconda3/lib/python3.7/site-packages
Requires: six
Required-by: lisc

```



{:.input_area}
```python
# see version information
import nltk
nltk.__version__
```





{:.output_data_text}
```
'3.3'
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
arr2
```





{:.output_data_text}
```
array([[5, 6],
       [7, 8]])
```





{:.input_area}
```python
# lists of lists don't store dimensionality well
[[1, 2], [3, 4]]
```





{:.output_data_text}
```
[[1, 2], [3, 4]]
```



#### Indexing Arrays



{:.input_area}
```python
# Check out an array of data
arr1
```





{:.output_data_text}
```
array([[1, 2],
       [3, 4]])
```





{:.input_area}
```python
# Check the shape of the array
arr1.shape
```





{:.output_data_text}
```
(2, 2)
```





{:.input_area}
```python
# Index into a numpy array
arr1[0, 1]
```





{:.output_data_text}
```
2
```



Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

#### Notes on Arrays



{:.input_area}
```python
# arrays are most helpful when they
# have the same length in each list
array4 = np.array([[1, 2, 3, 4], [2, 3, 4]])
```




{:.input_area}
```python
# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])
```





{:.output_data_text}
```
array([['1', '2', 'cogs18'],
       ['2', '3', '4']], dtype='<U21')
```



#### Working with Arrays

(Things you can't do with lists)



{:.input_area}
```python
# Add arrays together
arr1 + arr2
```





{:.output_data_text}
```
array([[ 6,  8],
       [10, 12]])
```





{:.input_area}
```python
# Matrix mutliplication
arr1 * arr2
```





{:.output_data_text}
```
array([[ 5, 12],
       [21, 32]])
```



#### A brief reminder: `zip()`

`zip()` takes two iterables (things you can loop over) and loop over them together.



{:.input_area}
```python
for a, b in zip([1,2], ['a','b']):
    print(a, b)
```


{:.output_stream}
```
1 a
2 b

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


{:.output_stream}
```
[6, 8, 10, 12]

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





{:.output_data_text}
```
36
```





{:.input_area}
```python
data.sum(axis=0)
```





{:.output_data_text}
```
array([ 6,  8, 10, 12])
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
d1
```





{:.output_data_text}
```
{'Subj_ID': '001', 'score': 16, 'group': 2, 'condition': 'cognition'}
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





<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Subj_ID</th>
      <th>condition</th>
      <th>group</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>001</td>
      <td>cognition</td>
      <td>2</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>002</td>
      <td>perception</td>
      <td>1</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```python
# You can index in pandas
df['condition']
```





{:.output_data_text}
```
0     cognition
1    perception
Name: condition, dtype: object
```





{:.input_area}
```python
# You can index in pandas
df.loc[0,:]
```





{:.output_data_text}
```
Subj_ID            001
condition    cognition
group                2
score               16
Name: 0, dtype: object
```



#### Working with DataFrames



{:.input_area}
```python
df.describe()
```





<div markdown="0">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.500000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.707107</td>
      <td>4.242641</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.250000</td>
      <td>17.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.500000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.750000</td>
      <td>20.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.000000</td>
      <td>22.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```python
# Take the average of all numeric columns
df.mean()
```





{:.output_data_text}
```
Subj_ID                     (1+9.5j)
condition    (2.1213203435596424+8j)
group                       (1.5+0j)
score                        (19+0j)
dtype: complex128
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



![png](../images/build/materials/15-OpenSource-API_100_0.png)


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



![png](../images/build/materials/15-OpenSource-API_106_0.png)


### Analysis - Statistical Comparisons



{:.input_area}
```python
# Statistically compare the two distributions
stats.ttest_ind(d1, d2)
```





{:.output_data_text}
```
Ttest_indResult(statistic=-11.321459970682378, pvalue=7.612910941171958e-29)
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





{:.output_data_text}
```
3.0
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





{:.output_data_text}
```
'Outlook not so good'
```





{:.input_area}
```python
# Import a specific object from a module using an alias
from random import choice as ch

# use shorter name 
ch(magic_8_ball)
```





{:.output_data_text}
```
"Don't Count on it"
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





{:.output_data_text}
```
5
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


{:.output_stream}
```
20

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


{:.output_stream}
```
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?term=brain

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


{:.output_stream}
```
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=30439964

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


{:.output_stream}
```
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?term=brain

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





{:.output_data_text}
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eSearchResult PUBLIC "-//NLM//DTD esearch 20060628//EN" "https://eutils.ncbi.nlm.nih.gov/eutils/dtd/20060628/esearch.dtd">
<eSearchResult><Count>1982799</Count><RetMax>20</RetMax><RetStart>0</RetStart><IdList>
<Id>32721125</Id>
<Id>32721123</Id>
<Id>32721081</Id>
<Id>32721055</Id>
<Id>32721035</Id>
<Id>32720915</Id>
<Id>32720904</Id>
<Id>32720895</Id>
<Id>32720870</Id>
<Id>32720869</Id>
<Id>32720857</Id>
<Id>32720856</Id>
<Id>32720845</Id>
<Id>32720835</Id>
<Id>32720776</Id>
<Id>32720756</Id>
<Id>32720711</Id>
<Id>32720707</Id>
<Id>32720701</Id>
<Id>32720690</Id>
</IdList><TranslationSet><Translation> <From>brain</From> <To>"brain"[MeSH Terms] OR "brain"[All Fields]</To> </Translation></TranslationSet><TranslationStack> <TermSet> <Term>"brain"[MeSH Terms]</Term> <Field>MeSH Terms</Field> <Count>1205235</Count> <Explode>Y</Explode> </TermSet> <TermSet> <Term>"brain"[All Fields]</Term> <Field>All Fields</Field> <Count>1590084</Count> <Explode>N</Explode> </TermSet> <OP>OR</OP> <OP>GROUP</OP> </TranslationStack><QueryTranslation>"brain"[MeSH Terms] OR "brain"[All Fields]</QueryTranslation></eSearchResult>
```



### EUtils Fetch, through Python



{:.input_area}
```python
print(fetch_url)
```


{:.output_stream}
```
http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=30439964

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
fetch_content
```





{:.output_data_text}
```
<?xml version="1.0" ?><!DOCTYPE PubmedArticleSet PUBLIC "-//NLM//DTD PubMedArticle, 1st January 2019//EN" "https://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd">
<html><body><pubmedarticleset>
<pubmedarticle>
<medlinecitation owner="NLM" status="MEDLINE">
<pmid version="1">30439964</pmid>
<datecompleted>
<year>2019</year>
<month>04</month>
<day>09</day>
</datecompleted>
<daterevised>
<year>2019</year>
<month>04</month>
<day>09</day>
</daterevised>
<article pubmodel="Electronic-eCollection">
<journal>
<issn issntype="Electronic">1932-6203</issn>
<journalissue citedmedium="Internet">
<volume>13</volume>
<issue>11</issue>
<pubdate>
<year>2018</year>
</pubdate>
</journalissue>
<title>PloS one</title>
<isoabbreviation>PLoS ONE</isoabbreviation>
</journal>
<articletitle>Hyperacute changes in blood mRNA expression profiles of rats after middle cerebral artery occlusion: Towards a stroke time signature.</articletitle>
<pagination>
<medlinepgn>e0206321</medlinepgn>
</pagination>
<elocationid eidtype="doi" validyn="Y">10.1371/journal.pone.0206321</elocationid>
<abstract>
<abstracttext>Stroke evolution is a highly dynamic but variable disease which makes clinical decision making difficult. Biomarker discovery programs intended to aid clinical decision making have however largely ignored the rapidity of stroke evolution. We have used gene array technology to determine blood mRNA expression changes over the first day after stroke in rats. Blood samples were collected from 8 male spontaneously hypertensive rats at 0, 1, 2, 3, 6 and 24h post stroke induction by middle cerebral artery occlusion. RNA was extracted from whole blood stabilized in PAXgene tubes and mRNA expression was detected by oligonucleotide Affymetrix microarray. Using a pairwise comparison model, 1932 genes were identified to vary significantly over time (pâ‰¤0.5x10(-7)) within 24h after stroke. Some of the top20 most changed genes are already known to be relevant to the ischemic stroke physiopathology (e.g. Il-1R, Nos2, Prok2). Cluster analysis showed multiple stereotyped and time dependent profiles of gene expression. Direction and rate of change of expression for some profiles varied dramatically during these 24h. Profiles with potential clinical utility including hyper acute or acute transient upregulation (with expression peaking from 2 to 6h after stroke and normalisation by 24h) were identified. We found that blood gene expression varies rapidly and stereotypically after stroke in rats. Previous researchers have often missed the optimum time for biomarker measurement. Temporally overlapping profiles have the potential to provide a biological "stroke clock" able to tell the clinician how far an individual stroke has evolved.</abstracttext>
</abstract>
<authorlist completeyn="Y">
<author validyn="Y">
<lastname>Dagonnier</lastname>
<forename>Marie</forename>
<initials>M</initials>
<identifier source="ORCID">0000-0002-0981-4962</identifier>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Wilson</lastname>
<forename>William John</forename>
<initials>WJ</initials>
<affiliationinfo>
<affiliation>The Commonwealth Scientific and Industrial Research Organisation (CSIRO), Sydney, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Favaloro</lastname>
<forename>Jenny Margaret</forename>
<initials>JM</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Rewell</lastname>
<forename>Sarah Susan Jane</forename>
<initials>SSJ</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Lockett</lastname>
<forename>Linda Jane</forename>
<initials>LJ</initials>
<affiliationinfo>
<affiliation>The Commonwealth Scientific and Industrial Research Organisation (CSIRO), Sydney, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Sastra</lastname>
<forename>Stephen Andrew</forename>
<initials>SA</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Jeffreys</lastname>
<forename>Amy Lucienne</forename>
<initials>AL</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Dewey</lastname>
<forename>Helen Margaret</forename>
<initials>HM</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Donnan</lastname>
<forename>Geoffrey Alan</forename>
<initials>GA</initials>
<identifier source="ORCID">0000-0001-6324-3403</identifier>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
</author>
<author validyn="Y">
<lastname>Howells</lastname>
<forename>David William</forename>
<initials>DW</initials>
<affiliationinfo>
<affiliation>The Florey Institute of Neuroscience and Mental Health, Melbourne Brain Centre, Austin Campus, Heidelberg, Australia.</affiliation>
</affiliationinfo>
<affiliationinfo>
<affiliation>School of Medicine, Faculty of Health, University of Tasmania, Hobart, Australia.</affiliation>
</affiliationinfo>
</author>
</authorlist>
<language>eng</language>
<publicationtypelist>
<publicationtype ui="D016428">Journal Article</publicationtype>
</publicationtypelist>
<articledate datetype="Electronic">
<year>2018</year>
<month>11</month>
<day>15</day>
</articledate>
</article>
<medlinejournalinfo>
<country>United States</country>
<medlineta>PLoS One</medlineta>
<nlmuniqueid>101285081</nlmuniqueid>
<issnlinking>1932-6203</issnlinking>
</medlinejournalinfo>
<chemicallist>
<chemical>
<registrynumber>0</registrynumber>
<nameofsubstance ui="D015415">Biomarkers</nameofsubstance>
</chemical>
<chemical>
<registrynumber>0</registrynumber>
<nameofsubstance ui="D012333">RNA, Messenger</nameofsubstance>
</chemical>
</chemicallist>
<citationsubset>IM</citationsubset>
<meshheadinglist>
<meshheading>
<descriptorname majortopicyn="N" ui="D000818">Animals</descriptorname>
</meshheading>
<meshheading>
<descriptorname majortopicyn="N" ui="D015415">Biomarkers</descriptorname>
<qualifiername majortopicyn="N" ui="Q000097">blood</qualifiername>
</meshheading>
<meshheading>
<descriptorname majortopicyn="Y" ui="D020869">Gene Expression Profiling</descriptorname>
</meshheading>
<meshheading>
<descriptorname majortopicyn="N" ui="D020244">Infarction, Middle Cerebral Artery</descriptorname>
<qualifiername majortopicyn="Y" ui="Q000097">blood</qualifiername>
<qualifiername majortopicyn="Y" ui="Q000235">genetics</qualifiername>
<qualifiername majortopicyn="N" ui="Q000601">surgery</qualifiername>
</meshheading>
<meshheading>
<descriptorname majortopicyn="N" ui="D012333">RNA, Messenger</descriptorname>
<qualifiername majortopicyn="N" ui="Q000097">blood</qualifiername>
<qualifiername majortopicyn="N" ui="Q000235">genetics</qualifiername>
<qualifiername majortopicyn="N" ui="Q000378">metabolism</qualifiername>
</meshheading>
<meshheading>
<descriptorname majortopicyn="N" ui="D051381">Rats</descriptorname>
</meshheading>
<meshheading>
<descriptorname majortopicyn="N" ui="D013997">Time Factors</descriptorname>
</meshheading>
</meshheadinglist>
<coistatement>The authors have declared that no competing interests exist.</coistatement>
</medlinecitation>
<pubmeddata>
<history>
<pubmedpubdate pubstatus="received">
<year>2018</year>
<month>03</month>
<day>08</day>
</pubmedpubdate>
<pubmedpubdate pubstatus="accepted">
<year>2018</year>
<month>10</month>
<day>10</day>
</pubmedpubdate>
<pubmedpubdate pubstatus="entrez">
<year>2018</year>
<month>11</month>
<day>16</day>
<hour>6</hour>
<minute>0</minute>
</pubmedpubdate>
<pubmedpubdate pubstatus="pubmed">
<year>2018</year>
<month>11</month>
<day>16</day>
<hour>6</hour>
<minute>0</minute>
</pubmedpubdate>
<pubmedpubdate pubstatus="medline">
<year>2019</year>
<month>4</month>
<day>10</day>
<hour>6</hour>
<minute>0</minute>
</pubmedpubdate>
</history>
<publicationstatus>epublish</publicationstatus>
<articleidlist>
<articleid idtype="pubmed">30439964</articleid>
<articleid idtype="doi">10.1371/journal.pone.0206321</articleid>
<articleid idtype="pii">PONE-D-18-07138</articleid>
<articleid idtype="pmc">PMC6237327</articleid>
</articleidlist>
<referencelist>
<reference>
<citation>Stroke. 2013 Jun;44(6 Suppl 1):S23-5</citation>
<articleidlist>
<articleid idtype="pubmed">23709718</articleid>
</articleidlist>
</reference>
<reference>
<citation>Lancet. 2004 Mar 6;363(9411):768-74</citation>
<articleidlist>
<articleid idtype="pubmed">15016487</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2000 Aug;31(8):1889-92</citation>
<articleidlist>
<articleid idtype="pubmed">10926952</articleid>
</articleidlist>
</reference>
<reference>
<citation>Genomics. 2014 Sep;104(3):163-9</citation>
<articleidlist>
<articleid idtype="pubmed">25135788</articleid>
</articleidlist>
</reference>
<reference>
<citation>Life Sci. 1999;64(13):1099-108</citation>
<articleidlist>
<articleid idtype="pubmed">10210272</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neuroimmunol. 2012 Aug 15;249(1-2):60-5</citation>
<articleidlist>
<articleid idtype="pubmed">22591946</articleid>
</articleidlist>
</reference>
<reference>
<citation>N Engl J Med. 1995 Dec 14;333(24):1581-7</citation>
<articleidlist>
<articleid idtype="pubmed">7477192</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 1989 Jan;20(1):84-91</citation>
<articleidlist>
<articleid idtype="pubmed">2643202</articleid>
</articleidlist>
</reference>
<reference>
<citation>Neurology. 2000 Dec 12;55(11):1649-55</citation>
<articleidlist>
<articleid idtype="pubmed">11113218</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Clin Neurosci. 2006 Jan;13(1):1-8</citation>
<articleidlist>
<articleid idtype="pubmed">16410192</articleid>
</articleidlist>
</reference>
<reference>
<citation>N Engl J Med. 2008 Sep 25;359(13):1317-29</citation>
<articleidlist>
<articleid idtype="pubmed">18815396</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neuroimmunol. 2007 Mar;184(1-2):53-68</citation>
<articleidlist>
<articleid idtype="pubmed">17188755</articleid>
</articleidlist>
</reference>
<reference>
<citation>Cerebrovasc Dis. 2011;32(6):517-27</citation>
<articleidlist>
<articleid idtype="pubmed">22104408</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neurol. 2014 Mar;261(3):533-45</citation>
<articleidlist>
<articleid idtype="pubmed">24477489</articleid>
</articleidlist>
</reference>
<reference>
<citation>Hum Mol Genet. 2014 Nov 15;23(22):5866-78</citation>
<articleidlist>
<articleid idtype="pubmed">24939910</articleid>
</articleidlist>
</reference>
<reference>
<citation>Chest. 2008 Jun;133(6 Suppl):630S-669S</citation>
<articleidlist>
<articleid idtype="pubmed">18574275</articleid>
</articleidlist>
</reference>
<reference>
<citation>Neurology. 2010 Sep 14;75(11):1009-14</citation>
<articleidlist>
<articleid idtype="pubmed">20837969</articleid>
</articleidlist>
</reference>
<reference>
<citation>Ann Neurol. 2001 Dec;50(6):699-707</citation>
<articleidlist>
<articleid idtype="pubmed">11761467</articleid>
</articleidlist>
</reference>
<reference>
<citation>PLoS One. 2012;7(9):e43830</citation>
<articleidlist>
<articleid idtype="pubmed">23028472</articleid>
</articleidlist>
</reference>
<reference>
<citation>Brain Res Bull. 2003 Aug 15;61(3):261-4</citation>
<articleidlist>
<articleid idtype="pubmed">12909296</articleid>
</articleidlist>
</reference>
<reference>
<citation>PLoS One. 2013 Sep 12;8(9):e72758</citation>
<articleidlist>
<articleid idtype="pubmed">24069157</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Stroke Cerebrovasc Dis. 2009 Jul-Aug;18(4):269-76</citation>
<articleidlist>
<articleid idtype="pubmed">19560680</articleid>
</articleidlist>
</reference>
<reference>
<citation>Circulation. 2005 Jan 18;111(2):212-21</citation>
<articleidlist>
<articleid idtype="pubmed">15630028</articleid>
</articleidlist>
</reference>
<reference>
<citation>Br J Clin Pharmacol. 2012 Aug;74(2):230-40</citation>
<articleidlist>
<articleid idtype="pubmed">22320313</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neurosci Methods. 2006 Sep 15;155(2):285-90</citation>
<articleidlist>
<articleid idtype="pubmed">16513179</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neurol Sci. 2014 Oct 15;345(1-2):202-8</citation>
<articleidlist>
<articleid idtype="pubmed">25109534</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2008 Oct;39(10):2902-9</citation>
<articleidlist>
<articleid idtype="pubmed">18658039</articleid>
</articleidlist>
</reference>
<reference>
<citation>Cerebrovasc Dis. 2009;27(1):37-41</citation>
<articleidlist>
<articleid idtype="pubmed">19018136</articleid>
</articleidlist>
</reference>
<reference>
<citation>Expert Opin Biol Ther. 2001 Mar;1(2):227-37</citation>
<articleidlist>
<articleid idtype="pubmed">11727532</articleid>
</articleidlist>
</reference>
<reference>
<citation>Biomark Insights. 2017 Dec 20;12:1177271917749216</citation>
<articleidlist>
<articleid idtype="pubmed">29308009</articleid>
</articleidlist>
</reference>
<reference>
<citation>Neurology. 2001 Apr 24;56(8):1015-20</citation>
<articleidlist>
<articleid idtype="pubmed">11320171</articleid>
</articleidlist>
</reference>
<reference>
<citation>Neurol Sci. 2014 Dec;35(12):1977-82</citation>
<articleidlist>
<articleid idtype="pubmed">25030125</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2002 Apr;33(4):988-93</citation>
<articleidlist>
<articleid idtype="pubmed">11935049</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2011 Oct;42(10):2838-43</citation>
<articleidlist>
<articleid idtype="pubmed">21852612</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2010 Oct;41(10):2171-7</citation>
<articleidlist>
<articleid idtype="pubmed">20798371</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Cereb Blood Flow Metab. 2006 Aug;26(8):1089-102</citation>
<articleidlist>
<articleid idtype="pubmed">16395289</articleid>
</articleidlist>
</reference>
<reference>
<citation>Nat Protoc. 2009;4(8):1184-91</citation>
<articleidlist>
<articleid idtype="pubmed">19617889</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2009 May;40(5):e380-9</citation>
<articleidlist>
<articleid idtype="pubmed">19286602</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2009 Jan;40(1):77-85</citation>
<articleidlist>
<articleid idtype="pubmed">18948614</articleid>
</articleidlist>
</reference>
<reference>
<citation>Biol Res Nurs. 2015 May;17(3):248-56</citation>
<articleidlist>
<articleid idtype="pubmed">25124890</articleid>
</articleidlist>
</reference>
<reference>
<citation>Hum Exp Toxicol. 2008 Oct;27(10):761-7</citation>
<articleidlist>
<articleid idtype="pubmed">19042962</articleid>
</articleidlist>
</reference>
<reference>
<citation>J Neurol. 2008 May;255(5):723-31</citation>
<articleidlist>
<articleid idtype="pubmed">18465111</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2004 Jan;35(1):57-63</citation>
<articleidlist>
<articleid idtype="pubmed">14671250</articleid>
</articleidlist>
</reference>
<reference>
<citation>Stroke. 2013 Mar;44(3):870-947</citation>
<articleidlist>
<articleid idtype="pubmed">23370205</articleid>
</articleidlist>
</reference>
<reference>
<citation>Circulation. 2012 Jan 3;125(1):188-97</citation>
<articleidlist>
<articleid idtype="pubmed">22215894</articleid>
</articleidlist>
</reference>
<reference>
<citation>Int J Stroke. 2015 Jul;10(5):759-62</citation>
<articleidlist>
<articleid idtype="pubmed">25833105</articleid>
</articleidlist>
</reference>
<reference>
<citation>Proc Natl Acad Sci U S A. 2012 Apr 3;109(14):5475-80</citation>
<articleidlist>
<articleid idtype="pubmed">22431614</articleid>
</articleidlist>
</reference>
<reference>
<citation>Cerebrovasc Dis. 2014;38(1):59-72</citation>
<articleidlist>
<articleid idtype="pubmed">25227260</articleid>
</articleidlist>
</reference>
<reference>
<citation>Pharmacol Rev. 2009 Mar;61(1):62-97</citation>
<articleidlist>
<articleid idtype="pubmed">19293146</articleid>
</articleidlist>
</reference>
</referencelist>
</pubmeddata>
</pubmedarticle>
</pubmedarticleset></body></html>
```



### BeautifulSoup Objects



{:.input_area}
```python
# Our 'fetch_content' variable is a custom BeautifulSoup object
type(fetch_content)
```





{:.output_data_text}
```
bs4.BeautifulSoup
```





{:.input_area}
```python
# We can use some methods to access particular information
fetch_content.find('year').text
```





{:.output_data_text}
```
'2019'
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


{:.output_stream}
```
Current clinical management of patients with glioblastoma.
Treatment-triggered onset and diagnosis of Sheehan syndrome in a multiple myeloma patient.
Phagocytosis-related NADPH oxidase 2 subunit gp91phox contributes to neurodegeneration after repeated systemic challenge with lipopolysaccharides.
Ceasing Antiquated Conceptions: A Telling of the Early and Evolving History of Epilepsy.
Deciphering the neural signature of human cardiovascular regulation.

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


{:.output_stream}
```
CalMatters
RT @mlevinreports: Thread on this story (1/?): Imperial County Superior Court proceeded with eviction cases in apparent violation of state… 

Marco Rogers
Oh. We really still talking about him losing? Like we've taken *any* action to stop voter suppression and election… https://t.co/3iXXJpUOYk 

Jeff Leek
RT @bencasselman: @PatcohenNYT @gillianreporter "But the stark urgency that faces families perilously close to losing their homes, skipping… 


```
