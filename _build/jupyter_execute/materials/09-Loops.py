#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# - Take-home portion of exam due Fri (tomorrow) 11:59 PM
# - CL5 and A3 will be released tomorrow
# 
# **Office Hours Updates**
# - This week only: Prof today/Th 1-1:50 PM (CSB 114)
# - Josh S - Fri 11-12; *new location*: M.O.M’s Cafe   

# # Control Flow - Loops
# 
# - `while`
# - `for`
# - `range`
# - `continue`
# - `break`

# ### SideNote: counters

# In[1]:


# Initialize a counter variable
counter = 0 
print(counter)


# In[2]:


counter = counter + 1
print(counter)


# In[3]:


counter = counter + 1
print(counter)


# The idea here...is that as the code executes, the value of the counter increases. We'll use these a lot in loops!

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


# ## `while` Loops

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

# ![](img/shopping_cart.jpeg)

# ### `while` Loop Example I

# In[5]:


number = -5

while number < 0:
    print(number)
    number = number + 1  # must have code to make condition evaluate as False at some point


# ### `while` Loop Example II

# In[6]:


shopping_budget = 20
bill = 0
index = 0
prices = [3, 4, 10, 3, 2, 15, 7]

while bill < shopping_budget:
  
    # add cost of item (prices) to bill
    bill = bill + prices[index]
    
    # increment index each time through the loop
    index = index + 1
    
    #print bill so we can see what's going on
    print(bill)


# #### Clicker Question #1
# 
# How many temperature values will be output from this `while` loop before "The tea is cool enough." is printed?

# In[7]:


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

# In[8]:


keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)


# <pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre> 

# ## `for` Loops

# <div class="alert alert-success">
# A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
# </div>

# ![](img/shopping_list.jpeg)

# ### For Loop Example I
# 
# Looping through a list of items

# In[9]:


# Define a list of items
list_of_items = ['A', True, 12]

# Loop across each element
for my_item in list_of_items:
     print(my_item)
    
# difference between printing within and outside loop
# print(my_item)


# ### For Loop Example II
# 
# Looping through a string

# In[10]:


# Loop across items in a string
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
my_string = 'python'

for char in my_string:
    if char not in vowels:
        print(char)


# #### Clicker Question #4
# 
# How many values will be `print`ed from this `for` loop before it *first* prints "The tea is too hot!"?

# In[11]:


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

# In[12]:


for ind in [0, 1, 2, 3, 4]:
    print(ind)


# In[13]:


# the asterisk here unpacks the range
# don't worry about this syntax now
print(*range(0, 5))


# In[14]:


# Loop across a sequence of numbers, using range
for ind in range(0, 5):
    print(ind)


# In[15]:


# Range, like indexing, is defined by 'start', 'stop', 'step'
for ind in range(2, 6, 2):
    print(ind)


# In[16]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')


# #### Clicker Question #5
# 
# How many values would this loop print and what would be the last value printed? 

# In[17]:


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

# In[18]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        continue
    
    print(item)


# In[19]:


courses = ['cogs9', 'cogs18', 'cogs108']

for course in courses:

    if course == 'cogs18':
        continue
  
    print(course)
    print(course + '!')


# In[20]:


string = "python"

for char in string: 
    
    if char == "p" or char == "y":
        continue
        
    print(char)


# **Counters within loops**
# 
# A counter within a loop...

# In[21]:


input_list = [0, 1, 2]
counter = 0        # initialize a counter

for val in input_list:
    # print value of counter
    print(counter)
    
    # increment by 1
    counter = counter + 1

# print after loop terminates
print("Final counter value:", counter)


# #### Clicker Question #6
# 
# What will be the value of `counter` after this code has run:

# In[22]:


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

# ### `break` examples

# In[23]:


lst = [0, 1, 2, 3]

for item in lst:
    
    if item == 2:
        break
    
    print(item)


# In[24]:


courses = ["cogs9", "cogs18", "cogs108"]

for course in courses:

    if course == "cogs18":
        break
  
    print(course)


# In[25]:


string = "love python"

for char in string: 
    if char == "p" or char == "y":
        break
        
    print(char)


# In[26]:


# using range in example above
for temp in range(114, 119): 
    print(temp)
    
    if(temp > 115):
        print('The tea is too hot!')
        break


# #### Clicker Question #7
# 
# What will the following code print out:

# In[27]:


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

# In[28]:


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

# In[29]:


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

# ### Dictionaries: Indexing & Looping

# In[30]:


dictionary = {'key_1' : 'val_1', 'key_2' : 'val_2'}


# In[31]:


# Dictionaries are indexed using their keys
dictionary['key_1']


# In[32]:


# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])


# In[33]:


# another approach that you will find if you Google
for key, val in dictionary.items():
    print('Loop Iteration')
    print('\tKey:\t', key)
    print('\tValue:\t', val)


# ## Code Style: Loops
# 
# - `for`/`while` statement with a colon at the end on first line
# - all code within the loop inside a code block (indented)

# **Good Code Style**

# In[34]:


number = 5
while number < 0:
    print(number)
    number = number + 1


# **Code Style to Avoid**

# In[35]:


number=-5
while number<0:print(number);number=number+1 # avoid all on a single line


# ## Loops Practice

# ### Loops Practice #1
# 
# Write a function `count_odd()` containing a loop that will add all the *odd* numbers for the input range together.

# In[36]:


def count_odd(range_to_loop_over):
    add_all = 0

    for value in range_to_loop_over:
        #conditional - determine if odd
        if value % 2 != 0:
            #increased the counter
            add_all = add_all + value
        else:
            continue
    
    return add_all


# In[37]:


count_odd([0, 2, 3,6,9])


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Loops Practice #2
# 
# Write a function `count_vowels()` containing a loop that will loop through all the letters in `my_name` (the input parameter) and count all the vowels in your name.

# In[13]:


# YOUR CODE HERE
def count_vowels(my_name):
#     vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
#     vowels = 'AEIOUaeiou'
    count = 0

    for ltr in my_name:
        if ltr in 'AEIOUaeiou':
            count = count + 1
        else:
            continue 
    
    return count
        
count_vowels('AEI')


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Loops Practice #3
# 
# Write a function `create_dictionary` that takes two input lists `lst_1` and `lst_2`. Inside the function, join the two lists to form a dictionary `joined_dictionary` where the first element in `lst_1` is the first key in `joined_dictionary` and the the first element in `lst_2` is the first value in `joined_dictionary` and so on and so forth. Then return `joined_dictionary` as the output. 
# 
# A) I did it! &emsp;B) I think I did it. &emsp;C) I tried but I am stuck. &emsp;D) Super duper lost

# In[ ]:


# YOUR CODE HERE


# In[ ]:


# YOUR CODE HERE
def create_dictionary(lst_1, lst_2):
    
    joined_dictionary = {}
    counter = 0

    for key in lst_1:
        joined_dictionary[key] = lst_2[counter]
        counter += 1

    return joined_dictionary


# In[ ]:


# TEST YOUR FUNCTION HERE
# Note that the two input lists are the 
# same length for the function to work properly
random_lst_1 = ['a', 'b', 'c', 'd']
random_lst_2 = [1, 2, 3, 4]

create_dictionary(random_lst_1, random_lst_2)

