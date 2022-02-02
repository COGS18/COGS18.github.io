#!/usr/bin/env python
# coding: utf-8

# **Course Announcements (Mon 1/31)**
# 
# Due Dates:
# - **A2** due tonight(11:59 PM)
# - **CL5** due Wednesday
# 
# Notes: 
# - Some in-person labs and office hours this week (see Canvas)
# - **CL4** grades posted
# - **A3** will be made available this afternoon

# **Q&A  (Mon 1/31)**
# 
# Q: Why is Python favored by many programmers? What are the benefits to using other programming languages?  
# A: It's often favored for its readability relative to other languages. Other languages however are faster, for example, and so are used instead of Python. Python is also used in many fields b/c of the external packages available that make doing a particular task easier in Python (i.e. data science, neuroscience, etc.)
# 
# Q: how we can check if theres an error is the code still passes silently  
# A: Check the output - is it what you expected? Like in a math class, where you can calculate a number...but it's wildly wrong/doens't make sense for the question. Same idea applies here. Errors catch "illegal" operations in the code; it's up to you to make sure that the code is actually doing what you intended.
# 
# Q: Why are syntax errors raised before any other error?  
# A: Because Python checks for those first, as the code cannot be processed/evaluated until those are corrected.
# 
# Q: is there a way to autofill python? this would help misspelling   
# A: Yup - you can use tab completion. Start typing a variable, and then hit tab; will autocomplete the variable (assuming it exists)
# 
# Q: When I look back at notes, I notice that they are changed. However, they are not changes I made. Is there a way for me to keep or retrieve the original notes?  
# A: Ah, so I post/update the notes with the changes reflected in class. I'll try to think on a way to keep original notes available.
# 
# Q: will we remain remote after Jan.31st?  
# A: See announcemnets at beginning of class from this past Friday (and see updates to Canvas home page). Lectures still on zoom; some office hours and some labs in perons.
# 
# Q: For lecture videos in the Media Gallery, why do some have subtitles/transcripts while others don't?  
# A: I've been wondering the same. I turn live transcript on every day in class...so I assumed subtitles would always be there, but recently they haven't been? I believe cc can always be turned on in Canvas; however, even if not automatic. Please reach out if you need CC and don't see it/don't know how to access.
# 
# Q: I was curious if there was a way to change between mutables and immutables. For example, is there some command or method to change a list to a tuple and vice versa?  
# A: You can typecast. For example use `list()` with something you want to be a list inside parentheses, but that's the closest.
# 
# Q: You mentioned that python checks for syntax errors first before like name errors for instance, so it seems like there is an order for how python checks for errors. I am wondering if we need to know that order.   
# A: You'll need to know it in the sense that you'll need to understand how to debug your code..but you won't be directly tested on this. 
# 
# Q: You mentioned that python checks for syntax errors first before like name errors for instance, so it seems like there is an order for how python checks for errors. I am wondering if we need to know that order.   
# A: It's not. It's due Wednesday. 
# 
# Q: what's offset mean in the debugging code?  
# A: It was a variable name chosen in the example used.

# **Course Announcements (Wed 2/2)**
# 
# Due Dates:
# - **CL5** due tonight
# - **A3** due Mon (11:59 PM)
# - [mid-course survey](https://docs.google.com/forms/d/e/1FAIpQLSdswcDdmqv_kogN7mGkhr_1DJ6jDMLPVblqlz_BZyxizZrOSw/viewform?usp=sf_link) "due" Mon (11:59 PM; optional for EC; link also on Canvas)
# 
# Notes: 
# - E1 grading underway - hope to post scores/discuss in class Monday
# - Happy Lunar New Year!

# **Q&A (Wed 2/2)**
# 
# Q: I understand the difference between an "if/else" block and a "try/except" block, but I'm still confused on why or when we would want to use a "try/except" block. Wouldn't we want our code to not error at all? Or if it did error, why would we want our code to continue on and not be broken when we could fix that error instead?  
# A: Think about this in the context of a loop. Say you have 1000 emails that you want to send and there is a typo in the 400th email. Would you only want the first 399 to send and then error out and stop? *Or* would you want it to send all of the 999 emails, *except* the 400th and just send you a little message letting you know that one wouldn't send. In my mind, the latter is much better...and would be a perfect case for a try/except block!
# 
# Q: For the debugging lecture, will there be any other errors that appear that we didnt go over?   
# A: There are some rare errors that exist that we didn't cover...but we discussed the vast majority of them.
# 
# Q: When could/would we have functions in a loop? How different is a function from a loop?  
# A: It's more typical to have a loop in a function. We'll see examples of these coming up (lots in A3!) And, a function allows you to specify a set of instructions, which run/execute that set of instructions when you call the function. A loop on the other hand specifies some set of operations that you want to execute over and over again until a condition is no longer true (while loop) *or* until you reach the end of the collection you're looping over (for loop)
# 
# Q: Learning that the placement of print statements inside loops can affect the loop itself (as shown in the bill, index example in class).  
# A: Just a reminder that the print statement did NOT change what the loop was doing. The placement of the print statement simply changed *when* a variable was being printed. The loop was still doing the same thing...it was just the print statement's location that changed.
# 
# Q: What's difference of defining variable inside and outside the function?  
# A: A variable defined outside the function exists in your global namespace...so you can call it at any point in your notebook. A variable defined inside your function only exists in your local (function's) namespace...so you can only use it/reference it within your function.
# 
# Q: I'm still a bit confused about the difference between loop and conditionals. Can you explain it again?  
# A: A conditional specifies which set of code should execute under which condition. A loop specifies to repeat a piece of code over and over again.
# 
# Q: do we use print or return statements in loops?  
# A: `print()`. `return` is only to return output from functions
# 
# Q: What specifically can we do with the raise function  
# A: Specify your own error messages to be used. We will *not* be requiring you to do this on your exam/assignments...but it's good to know it's possible to better understand that someone had to write the error messages you see...and b/c it is sometimes helpful when people go to do their final project.
# 
# Q: What are prime examples of coding loops being used in real life?  
# A: Oh my gosh there are so many! Any time you want to do a process over and over again, think loops! So, while it's not a programming example, each day is a bit like a loop in that you probably have a similar process to get ready in the morning (shower, brush teeth, eat breakfast, etc.). We'll see lots and lots of programming examples in A3.
# 
# Q: Will the answer be considered wrong if a print statement is not in the right place during a 'while' loop?  
# A: Nope. `print` statements are never required...they're there to help your understanding/to "see" what is going on inside the code.
# 
# Q: I have downloaded Anaconda, but the jupyter notebook that it opens does not have the lecture notes or anything related to this course. Is there a way to transfer the files and assignment to the Anaconda Jupyter notebook.  
# A: To get the notes, you would want to download them from the website and then open them in Anaconda *or* click on the first link on the home page of Canvas to pull the notes into datahub (this is what most students do). Definitely something we could help you with in office hours! 

# # Loops
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


# ## Loops

# <div class="alert alert-success">
# A <b>loop</b> is a procedure to repeat a piece of code.
# </div>

# ### Avoid copy + pasting
# 
# For repetitive actions, if you find yourself copying + pasting, rethink your strategy.
# 
# Loops are one way to avoid this.

# In[ ]:


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

# ### `while` Loop Example I

# In[9]:


number = -5

while number < 0:
    print(number)
    number = number + 1  # must have code to make condition evaluate as False at some point


# ### `while` Loop Example II

# In[20]:


20 <= 20


# In[22]:


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
    print(bill, index)


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

# ## `for` Loops

# <div class="alert alert-success">
# A <b>for loop</b> is a procedure a to repeat code for every element in a sequence.
# </div>

# ### For Loop Example I
# 
# Looping through a list of items

# In[ ]:


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

# In[ ]:


# Loop across items in a string
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
my_string = 'python'

for char in my_string:
    if char not in vowels:
        print(char)


# #### Clicker Question #3
# 
# How many values will be `print`ed from this `for` loop before it *first* prints "The tea is too hot!"?

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


# #### Clicker Question #4
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


# #### Clicker Question #5
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


# #### Clicker Question #6
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

# #### Clicker Question #7
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

# #### Clicker Question #8
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

# ### Dictionaries: Indexing & Looping

# In[ ]:


# Dictionaries are indexed using their keys
dictionary['key_1']


# In[ ]:


# Loop over a dictionary loops across the keys
#   Inside the loop, you can use the key to access the associated value
for item in dictionary:
    print('Loop Iteration')
    print('\tKey:\t', item)
    print('\tValue:\t', dictionary[item])


# In[ ]:


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

# In[ ]:


number = 5
while number < 0:
    print(number)
    number = number + 1


# **Code Style to Avoid**

# In[ ]:


number=-5
while number<0:print(number);number=number+1 # avoid all on a single line


# ## Loops Practice

# ### Loops Practice #1
# 
# Write a function `count_odd()` contatining a loop that will add all the *odd* numbers for the input range together.

# In[ ]:


# YOUR CODE HERE


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Loops Practice #2
# 
# Write a function `count_vowels()` containing a loop that will loop through all the letters in `my_name` (the input parameter) and count all the vowels in your name.

# In[ ]:


# YOUR CODE HERE


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

