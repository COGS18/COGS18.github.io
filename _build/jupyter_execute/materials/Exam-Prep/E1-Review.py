#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL4** due tonight 1/26 (11:59 PM)
# - **E1** (midterm) due Sun 1/30 11:59 PM (released Thurs at 3PM)
# - **A2** due Mon 1/31 (11:59 PM)
# 
# Notes:
# - **CL3** scores released 
# - Exam Prep answer keys posted
# - We *will* have lecture Friday 
#     - that material will NOT be on E1
#     - will discuss details for what labs/OH will be in-person Friday 

# **Q&A**
# 
# Q: How do you search values in a dictionary?  
# A: This typically requires use of dictionary methods. We'll get there, but for now feel free to check out [this link](https://thispointer.com/python-check-if-a-value-exists-in-the-dictionary-3-ways/).
# 
# Q: will we ever have to combine conditionals and collections?   
# A: Yup! This will mostly be done with loops (coming after E1), but it's possible to combine them now
# 
# Q: When the best time to use each collection and how they are typically implemented in programs.  
# A: Lists are best for storing multiple elements that you may want to update later. Tuples are best for storing multiple elements that you don't want the ability to change. Dictionaries are best for storing key-value pairs...so when you have two pieces of information that you want associated with one another.
# 
# Q: I am curious about why tuple are immutable  
# A: Tuples are immutable b/c sometimes you don't want to be able to update a collection after defintion. Tuples ensure that you can't change part of the collection after definition.
# 
# Q: How to delete parts in list?  
# A: You can use `del` (like the dictionary example). We'll also discuss methods in a few weeks, but for now see [this example](https://www.programiz.com/python-programming/methods/list/remove).
# 
# Q: What are nested lists? Are they really just lists within a list?  
# A: Yes.
# 
# Q: Since tuples are immutable, if we were to make a mistake and wanted to change it would that mean we would have to delete it and start over?  
# A: You would have to re-define the entire tuple, yes.
# 
# Q: The daily participation survey order/titles are kind of confusing me and I think I accidentally filled out Friday’s survey with Monday’s notes but I watched both lectures! I’m not sure what to do.   
# A: So long as you don't complete the survey for a day that hasn't happened yet, you're fine. I'd say the best way is to use the day of the week (Mon, Wed, Fri) for reference when choosing a lecture.
# 
# Q: I am having a little trouble interpreting the assignment error codes when viewing the feedback after the assignment has been graded. Perhaps you can spend some time going through this in class if possible.   
# A: This will be a focus of today's coding lab review - encouraging you to attend coding lab this week!

# **E1: Details**
# 
# - have from Thurs 3PM until Sunday 11:59 PM to complete
# - completed individually
#     - CAN: search the internet and notes for help on topics
#     - CANNOT: search for or post questions from the exam anywhere; discuss or work on the exam with anyone
# - No questions on campuswire about the exam
#     - if you're confused on wording, add a note in your exam directly
#     - if you have a technical issue (i.e. can't access the exam), DM Prof Ellis on Campuswire or email

# **E1: Plan**
# 
# Q0: Honor Code (0.15 pts)
# 
# **Part 1**: Variables & Operators (3.15 pts)
# - Q1: Variables (0.75 pts)
# - Q2: Math Operators (1 pt)*
# - Q3: Comparison Operators (1 pt)*
# - Q4: Membership Operators (0.4 pts)
# 
# **Part 2**: Collections & Indexing (2.75 pts)
# - Q5: Indexing (1 pt)
# - **Q6**: Dictionaries (1pt)*
# - Q7: Collections & Mutating (0.75 pts)
# 
# 
# **Part 3**: Control Flow - Conditionals, Functions, & Code Style (6.45 pts)
# 
# - **Q8**: Function Execution & Code Style (2 pts)*
# - Q9: Functions + Conditionals (2 pts)*
# - Q10: Accomplish a task (2.45 pts)*
# 
# Notes: 
# - \* question has possibility for partial credit
# - There are two questions (**Q6** & **Q8**) that require written responses on the exam
# - I will never intentionally try to trick you with wording
# - If it doesn't say to define a function, you don't have to define a function

# ![written response](../img/written_response.png)

# # Exam 1 Review

# ## Midterm Expectations
# 
# You will be expected to: 
# 
# 1. Recognize, understand and _respond_ to Python syntax:
#     - statements & comments, whitespace, code blocks & indentation levels
# 2. Recognize, understand and be able to _explain_ code constructions:
#     - variables, operators, data types, conditionals
# 3. Be able to apply what you've learned:
#     - Given a task:
#         - what kind of code constructions are needed to answer it?
#         - what kind of concepts does it relate to?
# 4. With respect to everything above, be able to read and respond to short code snippets and write out code.

# ### Reminder: 
# 
# There are also a few Exam #1 Practice Problems [here](https://cogs18.github.io/materials/Exam-Prep/E1-Practice.html).
# 
# And, there is a practice Exam on datahub.

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

