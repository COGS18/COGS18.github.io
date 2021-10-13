#!/usr/bin/env python
# coding: utf-8

# **[Ad]**: W.O.R.M in STEM
# 
# ![worm](img/worm.png)
# 
# Link: https://forms.gle/Ep8k1Xx7zmYydozj7

# **Course Announcements**
# 
# - Last chance to turn in **A1**: tonight at 11:59 PM
# - **CL3** due Wed
# - **A2** due Fri
# - **E1** (midterm) is on Mon, a week from today
#     - No lecture or OH on exam day
#     - There *will* be a review *and* a practice exam

# **Q&A**
# 
# Q: What does it mean when you are writing in a code cell and the In [  ]: on the left has an asterisk  In [ * ]:  instead of a number  In [ 7 ] : inside of it?  
# A: This means either your notebook is not connected to the internet OR that your code is still running.
# 
# Q: When you assign a variable to a number for example my_num = 5 and then you run it and then you put in a new number my_num = 10, would both variables assignments (5 and 10) be stored in the namespace or just the most recent one? Could you even store two numbers in one variable?   
# A: Just the most recent one. To store two numbers you would use a collection (list, tuple, or dictionary, etc.)
# 
# Q: When should we use try/except over if/else?  
# A: try/except when you want the except to run if an exception is encountered
# 
# Q: I recently got my iClicker, but I have no idea if it is working.  
# A: If you see a checkmark on your clicker after you click in, it's working.
# 
# Q: Can you make a lists within a list within a list?  
# A: Yup! But, they can be really difficult to work with. At the end of the quarter we'll see an easier-to-use alternative...the dataframe!
# 
# Q: How do i access campuswire  
# A: See link and access code on home page of Canvas.
# 
# Q: Do we need to memorize which error belongs to which error category?  
# A: Nope. But, if you understand what they each mean, debugging your code will be faster.
# 

# # Control Flow - Loops
# 
# - `while`
# - `for`
#     - `range`
#     - `continue`
#     - `break`

# ## Loops

# <div class="alert alert-success">
# A <b>loop</b> is a procedure to repeat a piece of code.
# </div>

# ### Avoid copy + pasting
# 
# For repetitive actions, if you find yourself copying + pasting, rethink your strategy.
# 
# Loops are one way to avoid this.

# In[4]:


lst = ['you@yahoo.com', 'them@bing.com']

email = lst[0]

email = lst[1]


# ## While Loops

# <div class="alert alert-success">
# A <b>while loop</b> is a procedure to repeat a piece of code while some condition is still met. 
# </div>

# `while` loops always have the structure:
# 
# ```python
# while condition:
#     # Loop contents
# ```
# 
# While condition is true, execute the code contents. 
# 
# Repeat until condition is no longer True. 

# ## While Loops

# ### `while` loop Example

# In[8]:


number = -5

while number < 0:
    print(number)
    number = number + 1


# #### Clicker Question #1
# 
# How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?

# In[ ]:


temperature = 115
 
while temperature > 112: 
    print(temperature)
    temperature = temperature - 1
    
print('The tea is cool enough.')


# - A) 1
# - B) 2
# - C) 3
# - D) 4
# - E) Infinite
# 

# #### Clicker Question #2
# 
# What will be the value of `counter` after this loop is run:

# In[ ]:


keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)


# <pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre> 

# ### Stepping Through the Loop
# 
# (Note: We skip this in class.) This is the same code as above with `print()` statements to explain what's going on at each step. If you're confused by the class example, walk through it here with the `print()` statements to guide you.

# In[ ]:


keep_looping = True
counter = 0

while keep_looping:
    print('START LOOP')
    print('\tStart counter: ', counter)

    counter = counter + 1
    
    print('\tMid counter: ', counter)
    
    if counter > 3:
        keep_looping = False
        
    print('\tEnd counter: ', counter)

print('\nFinal counter: ', counter)


# ## For Loops

# <div class="alert alert-success">
# A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
# </div>

# ### For Loop Example I
# 
# Looping through a list

# In[ ]:


# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)
    
print('\tLast value: ', my_item)


# ### For Loop Example II
# 
# Looping through a string

# In[ ]:


# Loop across items in a string
for char in 'python': 
    print(char)


# #### Clicker Question #3
# 
# What will the following loop print out:

# In[ ]:


my_lst = [0, 1, 2, 3, 4]

for item in my_lst[0:-2]:
    print(item + 1)


# - A) 0, 1, 2
# - B) 0, 1
# - C) 1, 2
# - D) 2, 3
# - E) 1, 2, 3

# #### Clicker Question #4
# 
# How many values will be output from this `for` loop before it *first* prints "The tea is too hot!"?

# In[ ]:


temperatures = [114, 115, 116, 117, 118]

for temp in temperatures: 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')


# - A) 1
# - B) 2
# - C) 3
# - D) 4
# - E) Infinite
# 

# ## `range`

# <div class="alert alert-success">
# <code>range</code> is an operator to create a range of numbers, that is often used with loops.
# </div>

# ### `range` Examples

# In[ ]:


for ind in [0, 1, 2, 3, 4]:
    print(ind)


# In[ ]:


# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))


# In[ ]:


# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)


# In[ ]:


# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)


# In[ ]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')


# #### Clicker Question #5
# 
# How many values would this loop print and what would be the last value printed? 

# In[ ]:


for ind in range(1, 10, 3):
    print(ind)


# - A) values printed: 3; last value: 7
# - B) values printed: 3; last value: 9
# - C) values printed: 4; last value: 9
# - D) values printed: 7; last value: 7
# - E) values printed: 7; last value: 9
# 

# ## `continue`

# <div class="alert alert-success">
# <code>continue</code> is a special operator to jump ahead to the next iteration of a loop.
# </div>

# ### `continue` examples

# In[ ]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        continue
    
    print(item)


# In[ ]:


courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue
  
    print(course)
    print(course + '!')


# In[ ]:


string = "python"

for char in string: 
    
    if char == "p" or char == "y":
        continue
        
    print(char)


# #### Clicker Question #6
# 
# What will be the value of `counter` after this code has run:

# In[ ]:


counter = 0
my_lst = [False, True, False, True]

for item in my_lst:
    if item in my_lst:
        continue
    else:
        counter = counter + 1
        
print(counter)


# - A) 0 
# - B) 1
# - C) 2 
# - D) 3
# - E) 4

# ## `break`

# <div class="alert alert-success">
# <code>break</code> is a special operator to break out of a loop.
# </div>

# In[ ]:


connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break


# ### `break` examples

# In[ ]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        break
    
    print(item)


# In[ ]:


courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break
  
    print(course)


# In[ ]:


string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)


# In[ ]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
        break


# #### Clicker Question #7
# 
# What will the following code print out:

# In[ ]:


number = 1

while True:
    if number % 3 == 0:
        break
   
    print(number)
    
    number = number + 1


# - A) 1 
# - B) 1 2 
# - C) 1 2 3
# - D) Something else 
# - E) This code prints forever

# #### Clicker Question #8
# 
# For how many `temp` will output be printed from this for loop? 
# 
# (In other words, how many times in this `for` loop will something be printed out?)

# In[ ]:


# using range in example above
for temp in range(114, 119): 
    
    if(temp < 116):
        continue
    elif(temp == 116):
        print('The tea is too hot!')
    else:
        break


# - A) 0 
# - B) 1
# - C) 3
# - D) 5
# - E) 6

# #### Clicker Question #9
# 
# What will be the value of `counter` after this code has run:

# In[ ]:


counter = 0
my_lst = [False, True, False, True]


for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
        
print(counter)


# - A) 0 
# - B) 1
# - C) 2 
# - D) 3
# - E) 4

# ## Loops Practice

# ### Loops Practice #1
# 
# Write a loop that adds all the *odd* numbers between 1 and 1000 together.

# In[ ]:


# YOUR CODE HERE


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Loops Practice #2
# 
# Store your name as a string in a variable called `my_name`.
# 
# Write a loop that will loop through all the letters in `my_name` and count all the vowels in your name.

# In[ ]:


# YOUR CODE HERE


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.
