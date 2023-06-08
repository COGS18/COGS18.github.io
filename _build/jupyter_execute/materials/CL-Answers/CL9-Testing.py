#!/usr/bin/env python
# coding: utf-8

# # CL9: Code Projects
# 
# Welcome to the ninth coding lab!
# 
# This coding lab focuses on documentation, writing code that adheres to good code style principles, and code testing.

# ## Part 0: Setup 
# 
# For testing out this first question, we'll use the same dataset from the previous lab, which you'll have to read in using `pandas`. Run the cell below before proceeding. 

# In[ ]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/voter-registration/new-voter-registrations.csv')


# ## Part I: Code Style & Docuemntation
# 
# For this first question... a function `get_most_common` is provided:
# 
# ```python
# # edit code style for this function
# def get_most_common(d,c):
#   MC=d[c].value_counts()
#   a=MC.idxmax();b=MC.max()
#   return a,b 
# 
# ```
# 
# For this question:
# 1. Take a look at the code and examples provided in the cells to understand what the function is doing. 
# 2. Consider the code style guidelines discussed in class and edit the code in the cell below to make the code more readable. 
# 3. Add a numpy-style docstring to the function.
# 
# Note: the name and the functionality of the code will *not* change, but the style (parameter/variable naming, spacing, indentation, capitalization, etc.) should be improved.

# In[ ]:


### BEGIN SOLUTION
def get_most_common(df, variable):  # better parameter names
    
    """ 
    Identify the most common category that shoes up in the column of the DataFrame
    specified on input as wel as how many times that value shows up.
    
    Parameters
    ----------
    df : DataFrame
        The pandas DataFrame containing the column to be summarized
    variable : str
        The column in the pandas DataFrame to be summarized
        
    Returns
    -------
    max_label : str
        The category/label that shows up most frequently in the column interrogated
    max_value : int
        The number of times the `max_label` shows up
    """
    
    # fix indentation; better spacing around operators; improve variable names
    most_common = df[variable].value_counts() 
    max_label = most_common.idxmax()
    max_value = most_common.max()  # separate out onto two lines
    
    return max_label, max_value 
### END SOLUTION


# In[ ]:


# execute function
get_most_common(df, 'Jurisdiction')


# In[ ]:


# execute function
# store output in two separate variables
month_common, month_val = get_most_common(df, 'Month')
print(month_common, month_val)


# Provided is a function you've seen before in A3:
# 
# ```python
# # edit code style for this function
# def end_chat(i):
#     if 'quit' in i:o='Bye';c=False
#     else:o=None;c=True      
#     return o, c
# ```
# 
# 
# ...but here, it's got particularly terrible code style. As above, edit the function for code style and add a numpy-style docstring. Its functionality will not change, but its readability and documentation will.

# In[ ]:


### BEGIN SOLUTION
def end_chat(input_string):  # better parameter name
    
    """
    Determine if the word 'quit' is in function's input
    
    Parameters
    ----------
    input_string : str
        The string to be analyzed to see if it contains the word 'quit'
        
    
    Returns
    -------
    output : str or None
        Function returns the string 'Bye' if 'quit' is in the input_string and None otherwise
    chat : bool
        Function returns False if 'quit' is in the input_string and True otherwise; controls if chat should continue
    
    """
    
    # fix indentation; better spacing around operators; improve variable names
    if 'quit' in input_string:
        output = 'Bye'
        chat = False # separate out onto two lines
    else:
        output = None
        chat = True
    
    return output, chat 
### END SOLUTION


# In[ ]:


# execute function
end_chat('I want to quit')


# In[ ]:


# execute function
# store output in two separate variables
output, chat = end_chat('I want to quit')
print(output, chat)


# ## Part II: Code Testing
# 
# After editing the function above, write a test function `test_get_most_common()` that will test the functionality of the `get_most_common` function above. 
# 
# Note: you'll likely need to create a dummy dataframe within the function

# In[ ]:


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


# In[ ]:


# should pass silently
# when you execute test
test_get_most_common()


# In[ ]:


# call test function
out = test_get_most_common()
# out should store none if passes silently
assert out == None


# ## Part III: `pytest` (*optional*)
# 
# Let's try out `pytest!`
# 
# 1. Copy the function `get_most_common` to a `functions.py` file (in the same directory as this notebook.)
# 2. Copy the test function `test_get_most_common` to a test file `test_functions.py`. Be sure to add the necessary `import` statement to the top of this file.
# 3. Execute `pytest` in the cell below.

# In[ ]:


### BEGIN SOLUTION
# executing this should show passing tests 
# once the above steps are carried out
# assumes test_functions.py is in same directory
# as this lab
get_ipython().system('pytest test_functions.py')
### END SOLUTION

