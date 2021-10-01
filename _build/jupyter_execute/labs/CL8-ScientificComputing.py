#!/usr/bin/env python
# coding: utf-8

# # CL8: Scientific Computing
# 
# Welcome to the eighth coding lab!
# 
# This coding lab focuses on getting comfortable working with data using `pandas`, writing code that adheres to good code style principles, and code testing.

# ## Part 0: Setup
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


# ## Part I: `pandas`

# ### `pandas`: data
# 
# FiveThirtyEight makes a lot of their data publicly available, so to get some practice using `pandas`, read in a dataframe directly using the `pandas` function `read_csv()`. The input to this function should be the following URL, as a string: https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv. Store, this in the object `df`. 

# In[3]:


### BEGIN SOLUTION
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv')
### END SOLUTION


# In[5]:


assert isinstance(df, pd.DataFrame) # correct object type
assert df.shape == (106, 4) # correct no. rows & columns


# ### `pandas`: attributes
# 
# `pandas` DataFrame objects have a number of attributes. In the cell below, look up the following information specified in the comment of each cell below.
# 
# Note: each cell should have code that looks like `df.attribute`, where `attribute` is replaced by the attribute that returns the information in the comment

# In[6]:


# number of rows and columns

### BEGIN SOLUTION
df.shape
### END SOLUTION


# In[7]:


# column names

### BEGIN SOLUTION
df.columns
### END SOLUTION


# ### `pandas`: methods
# 
# `pandas` DataFrame objects *also* have a number of helpful methods. In the cell below, look up the following information specified in the comment of each cell below.
# 
# Each cell should have code that looks like `df.method()`, where `method()` is replaced by the method that returns the information in the comment. 
# 
# Note that some methods will also need information within the parentheses following the method name (i.e. `df.method(arg=val)` and others may require you to specify the series on which you want to operate (i.e. `df['series'].method()`)

# In[8]:


# see the first 5 rows of df

### BEGIN SOLUTION
df.head()
### END SOLUTION


# In[9]:


# determine which different months are included in df

### BEGIN SOLUTION
df['Month'].unique()
### END SOLUTION


# In[10]:


# determine how many different months are included in df

### BEGIN SOLUTION
df['Month'].nunique()
### END SOLUTION


# In[11]:


# determine how many times each month shows up in df

### BEGIN SOLUTION
df['Month'].value_counts()
### END SOLUTION


# In[12]:


# calculate basic summary statistics
# on New registered voters

### BEGIN SOLUTION
df['New registered voters'].describe()
### END SOLUTION


# ## Part II: Code Style
# 
# Below a fucntion `get_most_common` is provided. Take a look at the code and examples provided in the cells to understand what the function is doing. Then, consider the code style guidelines discussed in class and edit the code in the cell below to make the code more readable. 
# 
# Note: the name and the functionality of the code will *not* change, but the style (parameter/variable naming, spacing, indentation, capitalization, etc.) shuold be improved.

# In[1]:


# edit code style for this function
def get_most_common(d,c):
  MC=d[c].value_counts()
  a=MC.idxmax();b=MC.max()
  return a,b 

### BEGIN SOLUTION
def get_most_common(df, variable):  # better parameter names
    
    # fix indentation; better spacing around operators; improve variable names
    most_common = df[variable].value_counts() 
    max_label = most_common.idxmax()
    max_value = most_common.max()  # separate out onto two lines
    
    return max_label, max_value 
### END SOLUTION


# In[14]:


# execute function
get_most_common(df, 'Jurisdiction')


# In[15]:


# execute function
# store output in two separate variables
month_common, month_val = get_most_common(df, 'Month')
print(month_common, month_val)


# ## Part III: Code Testing
# 
# After editing the function above, write a test function `test_get_most_common()` that will test the functionality of the function above. 
# 
# Note: you'll likely need to create a dummy dataframe within the function

# In[16]:


### BEGIN SOLUTION
def test_get_most_common():
    # create data frame for testing
    test_df = pd.DataFrame({'col1': ['a', 'b', 'b'], 
                            'col2': [3, 4, 5]}) 
    
    # execute function
    out = get_most_common(test_df, 'col1')
    
    # add assert statements that test function
    assert callable(get_most_common)
    assert isinstance(out, tuple)
    assert out == ('b', 2)
### END SOLUTION


# In[17]:


# should pass silently
# when you execute test
test_get_most_common()


# In[18]:


# call test function
out = test_get_most_common()
# out should store none if passes silently
assert out == None


# ## Part IV: `pytest` (*optional*)
# 
# Let's try out `pytest!`
# 
# 1. Copy the function `get_most_common` to a `functions.py` file (in the same directory as this notebook.)
# 2. Copy the test function `test_get_most_common` to a test file `test_functions.py`. Be sure to add the necessary `import` statement to the top of this file.
# 3. Execute `pytest` in the cell below.

# In[ ]:


### BEGIN SOLUTION
get_ipython().system('pytest test_functions.py')
### END SOLUTION

