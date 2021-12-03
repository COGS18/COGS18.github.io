#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - No Coding Lab to turn in tonight - Coding Lab today is project-focused
# - **A5** due Friday (11:59)
# - **Final exam/project** due Mon (12/6; 11:59 PM)
#     - Project EC: [GitHub EC](https://docs.google.com/forms/d/e/1FAIpQLSe9WBkspvL4OYKQocamdpwa58HLJGiEbYKQUi6VFn21utVM3g/viewform?usp=sf_link) (link also on Canvas) and/or "going above and beyond" (described in submitted notebook)
# - **Finals Week Office Hours** - normal office hours are *not* happening during finals week
#     - **Prof**: OH by 10 min appt on Mon 1-3 PM (see Canvas page for Calendly link to sign up; please cancel if you're not going to show; come ready to ask question - I will stick to the schedule)
#     - If **staff** decide to hold, they'll post to campuswire (they are not required to do so)
# - **CAPEs** - please fill out your [CAPEs](https://cape.ucsd.edu/) (+1% if >=85\% of class completes their CAPEs; currently: ~40%)
# - **[Post-Course Survey](https://docs.google.com/forms/d/e/1FAIpQLSfqwgORTqIj1h6Zb5MJB_StJnAVTgrOEboq60frGv4Z4xN3Wg/viewform?usp=sf_link)** ("due" 12/6 11:59 PM; link also on Canvas); ideally, fill out *after* taking final exam/completing final project

# **Q&A**
# 
# Q: Would the final be an overall test of all the material or would it be project like?  
# A: It will be project-like and test the material throughout the quarter with a focus on material learned since second midterm. See practice final to get a sense.
# 
# Q: How will we know that our project is at a level where we could believe we’d get a good grade? Is there a rubric?  
# A: https://cogs18.github.io/materials/Projects/overview.html#grading-rubric 
# 
# Q: Why I think atbash_encrypt and atbash_decrypt are essentially the same function? I could get 'HELLO' as output even if I use abash_encryot('SVOOL') rather than the decrypt function. Then how can I distinguish which function to use?   
# A: Yes! This is a great observation. This code needs to be refactored/reorganized. We'll comment on this today in class.
# 
# Q: I'm curious about how one could expand on the project, either by learning new code techniques or by simply writing more extensive code   
# A: You could go beyond the requirements of the project by writing more code than what is required, writing better documentation, implementing something we haven't talked about in class (i.e. a new package), teaching yourself something beyond what was covered in class, etc.
# 
# Q: How do you rename a folder?  
# A: From the terminal the command is `rm`. From the Files tab on datahub, click the box to the left of what you want to rename and select "Rename" from menu at top.
# 
# Q: Will there be extra OH to get help with this project?   
# A: Yes - I will hold OH on Monday by appt. 
# 
# Q: Is there a central place that includes all project requirements and how exactly to format everything? Do we have to include docstrings and comments on every function or only 3 of them?  
# A: Yes: https://cogs18.github.io/materials/Projects/overview.html with FAQ [here](https://cogs18.github.io/materials/Projects/faq.html)
# 
# Q: Where can I find the project file (Project_COGS18_FA21)?  
# A: Fetched from Assignments tab on datahub.
# 
# Q: Where can I find a rubric for the project. I see on the course website that there is a rubric in terms of grading percentage but I can't find the requirements of the project. for example I am not sure how many Classes or functions I need.   
# A: https://cogs18.github.io/materials/Projects/overview.html#grading-rubric states "Must include at least 3 original functions or methods"
# 
# Q: how many files should we submit for our project?  
# A: At a minimum, three. One notebook, one module/script, one test file: https://cogs18.github.io/materials/Projects/overview.html#submitting-your-project

# # Advanced Python
# 
# - software versioning
# - string formatting (`format`)
# - sets
# - `collections`
# - args & kwargs
# - list comprehensions
# - `filter`/`map`
# - APIs
# - overloading operators

# ...or: a day of extra info and shortcuts
# 
# Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

# It's hard to search for things you don't know exist.
# 
# Today's goal : let you know these things exist.
# 
# NOT today's goal : teach you all the details.

# You do *not* need to incorporate these into your project, but if they'll help you, go for it!

# In[1]:


import antigravity


# ## Documentation for a Software Project

# Documentation Files:
# - A `README` is a file that provides an overview of the project to potential users and developers
# - A `LICENSE` file specifies the license under which the code is available (the terms of use)
# - An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
# - Tutorials and/or Examples show examples and tutorials for using the codebase

# ## Documentation Sites

# <div class="alert alert-success">
# Documentation sites are a host of a package's documentation, for code users. 
# </div>

# ### Example: Function Documentation
# `numpy.array` :
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

# ### Example: Package Documentation
# **scikit learn** (`sklearn`) : https://scikit-learn.org/stable/index.html

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

# In[2]:


# see version information
import pandas as pd
pd.__version__


# In Python package development... when `<MAJOR>` == 0, suggests a package in development

# In[5]:


get_ipython().system('pip install lisc')


# In[6]:


# see version information
get_ipython().system('pip show lisc')


# ## String Formatting

# Use the `format` method to manipulate and format strings.

# In[7]:


name = "Shannon"
job = "Assistant Teaching Professor"
topic = "Python"

"Hello! My name is {}. My job is {}, and I work on {}".format(name, job, topic)


# ## Sets 

# Sets are a variable type that store **only unique entries**.

# In[8]:


my_set = set([1, 1, 2, 3, 4])
my_set


# Like lists, they are iterable & mutable.

# In[9]:


my_set.add(6)
my_set


# #### Clicker Question #1
# 
# How many values would be in the following set?

# In[10]:


clicker_set = set([1, 1, 2, 2, 3, 4])
clicker_set.add(6)
clicker_set.add(1)
clicker_set


# - A) 0
# - B) 4
# - C) 5
# - D) 6
# - E) ¯\\\_(ツ)\_/¯

# Reminder that if you add a value that is already in the set...the set will not change

# ## Collections

# The `collections` module has a number of useful variable types, with special properties. 

# "Special editions" of collections we've discussed before (lists, tuples, and dictionaries).

# In[11]:


from collections import Counter


# In[12]:


# count how many elements there are in collection
# return values in a dictionary
Counter([1, 0, 1, 2, 1])


# In[13]:


import collections


# In[14]:


collections.Counter([1, 0, 1, 2, 1])


# In[15]:


# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")


# Think back to our encryption scheme! 
# 
# The most common letter in the English language is 'e'.
# 
# If you just move each letter over by 1 position, you can just use a Counter to crack the code.
# 
# Why we moved to a variable encoder!

# ## `any` & `all`

# `any` and `all` evaluate collections for whether elements evaluate as True. 

# In[16]:


my_bool_list = [True, False, True]


# In[17]:


any(my_bool_list)


# In[18]:


all(my_bool_list)


# #### Clicker Question #2
# 
# What would the following return?

# In[19]:


my_list = [True, True, False, True]
any(my_list)


# - A) `True`
# - B) `False`
# - C) `[True, True, True]`
# - D) `[False]`
# - E) ¯\\\_(ツ)\_/¯

# ## `getattr` & `setattr`

# `getattr` and `setattr` can be used to get and set attributes, respectively. 

# Flexibly return and define instance attributes.

# In[20]:


class MyClass():
    
    def __init__(self):        
        self.var_a = 'string'
        self.var_b = 12

# create instance 
instance = MyClass()


# In[21]:


instance.var_a


# In[22]:


# Get a specified attribute
# define var_a as an input
getattr(instance, 'var_a')


# In[23]:


# Set a specified attribute
setattr(instance, 'var_b', 13)
print(instance.var_b)


# ## `args` & `kwargs`
# 
# - allow you to pass a variable number of arguments to a function
#     - `*args` - allow any number of extra arguments (including zero)
#     - `**kwargs` - allow any number of *keyword* arguments to be passed (as a dictionary)

# ### `*args`

# In[29]:


# use *arguments to demonstrate args
def tell_audience(*arguments):
    print(type(arguments))
    
    for arg in arguments:
        print(arg)


# In[30]:


tell_audience('asdf')


# In[31]:


tell_audience("Hello!", 
              "My name is Shannon.", 
              "My job is Assistant Teaching Professor.")


# ### `**kwargs`

# In[27]:


def tell_audience_kwargs(**info):
    print("type: ", type(info), '\n')
    
    for key, value in info.items():
        print("key: ", key)
        print("value: ", value, "\n")


# In[28]:


tell_audience_kwargs(first='Shannon', 
                     last='Ellis', 
                     email='sellis@ucsd.edu')


# ## List Comprehensions

# List comprehensions allow you to run loops and conditionals, *inside lists*.

# The general format is :
# 
# `[ expression for item in list if conditional ]`
# 

# In[32]:


# NOT a list comprehension
# how we've been doing it
input_list = [0, 1, 2]
output_list = []

for ind in input_list:
    output_list.append(ind + 1)
    
# look at output
output_list


# In[33]:


# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]


# In[34]:


# You can also include conditionals inside a list comprehension
my_list = [1, 2, 3, 4, 5]
my_list2 = [val for val in my_list if val % 2 == 0]


# In[35]:


print(my_list)
print(my_list2)


# #### Clicker Question #3
# 
# What would the following return?

# In[ ]:


list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1] 
multiplied


# - A) `True`
# - B) `False`
# - C) `[9, 12, 15]`
# - D) `15`
# - E) ¯\\\_(ツ)\_/¯

# Note: there are also tuple & dictionary comprehensions. They're just used less frequently.

# ## Regular Expressions

# Regular expressions allow you to work with **specified patterns in strings**.

# In[ ]:


import re


# In[ ]:


my_string = "If 12 Python programmers try to complete 14 tasks in 16 minutes, why?"


# In[ ]:


# can just search for a letter
re.findall('o', my_string)


# In[ ]:


# but the patterns are where these shine
re.findall('\d\d', my_string)


# ## filter

# `filter` is a function that takes in another function, and a collection object, and **filters the collection with the function**. 

# In[ ]:


def is_bool(val):
    if isinstance(val, bool):
        return True
    else:
        return False


# In[ ]:


#filter?


# In[ ]:


out = []

for val in [1, False, 's', True]:
    out.append(is_bool(val))

out


# In[ ]:


# apply function to every element of list
# function to apply is first input to filter
list(filter(is_bool, [1, False, 's', True]))


# ## Lambda Functions

# Lambda functions are small, anonymous functions. 
# 
# Can define them in line.

# In[ ]:


increment = lambda a: a + 1


# In[ ]:


increment(1)


# In[ ]:


# not a lambda function
def lambda_equivalent(a):
    
    output = a + 1
    
    return output


# In[ ]:


lambda_equivalent(1)


# #### Clicker Question #4
# 
# What would the following return?

# In[ ]:


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list


# - A) `[1, 5, 11, 3]`
# - B) `[1, 3, 5, 11]`
# - C) `[4, 6, 8, 12]`
# - D) `[1, 5, 4, 6, 8, 11, 3, 12]`
# - E) ¯\\\_(ツ)\_/¯

# ## map

# `map` applies a given function to each element in a collection. 

# In[ ]:


# create a function
def double(val):
    return val * 2


# In[ ]:


# map function to each element of list
my_list = [1, 2, 3, 4]
list(map(double, my_list))


# In[ ]:


# Note - we can use lambda functions with map
list(map(lambda x: x *2, my_list))


# ## Conditional Assignment

# You can use a conditional within an assignment, to manipulate what gets assigned given some condition. 

# In[ ]:


# variable assignment
condition = False
my_var = 1 if condition else 2


# In[ ]:


print(my_var)


# ## Unpacking

# You can unpack collection objects with `*`, and key, value pairs with `**`. 

# In[ ]:


def my_func(xx, yy, zz):
    print(xx, yy, zz)


# In[ ]:


# create list
my_list = [1, 2, 3]


# In[ ]:


# this will error
my_func(my_list)


# In[ ]:


# unpack the list
my_func(*my_list)


# In[ ]:


# create dictionary
my_dict = {'xx' : 1, 'yy' : 2, 'zz' : 3}


# In[ ]:


# unpack the dictionary
my_func(**my_dict)


# ## Application Programming Interface

# <div class="alert alert-success">
# An <b>API</b> is a programmatic interface to an application - a software to software interface, or way for programs to talk to other programs. 
# </div>

# If you are pointing and clicking on computer applications, that is _not_ an API.
# 
# If you are writing code to interact with software and get information, that _IS_ an API.

# ### Module APIs

# Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

# ### Web APIs

# APIs are an interface to interact with an application, _designed for programmatic use_ :
# - They allow systematic, controlled access to (for example) an applications database and procedures
# - They can be used to request data and/or to request that the the application perform some procedure

# ### RESTful API
# 
# (Representational State Transfer API) 
# 
# An approach to interact with web addresses

# ## Twitter API

# In[ ]:


# to use this on your computer
# uncomment and run following line
get_ipython().system('pip install tweepy')


# Then, follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) for authetication of tweepy with Python.

# In[ ]:


# Accessing Twitter API from Python
#  Note: to run this, you will have to fill in stw.py with your OAuth credentials.
#    You can do that here: https://apps.twitter.com/

# Import tweepy to access API
import tweepy
from tweepy import OAuthHandler

# Import my API credentials
from stw import *

# Twitter API requires Authentification with OAuth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object to access Twitter
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.user.name)
    print(status.text, '\n')


# ## Overloading Operators

# In other words: Nothing in Python is sacred.

# Operators and special operations for objects are defined by double underscore methods, which we can overload to change how the object acts. 

# In[ ]:


class Language():
    
    def __init__(self, name):
        self.name = name.lower()
    
    # Overload what the printed representation of the object as a string
    def __repr__(self):
        return "The programming language " + self.name
    
    # Overload the greater than symbol
    def __gt__(self, other):
        return True if self.name == 'python' else False


# Note: "dunder" is how we refer to those double underscore methods

# In[ ]:


python = Language('python')
perl = Language('perl')


# In[ ]:


print(python)


# In[ ]:


python > perl

