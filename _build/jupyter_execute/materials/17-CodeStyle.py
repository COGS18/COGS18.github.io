#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**
# - **CL8** due tonight
# - **A5** due Friday of week 10 (12/3)
# - **Final exam/project** due Mon of Finals week (12/6; 11:59 PM)
#     - Final Exam will be released Friday afternoon of week 10

# **Q&A**
# 
# Q: I'm curious to see what other packages can be imported and used in order to create a cool project.   
# A: There are SO many. If there's a topic/thing you care about, there's likely a package for it. Search packages [here](https://pypi.org/)
# 
# Q: What is an example of when I would use the summing of integers in an array `(data.sum(axis=0))` ?  
# A: See coding lab and A5! But, imagine you have data stored in a dataframe where `1` indicated yes and `0` indicated no. If you wanted to know how many respondents in your dataset said yes, it would be helpful!
# 
# Q: For the where method of array, why we use np.where( ) while other methods we just use our variable names like arriving.sum( )  
# A: Great question! `where()` is a *function* while `sum()` is a method that operates on (meaning is defined within) the `numpy.array` object.
# 
# Q: One clarification question I had was for finding positions in arrays or dataframes, do we count from 0 as we would for collections?  
# A: Yup!
# 
# Q: What is the difference between zip and using index to loop through integers?  
# A: While these topics can be used together, they are distinct. Indexing allows you to specify a position in a collection. `zip` allows you to iterate through two collections at the same time.
# 
# Q: On average, about how long does it take to complete the final exam?  
# A: ~3 hours (but of course there is a range)
# 
# Q: Do we need to incorporate this into our final project/exam?  
# A: If you do the final exam, we will use `pandas`. If you're doing hte final project, you don't *have* to...unless it would be helpful to what you're trying to accomplish (so it could be helpful). It will be required for A5 and CL8.
# 
# Q: What are some careers that use either pandas or numpy?  
# A: Data Scientist, Data analyst, Machine learning engineer, Neuroscientist, Psychology/Psychiatry, Biology research in general, etc.
# 
# Q: Is there a way to display the array as "empty seats" like [   ]  and then put an x in it when someone does choose that seat?  
# A: Yup! There is an np.nan, where nan stands "for not a number" that you could use as a placeholder until you "fill" the seat.
# 
# Q: When will we learn more about the formatting for the project? (i.e. documentation)  
# A: Testing this Friday. Documentation on Monday. (Course schedule [here](https://cogs18.github.io/assets/intro/syllabus.html#course-schedule)).
# 
# Q: It seems part 0 in CL8 has some problem: after I type "import np" and "import pd" there is an error saying there are no such modules?  
# A: Refer back to the notes on how to import these packages properly
# 
# Q: What is the grade breakdown for this class?  
# A: https://cogs18.github.io/assets/intro/syllabus.html#grading-attendance
# 
# Q: Why aren't you teaching COGS 108 next quarter? :(  
# A: Teaching a new course is *a lot* of work. So, Jason Fleischer (students love him!) taught COGS 108 for the first time this Fa21 quarter. To allow him to utilize all that work again, he'll teach it this winter as well. I'll be back to teaching it next academic year...but I know that may not be what you want to hear.
# 
# Q: What's the difference between 'replace = True' and 'replace = False' in parenthesis for the sample method?  
# A: This has to do with sampling with and without replacement (a statistics concept). Explanation [here](https://www.statisticshowto.com/sampling-with-replacement-without/).
# 
# Q: If we flat out did not understand today's topic, and we are not taking the final exam but doing the project instead, should we make sure we understand it or will we technically not be needing it?  
# A: You'll need it for CL8 and A5. 
# 
# Q: An we sit in the coding lab during week 10 and work on our projects even if we don't necessarily have a question before coming in?  
# A: Absolutely! Sometimes during week 10 students come in and stay for a handful of hours just to have a dedicated space/time to focus on the project. That's more than welcome!
# 
# Q: I also signed up for cogs 108 too (but waitlisted, would you know how many people get off the waitlist for this class?)  
# A: I can't say for sure. Typically it's ~3-5/section.
# 

# **E2 Notes**
# - Scores were posted on Mon; regrades due Thurs night
# - Functions:
#     - default values for parameters: `def wear_mask(group_size, location='indoors', vaccinated=True):`
# - Classes: 
#     - attributes vs parameters
#     - when the heck to use `self`

# **Q8**: `TaskCalculator()`
# 
# - when to use `self`
#     - first input "parameter" to any `def`
#     - any time you want to reference an instance attribute

# In[1]:


# from the answer key
class TaskCalculator():
        
    def __init__(self):  # why no parameter here
        self.daily_tasks = []
        
    def add_task(self, task):
        self.daily_tasks.append(task)
        
    def calculate_time(self):
        # if you want to use a variable, it must be an attribute, defined within method, or passed in as input
        long_tasks = ['write one exam', 'grade exam', 'prep lecture', 'office hours']
        short_tasks = ['review lecture', 'grade assignment', 'staff meeting', 'answer email']
        
        time_sum = 0
        
        for val in self.daily_tasks: # must use self to reference attribute!
            if val in long_tasks:
                time_sum += 2  # equivalent to time_sum = time_sum + 2
            elif val in short_tasks:
                time_sum +=1
                
        return time_sum


# In[5]:


### test it out
my_task = TaskCalculator()
my_task.daily_tasks


# In[6]:


my_task.add_task('test task')
my_task.add_task('write one exam')

my_task.daily_tasks


# In[7]:


my_task.calculate_time()


# # Code Style
# 
# - PEP8
# - spacing
# - line length
# - comments

# Or: How to be Pythonic

# Reasons to be Pythonic:
# - user friendly for humans
# - extra work up-front on the developers (pays off on the long run)
# - best to practice this early on (I promise!)

# ## Style Guides

# <div class="alert alert-success">
# Coding style refers to a set of conventions for how to write good code. 
# </div>

# Consistency is the goal. Rules help us achieve consistency.

# Much of this will apply to other programming languages, so it's good to learn...regardless of language.
# 
# Some of these Code Style notes will be more specific to Python, however.

# ## The Zen of Python

# In[8]:


import this


# ### Program Errors vs. Stylistic Issues
# 
# - Programmatic Error: something that breaks the code
# - Stylistic Issue: something that doesn't break the code, but is considered bad style - makes your code harder to understand

# ## Picking a Style Guide
# 
# - Code style is (at least partly) subjective
# - Consistency is key. It's easier to recognize & read consistent style

# ## Python Enhancement Proposals (PEPs)

# <div class="alert alert-success">
# Python PEPs are proposals for how something should be / work in the Python programming language. 
# </div>

# These are written by the people responsible for the Python Programming language.

# PEP are voted on before incorporation.

# ## PEP8

# <div class="alert alert-info">
# <b><a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a></b> is an accepted proposal that outlines the style guide for Python.
# </div>

# Defines the style guide for Pythonistas (people who code in Python).

# ## General Concepts

# - Be Explicit & Clear
#     - Prioritize Readability over 'Cleverness'
# - There should be specific, standard ways to do things
#     - Use them
# - Coding Style are guidelines, designed to help the code
#     - They are not laws

# ## Specific Guidelines - Structure
# 
# - blank lines
# - indentaion
# - spacing 
# - length
# - imports

# ### Blank Lines
# 
# - Use 2 blank lines between functions & classes, and 1 between methods
# - Use 1 blank line between segments to indicate logical structure

# This allows you to - at a glance - identify what pieces of code are there.

# In[9]:


# Badness
def my_func():
    my_nums = '123'
    output = ''
    for num in my_nums:
        output += str(int(num) + 1)
    return output


# In[10]:


my_func()


# In[ ]:


# Goodness
def my_func():   
    my_nums = '123'
    output = ''
    
    for num in my_nums: 
        output += str(int(num) + 1)
    
    return output


# Note that documentation here is missing (as are comments). This is to highlight the spacing. You'll need documentation and comments.
# 
# I promise it's better to comment as you go along rather than coming along after you've written all the code and adding comments.
# 
# Similar to writing: write comments -> write code -> review code & comments

# #### Clicker Question #1
# 
# Which of these is best - A, B, or C?

# In[ ]:


# Option A
def squared(input_number):
    val = input_number
    power = 2    
    output = val ** power
    return output


# In[ ]:


# Option B
def squared(input_number, power=2):
    
    output = input_number ** power
    
    return output


# In[ ]:


# Option C
def squared(input_number):
    
    val = input_number
    power = 2
    
    output = val ** power
    
    return output


# ### Indentation
# 
# Use spaces to indicate indentation levels, with each level defined as 4 spaces. 

# In[11]:


# Badness
if True:
  print('Words.')


# In[12]:


# Goodness
if True:
    print('Words.')


# ### Spacing
# 
# - Put one (and only one) space between each element
# - Index and assignment don't have a space between opening & closing '()' or '[]'

# In[13]:


# Badnesses
my_var=1+2==3
my_list  =  [ 1,2,3,4 ]
el = my_list [1]


# In[14]:


# Goodnesses
my_var = 1 + 2 == 3
my_list = [1, 2, 3, 4]
el = my_list[1]


# #### Clicker Question #2
# 
# Which of the following uses PEP-approved spacing?
# 
# - A) `my_list=[1,2,3,4,5]`
# - B) `my_list = [1,2,3,4,5]`
# - C) `my_list  =  [1, 2, 3, 4, 5]`
# - D) `my_list=[1, 2, 3, 4, 5]`
# - E) `my_list = [1, 2, 3, 4, 5]`

# ### Line Length
# 
# - PEP8 recommends that each line be at most 79 characters long

# Computers used to require this.
# 
# But, super long lines are hard to read at a glance.

# ### One Statement Per Line
# 
# - While you *can* condense multiple statements into one line, you usually shouldn't.

# In[15]:


# Badness
for i in [1, 2, 3]: print(i**2 + i%2)


# In[ ]:


# Goodness
for i in [1, 2, 3]:
    print(i ** 2 + i % 2)


# ### Multi-Line

# In[ ]:


my_long_list = [1, 2, 3, 4, 5,
                6, 7, 8, 9, 10]


# In[16]:


# Note: you can explicitly indicate a new line with '\'
my_string = 'Python is ' +             'a pretty great language.'


# ### Imports
# 
# - Import one module per line
# - Avoid `*` imports
# - Use the import order: standard library; 3rd party packages; local / custom code

# In[ ]:


# Badness
from numpy import *

import os, sys


# In[ ]:


# Goodness
import os
import sys

import numpy as np


# Note: If you don't know how to import a local/custom module, figure that out this week in Coding Lab or office hours.

# ## Specific Guidelines - Naming

# ### Valid Names
# 
# - Use descriptive names for all modules, variables, functions and classes, that are longer than 1 character

# In[ ]:


# Badness
a = 12
b = 24


# In[ ]:


# Goodness
n_filters = 12
n_freqs = 24


# Find + Replace also works better when you have specific variable names 

# ### Naming Style
# 
# - CapWords (leading capitals, no separation) for Classes
# - snake_case (all lowercase, underscore separator) for variables, functions, and modules

# In[ ]:


# Badness
def MyFunc():
    pass
    
class my_class():
    def __init__():
        pass


# In[ ]:


# Goodness
def my_func():
    pass


class MyClass():
    def __init__():
        pass


# Note: snake_case is easier to read than CapWords, so we use snake_case for the things (variables, functions) that we name more frequently.

# #### Clicker Question #3
# 
# If you were reading code and came cross the following, which of the following would you expect to be a class?
# 
# - A) `Phillies_Game`
# - B) `PhilliesGame`
# - C) `phillies_game`
# - D) `philliesgame`
# - E) `PhIlLiEsGaMe`

# #### Clicker Question #4
# 
# If you were reading code and came cross the following, which of the following would you expect to be a function or variable name?
# 
# - A) `Phillies_Game`
# - B) `PhilliesGame`
# - C) `phillies_game`
# - D) `philliesgame`
# - E) `PhIlLiEsGaMe`

# ### Indicating Scope
# 
# - Leading underscores indicate a 'private' attribute or method of the class, meaning it is an internal value, not expected to be accessed by the user.

# In[ ]:


class MyClass():
    def __init__():
        self.public = None
        self._private = None


# The leading underscore indicates to the user that this attribute shouldn't be changed/modified by the user.
# 
# `import *` will not import underscored attributes (private attributes).

# ## Specific Guidelines - String Quotes

# In Python, single-quoted strings and double-quoted strings are the same. 
# 
# This PEP does not make a recommendation for this. **Pick a rule and stick to it.** 
# 
# When a string contains single or double quote characters: use the other one to avoid backslashes in the string. It improves readability.
# 
# 

# In[17]:


# Badness
my_string = 'Prof\'s Project'


# In[18]:


# Goodness
my_string = "Prof's Project"


# #### Clicker Question #5
# 
# Which of the following would not cause an error in Python and would store the string *You're so close!*  ?
# 
# - A) `my_string = "You're so close!"`
# - B) `my_string = "You"re so close!"`
# - C) `my_string = 'You''re so close!'`
# - D) `my_string = "You\\'re so close"`
# - E) `my_string = 'You're so close!'`

# In[ ]:


#my_string = "You're so close!"
#my_string = "You"re so close!"
#my_string = 'You''re so close!'
#my_string = "You\\'re so close!"
#my_string = 'You're so close!'
#my_string


# ## Specific Guidelines - Comments

# Out-of-date comments are worse than no comments at all.
# 
# Keep your comments up-to-date.

# #### Block comments
# - apply to some (or all) code that follows them
# - are indented to the same level as that code. 
# - Each line of a block comment starts with a # and a single space

# In[19]:


# Badness
import random

def week_8():
# help try to destress students by picking one thing from the following list using random
    statements = ["You've totally got this!","You're so close!","You're going to do great!","Remember to take breaks!","Sleep, water, and food are really important!"]
    out = random.choice(statements)
    return out

week_8()


# In[20]:


# Goodness
def week_8():
    
    # Randomly pick from list of de-stressing statements
    # to help students as they finish the quarter.
    statements = ["You've totally got this!", 
                  "You're so close!", 
                  "You're going to do great!",
                  "Remember to take breaks!",
                  "Sleep, water, and food are really important!"]
    
    out = random.choice(statements)
    
    return out

week_8()


# #### Inline comments
# - to be used sparingly
# - to be separated by at least two spaces from the statement
# - start with a # and a single space

# In[22]:


# Badness
week_8()#words of encouragement


# In[24]:


# Goodness
week_8()  # words of encouragement


# ## Specific Guidelines - Documentation
# 
# - Write a descriptive docstring for all functions & classes

# Note: If you're borrowing functions from an assignment, you should add documentation to these functions.

# Comments within the functions you've borrowed noting that you've borrowed it as well as a general note in your project description will suffice for attribution.
# 
# If you've modified/edited the code from the assignment, state that you modified.

# ## Linters

# <div class="alert alert-success">
# A linter is a tool that analyzes code for both programmatic errors and stylistic issues. 
# </div>

# `pylint` is available from Anaconda to check this for you. (Not available on datahub.)
# 
# 
# ```python
# # to install on datahub
# !pip install --user pylint
# ```

# #### Clicker Question #6
# 
# How many PEP8 violations can you find in this code?

# In[ ]:


def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq


# - A) None
# - B) 1 or 2 
# - C) 3 or 4 
# - D) 5 or 6
# - E) 7 or more

# ### list here
# 

# In[1]:


# Let's fix this code


# In[ ]:


# check using pylint
get_ipython().system('pylint linter_example.py')

