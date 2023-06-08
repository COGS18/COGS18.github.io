#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A5** due Friday
# - **Final Exam/Final Project** due Tuesday of finals week (6/13; 11:59 PM)
#     - Practice Final Available on datahub (answer key available)
#     - You will need to understand DataFrames/`pandas` and be able to read, understand, and use documentation for methods from `pandas` for final exam
#     - GitHub EC for Final Project - part of the post-course survey; put your project on GitHub
# - [COGS 18 Post-Course Survey](https://docs.google.com/forms/d/e/1FAIpQLSe-HqmffnAeByzr0YKUa0lEg_DtitPUqG4WGm47Yym5QxGkCA/viewform?usp=sf_link) (link also on Canvas)
# - Please complete your CAPEs! (currently: 29%)

# # Wrap Up
# 

# ## Some (extra) Python
# 
# - string formatting (`format`)
# - sets
# - `collections`
# - args & kwargs
# - list comprehensions
# - map

# ...or: a day of shortcuts
# 
# Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

# It's hard to search for things you don't know exist.
# 
# Today's goal : let you know these things exist.
# 
# NOT today's goal : teach you all the details.

# You do *not* need to incorporate these into your project, but if they'll help you, go for it!

# In[ ]:


import antigravity


# ## String Formatting

# Use the `format` method to manipulate and format strings.

# In[4]:


name = "Shannon"
job = "Associate Teaching Professor"
topic = "Python"

"Hello! My name is {}. My job is {}, and I work on {}".format(name, job, topic)


# ## Sets 

# Sets are a variable type that store **only unique entries**.

# In[ ]:


my_set = set([1, 1, 2, 3, 4])
my_set


# Like lists, they are iterable & mutable.

# In[ ]:


my_set.add(6)
my_set


# Reminder that if you add a value that is already in the set...the set will not change

# ## Collections

# The `collections` module has a number of useful variable types, with special properties. 

# "Special editions" of collections we've discussed before (lists, tuples, and dictionaries).

# In[ ]:


from collections import Counter


# In[ ]:


# count how many elements there are in collection
# return values in a dictionary
Counter([1, 0, 1, 2, 1])


# In[ ]:


import collections


# In[ ]:


collections.Counter([1, 0, 1, 2, 1])


# In[ ]:


# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")


# Think back to our encryption scheme! 
# 
# The most common letter in the English language is 'e'.
# 
# If you just move each letter over by 1 position, you can just use a Counter to crack the code.
# 
# Why we moved to a variable encoder!

# ## `args` & `kwargs`
# 
# - allow you to pass a variable number of arguments to a function
#     - `*args` - allow any number of extra arguments (including zero)
#     - `**kwargs` - allow any number of *keyword* arguments to be passed (as a dictionary)

# ### `*args`

# In[ ]:


# use *arguments to demonstrate args
def tell_audience(*arguments):
    for arg in arguments:
        print(arg)


# In[ ]:


tell_audience('asdf')


# In[ ]:


tell_audience("Hello!", 
              "My name is Shannon.", 
              "My job is Associate Teaching Professor.")


# ### `**kwargs`

# In[ ]:


def tell_audience_kwargs(**info):
    print("type: ", type(info), '\n')
    
    for key, value in info.items():
        print("key: ", key)
        print("value: ", value, "\n")


# In[ ]:


tell_audience_kwargs(first='Shannon', 
                     last='Ellis', 
                     email='sellis@ucsd.edu')


# ## List Comprehensions

# List comprehensions allow you to run loops and conditionals, *inside lists*.

# The general format is :
# 
# `[ expression for item in list if conditional ]`
# 

# In[ ]:


# NOT a list comprehension
# how we've been doing it
input_list = [0, 1, 2]
output_list = []

for ind in input_list:
    output_list.append(ind + 1)
    
# look at output
output_list


# In[ ]:


# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]


# In[ ]:


# You can also include conditionals inside a list comprehension
[val for val in [1, 2, 3, 4, 5] if val % 2 == 0]


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


# ## The Goal

# To teach you a skill - of how to do things with Python.

# You've been more formally trained than *many* people out in the world programming.

# ## Where We've Been:
# 
# - Python & Jupyter
# - Variables
# - Operators
# - Conditionals
# - Functions
# - Lists, Tuples & Dictionaries
# - Loops
# - Objects & Classes
# - Command Line
# - Scientific Computing
# - Documentation, Code Style, Code Testing

# #### Class Question #1
# 
# After COGS 18, I feel \_\_\_\_\_\_\_\_\_\_\_\_ my Python programming abilities
# 
# - A) very confident in
# - B) somewhat confident in
# - C) middle-of-the-road about
# - D) somewhat unsure about
# - E) very unsure about
# 

# #### Class Question #2
# 
# After COGS 18, I feel the following about my future Python programming:
# 
# - A) will use again for sure
# - B) may use again
# - C) unsure if will use again
# - D) probably won't use again
# - E) definitely won't use again
# 

# ## How to Continue with Coding

# - Write Code
# - Read Code
# - Learn and follow standard procedures
# - Do code reviews
# - Interact with the community
# - Build a code portfolio

# ## Powered by Python

# This course used:
# - Python Programming Language
# - Jupyter Notebooks
# - RISE Jupyter Slides
# - nbgrader
# - Jupyter Book
# - scipy stack & many other 3rd party modules

# ## Where do you go from here

# - if want_more_data_science:
#     - go to COGS 9
# - if you want *to do* more_data_science:
#     - ...*and* Python: take COGS 108
#     - ...*and* R: take COGS 137
# - if interested_in_research:
#     - look for labs, tell them you can code
# - if you want_something_else:
#     - go do it!

# ## Acknowledgments

# Thank you to Tom for his original design of this course.

# Thank you to the TAs & IAs for their tireless work on this class.

# Thank you students for you time, effort and patience. 

# <center><h1> The End 
