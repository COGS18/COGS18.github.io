#!/usr/bin/env python
# coding: utf-8

# # Python Syntax

# This notebook is a quick overview of the basic properties and syntax of Python. 

# ## Code
# 
# Computer code is a set of instructions, that can be interpreted and executed by a computer.

# In[1]:


my_variable = 12


# In[2]:


number_1 = 4
number_2 = 7

print(number_1 * number_2)


# ## Comments

# In[3]:


# Comments are denoted with '#'

my_var = 1 # Comments can also be inline


# ## Statements

# A statement is a piece of code that does something. 
# 
# Typically, in Python, a statement in Python equivalent to a line of code. 

# In[4]:


# This line of code is a statement
my_variable = 1


# You can explicitly end a line of code with `;`

# In[5]:


# Explicitly end a statement
my_val = 1;


# In[6]:


# In Jupyter, using the semi-colon also squashes printing
'A string that would usually print out';


# In[7]:


# With explicit statement ends, you can also write multiple statements into a single line
val_a = 1; val_b = 2;


# You can explicitly extend a statement across multiple lines of code using `\`

# In[8]:


# Write one statement across multiple lines
my_list = [1, 2, 3,            4, 5, 6,            7, 8, 9]


# ## Whitespace

# Python is a whitespace language, which means that it matters where there is 'blank' space around code.
# 
# This whitespace is used to interpret the organization of the code - an indentation in Python is used to indicate a code block. 

# In[9]:


# Example of marking code blocks with indentation

condition = True
if condition:
    #       ^ this colon opens a code block
    #       Everything below this colon, part of the same code block, should be one indentation to the right
    print('Inside code block')

# When we want to end the code block, we step back one indentation to the right
other_thing = "This is now outside the indented code block from above"


# If you open a new code block inside a code block, indent one more level. 

# In[10]:


# Example with multiple indentations
my_list = [False, True, False]

print('Before the loop')
for element in my_list:
    
    # Indent one level to be inside the for loop code
    print('\tInside the loop - at the top.')
    
    if element == True:
        
        # Indent again to be inside the conditional (also still inside the loop)
        print('\t\tInside the conditional, inside the loop.')
    
    # Step back one indent, now outside the conditional, but still inside the loop
    print('\tInside the loop - at the bottom.')

# Step back one more, to be outside both the loop and the conditional
print('After the loop.')


# Note that whitespace within lines does not actually matter. 
# 
# However, it does make code harder to read - so the stylistic convention is to always use one space between things. 

# In[11]:


# Excessive whitespace within a line
a =   1.  +    2
print(a)


# ## Order of Operations & Grouping
# 
# Python has a specific order in which operations are executed.
# 
# Operations can also be grouped, using parentheses, that indicates which operations are to be performed first, on what elements. 

# In[12]:


# For numerical operations, Python follows the same order of operations as math
print(1 - 2 * 3)
print((1 - 2) * 3)


# In[13]:


# Use parenthesis to group elements - in this case
(False and False) or True


# In[14]:


# Use parenthesis to group elements - in this case changing order of execution
False and (False or True)


# <div class="alert alert-info">
# For the full list of order of operations in Python, check [here](http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html).
# </div>

# ## String Literals
# 
# 'Literals' mean to interpret what's written as a string containing the literal characters that are written, and not as a variable name or similar. 
# 
# String literals are denoted with single quote (') or double quote ("). 
# 
# Single quotes and double quotes are effectively equivalent - it doesn't matter which one you use. 

# In[15]:


'This is a string'


# In[16]:


"This is also a string."


# In[17]:


"""

Multi-line strings use triple quotes (can be triple single or double quotes).

"""


# ### Escapes
# 
# Inside a string, you can use the escape character, which is backslash (\), to 'escape' the next character. 
# 
# This means that the next character should be interpreted as something other than it's literal character value. 
# 
# For example, we can use this to indicate spacings, such as tabs and new lines.

# In[18]:


print("\t Escape 't' is a tab.")
print("\n Escape 'n' is a newline.")


# ## Keywords
# 
# Python has a list of special 'keywords', that do special things. 
# 
# In Jupyter notebooks, keywords are highlighted in bolded green, to indicate their special status. 
# 
# Keywords are single words, and, other than `True`, `False` and `None`, all  that are written as all lower-case.

# In[19]:


import keyword


# In[20]:


# Check out
print(keyword.kwlist)


# Keywords are protected in Python, meaning if you try to assign them a new value, this will fail. 

# In[21]:


# Trying to assign a new value to a keyword will always fail
None = '12'

