#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - CL3 due Wednesday (11:59 PM)
# - A1 due Friday (11:59 PM)

# <table border="0">
#  <tr>
#     <td><img src="img/climate.png" alt= “” width="500" height="500"></td>
#     <td>Reminder: You are allowed to attend a different lab section each week as needed.</td>
#  </tr>
# </table>

# # Conditionals
# 
# - `if`
# - `elif`
# - `else`

# ## Conditionals: `if`

# <div class="alert alert-success">
# Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
# </div>

# In[5]:


condition = True

if condition:
    print('This code executes if the condition evaluates as True.')


# In[8]:


# equivalent to above
if condition == True:
    print('This code executes if the condition evaluates as True.')


# #### Class Question #1
# 
# Replace `---` below with something that will print 'True'
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start.

# In[19]:


math = 2+2 == 4

if math:
    print('True')


# ## Conditional: `else`

# <div class="alert alert-success">
# After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
# </div>

# In[31]:


condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')


# #### Class Question #2
# 
# Replace `---` below with something that will print 'False'.
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start.

# In[36]:


bool(_)


# In[35]:


my_value = _

if my_value:
    print('True')
else: 
    print('False')


# ## Conditional: `elif`

# <div class="alert alert-success">
# After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
# </div>

# In[37]:


condition_1 = False
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')


# ### `elif` without an `else`
# 
# An else statement is not required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.

# In[38]:


condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ### `elif` *after* an `else` does not make sense
# 
# The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

# In[39]:


## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ## Conditionals With Value Comparisons

# <div class="alert alert-success">
# Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
# </div>

# In[44]:


speed_limit = 65
speed = 50

if speed > speed_limit:
    ticket = True
else:
    ticket = False


# In[45]:


print(ticket)


# In[54]:


# string value comparisons also possible
a1 = 'not started'

if a1 == 'completed':
    action = 'grade'
elif a1 == 'in progress':
    action = 'wait'
elif a1 == 'not started':
    action = 'incomplete'
else:
    action = 'uncertain'


# In[55]:


a1 == 'not started'


# In[53]:


a1


# In[56]:


print(action)


# #### Class Question #3
# 
# What will the following code snippet print out:

# In[57]:


condition = False

if condition:
    print("John")
elif not condition:
    print("Paul")
elif not condition:
    print("George")
else:
    print("Ringo")


# - A) John 
# - B) Paul, George, Ringo 
# - C) Paul 
# - D) Paul, George 
# - E) Ringo

# #### Class Question #4
# 
# What will the following code snippet print out:

# In[60]:


if 1/0:
    print('Hello')


# In[58]:


if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")


# - A) I did Math 
# - B) I broke Math
# - C) I didn't do math
# - D) This code won't execute

# #### Class Question #5
# 
# What will the following code snippet print out:

# In[66]:


conditional = True
python = "great"

if conditional:
    print('conditional is True')
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")


# - A) Yay Python!
# - B) Oh no.
# - C) I'm here.
# - D) This code won't execute

# ## Properties of conditionals
# 
# - All conditionals start with an `if`, can have an optional and variable number of `elif`'s and an optional `else` statement
# - Conditionals can take any expression that can be evaluated as `True` or `False`. 
# - At most one component (`if` / `elif` / `else`) of a conditional will run
# - The order of conditional blocks is always `if` then `elif`(s) then `else`
# - Code is only ever executed if the condition is met

# ## Code Style: Conditionals
# 
# - avoid single line statements
# - a single conditional (if + elif + else) has no additional line spaces between statements

# ### Conditionals: Good Code Style

# In[68]:


value = 16

if value % 2 == 0:
    out = "even"
else:
    out = "odd"


# ### Conditionals: Code Style to Avoid

# In[69]:


if value%2==0:out="even" # avoid statement on same line as conditional
                         # avoid blank line between if and else
else:out="odd"           # don't forget about spacing around operators!                     


# ## Functions + Conditionals
# 
# Let's define a more interesting function than what we did in the functions lecture. Here we are using conditionals within our function.

# In[70]:


# Determine if a value is even or odd
def even_odd(value): 

    if value % 2 == 0: 
        out = "even"
    else: 
        out = "odd"
        
    return out


# In[72]:


# Execute our function to check that
# it is working according to our expectations
even_odd(2)

