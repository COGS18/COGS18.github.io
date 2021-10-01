#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL1** due tonight (11:59 PM)
# - **A1** due Fri of week 2 (10/8; 11:59 PM)

# Notes: 
# - First coding lab today! 
# - iclicker app should now work...
# - Thanks to all who completed the pre-course survey (N=382)
#     - Extra credit now posted to Canvas
#     - 64% of the class has never programmed before
#     - Common Hobbies: reading, cooking, video games, board games, surfing, basketball
#     - Future Goals: Happy, Successful, Psychology, Neuroscience, SWE, grad school
#     - Common note: Nervous but excited

# **Q&A**
# 
# Q: Does the number of times we run a code affect our grade?  
# A: Nope!
# 
# Q: When you update the notes at the end of the lecture, do our edits (made during the lecture) still appear on those notes?  
# A: My updates will show up on the course website; Your notes on datahub will remain unchanged.
# 
# Q: So we don't need to download python or anaconda because everything is already accessible through datahub?  
# A: Correct. You are encouraged but not required to download Anaconda (to have access to course materials after COGS 18)
# 
# Q: For the assertion errors on assignments, are we only penalized/docked points when we submit an assignment with an error or are we penalized everytime we get a hidden assertion error?  
# A: If you submit an assignment that has an assertion error, from either a visible or hidden assert some partial points will be lost.
# 
# Q: What is the difference between the jupyter notebook you show us in class on your screen versus the one we can see on our own devices?  
# A: I'm displaying mine as slides using a plugin called RISE...but the starting document (the notebook) is exactly the same.
# 
# Q: What is the usual time you upload the lecture slide on the website?  
# A: On a good day, the afternoon prior. On a typical day around 7AM the day of.
# 
# Q: Should we attempt coding labs before attending a lab section, or are they to be done in our lab section?   
# A: Totally up to you! 
# 
# Q: i'm curious about how to underline/strikethrough a text in a markdown cell  
# A: There is no underline, but tildes around text do ~strikethrough~.
# 
# Q: I still would like to know what the overall curriculum will be for the course.  
# A: Schedule is [here](https://cogs18.github.io/assets/intro/syllabus.html#course-schedule).
# 
# Q: For the labs due Wednesday do we usually go over the material that it covers on Monday?  
# A: We sometimes finish Monday but often finish Wednesday prior to labs happening in person.
# 
# Q: In the assignments, if the code runs through without an alert message, does that mean the code is right? Or at least in the right format?  
# A: It means you're on the right track. You could pass the visible asserts and still not have done what we asked, but you're on the right track.
# 
# Q: It was actually a question from Q&A part. So not attending lab will not influence my grade as long as I submit coding labs by the deadline, right?  
# A: Correct.
# 
# Q: I am curious about who came up with 'notebooks' and how they are different from whatever software is used in real-world applications.  
# A: The first notebook was developed in 1980. Knuth came up with the idea of literate programming prior to that. And, notebooks are used *all over the place* in the real world, primarily for data analysis. They're less used in software development.
# 
# Q: A question that I still have is "how do I revert back my notebook?" What if I make an edit and messed up something but I want to revert the file back to its original unedited form, how would I achieve that?  
# A: If it's an assignment/coding lab, you can delete the folder (or change the name of the folder) and re-fetch a new copy from the assignments tab.  If it's notes, I'd recommend going to the website, downloading the notebook, and then uploading that to datahub.
# 
# Q: I could not find the clicker app on the ios app store.  
# A: https://apps.apple.com/us/app/iclicker-student/id899690067

# # Variables
# 
# - definition
# - Namespace
# - Variable types

# ## Programming With Python

# Programming: a way to ask computer to store values (variables), and do things with them (operations).`

# In[2]:


# This is a comment. You can write a comment by using a `#`
my_variable = 12 

my_other_variable = 13 # Comments can be 'inline', like this one


# ### Defining Variables

# <div class="alert alert-success">
# In programming, variables are things that store values. Variables are defined with <code>name = value</code>.
# </div>

# In[3]:


my_var = 1  # `my_var` is a variable

# This defines another variable
other_var = 'variables are cool'


# In[4]:


# once you create a variable it's stored in your namespace
other_var


# In[5]:


my_pound_sign = "#"


# ## Code Variables != Math Variables
# 
# In mathematics: `=` refers to equality (as a statement of truth).
# 
# In coding: `=` refers to assignment. 

# Math: What is x?
# 
# $y = 10x + 2$

# Code: What is x?
# 
# `x = x + 1`

# #### Clicker Question #1
# 
# After executing the following code, what will be the value of `my_var`?

# In[6]:


my_var = 2 

my_var = my_var + 1

print(my_var)


# - A) 2
# - B) 3
# - C) "my_var + 1"
# - D) This code will fail

# #### Clicker Question #2
# 
# After executing the following code, what will be the value of `diff_var`?

# In[7]:


my_var


# In[8]:


diff_var = my_variabel - my_var

print(diff_var)


# - A) 4
# - B) 9
# - C) "my_variable - my_var"
# - D) This code will fail

# ### Assignment Notes
# 
# - In programming `=` means assignment
# - There can be more than one assignment in a single line
# - Anything to the right of the `=` is evaluated before assignment
#     - This process proceeds from right to left

# ## Declaring Variables Cheat Sheet
# 
# - Names are always on the left of the `=`, values are always on the right
# - Names are case sensitive
# - Variables must start with letters (or underscores)
#     - After that, they can include numbers
#     - They cannot include special characters (like &, *, #, etc)
# - Python doesn't care what you name your variables
#     - Humans do care. Pick names that describe the data / value that they store

# ## Reserved Words
# 
# There are 33 words that are not allowed to be used for variable assignment in Python 3.9.

# In[9]:


False = 6


# <table type="text/css">
#   <tr>
#       <td><code>False</code></td>
#       <td><code>None</code></td>
#       <td><code>True</code></td>
#       <td><code>and</code></td>
#       <td><code>as</code></td>
#       <td><code>assert</code></td>
#       <td><code>break</code></td>
#   </tr>
#   <tr>
#       <td><code>class</code></td>
#       <td><code>continue</code></td>
#       <td><code>def</code></td>
#       <td><code>del</code></td>
#       <td><code>elif</code></td>
#       <td><code>else</code></td>
#       <td><code>except</code></td>
#   </tr>
#   <tr>
#       <td><code>finally</code></td>
#       <td><code>for</code></td>
#       <td><code>from</code></td>
#       <td><code>global</code></td>
#       <td><code>if</code></td>
#       <td><code>import</code></td>
#       <td><code>in</code></td>
#   </tr>
#   <tr>
#       <td><code>is</code></td>
#       <td><code>lambda</code></td>
#       <td><code>nonlocal</code></td>
#       <td><code>not</code></td>
#       <td><code>or</code></td>
#       <td><code>pass</code></td>
#       <td><code>raise</code></td>
#   </tr>    
#   <tr>
#       <td><code>return</code></td>
#       <td><code>try</code></td>
#       <td><code>while</code></td>
#       <td><code>with</code></td>
#       <td><code>yield</code></td>
#   </tr>    
# </table>

# In[10]:


# you will get an error if you try to assign a variable to one of these words
try = 6


# ## Kernels

# <div class="alert alert-success">
# The <b>kernel</b> is the thing that executes your code. It is what connects the notebook (as you see it) with the part of your computer that runs code. 
# </div>

# Your kernel also stores your **namespace** - all the variables and code that you have declared (executed). 
# 
# It can be useful to clear and re-launch the kernel. You can do this from the 'kernel' drop down menu, at the top, optionally also clearing all ouputs. Note that this will erase any variables that are stored in memory. 

# ## Namespace

# <div class="alert alert-success">
# The <b>namespace</b> is the 'place' where all your currently defined code is declared - all the things you have stored in active memory. 
# </div>

# In[11]:


get_ipython().run_line_magic('pinfo', 'whos')


# In[12]:


# You can list everything declared in the namespace with '%whos'
get_ipython().run_line_magic('whos', '')


# ## Variable Types

# <div class="alert alert-success">
# Every variable has a <b>type</b>, which refers to the kind of variable that it is, and how the computer stores that data.
# </div>

# In[13]:


# Declare a variable
variable_name = 1

# You can always ask Python 'what type is this variable' using:
type(variable_name)


# ### Int

# <div class="alert alert-success">
# <b>Integers</b> store whole numbers.
# </div>

# In[14]:


my_integer = 1
another_integer = 321


# In[15]:


# integers can be signed
yet_another_integer = -4
type(yet_another_integer)


# ### Float

# <div class="alert alert-success">
# <b>Floats</b> store signed, decimal-point numbers.
# </div>

# In[16]:


my_float = 1.0
another_float = -231.45


# In[18]:


type(my_float)


# ### String

# <div class="alert alert-success">
# <b>Strings</b> store characters, as text. 
# </div>

# In[19]:


my_string = 'words, words, words'
another_string = 'more words'

# Note that strings can be defined with either '' or ""
and_another = "and some more"


# In[20]:


print(and_another)
type(and_another)


# #### Quotation Marks
# 
# About those quotation marks...

# In[21]:


my_string = 'This is a single-quoted string.'
my_string


# In[22]:


my_string = "This is a double-quoted string."
my_string


# Note that Python will put single quotes around it, even if you specify double quotes. 
# 
# A general principle is to pick something and be consistent. In this course, I'll do my best to only use single quotes.

# #### Aside: What if you want to print a quotation mark?
# - use double quotes outside with apostraphe inside quotes
# - use an escape `\` (backslash) before character

# In[23]:


# double quotes on outside; single quote inside
my_string = "i wan't to see a quote."
my_string


# In[24]:


# backslash to "escape" quotation mark
string_quote = "And she said, \"Please teach me Python!\""
string_quote


# ## Boolean

# <div class="alert alert-success">
# <b>Booleans</b> store <code>True</code> or <code>False</code>. 
# </div>

# In[25]:


my_bool = True
another_bool = False


# In[26]:


type(another_bool)


# ## None

# <div class="alert alert-success">
# <code>None</code> is a special type that stores <code>None</code>, used to denote a null or empty value.
# </div>

# In[27]:


the_concept_of_nothing = None


# In[28]:


type(the_concept_of_nothing)


# #### Clicker Question #3
# 
# After executing the following code, what will the type of `var_a` be?

# In[29]:


var_a = -17.5
type(var_a)


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #4
# 
# After executing the following code, what will the type of `var_b` be?

# In[30]:


var_b = '-17.5'
type(var_b)


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #5
# 
# After executing the following code, what will the type of the variable `m` be?

# In[31]:


n = 1
a = 'm'
m = n
type(m)


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# ## Aliases

# <div class="alert alert-success">
# Variables are names assigned to a value. Values can have more than one name. 
# </div>

# In[32]:


# Make a variable, and an alias
a = 1
b = a
print(b)


# Here, the value 1 is assigned to the variable `a`.  
# 
# We then make an **alias** of `a` and store that in the variable `b`. 
# 
# Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

# ### Reminders

# - Multiple variables can relate to the same value(s)

# ### Mutable vs Immutable
# 
# The variable types we've talked about today are all **immutable**. This means they cannot be altered after they're created. 

# In[33]:


immutable_string = 'COGS18 is the best!'
immutable_string[4]


# In[34]:


# cannot change part of the string after creation
immutable_string[4] = '0'


# Python does have **mutable** types. We'll talk about these later in the course, and these are where aliasing shines!

# ## Indentation
# 
# Just a *brief* word on indentation.
# 
# Python *does* care about whitespace. 
# 
# You will get an error if Python runs into unanticipated whitespace.

# In[35]:


a = 1
    b = a
    
    print(b) 


# There *are* times when indentation will be required and expected. We'll discuss these in future lectures.

# 
# <center><img src="img/doing_it_right.png" width="900px"></center>
# 
