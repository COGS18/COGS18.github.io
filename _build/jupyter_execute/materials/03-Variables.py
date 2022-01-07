#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL1** has been graded; opportunity to resubmit for full credit by Sunday night
# - Pre-course survey "due" tonight (optional for EC; 11:59 PM)
# - **A1** now available; due Mon 1/17 (11:59 PM)
#     - Discuss: completion, `raise NotImplementedError()`, `asserts`, hidden tests, validate, Kernel

# **Q&A**
# 
# Q: I understand the notebook but I am still unsure as to what we need to do to it? Is it just for us to have and follow along during lecture or do we need to turn it in?  
# A: For lecture notes, what you do with the notebook is totally up to you. If I were taking the class, I'd follow along and add my notes to the Jupyter notebook and use that for studying. You do NOT turn your notes in. *However*, we will be using notebooks for labs, assignments, and exams. In those cases you *will* submit the notebook on datahub.
# 
# Q: Is it possible to pull from external libraries in this notebook?  
# A: (First, this is not required knowledge for COGS 18 students at this point) Yup! Some libraries have already been installed for you on datahub (`pandas`, `numpy`, etc.) and can be imported directly. For those not yet installed, you would have to install prior to being able to import into the notebook.
# 
# Q: What is anaconda?  
# A: Anaconda is a distribution of Python, Jupyter Notebooks, and additional software packages that make scientific computing possible. Unlike datahub (which lives on UCSD computers and to which you'll *eventually* lose access), Anaconda "lives" on your computer, giving you access to all the technology used in this class after COGS 18 ends.
# 
# Q: For the In [ ] part that shows how many times the cell is run, you said that for assignments/coding labs to keep everything in order. If we were to go back and forth/if we had to recheck something and it becomes out of order would we lose points for this? Or is there a way to clear it and get it to the right number?  
# A: Yup - going back and forth as you do the assignment/lab is totally normal. At the end, once you're finished "Kernel > Restart and Run All" will run your code from top to bottom. Good practice to get into right before you submit!
# 
# Q: For the coding time part, since it was possible to have multiple answers does it mean that there isn't a definite answer? Would this also apply to exams or is there a specific answer?  
# A: Yes. Sometimes on exams there are multiple approaches. So long as what you do follows the instructions, it will be correct.
# 
# Q: I have a question about the Practice Coding Lab. The code was favorite_class = 'A', but there was no output. The code is correct, so why is there no output. What is the difference between this code and a code that does have an output.  
# A: We'll discuss this more today! This is because you created a variable `favorite_class`. To see what is stored in that variable, you could add the line `favorite_class` beneath what you've written and it will display your choice.
# 
# Q: I am curious whether we can have access to these notes ahead of time like a week in advance if possible because I need to read over them a few times before lecture to be able to understand the professor faster or be on her pace.   
# A: I typically edit these the morning of lecture. I'll *try* to get them out the day before...but I can't make any promises. I wish I could get them done sooner! That said, older versions of the notes are available [here](https://github.com/COGS18/Materials)...so that could be a place to start. I start with these versions of the notes and update them for this quarter before class, so the notes at that link will be similar to what's presented in class.
# 
# Q: Everything is great, Dr. Ellis, can you please speak a bit slower? That will help do digest information.  
# A: A totally reasonable request - I'll work on this! (Not an excuse, but on Zoom, it's harder for me b/c I can't see your faces and see that I'm going too fast...so I'll just have to be more conscious of this. I *know* I speak too fast and am working on it. Thanks for this request!)
# 
# Q: I'm still curious about any other resources we'll be using throughout the quarter.  
# A: We've now covered all of the tools we'll be directly using this quarter.
# 
# Q: I couldn’t get command z to undo anything and the lecture said that is how you can undo. Is there a way to undo other than that?  
# A: Be sure the cell where you wanted to undo was selected. The other option is from the Edit menu at the top of the notebook.
# 
# Q: I know that it is recommended to download Anaconda if you intend to do the project at the end of the quarter, but how exactly would this program be more helpful than just using Jupyterhub for the project? I was considering downloading but still wasn't sure what the actual benefits were to using it, especially if by the end of the quarter I feel more comfortable with Jupyterhub.  
# A: Main benefits: 1) having acccess to technology after the course ends (And you lose access to datahub) and 2) datahub is web-based, which requires access to the Internet. At the end of the quarter, datahub gets quite busy so it can be slow *and* it occassionally goes down for a bit of time given all the students working on it. Having it on your computer avoids these issues. That said, most students choose to complete the final project on datahub given their comfort.
# 
# Q: Does it matter if we use Markdown or HTML tags in our Coding Labs should they be asked for?  
# A: Nope - you could use either.
# 
# Q: Is the final project and the final exam the same thing or different? and do we have to complete both?  
# A: You will choose to do either the exam or the project. We'll discuss later.
# 
# Q: Must this survey be submitted on the same day as the lecture?   
# A: Nope. If the lecture is available from the drop-down menu, then you can get credit.
# 
# Q: Are we going to use datahub during exam?  
# A: Yes.

# # Variables
# 
# - Definition
# - Namespace
# - Code Style
# - Variable types

# **Vocab**
# 
# - **Variable**: The name given to something in programming that stores some information
# - **Definition**/**Assignment**/**Declaration**: To create a variable using the assignment operator `=`

# ## Programming With Python

# Programming: a way to ask computer to store values (variables), and do things with them (operations).`

# In[ ]:


# This is a comment. You can write a comment by using a `#`
my_variable = 12 

my_other_variable = 13 # Comments can be 'inline', like this one


# ### Defining Variables

# <div class="alert alert-success">
# In programming, variables are things that store values. Variables are defined with <code>name = value</code>.
# </div>

# In[ ]:


my_var = 1  # `my_var` is a variable

# This defines another variable
other_var = 'variables are cool'


# In[ ]:


# once you create a variable it's stored in your namespace
other_var


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

# In[ ]:


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

# In[ ]:


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
# There are 33 words that are not allowed to be used for variable assignment in Python 3.6.

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

# In[ ]:


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

# In[ ]:


get_ipython().run_line_magic('pinfo', 'whos')


# In[ ]:


# You can list everything declared in the namespace with '%whos'
get_ipython().run_line_magic('whos', '')


# ## Code Style
# 
# Code style considerations *do NOT affect the functionality* of your code, but *DO affect readability*.
# 
# Get in good habits now!

# For variable assignment: 
# - we use a single space around assignment operator `=`
# - we use **snake_case** for variable names (All lowercase, underscores between words)
# - use informative variable names...something that tells you a bit about what's being stored

# - Ideal: `my_variable = 6`
# - Avoid: `MyVariable=6`

# ## Variable Types

# <div class="alert alert-success">
# Every variable has a <b>type</b>, which refers to the kind of variable that it is, and how the computer stores that data.
# </div>

# In[ ]:


# Declare a variable
variable_name = 1

# You can always ask Python 'what type is this variable' using:
type(variable_name)


# ### Int

# <div class="alert alert-success">
# <b>Integers</b> store whole numbers.
# </div>

# In[ ]:


my_integer = 1
another_integer = 321


# In[ ]:


# integers can be signed
yet_another_integer = -4
type(yet_another_integer)


# ### Float

# <div class="alert alert-success">
# <b>Floats</b> store signed, decimal-point numbers.
# </div>

# In[ ]:


my_float = 1.0
another_float = -231.45


# In[ ]:


type(another_float)


# ### String

# <div class="alert alert-success">
# <b>Strings</b> store characters, as text. 
# </div>

# In[ ]:


my_string = 'words, words, words'
another_string = 'more words'

# Note that strings can be defined with either '' or ""
and_another = "and some more"


# In[ ]:


print(and_another)
type(and_another)


# #### Quotation Marks
# 
# About those quotation marks...

# In[ ]:


my_string = 'This is a single-quoted string.'
my_string


# In[ ]:


my_string = "This is a double-quoted string."
my_string


# Note that Python will put single quotes around it, even if you specify double quotes. 
# 
# A general principle is to pick something and be consistent. In this course, I'll do my best to only use single quotes.

# #### Aside: What if you want to print a quotation mark?
# - use double quotes outside with apostraphe inside quotes
# - use an escape `\` (backslash) before character

# In[ ]:


# double quotes on outside; single quote inside
my_string = "i wan't to see a quote."
my_string


# In[ ]:


# backslash to "escape" quotation mark
string_quote = "And she said, \"Please teach me Python!\""
string_quote


# ## Boolean

# <div class="alert alert-success">
# <b>Booleans</b> store <code>True</code> or <code>False</code>. 
# </div>

# In[ ]:


my_bool = True
another_bool = False


# In[ ]:


type(another_bool)


# ## None

# <div class="alert alert-success">
# <code>None</code> is a special type that stores <code>None</code>, used to denote a null or empty value.
# </div>

# In[ ]:


the_concept_of_nothing = None


# In[ ]:


type(the_concept_of_nothing)


# #### Clicker Question #3
# 
# After executing the following code, what will the type of `var_a` be?

# In[ ]:


var_a = -17.5


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #4
# 
# After executing the following code, what will the type of `var_b` be?

# In[ ]:


var_b = '-17.5'


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# #### Clicker Question #5
# 
# After executing the following code, what will the type of the variable `m` be?

# In[ ]:


n = 1
a = 'm'
m = n
type(m)


# - A) String
# - B) Int
# - C) Float
# - D) Boolean
# - E) None

# ### Mutable vs Immutable
# 
# The variable types we've talked about today are all **immutable**. This means they cannot be altered after they're created. 

# In[ ]:


immutable_string = 'COGS18 is the best!'
immutable_string[4]


# In[ ]:


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

# In[ ]:


a = 1
    b = a
    
    print(b) 


# There *are* times when indentation will be required and expected. We'll discuss these in future lectures.

# 
# <center><img src="img/doing_it_right.png" width="900px"></center>
# 
