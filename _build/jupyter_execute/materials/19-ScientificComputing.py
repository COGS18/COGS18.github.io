**Course Announcements**

**Due Dates:**
- **A5** now due Friday of week 10 12/11 (11:59 PM) 

**Notes**
- No more coding labs to turn in! But, coding lab is still happening and is a great place for making project progress!
- Extra Credit opportunities:
    - Please fill out your **[CAPEs](cape.ucsd.edu)** (+0.5% to grades if >= 85% fill out)
        - Please fill out for instructional staff as well!
        - Feedback is really, really helpful!
    - Go above and beyond on **final project** (explain in notebook; up to 4% _on final project_)
    - Put final project on **GitHub** (1% _on final project_)
    - **Post-course survey** (not yet released; +0.25% to final grade)


**Modules vs Scripts**

- Modules: store code (typically functions and classes) that you want to be able to use (`import`) elsewhere
- Scripts: store code that you want to run from top to bottom to accomplish a task; may or may not `import` code from elsewhere at the top

**Clicker Question A**

Your final project is a chatbot that will discuss sports with you. How would you implement this?

- A) Jupyter Notebook only
- B) module only 
- C) module + Jupyter Notebook
- D) script only
- E) script + Jupyter Notebook

**Clicker Question B**

Your final project is a basic data analysis where you read a file in, create a few plots, and do a basic statistical analysis. How would you implement this?

- A) Jupyter Notebook only
- B) module only 
- C) module + Jupyter Notebook
- D) script only
- E) script + Jupyter Notebook

# Scientific Computing

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

import numpy as np

# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr1

# lists of lists don't store dimensionality well
[[1, 2], [3, 4]] 

#### Indexing Arrays

type(arr1)

# Check out an array of data
arr1

# Check the shape of the array
arr1.shape

# Index into a numpy array
arr1[0, 0]

Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

#### Notes on Arrays

# arrays are most helpful when they
# have the same length in each list
np.array([[1, 2, 3, 4], [2, 3, 4]])

# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])

#### Working with Arrays

(Things you can't do with lists)

arr1

arr2

# Add arrays together
arr1 + arr2

# Matrix mutliplication
arr1 * arr2

#### A brief aside: `zip()`

`zip()` takes two iterables (things you can loop over) and loop over them together.

for a, b in zip([1,2], ['a','b']):
    print(a, b)

#### Clicker Question #1

Given the following code, what will it print out?

data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0, :], data[1, :]):
    output.append(d1 + d2)

print(output)

- A) [1, 2, 3, 4]
- B) [1, 2, 3, 4, 5, 6, 7, 8]
- C) [6, 8, 10, 12]
- D) [10, 26]
- E) [36]

Note that if you find yourself looping over arrays...there is probably a better way.

a = np.arange(10)
a
np.where(a < 4)

data

data.sum()

np.sum?

np.where?

data.sum(axis=0)

## Heterogenous Data

- have continuous (numeric) and categorical (discrete) data
- different data types need to be stored
- uses a DataFrame object (think: spreadsheet)
- allows for column and row labels

### pandas

import pandas as pd

# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
d3 = {'Subj_ID': '003', 'score': 18, 'group' : 1, 'condition': 'perception'}

# Create a dataframe 
df = pd.DataFrame([d1, d2, d3], [0, 1, 2])

# Check out the dataframe
df

# You can index in pandas
df['condition']

# You can index in pandas
df.loc[0,:]
df.loc[0,'condition']

#### Working with DataFrames

There are *a lot* of functions within `pandas`. The general syntax is `df.function()` where the `function()` operates on the dataframe `df`.

# calculate summary statistics
df.describe()

# Take the average of all numeric columns
df.mean()

df['condition'].value_counts()

# breakdown of how many of each category there are
val_counts = df['condition'].value_counts()
val_counts

type(val_counts)

# what's the category that shows up the most 
val_counts.idxmax()

# what's the count of the value that shows up the most
val_counts.max()

#### Clicker Question #2

Comparing them to standard library Python types, which is the best mapping for these new data types?

- A) DataFrames are like lists, arrays are like tuples
- B) DataFrames and arrays are like lists
- C) DataFrames are like tuples, arrays are like lists
- D) DataFrames and arrays are like dictionaries
- E) Dataframes are like dictionaries, arrays are like lists

## Plotting

%matplotlib inline

import matplotlib.pyplot as plt

# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])

# Plot the data
plt.plot(dat)
# add xlabel
plt.xlabel('label')

- can change plot type
- _lots_ of customizations possible

## Analysis

- `scipy` - statistical analysis
- `sklearn` - machine learning

import scipy as sp
from scipy import stats

# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)

### Analysis - Plotting the Data

# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);

### Analysis - Statistical Comparisons

# Statistically compare the two distributions
stats.ttest_ind(d1, d2)

## COGS108: Data Science in Practice

<div class="alert alert-info">
If you are interested in data science and scientific computing in Python, consider taking <b>COGS108</b> : <a>https://github.com/COGS108/</a>.
</div>