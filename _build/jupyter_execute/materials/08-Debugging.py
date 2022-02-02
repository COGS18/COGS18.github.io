#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **E1** (midterm) due Sun 1/30 11:59 PM
# - **A2** due Mon 1/31 (11:59 PM)
# 
# Notes: 
# - **E1** is now available
# - **Updates for what is in person next week!** (Look at Canvas homepage)
#     - Lecture: Zoom
#     - Coding Lab: Some Zoom; Some In-Person
#     - Office Hours: Some Zoom; Some In-Person

# **Q&A**
# 
# Q: What is the point of ord and chr? I didn't really understand how it's applicable to class.  
# A: Take a look at A2 (and we'll see it again on A3) - it's a way to encrypt and decrypt messages.
# 
# Q: Can numbers be characters inputted to ord?  
# A: I'm not 100% sure I understand the question, but `ord()` will only accept integer values as input.
# 
# Q: how would we approach a string with multiple characters? so that would be several unicodes?   
# A: Excellent question! Loops! We start these on Monday! And, you'll get to use them on A3. 
# 
# Q: is unicode like the official way of indexing a list (e.g., list of letters in the alphabet)? so the unicode values are official? (e.g., 'a' will always return 97)  
# A: 'a' *will* always return 97...but that is separate from indexing into a list. Think of unicode more like a dictionary, where 'a' is the key and 97 is its value - they are "linked" to one another.
# 
# Q: What is the purpose of unicode if we do not ever have to learn which letter corresponds to which number?  
# A: Take a look at A2 ...and eventually A3 to see how we can utilize in our code to accomplish a task!
# 
# Q: it seems like i get the concepts separately but when asked to utilize all the stuff we learned under one function I blank. Could we maybe do problems like these at the end of lecture to test our knowledge? Because it seems like these are the questions we are getting on assignments and exams   
# A: Yup - I will work to incorporate more of these into lecture going forward. But, I also do want you to be able to do things on homework that puts concepts together. So, I'll try to make the jump from lecture to assignments smaller, but I won't make it go away completely b/c there is a lot of learning that happens when you have to combine concepts.
# 
# Q: What would happen if we don't understand the question? Are we allowed to email you or the TA for clarification?  
# A: On the exam no, you'll have to do your best to interpret the question as is. If you're unsure, feel free to explain how you interpreted the question.
# 
# Q: One question I have is what does this do; my_lst[1::2]  (the :: ).  
# A: The :: indicates there is no stop value, so go from the 1 index to the end of the list (b/c there is no stop)
# 
# Q: we can submit as twice as we want as long as it is before deadline, right?  
# A: I'm assuming you mean for the exam and yes, you can submit as  many times as you want before the deadline. We'll use your last submission.
# 
# Q: What has the average grade been for previous E1's?  
# A: ~85%
# 
# Q: How does unicode assign numbers?  
# A: These rules are actually established by a group that monitors/updates unicde rules. See more [here](https://en.wikipedia.org/wiki/Unicode). 
# 
# Q: curious about how difficult exam 1 will be compared to practice exam  
# A: Should be similar overall. My feeling (and one TA's feelings) is that Q1-9 are a bit easier than prevoius quarters/the practice exam, but Q10 is harder.
# 
# Q: Will Aliases be tested on any other exams?  
# A: You'll need to understand them, yes.
# 
# Q: The main thing I am still questioning is the rules when it comes to if, elif, and else. Which is ruled first?  
# A: The if is checked, then the elif, and the else finally.
# 
# Q: Can you further explain Exam 1 logistics? There's a 24 hour window to submit but we can have multiple days to work on it?  
# A: There's a *greater* than 24 hour window. The syllabus says I'll give at least 24 hours. B/c I know some people are traveling back to campus this weekend and busy with other midterms/life, I decided to give way more than 24h this time. You can start whenever you want. You can work on it as much as you want. It just must be submitted by Sunday night.
# 
# Q: I am struggling to understand how to properly write code to calculate the total number of components there are in a list.   
# A: Take a look at the collections notes for a function that can help you do this.
# 
# Q: Is there a comprehensive set of notes that we can refer to when struggling with remembering the proper code style?  
# A: Good idea! I'll try to pull something together and share! There is an [official guide](https://www.python.org/dev/peps/pep-0008/) but it goes way beyond what we've discussed so far.

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

# In[3]:


# will produce a syntax error
if True
    print('Yep.')


# Python does its best to tell you:
# - what type of error it is
# - and where it _thinks_ it occurred (`^`)

# In[14]:


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

# In[7]:


# produces ZeroDivisionError
1 / 0


# Python specifies:
# - the Exception and specific type / error
# - points you to where the error occurred

# ### NameError
# 
# NameError occurs when you try to access a name that Python does not know.

# In[8]:


# Define a variable
variable = 12


# In[9]:


# If you typo a name, you will get a NameError
varaible


# While it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.

# In[10]:


# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1


# ### IndexError
# 
# IndexError occurs when you try to access an index that doesn't exist.

# In[11]:


my_string = 'COGS18'
my_string[6]


# In[20]:


my_list = ['a', 'b']
# direct indexing errors
# my_list[2]
# can include an index that doesn't exist
# in a slice
my_list[1:5]


# In[12]:


# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']


# ### ValueError
# 
# ValueError occurs when you try to use an illegal value for something.

# In[21]:


int('cat')


# ### TypeError
# 
# TypeError occurs when you try to do something with a variable type that python cannot interpret.

# In[22]:


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

# In[23]:


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


num = 6


# In[24]:


if num > 0:
    print("Greater than 0")


# In[26]:


# syntax errors checked first
# then python executes code - checks for exceptions
if num > 0:
    print("Greater than 0")

my_val = 6

if my_val < 0
    print('hi')


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

# In[27]:


def encode_char(char):
    # turn into code point
    ord(char)
    # add offset
    char + 500 = offset
    # turn into character
    chr(offset)


# In[45]:


def encode_char(char):
    # turn into code point
    unicode = ord(char)
    # add offset
    offset = unicode + 500
    # turn into character
    offset = chr(offset)
    
    return offset


# In[ ]:


def encode_char(char):
    # turn into code point
    # add offset
    # into charaeter
    unicode = chr(ord(char) + 500)

    return unicode


# In[41]:


ord('a') + 500
chr(597)


# In[42]:


encode_char('a')


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

# In[46]:


assert callable(encode_char)
assert type(encode_char('c')) == str
assert encode_char('c') == 'ɗ'


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
# Google: "How to check whether a variable stores an even value _in python_"

# In[7]:


# this code has errors
# we're going to debug together in class
my_val = -2

if my_val > 0 and my_val % 2 == 0:
    output = 1
else:
    output = 0

output


# ### Don't understand the error message?
# 
# So you try to accomplish the task...below is your first attempt

# In[ ]:


# this code has errors
# we're going to debug together in class
my_val = 6

if my_val > 0 and my_val % 2 = 0:
    output == 1


# ## Try / Except
# 
# <div class="alert alert-success">
# Exceptions do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using <code>try</code> and <code>except</code>. 
# </div>

# For this example, I'm going to introduce `input()`, a function which allows us to get input from the user.

# In[12]:


# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)


# ### `try` / `except` Block

# In[11]:


int('monday')


# In[15]:


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

# In[17]:


my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int) 


# #### Clicker Question #3
# 
# Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.

# In[ ]:


# if ... is true:
    # run this code


# In[18]:


num1 = 56
num2 = 0

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)


# - A) I did it!
# - B) I _think_ I did it...
# - C) I'm totally lost.
