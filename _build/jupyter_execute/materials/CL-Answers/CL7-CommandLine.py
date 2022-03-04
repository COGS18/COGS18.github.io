#!/usr/bin/env python
# coding: utf-8

# # CL7: Command Line
# 
# Welcome to the seventh coding lab! 
# 
# **We will use this lab for two weeks in a row. This is not due until Wed. 3/2**
# 
# In this CodingLab we will be working with the command line, and with python files (module files and scripts). 
# 
# While this _may_ feel like busy work, understanding and completing this coding lab will be essential when it comes time for your project/final exam. Do your very best to complete all parts of this CodingLab!

# ## Part I: Command Line (Week 1)
# 
# Open a terminal from the Jupyter notebook server (either on your local computer or datahub), and do the following:
# 
# - Navigate to your desktop (or home directory on datahub)
# - Make a new directory
# - Move inside that directory
# - Create a new Python file
# - Open the file (this may be from the Files tab on datahub)
# - Write some Python code inside that file
#     - For example: print('Hello World')
# - Save the file (and return to the terminal
# - Execute the Python file from the terminal

# Describe your success/struggles/failures with the above steps here (These are notes to yourself/meant to describe to staff what you did here. This *could* be copy + paste of the code you typed into the terminal or just notes to yourself/staff describing what you learned/where you struggled.):
# 

# ## Part II: Module Files  (Week 1)
# 
# First, in the notebook below, do the following:
# 
# - Write at least one new Class
#     - Make sure there is at least one method in the class that returns something/prints something out
# - Write two new functions, that do something with instances of your new class(es)
#     - For example, take a list of custom objects, and call a method on each one

# In[ ]:


# Class(es) here

### BEGIN SOLUTION
# Classes here
class Noodles():
    def __init__(self, size = 'large', available = 'Yes'):
        self.size = size
        self.available = available
        
    def order_to_go(self):
        if self.available == None:
            out = "I'm sorry, but we aren't taking to-go orders right now."
        if self.available == 'Yes':
             out = "I'll have your order ready in 20 minutes"
        return out
### END SOLUTION


# In[ ]:


# function(s) here

### BEGIN SOLUTION
# new functions here
def eating(Noodles):
    if Noodles.available == 'Yes':
        print('Itadakimasu') # means "I will receive"; something you say before eating
        out = 'Slurp slurp slurp, delicious!'
    else:
        out = 'Quarantine can be rough. It be like that sometimes.'
    return out

def soup(Noodles):
    if Noodles.size == 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "I really shouldn't... There's too much sodium."
    if Noodles.size != 'large':
        out = "\n" + 'Should I drink the soup?' + "\n\t" + "You only live once! Slurp slurp slurp!"
    return out
### END SOLUTION


# Next, we are going to move this code to an external file - a Python module file. (**Week 2**)
# 
# - Open a new text file, from the Jupyter server page
# - Copy your classes and functions into that file
# - Save that file ***in the same folder/directory where this notebook is located***, with some name that you give it, and a '.py' extension.
# - Now, import the classes and functions from that file into the notebook, and check that you can use them. 

# In[ ]:


import ...

### BEGIN SOLUTION
import cravings as crave

tonkotsu = crave.Noodles()
print(crave.eating(tonkotsu))
print(crave.soup(tonkotsu))
### END SOLUTION


# ## Part III: Python Scripts (Week 2)
# 
# Now write a small script that imports from your module file, and uses that code to do something.
# 
# To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension ***in the same folder/directory where this notebook is located**, and then execute it from the terminal.

# In[ ]:


# (optional) You can draft your script before moving it 
# to an external file here     

### BEGIN SOLUTION
# I've stored the following few lines of code in a file 
# called `cravings_script.py`:
import cravings as crave

tonkotsu = crave.Noodles()
print(crave.eating(tonkotsu))s
print(crave.soup(tonkotsu))

# execute script
get_ipython().system('python cravings_script.py')
### END SOLUTION


# Explain your success/struggles/failures with the above here:

# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
