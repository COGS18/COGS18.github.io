#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL2** due Wednesday (11:59 PM)
# - **A1** due next Mon 1/17 (11:59 PM)
#     - originally a typo in Q10, instructions referred to `student_b` twice, third one should be `student_c` (`assert`s would make it clear we wanted `student_c`)
# 
# Notes:
# - Office Hours Start today!
# - Waitlist: I've reached out to staff
# - Anaconda demo
# - **CL1** has been (re-)graded
# - Pre-course survey EC has been posted; responses to survey sent

# **Pre-Course Survey Summary**
# 
# - N=347 (338 unique)
# - 70.1% of the class has never programmed before
# - Common hobbies/activities: Surfing, Netflix/shows, cooking/baking, spots/working out, music/kpop, work 
# - Common futures: Psychology, Neuroscience, Physician, Happy, Content, Employed
# - Common note: Nervous/anxious scared, but excited and/or willing to work hard

# **Q&A**
# 
# Q: What's the difference between print() and just typing the variable name by itself to display the output?   
# A: For our purposes they're very similar. One small difference is that `print()` will *always* print out whatever is in the parentheses; Typing the variable by itself will only show what the variable stores if it is the last thing in the cell.
# 
# Q: Do the numbers on the side (that appear once you run the code) show up for you (the grader)? Like if I make a mistake and have to run the code multiple times so now I have a large number or something, is that bad?  
# A: We can see them when you submit. However, it doesn't matter to me how long it takes you to understand...just that you understand! So, definitely do not worry about/stress over this!
# 
# Q: How are hidden test created? What functions are employed? Does it require some new libraries? I have heard of hidden tests in coding assignments before but have never "seen" one and see how it is implemented to check a piece of code.   
# A: Occassionally I'll import new libraries. But, the hidden tests are typically just additional `assert` statements, like the ones you can see in your assignments. That said, when assignments are graded, you'll see all assert statements, hidden ones included...so after A1 is graded, you'll have a better sense for the hidden tests!
# 
# Q: do the hidden tests effect anything more than just checking our work? Is the verify button basically the same thing?  
# A: The validate button only checks that you passed the *visible* tests. And, nope, hidden tests are just there to check your answers.
# 
# Q: How would you be able to fix it if you accidentally delete a cell? Is there a way to start over an assignment if needed?  
# A: You can use the "Undo Delete Cell" from the Edit menu at top. To completely restart an assignment, rename the folder where the assignment is stored...and then you'll be able to fetch a fresh copy of the assignment from the assignments tab on datahub.
# 
# Q: I want to know what each color means when we encode. Sometimes it’s red, green, and mostly black and I am sure other colors will come up.   
# A: I'll point these out as we go! For now, variables you create are black. Functions that exist in python are green. Reserved keywords are bold and green. Red is typically to point out an issue/something you want to fix.
# 
# Q: If we want to write notes on jupyterhub, how do we change the color of the notes?  
# A: https://campuswire.com/c/G9193CB28/feed/10  
# 
# Q: What is the purpose of the raise NotImplemented(error)?  
# A: To indicate that this is where you're supposed to put your code. You should delete this line and replace it with your code.
# 
# Q: Do we need an underscore for a variable name if it is only one word. Example "flowers"  
# A: No
# 
# Q: Why does python not have variable types?   
# A: It does, but it is a dynamically-typed programming language.
# 
# Q: How can we use Anaconda to access the course content, since it's not necessarily connected to UCSD's datahub? Would we download each individual page from the course website and upload it to our own Jupyter notebook?  
# A: Downloading from website would be the best way unless you're familiar with git/GitHub.

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


# In[6]:


reusable = 4 / 2
type(reusable)


# In[3]:


div_result = 4 / 2 
print(div_result)
type(div_result)


# ### Order of Operations
# 
# Mathematical operators follow the rules for order of operations.

# - follow the rules for order of operations.
# - parentheses specify which order you want to occur first

# In[7]:


order_operations = 3 + 16 / 2
print(order_operations)


# To specify that you want the addition to occur first, you would use parentheses.

# In[8]:


specify_operations = (3 + 16) / 2
print(specify_operations)


# #### Clicker Question #1
# 
# What would be the value stored in `my_value`? 
# 
# Note: Best to think about it before running the code to ensure you understand.

# In[13]:


my_value = (3 + 2) + 16 / (4 / 2)
print(my_value)


# - A) 7.0
# - B) 10.5
# - C) 13.0
# - D) 20.0
# - E) Produces an error

# ### More Math

# <div class="alert alert-success">
# Python also has <code>**</code> for exponentiation and <code>%</code> for remainder (called modulus). These also return numbers.
# </div>

# In[14]:


# 2 to the power 3
2 ** 3


# In[15]:


# remainder of 17 divided by 7
17 % 7


# #### Clicker Question #2
# 
# What would be the value stored in `remainder`?

# In[16]:


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

# In[17]:


True and True


# In[18]:


True or True


# In[19]:


True and not False


# In[20]:


not False


# In[21]:


# two nots cancel one another out
not (not True)


# ### Capitalization matters

# In[22]:


# this will give you an error
# 'TRUE' is not a boolean
# 'True' is
TRUE and TRUE


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

# In[23]:


a = 12
b = 13
a > b


# In[24]:


True == True


# In[25]:


True != False


# In[28]:


'aa' == 'aa'


# In[29]:


12 <= 13


# #### Clicker Question #4
# 
# How will the following boolean expression evaluate:

# In[34]:


(6 > 10) and (4 == 4)


# In[30]:


(6 < 10) and (4 == 4)


# - A) True
# - B) False
# - C) None
# - D) This code will fail

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

# In[37]:


## EDIT CODE HERE
sword_charge = 90
shield_energy = 100

(sword_charge >= 90) and (shield_energy >= 100)


# ## Identity Operators
# 
#  Identity operators are used to check if two values (or variables) are located on the same part of the memory.

# <div class="alert alert-success">
# Python uses <code>is</code> and <code>is not</code> to compare identity. These operators return booleans.
# </div>

# - `is` : True if both refer to the same object
# - `is not` : True if they do not refer to the same object

# In[38]:


a = 927
b = a
c = 927


# In[39]:


print(a is b)
print(c is a)


#  Two variables that are equal does **not** imply that they are identical.

# If we wanted that second statement to evaluate as `True` we could use `is not`...

# In[40]:


# make a True statement
print(c is not a)


# In[41]:


# testing for value equality
a == b == c


# #### Clicker Question #6
# 
# 
# Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 
# 
# 
# - A) I did it!
# - B) I tried but am stuck.
# - C) I'm unsure where to start

# In[42]:


z = 5
x = '5'
c = 'Hello'
d = c
e = [1, 2, 3]
f = [1, 2, 3]

# EDIT CODE HERE
true_variable = z is not x
false_variable = z is x

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


# #### Clicker Question #7
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

# In[43]:


x = 'I love COGS18!'
print('l' in x)


# In[44]:


print('L' in x)


# In[45]:


print('COGS' in x)


# In[46]:


print('CSOG' in x)


# In[47]:


print(' ' in x)


# ## String Concatenation

# <div class="alert alert-success">
# Operators sometimes do different things on different types of variables. For example, <code>+</code> on strings does concatenation.
# </div>

# In[48]:


'COGS' + ' 18'


# In[53]:


cogs = 'COGS'
number = '18'
cogs + ' ' + number


# In[49]:


'a' + 'b' + 'c'


# ## Chaining Operators

# <div class="alert alert-success">
# Operators and variables can also be chained together into arbitrarily complex expressions.
# </div>

# In[56]:


('COGS' + '18' == 'COGS18')


# In[55]:


# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('COGS' + '18' == 'COGS18')


# In[57]:


(13 % 7 >= 7)


# In[58]:


('COGS' + '18' == 'COGS18')


# #### Clicker Question #8
# 
# How will the following expression evaluate:

# In[62]:


13%3 > 1


# In[63]:


2**2 >= 4 and 13%3 > 1


# - a) True
# - b) False
# - c) None
# - d) This code will fail

# ## Code Style: Operators
# 
# - Single space around operators
# - No spaces after leading parentheses or before trailing parentheses

# Notes below are from student questions/discussion at the end of lecture:

# In[68]:


# or clarification
# one side must evaluate as True to return True

my_var = 6 > 10
print(my_var)
my_other_var = 5 <= 5

my_var or my_other_var


# In[69]:


a = '5'
b = "5" 
a == b

