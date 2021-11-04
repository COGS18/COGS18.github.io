#!/usr/bin/env python
# coding: utf-8

# # Exam 2 Review (Answers)
# 

# ### Functions
# 
# - `def`
#     - `return`
# - executing a function
#     - parameters
#         - keyword vs. positional
#         - default values
#     - have a separate namespace
# - methods 
#     - in place vs. not in place

# #### Functions Question #1
# Write, in real code, a function called `remainder` that takes two inputs, divides the first input by the second and returns the remainder.

# In[1]:


## YOUR CODE HERE


# #### Functions Question #2
# Using the function `remainder` you wrote above, write the python code you would use to return the remainder of 10 divided by 4. Store the output in the variable `my_remainder`.

# In[2]:


## YOUR CODE HERE


# #### Functions Question #3
# Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

# In[3]:


def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total


# In[4]:


## CODE TO TEST HERE


# #### Functions Answers

# In[5]:


## Functions Quesiton #1

def remainder(num1, num2):  # set default values within parenthesis
    out = num1 % num2
    return out


# In[6]:


## Functions Question #2

my_remainder = remainder(10, 4)
my_remainder


# In[7]:


## Functions Question #3
sum_list([1, 2, 3])


# ### Objects & Classes
# 
# - objects & `class`
#     - attributes
#     - methods
#     - instances
# 

# #### Objects & Classes Question #1
# 
# **Part A**
# 
# We want to simulate a rocket ship for a game.
# 
# Write code that will create a class `Rocket`. 
# 
# This class should have two instance attributes: `x` and `y`. These will specify the x,y position of the rocket. Each attribute should be initialized with hte value 0. 
# 
# Your `Rocket` should also have the method `move_up()`. This method should increment the y-position of the rocket by 1. 

# In[8]:


## YOUR CODE HERE


# The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

# **Part B**
# 
# Create an instance `my_rocket` of your Rocket object.

# In[9]:


## YOUR CODE HERE


# **Part C**
# 
# Update `my_rocket` so that `my_rocket` has the `y` position 3.

# In[10]:


## YOUR CODE HERE


# #### Objects & Classes Question #2
# 
# Fill in the blanks:
# 
# 	What is the name of a function defined within a class: ______________
# 
# 	In Python, everything is a(n) ______________. 
# 

# #### Objects & Classes Answers
# 
# Question #1A: 

# In[11]:


class Rocket():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def move_up(self):
        self.y += 1


# Question #1B:

# In[12]:


my_rocket = Rocket()


# Question #1C:

# In[13]:


my_rocket.move_up()
my_rocket.move_up()
my_rocket.y


# Question #2: 
# - method
# - object

# ### Python & Jupyter Extras
# - encodings (`chr` & `ord`)
# - whitespace
# - namespace
# - kernel
# - code comments
# - magic functions

# #### Extras Question #1
# What will the following piece of code print out?
# 
# ```print(chr(ord('A')))``` 
#     
#      _____________

# #### Extras Question #2 
# 
# What is the magic function `%whos` used for?

# #### Extras Question #3
# 
# For each of the following, indicate if the statement is True or False about Python and programming:
# 
# - True/False Whitespace matters in Python
# - True/False Comments in Python start with '%' 					
# - True/False You have to specify a data type when you define a variable
# - True/False Every Python variable is available from every namespace		
# - True/False `ls` is a shell command that creates a new file 		
# - True/False `cd` returns your current working directory		
# - True/False Everything in Python is an object
# - True/False `print_name()` folles best practices for function naming

# #### Extras Answers

# In[14]:


# Extras Question #1
print(chr(ord('A')))


# Extras Question #2
# 
# returning information about what objects are stored in your namespace (i.e. variables, functions, classes, etc.)

# In[15]:


get_ipython().run_line_magic('whos', '')


# Extras Question #3
# 
# For each of the following, indicate if the statement is True or False about Python and programming:
# 
# - **True**/False Whitespace matters in Python
# - True/**False** Comments in Python start with '%' 					
# - True/**False** You have to specify a data type when you define a variable
# - True/**False** Every Python variable is available from every namespace		
# - True/**False** `ls` is a shell command that creates a new file 		
# - True/**False** `cd` returns your current working directory		
# - **True**/False Everything in Python is an object
# - **True**/False `print_name()` follows best practices for function naming

# <h2><center>After the second exam:</center></h2>

# <h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

# <h3><center> We also become a project based course. </center></h3>
