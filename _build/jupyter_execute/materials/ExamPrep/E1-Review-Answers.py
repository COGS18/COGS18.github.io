#!/usr/bin/env python
# coding: utf-8

# # Exam 1 Review (Answers)

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

# #### Data Types Answers

# Data Types Question #1
# 
# Tuples are created with () and are immutable.  
# Lists are created with [] and are mutable.

# In[2]:


# Data Types Question #2
ice_cream = ['vanilla', 'chocolate', 'strawberry', 'cherry', 'salted caramel']
print(ice_cream[-5:-2])
print(ice_cream[:3])
ice_cream[0:3]


# In[ ]:


# Data Types Question #3
my_list[2] = 12 


# In[3]:


# Data Types Question #3
my_list = [1, 2 , 3, 4, 5, 6]
my_list[2] = 12
my_list


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
# Create a variable `oper_var` that uses both the `not` and `or` operators (each at least once) such that `oper_var` stores (returns) the value `True`.

# #### Operators Question #3
# 
# Using at least 4 different math operators, create a variable `math_var` that stores (returns) the value '18' (or 18.0)

# #### Operators Question #4
# 
# Create a variable `string_concat` that demonstrates how you can concatenate two different strings together with a space between the two different strings. 

# #### Operators Answers

# Operators Question #1
# 
# = is an assignment operator  
# == checks for equality

# In[9]:


# Operators Question #2

# one possible answer
# a = not False
# b = not True
# open_var = a or b

# OR
open_var = not False or not True
print(open_var)


# In[6]:


# Operators Question #3
# one possible answer to get to 18
math_var =   36 // ((((2 + 3) * 2) / 2) - 3)
math_var 


# In[11]:


# Operators Question #4
# possible answer

string_concat = 'COGS' + ' ' + '18'
print(string_concat)
# OR
a = 'COGS'
b = '18'
string_concat = a + ' ' + b
print(string_concat)

string_concat = 'COGS ' + '18'
print(string_concat)


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
# 2. If `COND_A` is `False` and `COND_B` is `True`, which code block(s) evaluate?

# #### Conditionals Question #3
# 
# You use have a list that stores 20 different integers. You use a comparison operator to compare the relationship between two of the elements in the list and store that output in a variable. What would the type of that output variable be?

# #### Conditionals Answers

# Conditionals Question #1
# 
# necessary, optional, optional

# Conditionals Question #2
# 
# 1. Code Block A
# 2. Code Block B

# In[12]:


###### how to check your thinking when you're studying
COND_A = True
COND_B = True

if COND_A:
    print('a')
elif COND_B:
    print('b')
else:
    print('c')


# Conditionals Question #3
# 
# A Boolean

# In[14]:


# Example code to demonstrate:
test_list = range(0,21)

# test 1
out = test_list[1] != test_list[2]
print(type(out))

# test 2
out = test_list[17] <= test_list[15]
print(type(out))


# ### Functions
# 
# - `def`
#     - `return`
# - executing a function
#     - parameters
#         - keyword vs. positional
#         - default values
#     - have a separate namespace

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


# #### Functions Answers

# In[5]:


## Functions Question #1

def remainder(num1, num2):  # set default values within parenthesis
    out = num1 % num2
    return out


# In[6]:


## Functions Question #2

my_remainder = remainder(10, 4)
my_remainder


# In[4]:


## Functions Question #3

double_list([1, 2, 3])

