#!/usr/bin/env python
# coding: utf-8

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

# In[ ]:


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

# In[ ]:


print(2 + 3)


# In[ ]:


div_result = 4 / 2 
print(div_result)
type(div_result)


# ### Order of Operations
# 
# Mathematical operators follow the rules for order of operations.

# - follow the rules for order of operations.
# - parentheses specify which order you want to occur first

# In[ ]:


order_operations = 3 + 16 / 2
print(order_operations)


# To specify that you want the addition to occur first, you would use parentheses.

# In[ ]:


specify_operations = (3 + 16) / 2
print(specify_operations)


# #### Class Question #1
# 
# What would be the value stored in `my_value`? 
# 
# Note: Best to think about it before running the code to ensure you understand.

# In[ ]:


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

# In[ ]:


# 2 to the power 3
2 ** 3


# In[ ]:


# remainder of 17 divided by 7
17 % 7


# #### Class Question #2
# 
# What would be the value stored in `remainder`?

# In[ ]:


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

# In[ ]:


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

# In[ ]:


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

# In[ ]:


True and True


# In[ ]:


True or True


# In[ ]:


True and not False


# In[ ]:


not False


# In[ ]:


# two nots cancel one another out
not (not True)


# ### Capitalization matters

# In[ ]:


# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE


# #### Class Question #4
# 
# How will the following boolean expression evaluate:

# In[ ]:


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

# In[ ]:


a = 12
b = 13
a > b


# In[ ]:


True == True


# In[ ]:


True != False


# In[ ]:


'aa' == 'aa'


# In[ ]:


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

# In[ ]:


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

# In[ ]:


a = 927
b = a
c = 927


# In[ ]:


print(a is b)
print(c is a)


#  Two variables that are equal does **not** imply that they are identical.

# If we wanted that second statement to evaluate as `True` we could use `is not`...

# In[ ]:


# make a True statement
print(c is not a)


# In[ ]:


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

# In[ ]:


z = 5
x = '5'
c = 'Hello!'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = ---
false_variable = ---

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

# In[ ]:


x = 'I love COGS18!'
print('l' in x)


# In[ ]:


print('L' in x)


# In[ ]:


print('COGS' in x)


# In[ ]:


print('CSOG' in x)


# In[ ]:


print(' ' in x)


# ## String Concatenation

# <div class="alert alert-success">
# Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
# </div>

# In[ ]:


'COGS' + ' 18'


# In[ ]:


'a' + 'b' + 'c'


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
