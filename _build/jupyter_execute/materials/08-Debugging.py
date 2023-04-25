#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL3** grades now on Canvas
# - **CL4** due Wed
# - **A2** due Friday
# - **E1** (midterm) is Tues 5/2
#     - *in-class*: conceptual (reading code, explaining concepts)
#     - *take-home*: technical (writing code); released after class; taken *individually* on datahub; due Fri 5/5
#     - content: Tooling through Debugging
#     - review: in-class Thursday; bring questions to class

# # Debugging
# 
# - Errors
#     - Syntax
#     - Exceptions
# - Debugging Process
#     - Stack trace
#     - Using outside resources
# - `try`/`except`

# <div class="alert alert-success">
# Debugging is the process of finding and fixing errors in a computer program.
# </div>

# ## Errors

# <div class="alert alert-success">
# Errors are problems with code definition or execution that interrupt running Python code.
# </div>

# ### Syntax Errors
# 
# - Syntax Errors
# - Indentation Errors

# <div class="alert alert-success">
# Syntax & Indentation Errors reflect code that doesn't follow Python structure, and will necessarily fail. 
# </div>

# ### Syntax Error Examples

# In[ ]:


# will produce a syntax error
if True
    print('Yep.')


# Python does its best to tell you:
# - what type of error it is
# - and where it _thinks_ it occurred (`^`)

# In[ ]:


# will produce a syntax error
# and specifically an indentation error
if 3 < 5:
print(value)


# Python gives you a readout about what it was expecting and where you appear to have gone wrong.

# ## Exceptions
# 
# <div class="alert alert-success">
# Exceptions are errors that occur when a code is executed.
# </div>

# For these, there's nothing wrong with the _syntax_ or _structure_ of the code, but in your specific case and how you're trying to use it, Python says 'no'.

# ### ZeroDivisionError
# 
# ZeroDivisionError occurs when you try to divide by zero. 

# In[ ]:


# produces ZeroDivisionError
1 / 0


# Python specifies:
# - the Exception and specific type / error
# - points you to where the error occurred

# ### NameError
# 
# NameError occurs when you try to access a name that Python does not know.

# In[ ]:


# Define a variable
variable = 12


# In[ ]:


# If you typo a name, you will get a NameError
varaible


# While it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.

# In[ ]:


# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1


# ### IndexError
# 
# IndexError occurs when you try to access an index that doesn't exist.

# In[ ]:


my_string = 'COGS18'
my_string[6]


# In[ ]:


# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']


# ### ValueError
# 
# ValueError occurs when you try to use an illegal value for something.

# In[ ]:


int('cat')


# ### TypeError
# 
# TypeError occurs when you try to do something with a variable type that python cannot interpret.

# In[ ]:


'a_string' + 12


# ## Error Recap
# 
# - Syntax Errors
#     - `SyntaxError`
#     - `IndentationError`
# - Exceptions
#     - `ZeroDivisionError` 
#     - `NameError`
#     - Index Errors
#         - `IndexError`
#         - `KeyError`
#     - `ValueError`
#     - `TypeError`
# 

# #### Clicker Question #1
# 
# What type of error will the following code produce?

# In[ ]:


if num > 0
    print("Greater than 0")


# - A) Syntax 
# - B) Name
# - C) Type
# - D) Index
# - E) Value

# #### Clicker Question #2
# 
# What type of error will the following code produce?

# In[ ]:


if num > 0:
    print("Greater than 0")


# - A) Syntax 
# - B) Name
# - C) Type
# - D) Index
# - E) Value

# ## Stack Trace
# 
# **Read (and understand!) your error messages!**
# 
# The trace (log) of what Python did as it went through your code. Gets printed out if Python runs into an error.

# For example...say you're trying to write a function that takes a character as input, turns it into its unicode code point...with an offset of 500, turns *that* back into a character and returns the output...Your first attempt (**which has errors**) is below:

# In[1]:


def encode_char(char):
    # turn into code point
    ord(char)
    # add offset
    char + 500 = offset
    # turn into character
    chr(offset)


# What to look for and think about:
# 1. What *kind* of error is it?
# 2. What line of code/where in the line of code is the error pointing to? 
# 3. What does it *mean*? How do I fix this?
# 
# Sometimes these get really complex. We're here to get better at interpreting these traces. Note that if external functions are being used, these will get longer.

# Sometimes you even have `assert` messages to guide you...how should you use `assert` messages?
# 
# 1. Read them; understand them
# 2. Revisit the part of your code most likely associated with the assert
# 3. *Think* about what you would need to change to fix the issue (do not just guess wildly trying to pass the `assert` - will waste your time)
# 4. Fix the code; re-execute; re-run the assert

# In[ ]:


assert callable encode_char
assert type(encode_char('c')) == str
assert encode_char('c') == 'ɗ'


# ## Try / Except
# 
# <div class="alert alert-success">
# Exceptions do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using <code>try</code> and <code>except</code>. 
# </div>

# For this example, I'm going to introduce `input()`, a function which allows us to get input from the user.

# In[ ]:


# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)


# ### `try` / `except` Block

# In[ ]:


try:
    int(input('Number'))
except:
    print("nahhh")


# ## Raising Errors
# 
# <div class="alert alert-success">
# You can also write code to raise an Exception if something unexpected happens.
# </div>

# ### Raise Exception Examples
# 
# `raise` is a keyword that tells Python you want to create your own error.

# In[ ]:


my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int) 


# #### Clicker Question #3
# 
# Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.

# In[ ]:


num1 = ---
num2 = ---

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)


# - A) I did it!
# - B) I _think_ I did it...
# - C) I'm totally lost.

# ## Helping yourself when debugging
# 
# - Pause and *think*
# - You aren't sure how to approach a problem: add 'in python'
# - You don't understand an error message: 
#     - Use `print()` statements
#     - Google the error message...but then you need to understand what you're reading

# ### Unsure how to approach a problem?
# 
# "Write code that will check whether the value stored in `my_val` is both positive and even. If it is, store the integer `1` in the variable `output`"
# 
# ...How do I check whether a variable stores an even value?
# 
# **Google**: "How to check whether a variable stores an even value _in python_"
# 
# **ChatGPT**: How would I write a function in python to determine whether a variable stores an even value?

# In[ ]:





# ### Don't understand the error message?
# 
# So you try to accomplish the task...below is your first attempt

# In[ ]:


# this code has errors
# we're going to debug together in class
my_val = 6

if my_val > 0 and my_val % 2 = 0:
    output == 1


# Putting it all together...function, try/except, raising errors:

# In[ ]:





# This is the end of material on the first midterm!
