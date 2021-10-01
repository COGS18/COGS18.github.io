#!/usr/bin/env python
# coding: utf-8

# # Coding Lab 2: Programming I
# 
# 
# Welcome to the second coding lab!
# 
# CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each still fill out your own notebook for submission.
# 
# CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! If you explore something beyond what is required in the notebook, feel free to leave that exploratory code in the notebook you submit.
# 
# If you have a question about how something works / what something does - try it out, and see what happens! If you can't figure it out, reach out to your instructional staff - we're here to help!

# ## Part 1: Variables
# 
# Variables are used in Python to store values. 

# ### Defining Variables
# 
# Declare an int, float, string, and boolean. Fill them with with any values you want. 
# 
# Call them `my_int`, `my_float`, `my_string` and `my_boolean`. 

# In[1]:


### BEGIN SOLUTION
# specific values will differ
my_int = 12
my_float = 56.3
my_string = 'hello'
my_boolean = True
### END SOLUTION


# You'll see a lot of `assert` test cells throughout this course - most often in exams and assignments, but sometimes in coding labs. These are meant to ensure you're on the right track!
# 
# When you see `assert` followed by a variable name, that is Python checking to ensure that variable exists. If you mistyped the variable name above (when defining the variable name), you would get an assertion error when running the cell below. The assertion error will point to which `assert` led the error to be raised. It's then your job to go back to your code and figure out why the `assert` test failed!
# 
# If you're on the right track, there will be no output - or as you'll hear us say, these will "pass siltently". This doesn't guarantee your answer is right...but it let's you know you're on the right track!

# In[2]:


assert my_int
assert my_float
assert my_string
assert my_boolean


# Use the following cells to check the types of the variables you write are as expected

# In[3]:


type(my_int)


# In[4]:


type(my_float)


# In[5]:


type(my_string)


# In[6]:


type(my_boolean)


# Note that we could also use `assert` statements to test the type. If the `type` of `my_int` is an integer (`int`), this cell will "pass silently" (meaning give no output). If it raised an asserttion error, we would know we had done something wrong above.

# In[7]:


# test that my_int is an int
assert type(my_int) == int


# ## Part 2: Operators & Comparisons
# 
# Operators are used in Python to do things with variables. 

# ### Operator Questions

# First - explore using Python operators. Make sure you can add and subtract numbers, concatenate strings, do boolean comparisons, etc.

# In[8]:


## Do some exploring!

### BEGIN SOLUTION
# possible explorations
# Add & subtract numbers
print(1 + 2)
print(2 - 2)

# Concatenate string
print('ab' + 'cd')

# Boolean comparisons
print(True and True)
print(False or True)
### END SOLUTION


# Once you have explored using operators, try to answer some quesions using them. 
# 
# Let's start with an example: is the multiplication of 13 and 15 greater than 200?

# In[9]:


13 * 15 > 200


# Similar to that example, try to answer the following questions using Python variables & comparisons. You can assign the output to whatever variable name you like:
# - Is the remainder of dividing 323 by 13 greater than 6?
# - Is 7 to the power of 3 greater than or equal to 300?
# - Is 49 squared greater than 2500 or (boolean comparison) is 14 to the power of 3 greater than 2500
# - Is 49 modulus 9 equal to 67 modulus 9 and (boolean comparison) is the sum 49 & 67 modulus 9 greater than 7

# In[10]:


### BEGIN SOLUTION
323 % 13 > 6
7 **3 >= 300
49**2 > 2500 or 14**3 > 2500
49%9 == 67%9 and (49 + 67) % 9 > 7
### END SOLUTION


# ### Operator Challenges
# 
# The following are more challenging operator related questions. If they seem too tricky for now, just skip ahead to the next section.
# 
# Some more comparisons, with variable assignment:
# - Set the variable `comp_1` to the result of whether 17 squared is not the same as 867 divided by 3
# - Set the variable `comp_2` to the result of whether 4^3 is less than 3^4 **and** also greater than the remainder of dividing 1234 by 99
# 
# Bonus: both of the above questions can be written in (at least) two ways. 
# 
# If you found an answer to them, see if you can update the construction (by changing at least one operator) to answer the question in a different way. 
# 
# Note: x^y indicates 'x to the power of y'

# In[11]:


### BEGIN SOLUTION
comp_1 = not 17**2 == 289/3
comp_1 = 17**2 != 289/3

comp_2 = (3**4) > (4**3) > (1234 % 99)
comp_2 = ((3**4) > (4**3)) and ((4**3)) > (1234 % 99)
### END SOLUTION


# ### Operator Explorations
# 
# For each of the following questions, start by writing out your guess on the outcome. 
# 
# Then, test out each one by writing out some code. 
# 
# Finally, once you have answered the question using code, add a comment in markdown with the answer. 
# 
# Questions:
# - If you divide a float by an int, what is the type of the outcome? What about dividing an int by a float?
# - What happens if you multiply a string with a number?
# - The `+` sign works if you for adding numbers and for concatenating strings. Can you use `+` with a number and string in the same operation?
# - Since you can use `+` and `*` with strings, what happens if you try to substract two strings using `-`?

# In[12]:


### BEGIN SOLUTION
# possible explorations

# Dividing with a float and an int, in either order, returns a float
print(type(12.0/2))
print(type(12/2.0))

# Multiplying a string by a number repeats that string number times
'hodor ' * 8

# No, this code (when uncommented) fails. You cannot use '+' with a number and a string
# 12 + 'str'

# No, this code fails (when uncommented). You cannot use '-' with strings
# 'abc' - 'a' 
### END SOLUTION


# ## Part 3: Asserts
# 
# You will notice, through the coding labs and assignments, code that looks something like `assert True`, in which the assert statement is used.
# 
# Using assert essentially means to `assert that the following code is True`.
# 
# Or, slightly more formally, `assert that the following code evaluates as True`.
# 
# If the asserted code does not evaluate as True, it raises an error - meaning it interrupts the code execution because something went wrong.
# 
# This can be used as a way to test that code does what you expect it to do, and is therefore part of how we will test your code programmatically. 
# 
# Because the use of `assert` will be common in course materials, let's take a moment to explore how it works and what happens when we use it.

# In[13]:


# Declare a variable called `boolean` that  has type boolean, and passes the assert in the next cell


### BEGIN SOLUTION
boolean = True
### END SOLUTION


# In[14]:


# Check that there is variable called `boolean` that is a boolean
assert type(boolean) == bool


# In[15]:


# Check that the variable called `boolean` passes the assert
assert boolean


# ###  Assert Explorations
# 
# Now, explore using assert. What happens if you assert an integer, or a string? 
# 
# What happens if you assert None?
# 
# Find at least one integer that raises an assertion error. 

# In[16]:


### BEGIN SOLUTION
# specific asserts will vary 

# Asserting an integer asserts as True
assert 12

# Asserting a string asserts as True
assert 'hello'

# Asserting None asserts as False
assert None

# The integer 0 asserts as False (it gets interpreted as False)
assert 0

### END SOLUTION


# ## The End!
# 
# This is the end of this Coding Lab!
# 
# Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on Datahub!
