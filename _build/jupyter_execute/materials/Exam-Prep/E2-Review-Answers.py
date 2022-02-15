#!/usr/bin/env python
# coding: utf-8

# # Exam 2 Review (Answers)
# 

# ### Loops

# #### Loops Question #1
# What are the two kinds of loops? ____________ and ____________

# #### Loops Question #2
# Use the following:
# `ind = 1` to write a loop (using real Python code) that would loop and print the value `ind` of ind each time through the loop _and_ update the value of ind by 1. Have this loop stop after 4 iterations. 

# In[3]:


## YOUR CODE HERE


# #### Loops Question #3
# 
# Create a list that stores each letter of your favorite animal as a different element in a list. Store that in the variable `fav_pet`. 
# 
# Initialize an additional variable called `reverse_pet` that will store an empty list to start.
# 
# Then, using indexing, loop through each letter in that list such that `reverse_pet` stores a list with your favorite pet spelled backward.
# 
# For example, if your favorite pet were "cat", the output stored in `reverse_pet` should be: `['t', 'a', 'c']`
# 

# In[8]:


## YOUR CODE HERE


# #### Loops Question #4
# Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

# In[10]:


def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total


# In[4]:


## CODE TO TEST HERE


# #### Loops Answers
# 

# **Loops Question #1**
# 
# `for` and `while`

# **Loops Question #2**

# In[3]:


# Loops Question #2
ind = 1

while ind < 5:  # could also be <= 4
    print(ind)
    ind += 1


# **Loops Question #3**
# 

# In[8]:


=fav_pet = ['h', 'o', 'r', 's', 'e']

reverse_pet = []
index = -1

for ltr in fav_pet:
    reverse_pet.append(fav_pet[index])
    index = index -1

print(reverse_pet)


# **Loops Question #4**
# 

# In[11]:


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
# - **True**/False Everything in Python is an object
# - **True**/False `print_name()` follows best practices for function naming

# <h2><center>After the second exam:</center></h2>

# <h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

# <h3><center> We also become a project based course. </center></h3>
