#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A4** due tonight (11:59 PM)
# - **CL7** due Wednesday

# Looking forward:
# - **CL8** due *next* Wed 3/9
# - **A5** due *next* Fri 3/11
# - **Final exam/project** due Mon 3/14
#     - Project: Submit on either Canvas or datahub
#         - if you submit on datahub, Canvas will say your project is "missing" - it's NOT missing; if you see under submitted assignments on datahub, you're fine
#         - when you submit on datahub, it will *look* like only your notebook is submitted; I promise everything in the folder is submitted
#         - I reach out to students who do not submit either a final exam/final project, so if you don't hear from me on Tuesday of finals week, your submissi0n is fine.
#     - Exam: Complete and submit on datahub; there will be a practice exam

# **Q&A**
# 
# Q: Is the final exam a project or will it have questions similar to the previous exams we have taken?   
# A: The final exam is a "mini project" - there will be a practice final exam so you can see. There will be a few questions similar to previous exams but it will also involve modules, documentation, and testing (the material focused on the last few weeks), which will involve .py files along with a jupyter notebook.
# 
# Q: For the final project I have a few ideas, but after looking at some examples I am feeling a bit scrambled. I know Andrew said that he had some trouble thinking of how to start, and I was wondering there could be some more explanation on maybe a general process of the final project?  
# A: I will do a demo final project in class during week 10, but we would love you to get started before that, so office hours can be a great place to get your thoughts sorted out!
# 
# Q: how difficult will the final exam be?  
# A: About as difficult as previous exams. There will be less coding but more "pieces" that have to fit/work togeter (see first Q from today)
# 
# Q: I am wondering how to come up with a project, or know if something is within my knowledge to create? I have some ideas but they feel too ambitous  
# A: We can help you scope your project during office hours!
# 
# Q: Were the banned topics listed in class the only banned topics, or are there more?  
# A: Those are the only ones. Generally, it's in your best interest NOT to choose a project where there's a whole bunch of code already online. You just want to avoid using someone else's code and claiming it as your own. (You *can* use someone else's code, but you must cite it and it cannot count as your original code).
# 
# Q: Can the Final Project be Assignment style where I pretend I am the professor of a class assigning a task (haha)?  
# A: Sure! Just be sure you plan out ahead of time what your three original functions/methods would be and the general approach. Like, is this game-like? Or are you building a system to help profs make assignments? something else?
# 
# Q: When I try to use 'vi new_script.py' in the terminal on datahub, I get an error message saying a swap file already exists ".new_script.py.swp". I chose 'edit anyway' but then it doesn't let me edit the file. Is there a way to fix this?  
# A: This is a question for office hours. We'd have to see your computer specifically.
# 
# Q: Do we get partial points on the final exam if we get part of the code right?   
# A: Yes
# 
# Q: For the project what software can I use to work on it away from datahub?  
# A: Anaconda - see last part of the first coding lab 
# 
# Q: For the final exam, it is said that we can't get A+ does that mean if we have an A+ at the end will it be brought to an A or does it mean that if we have an A it can't be brought to an A+?  
# A: The former. If you do the final exam, the highest grade you can get is an A.
# 
# Q: How will the extra credit be applied to the final project based on component we needed additionally?  
# A: If you go above and beyond, we will award up to 4% on the final project. This will be part of your project grade

# # Modules & Scripts
# 
# - namespaces & scope
# - modules
# - `import`
#     - `from`
#     - `as`

# ## Namespaces & Scope

# <div class="alert alert-success">
# A <b>namespace</b> is a 'place' with a set of names and their corresponding objects.
# </div>

# Each Jupyter Notebook has its own Namespace.
# 
# If you have two notebooks open at the same time, they don't know about eachother or what variables have been created in the other.

# Names that are defined and available in a given namespace are in **scope**.

# That is, the *scope* of an object is where it is available to / from. 

# In[1]:


# see what's stored in global namespace
a = 3
b = 15
get_ipython().run_line_magic('whos', '')


# ## Modules & Packages

# <div class="alert alert-success">
# A <b>module</b> is a set of Python code with functions, classes, etc. available in it. A Python <b>package</b> is a directory of modules.
# </div>

# Modules are stored in Python files (.py). We can import these files into our namespace, to gain access to the module within Python.

# In A3 you had to import the package: `nltk`: 
# 
# - **package** is a whole bunch of modules
# - a **module** stores python (.py) files
# - when imported, we have access to its functionality

# ## `import`

# <div class="alert alert-success">
# <code>import</code> is a keyword to import external code into the local namespace.
# </div>

# Why do it this way (importing modules)? 
# 
# 1. Minimize startup costs
# 2. Functions in different packages could have the same name - break programs

# ### `import` example: math module

# For something not yet in your Namespace...

# In[2]:


# we haven't imported the module yet
# this code fails if you haven't yet imported math
type(math)


# In[3]:


# Import the math module
import math


# In[4]:


# Check the type of math
type(math)


# In[ ]:


math.


# In[5]:


# By the way - modules are objects
isinstance(math, object)


# In[6]:


# Using code from our math module
# remember to tab complete or use dir(math)
math.sqrt(9)


# ### `import` example: random module

# In[7]:


import random


# In[8]:


# Random is also a module
type(random)


# In[9]:


# Explore what is available in random
dir(random)


# In[ ]:


# working with random
random.


# In[10]:


## access documentation
get_ipython().run_line_magic('pinfo', 'random.choice')


# In[11]:


## access underlying code
get_ipython().run_line_magic('pinfo2', 'random.choice')


# ### `random` Example

# In[12]:


# random.sample() documentation
get_ipython().run_line_magic('pinfo', 'random.sample')


# In[14]:


# Random example
to_choose_from = ['1', '2', '3', '4', '5']
number_to_choose = 2

chosen = random.sample(to_choose_from, number_to_choose)

print(chosen)


# ## Imports: `from` & `as`

# <div class="alert alert-success">
# <code>from</code> and <code>as</code> allows us to decide exactly what objects to import into our namespace, and what we call them (in our namespace).
# </div>

# In[15]:


# Import a specific object from a module
from random import choice


# In[16]:


## do NOT have to type module name 
## using this approach
## to call this
choice(to_choose_from)


# In[17]:


# Import a module with a specific name in our namespace
# used when module names are long
import collections as cols


# In[ ]:


## collections is not defined
## this code will fail
collections.


# In[ ]:


# this is how you would do it
cols.


# In[20]:


punctuation


# In[19]:


punc


# In[18]:


# putting it all together
# Import a specific thing and give it a specific name
from string import punctuation as punc


# #### Clicker Question #1
# 
# Which of the following is NOT a valid Python import statement?
# 
# - A) `import collections as col`
# - B) `from statistics import mean as average`
# - C) `from os import path`
# - D) `from random import choice, choices`
# - E) `import ascii_letters from string`

# #### Clicker Question Answer

# In[21]:


# Check our imports
# import collections as col
# from statistics import mean as average
# from os import path
# from random import choice, choices
import ascii_letters from string


# ## Importing Custom Code I

# Why do this? 
# 
# Having a whole bunch of functions in a Jupyter Notebook will start to get clutered.
# 
# Also, they're not reusable later without copying them into your new notebook. 
# 
# Modules avoid this!

# ## module: `remote.py`
# 
# If you want to practice using import with the `remote` example in lecture, store the code in the next cell in a text file saved as `remote.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[ ]:


def my_remote_function(input_1, input_2):
    """A function from far away.
    
    This function returns the sum of the two inputs.
    """
    
    return input_1 + input_2

def choice(list_to_choose_from):
    """Choose and return an item from a list. 
    
    Notes: I am a custom choice function: I am NOT from `random`.
    
    Hint: my favorite is the last list item.
    """
    
    return list_to_choose_from[-1]

class MyNumbers():
    
    kind_of_thing = 'numbers'
    
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        
        return self.num1 + self.num2
    
    def subtract(self):
        
        return self.num2 - self.num1


# In[1]:


# Import some custom code
from remote import my_remote_function


# In[2]:


# Investigate our imported function
get_ipython().run_line_magic('pinfo', 'my_remote_function')


# In[3]:


# Run our function
my_remote_function(2, 1)


# ## Importing Custom Code II

# In[4]:


# Import a class class from an external module
from remote import MyNumbers


# In[5]:


# Define an instance of our custom class
nums = MyNumbers(2, 3)
type(nums)


# In[6]:


# Check 
nums.add()


# In[7]:


# Check the definition of the code we imported
get_ipython().run_line_magic('pinfo2', 'nums.add')


# ## Name Conflicts

# In[17]:


from random import choice


# In[9]:


# choice is currently from random module
get_ipython().run_line_magic('pinfo', 'choice')


# In[18]:


choice([1, 2, 3, 4, 5])


# In[19]:


from remote import choice


# In[12]:


# now it's from my remote module
get_ipython().run_line_magic('pinfo', 'choice')


# In[20]:


choice([1, 2, 3, 4, 5])


# While you _can_ have functions with the same name in two different places...do your best to avoid this.
# 
# It's Python legal but bad for your nerves.

# ## A note on `*`
# 
# If you see `from module import *` this means to import everything (read as 'from module import everything'). 
# 
# This is generally considered not to be the best, as it is then unclear in your code exactly where the functionality came from.

# In[ ]:


# avoid this
from random import *
choice()


# In[21]:


# a valid way to import
from random import choice
choice([2,3,4])


# In[22]:


# a valid way to import
import random
random.choice([2,3,4])


# ## script: `remote_script.py`
# 
# 
# If you want to run your own script example in lecture, store the code in the next cell in a text file saved as `remote_script.py`. Be sure this is saved in the same directory (folder) as the notebook from which you're trying to call it.

# In[ ]:


from remote import MyNumbers
nums = MyNumbers(2, 3)
print("nums value: ", nums)
print("nums type: ", type(nums))


# In[23]:


# run the script
get_ipython().system('python remote_script.py')

