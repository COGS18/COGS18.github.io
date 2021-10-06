#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL2** now available; due Wed at 11:59 PM
# - **A1** due Fri (10/8; 11:59 PM)

# **Q&A**
# 
# Q: When it says `raise NotImplementedError`, do you delete it and write your code?  
# A: Yes! If not, an error will be raised. This is your indication to replace that line of code with your answer.
# 
# Q: What is the difference between print and assert? When do we use each?   
# A: `print` statements show (print) what information is stored in a variable. You use these when you want to check the contents of a variable. `assert` statements check whether the information follows it is True. We use these in coding labs and assignments to make sure you're on the right track. You'll also get more practice with these in CL2.
# 
# Q: Do you have any recommended website for practice?  
# A: There are additional practice questions (and their answers) in our ["textbook"](https://shanellis.github.io/pythonbook/content/intro.html). Some students really like [leetcode](https://leetcode.com/). Additional exercises [here](https://www.practicepython.org/).
# 
# Q: Could you please remind us to fill out this daily survey at the end of class? I almost keep forgetting to do these. Thanks!    
# A: I *really* want to. I'll try to add it to the notes to remind myself...but I forget too :(. I'll try harder!
# 
# Q: Thank you Professor Ellis and TAs for answering all my questions. Could you give one (or few) example(s) that you have been using python in teaching?  
# A: I use code to manage all aspects surrounding grading. To switch between formats (i.e. Coding lab grades in a Google sheet -> Canvas format). To check who completed the course surveys. To see who's struggling in class (using comparison operators). To submit your grades at the end of the quarter. Just one example! There are lots!
# 
# Q: I'm just wondering why the Python developers made the boolean operators function that way mentioned above?  
# A: It's more memory efficient! (Albeit a little confusing)
# 
# Q: I am a little confused about asserts, how can I use them to check my work?  
# A: See answer above and check out CL2! Definitely a focus of coding lab this week!
# 
# Q: Where are the lab answers?  
# A: Course website: https://cogs18.github.io/
# 
# Q: How much time should we set aside for A1?  
# A: There is a wide range, but the median for students is 2 hours.

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


# In[6]:


# equivalent to above
if condition == True:
    print('This code executes if the condition evaluates as True.')


# #### Clicker Question #1
# 
# Replace `---` below with something that will print 'True'
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start

# In[10]:


math = ' '

if math:
    print('True')


# ## Conditional: `else`

# <div class="alert alert-success">
# After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
# </div>

# In[11]:


condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')


# #### Clicker Question #2
# 
# Replace `---` below with something that will print 'False'.
# 
# - A) I did it!
# - B) I think I did it!
# - C) I tried but am stuck.
# - D) I'm unsure where to start

# In[ ]:


my_value = ---

if my_value:
    print('True')
else: 
    print('False')


# ## Conditional: `elif`

# <div class="alert alert-success">
# After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
# </div>

# In[ ]:


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

# In[ ]:


condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ### `elif` *after* an `else` does not make sense
# 
# The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

# In[ ]:


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

# In[ ]:


language = "s"

if language == "Python" or language == "R":
    print("Yay!")
elif language == "Perl":
    print("Hmmmmmmm")
else:
    print("Get yourself a programming language!")


# In[ ]:


# Exploring conditionals
number = 4

print('Before Conditional')
 
if number < 5:
    print('    if statement execution')
elif number > 5:
    print('    elif statement execution')

print('After Conditional')


# #### Clicker Question #3
# 
# What will the following code snippet print out:

# In[ ]:


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

# #### Clicker Question #4
# 
# What will the following code snippet print out:

# In[ ]:


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

# #### Clicker Question #5
# 
# What will the following code snippet print out:

# In[ ]:


conditional = False
python = "great"

if conditional:
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

# **Final Notes**
# 
# - You now have all information needed for A1
# - Reminder to fill out daily feedback survey
