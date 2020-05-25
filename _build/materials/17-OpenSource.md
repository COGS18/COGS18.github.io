---
interact_link: content/materials/17-OpenSource.ipynb
download_link: assets/downloads/17-OpenSource.ipynb.zip
pdf_link: assets/pdf/17-OpenSource.pdf
layout: materials
title: '17-OpenSource'
prev_page:
  url: /materials/16-CommandLine
  title: '16-CommandLine'
next_page:
  url: /materials/18-Documentation
  title: '18-Documentation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<center><img src="img/Explore the world!.png" width="550px"></center>


## Course Announcements

- CL7 score posted (Drop lowest two - that's your final CL score)
- Brief Discussions:
    - COGS18: Letter grade vs. P/NP
    - A5 Chat 

### Projects: Datahub vs Locally
- Datahub: your current comfort level
- Anaconda (or Python on your computer): additional flexibility
- Project Template: a good place to start

# Open Source & Scientific Computing

# Open Source

- Open Source Software
- History of Python
- Zen of Python
- Versioning
- GitHub
- PyPI, PIP, Conda

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

### Zen of Python

- 20 guidelines (the 20th is missing)
- sometimes contradictory in favor of flexibility



{:.input_area}
```python
# a hidden easter egg
import this
```


{:.output_stream}
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

Tim Peters -- the author of the Zen of Python -- is a software developer and was a major contributor to the Python Programming language.

### Beautiful is better than ugly. Readability counts.

- readability prioritized
- Python prides itself on ease to work with
- code is read more often than it's written
- documentation matters.

### Simple is better than complex. Complex is better than complicated.

- There's more than one approach to solving a problem
- Something that is overly-complicated should be reconsidered - a different approach? A simpler solution?

### There should be one - and preferably only one - obvious way to do it

- A slight shot at other programming languages
- With more than one way, reading is harder and writing is easier. Flexibility not worth it to Pythonistas.

### Namespaces are one honking great idea - let's do more of those

- Namespaces and global/local scopes prevent names in one module/scope from conflicting with names in another
- Namespaces are for avoiding naming conflicts (_not_ unecessary categorization - b/c flat is better than nested)

### A Final Note on The Zen of Python

The Zen of Python is a set of guidelines for Python.

There are arguments for and against any of these.

Different languages take different approaches.

Language Wars are stupid.

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

<div class="alert alert-info">
If you create a GitHub account and add your final project to a public repository on GitHub, you will receive extra credit on your final project.
</div>

But...what if you just want to _use_ what's available to you in Python...

### PyPI: Python Package Index

<div class="alert alert-success">
The Python Package Index is a software repository for the Python programming language.
</div>

Where packages are hosted. You can search and use packages from Python.

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


#### A brief aside: `zip()`

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
for d1, d2 in zip(data[0, :], data[1, :]):
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
