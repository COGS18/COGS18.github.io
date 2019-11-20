---
interact_link: content/materials/18-ScientificComputing.ipynb
download_link: assets/downloads/18-ScientificComputing.ipynb.zip
pdf_link: assets/pdf/18-ScientificComputing.pdf
layout: materials
title: '18-ScientificComputing'
prev_page:
  url: /materials/17-APIs
  title: '17-APIs'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- Exams available in all Coding Lab today
- You should have a good idea about what your project topic by the end of this week

## APIs

**LISC example**
- will work on datahub
- did not work on Monday b/c LISC changed their API
    - I was using an old version
    - I have updated the notes on the website
    - I should have double checked this before class

- Authors did not change the major version of their software
    - Gives me an opportunity to talk about software versioning!

## Software Versioning

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

In Python package development... when `<MAJOR>` == 0, suggests a package in development



{:.input_area}
```python
# see version information
!pip show lisc
```




{:.input_area}
```python
# see version information
import lisc
lisc.__version__
```


## Exam Review

- [Exam #2 (Blank)](https://cogs18.github.io/assets/intro/exams/E2_Fa19.pdf)
- [Exam #2 (Answers)](https://cogs18.github.io/assets/intro/exams/E2_Fa19_answer.pdf)
- [Exam #2 (Code)](https://cogs18.github.io/materials/E2-Answers)

# Scientific Computing

<div class="alert alert-success">
<b>Scientific Computing</b> is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
</div>

## Scientific Python: Scipy Stack

Scipy = Scientific Python

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


### Clicker Question #1

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


### Clicker Question #2

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
