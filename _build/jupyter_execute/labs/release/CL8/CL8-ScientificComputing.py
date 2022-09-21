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

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert pd
assert np


# ## Part I: `pandas`

# ### `pandas`: data
# 
# FiveThirtyEight makes a lot of their data publicly available, so to get some practice using `pandas`, read in a dataframe directly using the `pandas` function `read_csv()`. The input to this function should be the following URL, as a string: https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv. Store, this in the object `df`. 

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


assert isinstance(df, pd.DataFrame) # correct object type
assert df.shape == (106, 4) # correct no. rows & columns


# ### `pandas`: attributes
# 
# `pandas` DataFrame objects have a number of attributes. In the cell below, look up the following information specified in the comment of each cell below.
# 
# Note: each cell should have code that looks like `df.attribute`, where `attribute` is replaced by the attribute that returns the information in the comment

# In[ ]:


# number of rows and columns

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# column names

# YOUR CODE HERE
raise NotImplementedError()


# ### `pandas`: methods
# 
# `pandas` DataFrame objects *also* have a number of helpful methods. In the cell below, look up the following information specified in the comment of each cell below.
# 
# Each cell should have code that looks like `df.method()`, where `method()` is replaced by the method that returns the information in the comment. 
# 
# Note that some methods will also need information within the parentheses following the method name (i.e. `df.method(arg=val)` and others may require you to specify the series on which you want to operate (i.e. `df['series'].method()`)

# In[ ]:


# see the first 5 rows of df

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# determine which different months are included in df

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# determine how many different months are included in df

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# determine how many times each month shows up in df

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# calculate basic summary statistics
# on New registered voters

# YOUR CODE HERE
raise NotImplementedError()


# ## Part II: Code Style & Docuemntation
# 
# Below a fucntion `get_most_common` is provided. 
# 
# For this question:
# 1. Take a look at the code and examples provided in the cells to understand what the function is doing. 
# 2. Consider the code style guidelines discussed in class and edit the code in the cell below to make the code more readable. 
# 3. Add a numpy-style docstring to the function.
# 
# Note: the name and the functionality of the code will *not* change, but the style (parameter/variable naming, spacing, indentation, capitalization, etc.) shuold be improved.

# In[ ]:


# edit code style for this function
def get_most_common(d,c):
  MC=d[c].value_counts()
  a=MC.idxmax();b=MC.max()
  return a,b 

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# execute function
get_most_common(df, 'Jurisdiction')


# In[ ]:


# execute function
# store output in two separate variables
month_common, month_val = get_most_common(df, 'Month')
print(month_common, month_val)


# Provided is a function you've seen before in A3...but here with particularly terrible code style. As above, edit the function for code style and add a numpy-style docstring. Its functionality will not change, but its readability and documentation will.

# In[ ]:


# edit code style for this function
def end_chat(i):
    if 'quit' in i:o='Bye';c=False
    else:o=None;c=True      
    return o, c

# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# execute function
end_chat('I want to quit')


# In[ ]:


# execute function
# store output in two separate variables
output, chat = end_chat('I want to quit')
print(output, chat)


# ## Part III: Code Testing
# 
# After editing the function above, write a test function `test_get_most_common()` that will test the functionality of the `get_most_common` function above. 
# 
# Note: you'll likely need to create a dummy dataframe within the function

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# should pass silently
# when you execute test
test_get_most_common()


# In[ ]:


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


# YOUR CODE HERE
raise NotImplementedError()

