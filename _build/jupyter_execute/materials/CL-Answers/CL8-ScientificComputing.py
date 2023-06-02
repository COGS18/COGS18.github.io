#!/usr/bin/env python
# coding: utf-8

# # CL8: Scientific Computing
# 
# Welcome to the eighth coding lab!
# 
# This coding lab focuses on getting comfortable working with data using `pandas`, writing code that adheres to good code style principles, and code testing.

# ## Part 1: Setup
# 
# Data wrangling often requires additional functionality outside what's included in Python by default. For this, we'll import other functionality from helpful packages.

# **Import the following packages using their common shortened name found in parentheses:**
# 
# * `numpy` (`np`)
# * `pandas` (`pd`)

# In[1]:


### BEGIN SOLUTION
import numpy as np
import pandas as pd
### END SOLUTION


# In[2]:


assert pd
assert np


# ## Part II: Module Files
# 
# First, in the notebook below, do the following:
# 
# - Write at least one new Class
#     - Make sure there is at least one method in the class that returns something/prints something out
# - Write two new functions, that do something with instances of your new class(es)
#     - For example, take a list of custom objects, and call a method on each one

# Classes here:

# In[ ]:


### BEGIN SOLUTION
# Classes here
class Noodles():
    def __init__(self, size = 'large', available = 'Yes'):
        self.size = size
        self.available = available
        
    def order_to_go(self):
        if self.available == None:
            out = "I'm sorry, but we aren't taking to-go orders right now."
        if self.available == 'Yes':
             out = "I'll have your order ready in 20 minutes"
        return out
### END SOLUTION


# Functions here:

# In[ ]:


### BEGIN SOLUTION
# new functions here
def eating(Noodles):
    if Noodles.available == 'Yes':
        print('Itadakimasu') # means "I will receive"; something you say before eating
        out = 'Slurp slurp slurp, delicious!'
    else:
        out = 'Quarantine can be rough. It be like that sometimes.'
    return out

def soup(Noodles):
    if Noodles.size == 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "I really shouldn't... There's too much sodium."
    if Noodles.size != 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "You only live once! Slurp slurp slurp!"
    return out
### END SOLUTION


# Next, we are going to move this code to an external file - a Python module file.
# 
# - Open a new text file, from the Jupyter server page
# - Copy your classes and functions into that file
# - Save that file ***in the same folder/directory where this notebook is located***, with some name that you give it, and a '.py' extension.
# - Now, `import` the classes and functions from that file into the notebook, and check that you can use them. 

# In[ ]:


### BEGIN SOLUTION
# save the above in crave.py
import cravings as crave

tonkotsu = crave.Noodles()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))
### END SOLUTION


# ## Part III: `pandas`

# ### `pandas`: data
# 
# FiveThirtyEight makes a lot of their data publicly available, so to get some practice using `pandas`, read in a dataframe directly using the `pandas` function `read_csv()`. The input to this function should be the following URL, as a string: https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv. Store, this in the object `df`. 

# In[3]:


### BEGIN SOLUTION
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv')
### END SOLUTION


# In[4]:


assert isinstance(df, pd.DataFrame) # correct object type
assert df.shape == (106, 4) # correct no. rows & columns


# ### `pandas`: attributes
# 
# `pandas` DataFrame objects have a number of attributes. In the cell below, look up the following information specified by the text provided above each code cell.
# 
# Note: each cell should have code that looks like `df.attribute`, where `attribute` is replaced by the attribute that returns the information in the comment

# Calculate the number of rows and columns:

# In[5]:


### BEGIN SOLUTION
df.shape
### END SOLUTION


# Column names:

# In[6]:


### BEGIN SOLUTION
df.columns
### END SOLUTION


# ### `pandas`: methods
# 
# `pandas` DataFrame objects *also* have a number of helpful methods. In the cell below, look up the following information specified in cell above each code cell.
# 
# Each cell should have code that looks like `df.method()`, where `method()` is replaced by the method that returns the information in the comment. 
# 
# Note that some methods will also need information within the parentheses following the method name (i.e. `df.method(arg=val)` and others may require you to specify the series on which you want to operate (i.e. `df['series'].method()`)

# see the first 5 rows of `df`:

# In[7]:


### BEGIN SOLUTION
df.head()
### END SOLUTION


# determine which different months are included in `df`:

# In[8]:


### BEGIN SOLUTION
df['Month'].unique()
### END SOLUTION


# determine how many different months are included in `df`:

# In[9]:


### BEGIN SOLUTION
df['Month'].nunique()
### END SOLUTION


# determine how many times each month shows up in `df`:

# In[10]:


### BEGIN SOLUTION
df['Month'].value_counts()
### END SOLUTION


# calculate basic summary statistics on New registered voters:

# In[11]:


### BEGIN SOLUTION
df['New registered voters'].describe()
### END SOLUTION

