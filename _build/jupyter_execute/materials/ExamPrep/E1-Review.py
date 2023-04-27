#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A2** due Friday
# - **E1** on Tuesday 5/2
#     - in class , closed notes 11AM
#     - take home: released after class; due Friday 5/5 at 11:59 PM
# - No Coding Lab next week
#     - CL5 due 5/10 (this is a change; Canvas and syllabus have been udpated)
# - Staff will have office hours as usual next week; no exam questions in OH

# # Exam 1 Review

# ## Midterm Expectations
# 
# You will be expected to: 
# 
# 1. Recognize, understand and _respond_ to Python syntax:
#     - statements & comments, whitespace, code blocks & indentation levels
# 2. Recognize, understand and be able to _explain_ code constructions:
#     - variables, operators, data types, conditionals, functions
# 3. Be able to apply what you've learned:
#     - Given a task:
#         - what kind of code constructions are needed to answer it?
#         - what kind of concepts does it relate to?
# 4. With respect to everything above, be able to read and respond to short code snippets and write out code.

# ### Exam 1 Plan
# 
# **In-Class**:
# - Q1-6 Multiple Choice
# - Q7-10 Very Short Answer
# - Q11-13 Short Answer
# - Q14-16
#     - Function Explanation
#     - Function Debugging
#     - Function Description
#     
# **Take-Home**: 3Qs
# 1. Function Execution
# 2. Function Debugging
# 3. Function Writing
# 
# Note: This is the expected layout. Small changes to this could be made after the staff proofread/test-drive the exam.

# ### Additional Practice: 
# 
# - Old take-home exam on datahub (<- this take-home is *way* longer than your take-home will be)
# - [Old in-class exam](https://docs.google.com/document/d/1z6BXAGRP1TBYFzhImc0YlZVZB2QCclu474c8fTDcbXQ/edit?usp=sharing) (<- this in-class exam is similar but not the same format as our in-class exam and does not cover functions)

# ## Topics & Example Questions
# 
# - Variables & Data Types
# - Operators
# - Functions
# - Conditionals
# 
# Note: The questions below are _less_ involved than the questions on your midterm. These are meant to help guide your studying. If you're stuck on one of these, you know where to focus your studying.

# ### Variables & DataTypes
# 
# Types:
# - strings, integers, floats, Booleans, None
# - Collections
#     - Lists
#     - Tuples
#     - Dictionaries
# 
# Concepts:
# - Mutable vs. Immutable
# - Indexing

# #### Data Types Question #1
# 
# What is the difference between a tuple and a list?

# #### Data Types Question #2
# 
# Given the following list: 
# 
# ```python
# ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']
# 
# ```
# 
# Edit the code at right with how would you return the specified values on left:
# 
# ```python
# ['vanilla', 'chocolate', 'strawberry'] : ice_cream[      ]
# ```

# #### Data Types Question #3
# 
# Write a line of code that would change the third element of a list `my_list` to store the value `12`.

# ### Operators
# 
# - assignment : `=`
# - math: `+`, `-`, `/`, `*`, `**`, `//`
# - comparison : `==`, `!=`, `<`, `>`, `<=`, `>=`
# - logic: `and`, `or`, `not`
# - identity: `is`, `is not`
# - membership : `in`, `not in`

# #### Operators Question #1
# 
# What is the difference between `=` and `==`?

# #### Operators Question #2
# 
# Create a variable `oper_var` that uses both the not and or operators (each at least once) such that `oper_var` stores (returns) the value `True`.

# #### Operators Question #3
# 
# Using at least 4 different math operators, create a variable `math_var` that stores (returns) the value '18' (or 18.0)

# #### Operators Question #4
# 
# Create a variable `string_concat` that demonstrates how you can concatenate two different strings together with a space between the two different strings. 

# ### Conditionals
# 
# - `if`, `elif`, & `else`

# #### Conditionals Question #1
# 
# Circle necessary or optional, as applicable: In Python, a conditional has a necessary / optional `if` statement, one or more necessary / optional `elif` statement(s) and a necessary / optional `else` statement. 

# #### Conditionals Question #2
# 
# Given the following outline of a conditional:
# 
# ```python
#     if COND_A:
#         # Code Block A
# 	elif COND_B:
# 		# Code Block B
# 	else:
# 		# Code Block C
# ```
# 
# 1. If `COND_A` and `COND_B` are both `True`, which code block(s) evaluate?
# 2. If `COND_A` is False and `COND_B` is `True`, which code block(s) evaluate?

# #### Conditionals Question #2
# 
# You use have a list that stores 20 different integers. You use a comparison operator to compare the relationship between two of the elements in the list and store that output in a variable. What would the type of that output variable be?

# ## Functions
# 
# - `def`
#     - `return`
# - executing a function
#     - parameters
#         - keyword vs. positional
#         - default values
# - have a separate namespace

# #### Functions Question #1
# Write, in real code, a function called `remainder` that takes two inputs, divides the first input by the second and returns the remainder.

# In[1]:


## YOUR CODE HERE


# #### Functions Question #2
# Using the function `remainder` you wrote above, write the python code you would use to return the remainder of 10 divided by 4. Store the output in the variable `my_remainder`.

# In[2]:


## YOUR CODE HERE


# #### Functions Question #3
# Assuming the following function has been defined, what would `double_list([1, 2, 3])` return?

# In[1]:


def double_list(my_list):
   
    total = my_list * 2
        
    return total


# In[3]:


## CODE TO TEST HERE

