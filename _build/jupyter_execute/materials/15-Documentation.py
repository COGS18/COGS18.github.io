#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL9** due *next* Wednesday (testing, documenting, refactoring)
# - **A5** due *next* Friday
# - **Final Exam/Final Project** due Tuesday of finals week (6/13; 11:59 PM)
# 
# Note: Error in CL7 grading was fixed just before class.

# **Exam Discussion**
# 
# - Scores & [Answer Keys](https://cogs18.github.io/materials/ExamPrep/E2_COGS18_SP23-Answers.html) Posted
# - In-class: 8.3/10 (83%; with curve)
#     - Discuss: Q12; Q13
# - Take-home: 2.11/2.5 (84%) 
#     - If you lost *a lot* of credit for a *small* mistake, I'm happy to take a closer look via regrade
# 
# Questions?

# # Code Style & Documentation
# 
# - readability
# - code style
# - PEP8
# - comments
# - documentation
# - linters
# - versioning

# ## Code Readability (API)

# "Code is more often read than written" - Guido van Rossum

# So: code should be written to be readable by humans.

# Note: one of those humans is future you.

# ## The Zen of Python

# In[1]:


import this


# ### Writing Readable Code

# So how do we write good code for humans?
# 
# - Use good structure
# - Use good naming
# - Use code comments and include documentation

# ### Good Structure
# 
# If you design your program using separate functions for each task, avoid copying + pasting (functions and loops instead), and consider structure beforehand, you'll be set up for success

# ### Good Naming
# 
# Clear names are for humans. The computer doesn't care, but you and others reading your code do.

# ### Code comments & Documentation
# 
# Helpful comments and documentation take your code to the next level. The final piece in the trifecta of readable code! 

# Good code has good documentation - but code documentation should _not_ be used to try and fix unclear names, or bad structure. 
# 
# Rather, comments should add any additional context and information that helps explain what the code is, how it works, and why it works that way. 

# These will all be components of your final project grade.

# #### Class Question #1
# 
# What does the following code do?

# In[2]:


def ff(jj):
    oo = list(); jj = list(jj) 
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
ff('Hello World.')


# - A) Returns unicode code points, as a list
# - B) Encodes a string as a cypher, returning a string of alphabetical characters
# - C) Returns unicode code points, as a string
# - D) Encodes inputs alphabetical characters, returned as a list
# - E) This code will fail

# Improvement Considerations:
# - Structural considerations: indentations & spacing
# - Improved naming: functions & variables
# - Add Comments within code

# In[3]:


def return_unicode(input_list):
    string = list() #[]
    input_list = list(input_list)
      
    for character in input_list: 
        string.append(str(ord(character)))
        
    output_string = '+'.join(string)
    return output_string

return_unicode('Hello World.')


# - A) Returns unicode code points, as a list
# - B) Encodes a string as a cypher, returning a string of alphabetical characters
# - C) Returns unicode code points, as a string
# - D) Encodes inputs alphabetical characters, returned as a list
# - E) This code will fail

# Improvement Considerations:
# - Structural considerations: indentations & spacing
# - Improved naming: functions & variables
# - Add Comments within code
# - **Proper Documentation!**

# In[ ]:


# Let's fix this code!
def convert_to_unicode(input_string):
    """Converts an input string into a string containing the unicode code points.
    
    Parameters
    ----------
    input_string : string
        String to convert to code points
        
    Returns
    -------
    output_string : string
        String containing the code points for the input string.
    """ 
    
    output = list()
    # Converting a string to a list, to split up the characters of the string
    input_list = list(input_string)
    
    for character in input_list:   
        temp = ord(character)
        output.append(temp)

    output_string = '+'.join(output)
        
    return output_string


# ## Code Style

# Or: How to be Pythonic

# Reasons to be Pythonic:
# - user friendly for humans
# - extra work up-front on the developers (pays off on the long run)
# - best to practice this early on (I promise!)

# ### Style Guides

# <div class="alert alert-success">
# Coding style refers to a set of conventions for how to write good code. 
# </div>

# Consistency is the goal. Rules help us achieve consistency.

# Much of this will apply to other programming languages, so it's good to learn...regardless of language.
# 
# Some of these Code Style notes will be more specific to Python, however.

# #### Python Enhancement Proposals (PEPs)

# <div class="alert alert-success">
# Python PEPs are proposals for how something should be / work in the Python programming language. 
# </div>

# These are written by the people responsible for the Python Programming language.

# PEP are voted on before incorporation.

# #### PEP8

# <div class="alert alert-info">
# <b><a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a></b> is an accepted proposal that outlines the style guide for Python.
# </div>

# Defines the style guide for Pythonistas (people who code in Python).

# ## Code Style: Structure
# 
# - blank lines
# - indentaion
# - spacing 
# - length <- NEW
# - imports <- NEW

# ### Blank Lines
# 
# - Use 2 blank lines between functions & classes, and 1 between methods
# - Use 1 blank line between segments to indicate logical structure

# ### Indentation
# 
# Use spaces to indicate indentation levels, with each level defined as 4 spaces. 

# ### Spacing
# 
# - Put one (and only one) space between each element
# - Index and assignment don't have a space between opening & closing '()' or '[]'

# ### Line Length (NEW)
# 
# - PEP8 recommends that each line be at most 79 characters long

# Computers used to require this.
# 
# But, super long lines are hard to read at a glance.

# ### Multi-Line

# In[ ]:


my_long_list = [1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]


# In[ ]:


# Note: you can explicitly indicate a new line with '\'
my_string = 'Python is ' +             'a pretty great language.'


# ### One Statement Per Line (NEW-ish)
# 
# - While you *can* condense multiple statements into one line, you usually shouldn't.

# In[4]:


# Badness
for i in [1, 2, 3]: print(i**2 + i%2)


# In[5]:


# Goodness
for i in [1, 2, 3]:
    print(i**2 + i%2)


# ### Imports
# 
# - Import one module per line
# - Avoid `*` imports
# - Use the import order: standard library; 3rd party packages; local / custom code

# In[ ]:


# Badness
from numpy import *

import os, sys


# In[6]:


# Goodness
import os
import sys
import numpy as np


# Note: If you don't know how to import a local/custom module, figure that out this week in Coding Lab or office hours.

# ## Specific Guidelines - Naming (review)

# ### Valid Names
# 
# - Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

# ### Naming Style
# 
# - CapWords (leading capitals, no separation) for Classes
# - snake_case (all lowercase, underscore separator) for variables, functions, and modules

# ## Code Documentation

# <div class="alert alert-success">
# Code documentation is text that accompanies and/or is embedded within a software project, that explains what the code is and how to use it. 
# </div>

# Stuff written for humans in human language to help the humans.

# ### Code Comments vs. Documentation

# #### Comments

# Comments are string literals written directly in the code, typically directed at developers - people reading and potentially writing the code. 

# #### Documentation

# Documentation are descriptions and guides written for code users. 

# ### Inline Comments

# Code comments should use `#`, and be written at the same indentation level of the code it describes. 

# How to use comments:
# - Generally:
#     - focus on the *how* and *why*, over literal 'what is the code'
#     - explain any context needed to understand the task at hand
#     - give a broad overview of what approach you are taking to perform the task
#     - if you're using any unusual approaches, explain what they are, and why you're using them
# - Comments need to be maintained - make sure to keep them up to date

# #### Bad Comments

# In[ ]:


# This is a loop that iterates over elements in a list
for element in list_of_elements:
    pass


# #### Good Comments

# In[ ]:


# Because of X, we will use approach Y to do Z
for element in list_of_elements:
    # comment for code block
    pass


# ## Code Style: Comments

# Out-of-date comments are worse than no comments at all.
# 
# Keep your comments up-to-date.

# #### Block comments
# - apply to some (or all) code that follows them
# - are indented to the same level as that code. 
# - Each line of a block comment starts with a # and a single space

# In[7]:


# Badness
import random

def week_9():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_9()


# In[10]:


# Goodness
def week_9():
    
    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

week_9()


# #### Inline comments
# - to be used sparingly
# - to be separated by at least two spaces from the statement
# - start with a # and a single space

# In[11]:


# Badness
week_9()#words of encouragement


# In[12]:


# Goodness
week_9()  # words of encouragement


# ## Docstrings

# <div class="alert alert-success">
# <b>Docstrings</b> are in-code text that describe modules, classes and functions. They describe the operation of the code.
# </div>

# ### Numpy style docs
# [Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. 

# ### Example Docstring

# In[14]:


def add(num1, num2):
    """Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer


# Docstrings
# 
# - multi-line string that describes what's going on
# - starts and ends with triple quotes `"""`
# - one sentence overview at the top - the task/goal of function
# - **Parameters** : description of function arguments, keywords & respective types
# - **Returns** : explanation of returned values and their types

# **Docstrings** are available to you *outside* of the source code.

# ### Docstrings are available through the code

# In[15]:


get_ipython().run_line_magic('pinfo', 'add')


# In[16]:


# The `help` function prints out the `docstring` 
# of an object (module, function, class)
help(add)


# #### `__doc__`

# In[17]:


# Docstrings get stored as the `__doc__` attribute
# can also be accessed from there
print(add.__doc__)


# #### Class Question #2
# 
# What should be included in a docstring?
# 
# 1) Input arguments and their types  
# 2) A brief overview sentence about the code  
# 3) A copy of the `def` line  
# 4) Returned variables and their types  
# 5) A step by step description of the procedure used in the code  
# 
# - A) 1, 4 
# - B) 2, 3, 5
# - C) 3, 5 
# - D) 1, 2, 4 
# - E) 1, 2, 3, 4, 5

# ### Projects & Documentation
# 
# **Do *all* of my functions need `numpy` documentation?**
# 
# 1. Your original code definitely needs `numpy` docstrings (required)
# 2. It's best if all your main functions have docstrings (optional)
#     - If you include functions from an assignment, go ahead document them
#     - If you write a teeny tiny function to accomplish a super small task, no need to document

# ### Documentation for a Software Project

# Documentation Files:
# - A `README` is a file that provides an overview of the project to potential users and developers
# - A `LICENSE` file specifies the license under which the code is available (the terms of use)
# - An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
# - Tutorials and/or Examples show examples and tutorials for using the codebase

# ### Documentation Sites

# <div class="alert alert-success">
# Documentation sites are a host of a package's documentation, for code users. 
# </div>

# #### Example: Function Documentation
# `numpy.array` :
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

# #### Example: Package Documentation
# **scikit learn** (`sklearn`) : https://scikit-learn.org/stable/index.html

# ## Linters

# <div class="alert alert-success">
# A linter is a tool that analyzes code for both programmatic errors and stylistic issues. 
# </div>

# `pylint` is available from Anaconda to check this for you. (also available on datahub.)
# 
# 
# ```python
# # to install on datahub
# !pip install --user pylint
# ```

# #### Class Question #3
# 
# How many PEP8 violations can you find in this code?

# In[ ]:


def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq


# - A) None
# - B) 1 or 2 
# - C) 3 or 4 
# - D) 5 or 6
# - E) 7 or more

# ### list here
# - capitalization in function name; should be snake case
# - conditional in line 4; should be on multiple lines
# - line 9 : no space around the operator
# - no blank line between sections of code 
# - line 6 ; incorrect indentation

# In[ ]:


# Let's fix this code
def my_function(input_num):

    my_list = [0,1,2,3]

    if 1 in my_list: 
        ind = 1
    else:
      ind = 0

    output_list = []
    for i in my_list [ind:]:
        output_list.append(input_num/i)
    return output_list


# In[ ]:


# check using pylint
get_ipython().system('pylint linter_example.py')


# ## Software Versioning
# 
# When you make changes to the software you've released into the world, you have to change the version of that software to let people know changes have occurred.

# ### Versioning Schemes
# 
# The rules, if you're new to this can be [dizzying](https://www.python.org/dev/peps/pep-0440/#version-scheme), so we'll [simplify](https://www.python.org/dev/peps/pep-0396/) for now:
# 
# - `<MAJOR>.<MINOR>`
#     - i.e. 1.3
#     
# - `<MAJOR>.<MINOR>.<MAINTENANCE>`
#     - i.e. 1.3.1

# - `<MAJOR>` - increase by 1 w/ incompatible API changes
# - `<MINOR>` - increase by 1 w/ added functionality in a backwards-compatible manner
# - `<MAINTENANCE>` - (aka patch) increase by 1 w/  backwards-compatible bug fixes.

# In[18]:


# see version information
import pandas as pd
pd.__version__


# In Python package development... when `<MAJOR>` == 0, suggests a package in development

# In[19]:


# see version information
get_ipython().system('pip show lisc')

