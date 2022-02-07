#!/usr/bin/env python
# coding: utf-8

# # Python Code Style
# 
# [PEP8](https://www.python.org/dev/peps/pep-0008/) exists and discusses an in-depth proposal for code style in Python. What is included here should agree with PEP8, but is a shorter and less detailed summary.
# 
# Remember that code style considerations *do NOT affect the functionality* of your code, but *DO affect readability*. It's best to get in good habits now...so you don't have to break them later.

# ## Variables

# - we use a single space around assignment operator `=`
# - we use **snake_case** for variable names (All lowercase, underscores between words)
# - use informative variable names...something that tells you a bit about what's being stored

# - Ideal: `my_variable = 6`
# - Avoid: `MyVariable=6`

# Note: for collections (lists, tuples, dictionaries, etc.), a space after comma separating elements is ideal.
# 
# - Ideal: `my_list = ['a', 'b', 'c']`
# - Avoid: `my_list = ['a','b','c']`

# ## Operators
# 
# - Single space around operators
# - No spaces after leading parentheses or before trailing parentheses

# - Ideal: `calculate = (7 * 4) - 16`
# - Avoid: `calculate=( 7*4 )-16`

# ## Functions
# 
# - Function names should be snake_case 
# - Function names should describe task accomplished by function
# - Separate out logical sections within a function with new lines
# - Arguments should be separated by a comma and a space
# - Default values do NOT need a space around the `=`

# **Good Code Style**

# In[ ]:


def remainder(number, divider=2):
    
    r = number % divider
    
    return r


# **Code Style to Avoid**

# In[ ]:


# could be improved by adding empty lines to separate out logical chunks
def remainder(number,divider=2): # needs space after comma
    r=number%divider # needs spacing around operators
    return r


# ## Conditionals
# 
# - avoid single line statements
# - a single conditional (if + elif + else) has no additional line spaces between statements

# **Good Code Style**

# In[ ]:


value = 16

if value % 2 == 0:
    out = "even"
else:
    out = "odd"


# **Code Style to Avoid**

# In[ ]:


if value%2==0:out="even" # avoid statement on same line as conditional
                         # avoid blank line between if and else
else:out="odd"           # don't forget about spacing around operators!                     


# ## Loops
# 
# - `for`/`while` statement with a colon at the end on first line
# - all code within the loop inside a code block (indented)

# **Good Code Style**

# In[ ]:


number = 5
while number < 0:
    print(number)
    number = number + 1


# **Code Style to Avoid**

# In[ ]:


number=-5
while number<0:print(number);number=number+1 # avoid all on a single line


# ## Classes 
# 
# Coming Soon

# ## Overall Structure

# ### Blank Lines
# 
# - Use 2 blank lines between functions & classes, and 1 between methods
# - Use 1 blank line between segments to indicate logical structure

# **Good Code Style**

# In[ ]:


def my_func():
    
    my_nums = '123'
    output = ''
    
    for num in my_nums: 
        output += str(int(num) + 1)
    
    return output


# **Code Style to Avoid**

# In[ ]:


def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output


# ### Indentation
# 
# Use spaces to indicate indentation levels, with each level defined as 4 spaces. 

# **Good Code Style**

# In[ ]:


if True:
    print('Words.')


# **Code Style to Avoid**

# In[ ]:


# only has 3 spaces
if True:
  print('Words.')


# ### Spacing
# 
# - Put one (and only one) space between each element
# - Index and assignment don't have a space between opening & closing '()' or '[]'

# **Good Code Style**

# In[ ]:


my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]


# **Code Style to Avoid**

# In[ ]:


my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]


# ### Line Length
# 
# - PEP8 recommends that each line be at most 79 characters long

# ### One Statement Per Line
# 
# - While you *can* condense multiple statements into one line, you usually shouldn't.

# **Good Code Style**

# In[ ]:


for i in [1, 2, 3]:
    print(i**2 + i%2)


# **Code Style to Avoid**

# In[ ]:


for i in [1, 2, 3]: print(i**2 + i%2)


# ### Imports
# 
# - Import one module per line
# - Avoid `*` imports
# - Use the import order: standard library; 3rd party packages; local / custom code

# **Good Code Style**

# In[ ]:


import os
import sys

import numpy as np


# **Code Style to Avoid**

# In[ ]:


from numpy import *

import os, sys


# ## Naming

# ### Valid Names
# 
# - Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

# **Good Code Style**

# In[ ]:


n_filters = 12
n_freqs = 24


# **Code Style to Avoid**

# In[ ]:


a = 12
b = 24


# ### Naming Style
# 
# - CapWords (leading capitals, no separation) for Classes
# - snake_case (all lowercase, underscore separator) for variables, functions, and modules

# **Good Code Style**

# In[ ]:


def my_func():
    pass


class MyClass():
    def __init__():
        pass


# **Code Style to Avoid**

# In[ ]:


def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass


# ## String Quotes

# In Python, single-quoted strings and double-quoted strings are the same. 
# 
# This PEP does not make a recommendation for this. **Pick a rule and stick to it.** 
# 
# When a string contains single or double quote characters: use the other one to avoid backslashes in the string. It improves readability.
# 
# 

# **Good Code Style**

# In[ ]:


my_string = "Prof's Project"


# **Code Style to Avoid**

# In[ ]:


my_string = 'Prof\'s Project'

