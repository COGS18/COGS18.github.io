#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# - defining a function
#     - `def`
#     - `return`
#     - default values
#     - keyword vs. positional arguments
# - executing a function
#     - parameters
#     - separate namespace

# ## Vocab
# 
# - **Define/create/make** a function: To set up and write the instructions for a function.
# - **Execute/call/use** a function: To actually use the pre-defined function.
# 
# - **Input/parameter/argument**: A variable defined by the user that is put/passed in between the parantheses `()` that comes after the function name.  
# - **Output**: The variable that is `return`ed to the user after the function is executed.

# ## Functions
# 
# <div class="alert alert-success">
# A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
# </div>

# ![cheeseburger](img/cheeseburger.png)

# ## Modular Programming
# 
# <div class="alert alert-success">
# Modular programming is an approach to programming that focuses on building programs from independent modules ('pieces'). 
# </div>

# Copy + Pasting the same/similar bit of code is to be avoided.
# 
# **Functions** are one way to avoid this.
# 
# **Loops** are another! (we'll get to these soon...)

# ## Functions for Modular Programming

# - Functions allow us to flexibly re-use pieces of code
# - Each function is independent of every other function, and other pieces of code
# - Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
#     - This allows us to build up arbitrarily complex, well-organized programs

# In[ ]:


# you've seen functions before
# here we use the type() function
my_var = 3
type(my_var)


# In[ ]:


# the function print() doesn't depend on type()
# but they can both be used on the same variable
print(my_var)


# ## Function Example I
# 
# When you use `def`, **you are defining a function**.
# You are metaphorically writing the instructions for how to make the cheeseburger.

# In[ ]:


# define a function: double_value
# Notice that the parameter `num` is not explicitly defined with an = 
# This is because it will be defined later by the user when they execute the function.
def double_value(num):

    # do some operation
    doubled = num + num
    
    # return output from function
    return doubled    


# In[ ]:


# excecute a function by calling the function's name
# and defining the parameter within the parentheses
double_value(num = 2) 


# In[ ]:


# equivalent function call
# Here the parameter `num` is defined without 
# explicitly specifying the name of the parameter
double_value(2) 


# ## Function Example II
# 
# Here we are defining a function with multiple parameters

# In[ ]:


def add_two_numbers(num1, num2):
    
    # Do some operations with the parameters
    answer = num1 + num2
    
    # Return the variable answer
    return answer


# In[ ]:


add_two_numbers(5, 14)


# In[ ]:


# Execute our function again on some other inputs to double check 
# that our function is working how we think it should
output = add_two_numbers(-1, 4)
print(output)


# ## Function Properties

# - Functions are defined using `def` followed by the name of the function, parentheses `()`, parameters within the parentheses, and then `:` after the parentheses, which opens a code-block that comprises the function
#     - Running code with a `def` block *defines* the function (but does not *execute* it)

# - Functions are *executed* with the name of the function and parentheses - `()` without `def` and `:`
#     - This is when the code inside a function is actually run

# - Inside a function, there is code that performs operations on the available variables

# - Functions use the special operator `return` to exit the function, passing out any specified variables

# - When you use a function, you can assign the output (whatever is `return`ed) to a variable

# #### Class Question #1
# Given the function defined below, what will the second code cell below print out?
# 
# A) 0   &emsp;B) 2    &emsp;C) 4    &emsp;D) '2r.2 + 1'    &emsp;E) ¯\\\_(ツ)\_/¯

# In[ ]:


def remainder(number, divider):
    
    r = number % divider
    
    return r


# In[ ]:


ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

print(ans_1 + ans_2)


# #### Class Question #2
# 
# Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.
# 
# A) I did it! &emsp;B) I think I did it. &emsp;C) I tried but I am stuck. &emsp;D) Super duper lost

# In[ ]:


## YOUR CODE HERE  


# In[ ]:


# TEST YOUR FUNCTION HERE


# ## Default Values

# <div class="alert alert-success">
# Function parameters can also take <b>default values</b>. This makes some parameters optional, as they take a default value if not otherwise specified.
# </div>

# #### Default Value Functions
# 
# Specify a default value in a function by doing an assignment within the function definition.

# In[ ]:


# Create a function, that has a default values for a parameter
def exponentiate(number, exponent=2):  
    return number ** exponent


# In[ ]:


# Use the function, using default value
exponentiate(3)


# In[ ]:


# Call the function, over-riding default value with something else
# python assumes values are in order of parameters specified in definition
exponentiate(2, 3)


# In[ ]:


# you can always state this explicitly
exponentiate(number=2, exponent=3)


# ## Positional vs. Keyword Arguments

# <div class="alert alert-success">
# Arguments to a function can be indicated by either position or keyword.
# </div>

# In[ ]:


# Positional arguments use the position to infer which argument each value relates to
exponentiate(2, 3)


# In[ ]:


# Keyword arguments are explicitly named as to which argument each value relates to
exponentiate(number=2, exponent=3)


# In[ ]:


exponentiate(exponent=3, number=2)


# In[ ]:


# Note: once you have a keyword argument, you can't have other positional arguments afterwards
# this cell will produce an error
exponentiate(number=2, 3)


# Reminder, setting a default value for parameters is allowed during function *definition*.
# 
# (This may look like what we did above, but here we are including a default value for one parameter during function definition. During function *execution*, you can't mix and match using positional vs. keywords)

# In[ ]:


def exponentiate(number, exponent=2):    
    return number ** exponent


# #### Class Question #3
# 
# What will the following code snippet return?

# In[ ]:


def exponentiate(number, exponent=2):    
    return number ** exponent

exponentiate(exponent=3, number=2)


# - A) 8
# - B) 9
# - C) SyntaxError
# - D) None
# 

# Note: when using Keyword arguments position/order no longer matters

# ## Function Namespace 

# - Each function has its own namespace
# - Functions only have access to:
#     - variables explicitly passed into them
#     - variables defined inside the function

# In[ ]:


# You can check variables defined in the global namespace with `%whos`
get_ipython().run_line_magic('whos', '')


# ### Variables defined inside a function only exist within that function.

# In[ ]:


# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

print(my_var)


# In[ ]:


# define a function that uses my_var inside the function
def concat_self(my_var):
    
    my_var = my_var + ' ' + my_var
    
    return my_var

print(concat_self(my_var))


# In[ ]:


# see that my_var in global name space remains unchanged
print(my_var)


# In[ ]:


# only way to change my_var in global namespace
# is to assign to variable my_var in global namespace
my_var = concat_self(my_var)
print(my_var)


# ## Code Style: Functions
# 
# - Function names should be snake_case 
# - Function names should describe task accomplished by function
# - Separate out logical sections within a function with new lines
# - Arguments should be separated by a comma and a space
# - Default values do NOT need a space around the `=`

# ### Functions: Good Code Style

# In[ ]:


def remainder(number, divider=2):
    
    r = number % divider
    
    return r


# ### Functions: Code Style to Avoid

# In[ ]:


# could be improved by adding empty lines to separate out logical chunks
def remainder(number,divider=2): # needs space after comma
    r=number%divider # needs spacing around operators
    return r


# ## Summary
# - how to define a function
# - how to execute a function
# - default values
# - position vs. keyword arguments
# - global namespace vs. local namespace
# - code style
