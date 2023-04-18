#!/usr/bin/env python
# coding: utf-8

# **Course Announcments**
# 
# Due Dates: 
# - CL2 due Wednesday
# - A1 released; due *next* Friday (4/21)
# 
# Notes:
# - CL1 graded - score on Canvas (if you completed but failed to submit, submit by tonight, Tues, for full credit)
#     - Answer keys: posted on website and in folder in `LectureNotes-COGS18`
# - Pre-course survey "graded" 

# **Survey Summary** (N=383): 
# - 75% of the class has never programmed before (12% know Python; a handful know other languages)
# - 92% of the class wanted 11:59 PM due dates
# - 37% of the class asked for at least one extension last quarter
# - Common comment: *Nervous but excited*
# - Outside of class: work, workout (volleyball, surf,  yoga, basketball, soccer, spikeball), explore (try cafes, window shop, thrifting, hike), art (write, read, music, poetry, dance, paint), parent (children and pet...shout out to Sharkbait!) and caring for family members (older family members and younger siblings)
# - Most fun future pursuits: Mattress tester, an inspiration to someone, an animal whisperer, happy, astronaut, world traveler, NBA analyst
# - Most common future pursuits: don't know, psychologist, tech-centric/adjacent

# # Operators
# 
# - assignment
# - math
# - logic
# - comparison
# - identity
# - membership

# <div class="alert alert-success">
# Operators are special symbols in Python that carry out arithmetic or logical computation.
# </div>

# ## Assignment Operator

# <div class="alert alert-success">
# Python uses <code>=</code> for assignment.
# </div>

# In[1]:


my_var = 1


# ## Math Operators
# 
# 
# - `+`, `-`, `*`, `/` for addition, subtraction, multiplication, & division
# - `**` for exponentiation & `%` for modulus (remainder)
# - `//` for floor division (integer division)

# <div class="alert alert-success">
# Python uses the <b>mathematical operators</b> <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> for 'sum', 'substract', 'multiply', and 'divide', repsectively.
# </div>

# In[2]:


print(2 + 3)


# In[3]:


div_result = 4 / 2 
print(div_result)
type(div_result)


# ### Order of Operations
# 
# Mathematical operators follow the rules for order of operations.

# - follow the rules for order of operations.
# - parentheses specify which order you want to occur first

# In[4]:


order_operations = 3 + 16 / 2
print(order_operations)


# To specify that you want the addition to occur first, you would use parentheses.

# In[5]:


specify_operations = (3 + 16) / 2
print(specify_operations)


# #### Class Question #1
# 
# What would be the value stored in `my_value`? 
# 
# Note: Best to think about it before running the code to ensure you understand.

# In[6]:


my_value = (3 + 2) + 16 / (4 / 2) 
my_value


# - A) 7.0
# - B) 10.5
# - C) 13.0
# - D) 20.0
# - E) Produces an error

# ### More Math

# <div class="alert alert-success">
# Python also has <code>**</code> for exponentiation and <code>%</code> for remainder (called modulus). These also return numbers.
# </div>

# In[7]:


# 2 to the power 3
2 ** 3


# In[8]:


# remainder of 17 divided by 7
17 % 7


# #### Class Question #2
# 
# What would be the value stored in `remainder`?

# In[9]:


remainder = 16 % 5
remainder


# - A) 0
# - B) 1
# - C) 3
# - D) 3.2
# - E) Produces an error

# #### Class Question #3
# 
# What would be the value stored in `modulo_time`?

# In[10]:


modulo_time = 4 * 2 % 5
modulo_time


# - A) 0
# - B) 1
# - C) 3
# - D) 3.2
# - E) Produces an error

# ## Remainder
# 
# How to get Python to tell you the integer and the remainder when dividing?

# In[11]:


a = 17 // 7
b = 17 % 7

print(a, 'remainder', b)


# `//` is an operator for floor division (integer division)

# ## Logical (Boolean) operators
# - use Boolean logic
# - logical operators: `and`, `or`, and `not`

# Booleans are named after the British mathematician - George Boole. He first formulated Boolean algebra, which are a set of rules for how to reason with and combine these values. This is the basis of all modern computer logic.

# <div class="alert alert-success">
# Python has <code>and</code>, <code>or</code> and <code>not</code> for boolean logic. These operators often return booleans, but can return any Python value.
# </div>

# - `and` : True if both are true
# - `or` : True if at least one is true
# - `not` : True only if false

# In[12]:


True and True


# In[13]:


True or True


# In[14]:


True and not False


# In[15]:


not False


# In[16]:


# two nots cancel one another out
not (not True)


# ### Capitalization matters

# In[17]:


# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE


# #### Class Question #4
# 
# How will the following boolean expression evaluate:

# In[18]:


(6 < 10) and (4 == 4)


# - A) True
# - B) False
# - C) None
# - D) This code will fail

# ## Comparison Operators

# <div class="alert alert-success">
# Python has comparison operators <code>==</code>, <code>!=</code>, <code><</code>, <code>></code>, <code><=</code>, and <code>>=</code> for value comparisons. These operators return booleans.
# </div>

# - `==` : values are equal
# - `!=` : values are not equal
# - `<` : value on left is less than value or right
# - `>` : value on left is greater than value on right
# - `<=` : value on left is less than *or equal to* value on right
# - `>=` : value on left is greater than or equal to value on the right

# In[19]:


a = 12
b = 13
a > b


# In[20]:


True == True


# In[21]:


True != False


# In[22]:


'aa' == 'aa'


# In[23]:


12 <= 13


# #### Class Question #5
# 
# Assume you're writing a videogame that will only slay the dragon only if our magic lightsabre sword is charged to 90 or higher and we have 100 or more energy units in our protective shield. 
# 
# 
# Start with the code in the following cell. Replace `---` with operators or values that will evaluate to `True` when the cell is run (and slay the dragon!).
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[24]:


## EDIT CODE HERE
sword_charge = ---
shield_energy = ---

(sword_charge ---) and (shield_energy ---)


# ## Identity Operators
# 
#  Identity operators are used to check if two values (or variables) are located on the same part of the memory.

# <div class="alert alert-success">
# Python uses <code>is</code> and <code>is not</code> to compare identity. These operators return booleans.
# </div>

# - `is` : True if both refer to the same object
# - `is not` : True if they do not refer to the same object

# In[25]:


a = 927
b = a
c = 927


# In[26]:


print(a is b)
print(c is a)


#  Two variables that are equal does **not** imply that they are identical.

# If we wanted that second statement to evaluate as `True` we could use `is not`...

# In[27]:


# make a True statement
print(c is not a)


# In[28]:


# testing for value equality
a == b == c


# #### Class Question #6
# 
# 
# Using the variables provided below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 
# 
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[30]:


z = 5
x = '5'
c = 'Hello!'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = e is f
false_variable = e is not f

print(true_variable, false_variable)


# ## Membership Operators

# <div class="alert alert-success">
# Python uses <code>in</code> and <code>not in</code> to compare membership. These operators return booleans.
# </div>

# Membership operators are used to check whether a value or variable is found in a sequence.
# 
# Here, we'll just be checking for value membership in strings. But, we'll discuss lists, tuples, sets, and dictionaries soon.

# - `in` : True if value is found in the sequence
# - `not in` : True if value is not found in the sequence

# In[31]:


x = 'I love COGS18!'
print('l' in x)


# In[32]:


print('L' in x)


# In[33]:


print('COGS' in x)


# In[34]:


print('CSOG' in x)


# In[35]:


print(' ' in x)


# ## String Concatenation

# <div class="alert alert-success">
# Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
# </div>

# In[40]:


'COGS' + ' 18'


# In[41]:


'a' + 'b' + 'c'


# In[42]:


# in class question (no space)
'COGS' + '18'


# In[43]:


# alternative approach to add a space (discussed in class)
'COGS' + ' ' + '18'


# ## Chaining Operators

# <div class="alert alert-success">
# Operators and variables can also be chained together into arbitrarily complex expressions.
# </div>

# In[ ]:


# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('COGS' + '18' == 'COGS18')


# In[ ]:


(13 % 7 >= 7)


# In[ ]:


('COGS' + '18' == 'COGS18')


# #### Class Question #7
# 
# How will the following expression evaluate:

# In[ ]:


2**2 >= 4 and 13%3 > 1


# - a) True
# - b) False
# - c) None
# - d) This code will fail

# ## Code Style: Operators
# 
# - Single space around operators
# - No spaces after leading parentheses or before trailing parentheses
