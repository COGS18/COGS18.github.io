#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL7** due tonight (be sure your .py files are in the `CL7_COGS18_WI22/` directory)
# - **CL8** due *next* Wed 3/9
# - **A5** due *next* Fri 3/11 (now available)
# - **Final exam/project** due Mon 3/14
# 
# Notes:
# - Please fill out your CAPEs! (+1% to everyone's grade if >=85% of the class completes)
# - **E2** scores released (0.25pt curve)

# **Q&A**
# 
# Q: when finals are done, how do i download the juptyter notebook? i want to be able to refer to my notes in the future. once downloaded, do i access it through anaconda?  
# A: I will post a how to get all your materials off of datahub at the end of the quarter to campuswire. And yes, notebooks can be opened with Jupyter...which is part of the anaconda installation.
# 
# 
# Q: I am very confused about how to create the module "remote". Every time I tried to use it, it would say that "remote" did not exist.   
# A: 1) Check the location. Ensure that `remote.py` is in the same directory as the notebook you're trying to read it in from; 2) Restart your kernel and try again
# 
# Q: I still don't completely understand scripts. I understand that they run the entire code, but in what context would we use them? It seems like we can simply call on a particular function similar to how modules are imported and called, so what is the purpose of running a script.   
# A: Say there's a bunch of code you need to run...but really only care about the final output. A perfect time for a script! You can store the code in the script and then just execute it, which would display the output you care about.
# 
# Q: From what I understand, a text-file is unable to run any codes so I was wondering do people usually create, run and try those classes and functions in a notebook before copy-pasting into the text files?  
# A: In this course, yes, students often write in notebooks first because they're most comfortable there. Other people use what's known as an "IDE" to write and test their code. Spyder is one of these that is downloaded with anaconda. NOT required for this class, but giving you something to google/be aware of.
# 
# Q: The most confusing part was trying to understand the standard library and know when it's useful to import modules like there is just so many out there, I wouldn't know when to import unless I was being told to do so.  
# A: And that's ok in the beginning! One thing to keep in mind is that if you're writing code for a task that seems "common" ...there may already be a module/function for that so you can google to see if it exists. Alternatively, it can be helpful just to scan [this](https://docs.python.org/3/library/) to see what's available in the standard library.
# 
# Q: Are there modules for data analysis that we can use for any type of data manipulation?  
# A: Yes! we're discussing a few of the most popular today!
# 
# Q: When should we make script and when should we choose module file?  
# A: Module to store functions/classes you want to import later. Scripts to actually execute code.
# 
# Q: when you create a remote.py through terminal why you type "touch" before you type "remote.py"?  
# A: `touch` is the shell command to "create a file." So, before the filename you want to create you need `touch`.

# # Scientific Computing

# <div class="alert alert-success">
# <b>Scientific Computing</b> is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
# </div>

# ## Scientific Python: Scipy Stack
# 
# Scipy = Scientific Python
# 
# - `scipy`
# - `numpy`
# - `pandas`
# - Data Analysis in Python

# <div class="alert alert-success">
# <b><code>Scipy</code></b> is an <i>ecosystem</i>, including a collection of open-source packages for scientific computing in Python.
# </div>

# A 'family' of packages that all work well together to do scientific computing.
# 
# Not made by the same people who manage the standard library.

# **Packages must be installed before you can use them.** Install once. Import as many times as you want.
# 
# The packages we're using today have 1) already been installed for you on datahub and 2) are part of the Anaconda distribution.
# 
# However, for your final project, you may want to install additional packages. To do so: `pip install --user package` (where you replace `package` with the package to be installed.

# ## Homogenous Data
# 
# - for example: store data of the same type (i.e. all numerics)
# - recordings of values from experimental participants
# - heights or quantitative information from survey data

# Lists are a start, and lists of lists are possible.
# 
# But, they can get nightmareish.
# 
# So we use arrays.

# ### `numpy`
# 
# **`numpy`** - stands for numerical python

# **arrays** - work with arrays (matrices)
# 
# Allow you to efficiently operate on arrays (linear algebra, matrix operations, etc.)

# In[1]:


import numpy as np


# In[2]:


# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])


# In[5]:


arr2


# In[6]:


# lists of lists don't store dimensionality well
[[1, 2], [3, 4]] 


# #### Arrays: attributes, methods, & indexing

# In[7]:


# Check out an array of data
arr1


# `numpy` arrays are an object type...so they have associated attributes (below) and methods (we'll get to these in a second)!

# In[8]:


# Check the shape of the array
arr1.shape


# In[9]:


# Index into a numpy array
arr1[0, 0]


# In[11]:


arr1[1,0]


# Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

# #### Notes on Arrays

# In[12]:


# arrays are most helpful when they
# have the same length in each list
np.array([[1, 2, 3, 4], [2, 3, 4]])


# In[13]:


# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])


# #### Working with Arrays
# 
# (Things you can't do with lists)

# In[14]:


# Add arrays together
arr1 + arr2


# In[15]:


# Matrix mutliplication
arr1 * arr2


# #### A brief aside: `zip()`

# `zip()` takes two iterables (things you can loop over) and loop over them together.

# In[16]:


for a, b in zip([1,2], ['a','b']):
    print(a, b)


# #### Clicker Question #1
# 
# Given the following code, what will it print out?

# In[19]:


data[1, :]


# In[17]:


data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0, :], data[1, :]):
    output.append(d1 + d2)

print(output)


# - A) [1, 2, 3, 4]
# - B) [1, 2, 3, 4, 5, 6, 7, 8]
# - C) [6, 8, 10, 12]
# - D) [10, 26]
# - E) [36]

# Note that if you find yourself looping over arrays...there is probably a better way.

# In[20]:


data


# In[21]:


# sum method
# by default sums all values in array
data.sum()


# In[22]:


# sum method
# has an axis parameter
# axis=0 sums across columns
data.sum(axis=0)


# In[23]:


# typecasting to a different variable type
out_list = data.sum(axis=0).tolist()
print(out_list)
type(out_list)


# What if you wanted to find the max value in an array...there's a method for that!

# In[24]:


# find max value in array
max_val = data.max()
max_val


# But what if you wanted to know not what the max value was...but where in your original array that value was found. 
# 
# There are also *functions* in `numpy` that operate on arrays. 

# In[25]:


# see documentation for np.where()
get_ipython().run_line_magic('pinfo', 'np.where')


# In[26]:


data


# In[27]:


max_val


# In[28]:


# find position in array with max value
out = np.where(data == max_val)
out


# In[29]:


# check to be sure
data[1,3]


# ## Heterogenous Data
# 
# - have continuous (numeric) and categorical (discrete) data
# - different data types need to be stored
# - uses a DataFrame object (think: spreadsheet)
# - allows for column and row labels

# ### pandas

# Pandas is Python library for managing heterogenous data.
# 
# At it's core, Pandas is built around the **DataFrame** object, which is:
# - a data structure for labeled rows and columns of data
# - associated methods and utilities for working with data.
# - each column contains a `pandas` **Series**

# In[30]:


import pandas as pd


# In[31]:


# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
d3 = {'Subj_ID': '003', 'score': 18, 'group' : 1, 'condition': 'perception'}


# In[32]:


# Create a dataframe 
df = pd.DataFrame([d1, d2, d3], [0, 1, 2])


# In[33]:


# Check out the dataframe
df


# In[34]:


# You can index in pandas
# columns store information in series
df['condition']


# In[41]:


# You can index in pandas
# loc specifies row, column position
df.loc[0,'condition'] # gets single value
df.loc[0,:] # gets whole row


# In[40]:


# to use iloc, which gets you a specific value 
# based on indices/location
df.iloc[0,2] # indexes based on location only


# In[42]:


### attribute of df object
# row, columns
df.shape


# In[43]:


# how many rows there are in a series/df
df.shape[0] # len(df) would also work


# #### Working with DataFrames
# 
# There are *a lot* of functions and methods within `pandas`. The general syntax is `df.method()` where the `method()` operates directly on the dataframe `df`.

# In[44]:


# calculate summary statistics
df.describe()


# In[45]:


df


# In[46]:


# Take the average of a specific column
df['score'].mean()


# In[47]:


# edit values within a column and replace original values
df['Subj_ID'] = df['Subj_ID'].replace('00', '000', regex=True)
df['Subj_ID']


# In[56]:


df['score'].astype(int)


# In[48]:


df['score'].astype(float)


# In[49]:


df


# In[50]:


# specify the type of a variable in a column
df['score'] = df['score'].astype(float)
df['score']


# In[51]:


# breakdown of how many of each category there are
val_counts = df['condition'].value_counts()
val_counts


# In[52]:


# which unique values are there in condition? 
df['condition'].unique()


# In[53]:


# how many unique values are there
df['condition'].nunique()


# In[54]:


# what's the category that shows up the most 
val_counts.idxmax()


# In[55]:


# what's the count of the value that shows up the most
val_counts.max()


# #### Clicker Question #2
# 
# Comparing them to standard library Python types, which is the best mapping for these new data types?
# 
# - A) DataFrames are like lists, arrays are like tuples
# - B) DataFrames and arrays are like lists
# - C) DataFrames are like tuples, arrays are like lists
# - D) DataFrames and arrays are like dictionaries
# - E) Dataframes are like dictionaries, arrays are like lists

# ## Plotting

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# In[ ]:


# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])


# In[ ]:


# Plot the data
plt.plot(dat);


# - can change plot type
# - _lots_ of customizations possible

# ## Analysis
# 
# - `scipy` - statistical analysis
# - `sklearn` - machine learning

# In[ ]:


import scipy as sp
from scipy import stats


# In[ ]:


# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)


# ### Analysis - Plotting the Data

# In[ ]:


# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);


# ### Analysis - Statistical Comparisons

# In[ ]:


# Statistically compare the two distributions
stats.ttest_ind(d1, d2)


# ## COGS 108: Data Science in Practice

# <div class="alert alert-info">
# If you are interested in data science and scientific computing in Python, consider taking <b>COGS 108</b> : <a>https://github.com/COGS108/</a>.
# </div>
