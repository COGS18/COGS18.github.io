#!/usr/bin/env python
# coding: utf-8

# # Exam 2 Review

# ## Exam II Plan (12.5 points)
# 
# 
# Part I: **Methods, Debugging, & Code Style** (4.5 points) 
# - Q1: Method I (0.75 points)*
# - Q2: Method II (1.25 points)*
# - Q3: Debugging & Code Style (2.5 points)*
# 
# Part II: **Loops & Functions** (4 points)  
# - Q4: Function I (1.75 points)*
# - Q5: Function II (2.25 points)*
# 
# Part III: **Classes** (4 points)
# - Q6: Classes I (1.5 points)*
# - Q7: Classes II (2.5 points)*
# 
# \* : includes manual grading (partial credit)

# ### Reminder: 
# 
# There are three extra notebooks that you can use for review (in addition to your notes, labs, and assignments):
# 
# 1. [A1-CodeSytle](https://cogs18.github.io/materials/A1-CodeStyle.html)
# 1. [A2-Syntax](https://cogs18.github.io/materials/A2-Syntax.html)
# 2. [A3-Examples](https://cogs18.github.io/materials/A3-Examples.html)
# 
# There is also a practice exam on datahub and additional practice problems [here](https://shanellis.github.io/pythonbook/content/intro.html). Note that answers are included for all practice problems in the "Answers" chapter.

# ### Questions?

# ### Loops
# 
# - loops: `for` and `while`
#     - `continue`, `break`, `pass`

# #### Loops Question #1
# What are the two kinds of loops? ____________ and ____________

# #### Loops Question #2
# Use the following:
# `ind = 1` to write a loop (using real Python code) that would loop and print the value `ind` of ind each time through the loop _and_ update the value of ind by 1. Have this loop stop after 4 iterations. 

# #### Loops Question #3
# 
# Create a list that stores each letter of your favorite animal as a different element in a list. Store that in the variable `fav_pet`. 
# 
# Initialize an additional variable called `reverse_pet` that will store an empty string to start.
# 
# Then, using indexing, loop through each letter in that list such that `reverse_pet` stores a list with your favorite pet spelled backward.
# 
# For example, if your favorite pet were "cat", the output stored in `reverse_pet` should be: `['t', 'a', 'c']`
# 

# #### Loops Question #4
# Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

# In[10]:


def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total


# In[4]:


## CODE TO TEST HERE


# ## Objects & Classes
# 
# - objects & `class`
#     - attributes
#     - methods
#     - instances
# 

# #### Objects & Classes Question #1
# 
# **Part A**
# 
# We want to simulate a rocket ship for a game.
# 
# Write code that will create a class `Rocket`. 
# 
# This class should have two instance attributes: `x` and `y`. These will specify the x,y position of the rocket. Each attribute should be initialized with hte value 0. 
# 
# Your `Rocket` should also have the method `move_up()`. This method should increment the y-position of the rocket by 1. 

# In[8]:


## YOUR CODE HERE


# The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

# **Part B**
# 
# Create an instance `my_rocket` of your Rocket object.

# In[9]:


## YOUR CODE HERE


# **Part C**
# 
# Update `my_rocket` so that `my_rocket` has the `y` position 3.

# In[10]:


## YOUR CODE HERE


# #### Objects & Classes Question #2
# 
# Fill in the blanks:
# 
# 	What is the name of a function defined within a class: ______________
# 
# 	In Python, everything is a(n) ______________. 
# 

# ## Python & Jupyter Extras
# - encodings (`chr` & `ord`)
# - whitespace
# - namespace
# - kernel
# - code comments
# - magic functions

# #### Extras Question #1
# What will the following piece of code print out?
# 
# ```print(chr(ord('A')))``` 
#     
#      _____________

# #### Extras Question #2 
# 
# What is the magic function `%whos` used for?

# #### Extras Question #3
# 
# For each of the following, indicate if the statement is True or False about Python and programming:
# 
# - True/False Whitespace matters in Python
# - True/False Comments in Python start with '%' 					
# - True/False You have to specify a data type when you define a variable
# - True/False Every Python variable is available from every namespace				
# - True/False `print_name()` folles best practices for function naming

# <h2><center>After the second exam:</center></h2>

# <h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

# <h3><center> We also become a project based course. </center></h3>
