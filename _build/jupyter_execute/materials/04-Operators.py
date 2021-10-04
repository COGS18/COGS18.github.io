#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A1** due *next* Fri (10/8; 11:59 PM)
# - **CL2** will be posted this afternoon
# - **CL1** "answers" are posted on the website 

# - CL grades are typically posted before class on *Mondays*
#     - this week: they've been posted on Canvas
#     - if you messed up submission, go ahead and submit (*this week only*)
#     - I will regrade and give credit if you submit by 11:59 PM tonight (Friday)

# **Q&A**
# 
# Q: I am not sure which assignment I submit will be graded (is it the last one?)  
# A: Yes. We only have access to the most recent submission.
# 
# Q: I’m a little confused about when we open a new box versus add new lines    
# A: Largely, this is up to you. On assignments, typically, a single cell is provided. All your code can go in that single cell. However, you're allowed to add additional cells if you prefer. It matters that the code is there, and that the answer is in a cell before the tests (the `assert`s), but not how many cells there are.
# 
# Q: I am still confused on how to print quotation marks in strings. Can the apostrophe be used anywhere inside quotes? What is the backslash used for and where should it be placed?     
# A: If you use double quotes (") to start the string, you can have as many apostrophes within the string as you want. The backslash is used any time you want to indicate that the following character right after the backslash should be a "string literal" ...meaning part of the string.
# 
# Q: When will iclickers become mandatory?   
# A: They will not be mandatory this quarter, as I'm not requiring/incentivizing attendance. However, they will be used to check the class' understanding.
# 
# Q: in the notebook, on the top right of each cell, there is a dropdown for 'slide type'. what does that do? I observed no change on the notebook when I change it.   
# A: This is what I use to display as a slideshow. Changing it on your end will not change the notebook.
# 
# Q: Is there a way to clear all code I've written in a notebook not just the output (which seemed to be an option under Kernel). For example, what if I started an assignment but I wanted to be safe the next time I open it, and I wanted to clear everything I edited and wrote?   
# A: There is no straightforward way to do this in the same notebook. *However*, if you rename the folder containing the assignment/lab, you'll be able to fetch a new (blank) copy from the assignments tab.
# 
# Q: What did you mean by immutable cannot be altered after being created? What is or is not being altered?   
# A: Immutable means that you cannot change a part of the value stored in the variable once it is defined. For example if a variable stores the string "cat", you cannot change it to "bat" (changing the first letter) by specifying you want to change the c to a b. This is because it is an immutable type variable. If you wanted to store "bat", you would have to redefine the entire string "bat". This will make more sense when we get to mutable type variables next week! 
# 
# Q: Will we get feedback on the homework? And if there is tutoring aside from lab?  
# A: Yes, you will get feedback on homework and coding lab answers are posted for you to check your work. No tutoring, but there are lots of office hours throughout the week!
# 
# Q: how to pound(#) multiple lines?  
# A: Highlight them and then use cmd/ctrl + space bar on your keyboard.

# **A1: Clarification/Demo**
# 
# - when finished, your assignments should run from top to bottom *without you having to change anything*
# - variables created in `%%writefile` will be stored in file
# - these variables will overwrite variables created in test cells

# In[1]:


get_ipython().run_cell_magic('writefile', 'new_file.py', "# You can ignore the line above - it is used to help check your code\n\na = 3\nb = 'new'\nprint(status)")


# In[2]:


status = False

get_ipython().run_line_magic('run', '-i new_file.py')
assert status == False


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

# In[3]:


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

# In[4]:


print(2 + 3)


# In[5]:


div_result = 4 / 2 
print(div_result)
type(div_result)


# ### Order of Operations
# 
# Mathematical operators follow the rules for order of operations.

# - follow the rules for order of operations.
# - parentheses specify which order you want to occur first

# In[8]:


order_operations = 3 + 16 / 2
print(order_operations)


# To specify that you want the addition to occur first, you would use parentheses.

# In[9]:


specify_operations = (3 + 16) / 2
print(specify_operations)


# #### Clicker Question #1
# 
# What would be the value stored in `my_value`? 
# 
# Note: Best to think about it before running the code to ensure you understand.

# In[10]:


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

# In[11]:


# 2 to the power 3
2 ** 3


# In[12]:


# remainder of 17 divided by 7
17 % 7


# #### Clicker Question #2
# 
# What would be the value stored in `remainder`?

# In[13]:


remainder = 16 % 5
remainder


# - A) 0
# - B) 1
# - C) 3
# - D) 3.2
# - E) Produces an error

# #### Clicker Question #3
# 
# What would be the value stored in `modulo_time`?

# In[14]:


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
# 
# The way I first thought of involved a package and we haven't talked about those yet...

# In[15]:


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

# In[16]:


True and True


# In[17]:


True or True


# In[18]:


True and not False


# In[19]:


not False


# In[20]:


# two nots cancel one another out
not (not True)


# ### Capitalization matters

# In[21]:


# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE


# #### Clicker Question #4
# 
# How will the following boolean expression evaluate:

# In[22]:


True and not False


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

# In[29]:


a = 12
b = 13
a > b


# In[30]:


True == True


# In[31]:


True != False


# In[34]:


'aa' == 'aa'


# In[35]:


12 <= 13


# #### Clicker Question #5
# 
# Assume you're writing a videogame that will only slay the dragon only if our magic lightsabre sword is charged to 90 or higher and we have 100 or more energy units in our protective shield. 
# 
# 
# Start with the code in the following cell. Replace `---` with operators or values that will evaluate to `True` when the cell is run (and slay the dragon!).
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[40]:


# variables must be defined prior to using in operations
friday > 5 and saturday > 6

friday = 10
saturday = 7


# In[41]:


sword_charge


# In[42]:


## EDIT CODE HERE
sword_charge = 95
shield_energy = 100

(sword_charge >= 90) and (shield_energy >= 100)


# ## Understanding Boolean logic
# 
# When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.
# 
# Let's look at an example that could trip you up now.
# 

# 1. Python considers empty strings as having boolean value of `False`. Non-empty string as having boolean value of `True`.
# 

# In[43]:


empty_string = ''
bool(empty_string)


# In[46]:


nonempty_string = 'string has something in it'
bool(nonempty_string)


# 2.  For `and` operator if left value is `True`, then right value is checked and returned. If left value is `False`, then that left value is returned.
# 

# In[47]:


True and False


# In[48]:


bool('a')


# In[49]:


'a' and 'b'


# In[50]:


'b' and 'a'


# #### Clicker Question #6
# 
# What would the following code cell return?

# In[51]:


'' and 'a'


# - A) ''
# - B) 'a'
# - C) `True`
# - D) `False`

# In[52]:


# the left value in parentheses evaluates as True
'a' == ('b' and 'a')


# In[53]:


# the left value in parentheses evaluates as True
'a' == ('a' and 'b')


# In[54]:


# the left value in parentheses evaluates as False
'a' == ('' and 'a')


# In[55]:


# what we actually wanted python to do
# to look at a in a and b
'a' == 'a' and 'a' == 'b' 


# 3. For `or` operator if left value is `True`, then it is returned, otherwise if left value is `False`, then right value is returned.

# In[ ]:


'a' or 'b'


# In[ ]:


# empty string evaluates as False
'' or 'b'


# In[ ]:


'a' == ('a' or 'b')


# In[ ]:


'b' == ('a' or 'b')


# In[ ]:


'b' == 'a' or 'b' == 'b'


# #### Clicker Question #7
# 
# What would the following code cell return?

# In[ ]:


'a' == ('' or 'a')


# - A) ''
# - B) 'a'
# - C) `True`
# - D) `False`

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


# #### Clicker Question #8
# 
# 
# Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 
# 
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[ ]:


z = 5
x = '5'
c = 'Hello'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = ---
false_variable = ---

print(true_variable, false_variable)


# ### Delving Deeper: Identity Operators

# A **new object** is created each time we have a variable that makes reference to it, but there are *few notable exceptions*:
# 
# - some simple strings
# - Integers between -5 and 256 (inclusive)
# - empty immutable containers (e.g. tuples) - we'll get to these later
# 
# While these may *seem* random, they exist for memory optimization in Python implementation. 

# Shorter and less complex strings are "interned" (share the same space in memory).
# 
# The rules behind this are a bit fuzzy, so we'll just go through a few examples here. But, if you want to read more about string interning and how Python handles this, you can read more [here](http://guilload.com/python-string-interning/).

# In[ ]:


simple_string = 'string'
simple_string2 = 'string'


# In[ ]:


simple_string is simple_string2


# In[ ]:


print(id(simple_string), id(simple_string2))


# In[ ]:


longer_string = 'really long string that just keeps going'
longer_string2 = 'really long string that just keeps going'


# In[ ]:


longer_string is longer_string2


# In[ ]:


print(id(longer_string), id(longer_string2))


# In[ ]:


d = 5
e = 5


# In[ ]:


print(id(d), id(e))


# In[ ]:


print(d is e)


# Python implementation front loads an array of integers between -5 to 256, so these objects *already exist*.

# In[ ]:


# Python doesn't create a new object here
j = 5
k = 5
l = 'Hello'
m = 'Hello'

true_variable_integer = j is k
true_variable_string = l is m

print(true_variable_integer, true_variable_string)


# In[ ]:


# Python DOES create a new object here
n = 975 #greater than 256
o = 975
p = 'Hello!' #that exclamation point makes it more complex
q = 'Hello!'

false_variable_integer = n is o
false_variable_string = p is q

print(false_variable_integer, false_variable_string)


# #### Clicker Question #9
# 
# Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[ ]:


a = 5
b = 5
c = b
d = 'Hello!'
e = 'Hello!'
f = 567
g = 567

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


# #### Clicker Question #10
# 
# How will the following expression evaluate:

# In[ ]:


2**2 >= 4 and 13%3 > 1


# - a) True
# - b) False
# - c) None
# - d) This code will fail
