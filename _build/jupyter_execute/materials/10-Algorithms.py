#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **A3** due Thursday 2/10 (11:59 PM) [This is a change; Canvas and syllabus updated; late deadline Sunday]
# - [mid-course survey](https://docs.google.com/forms/d/e/1FAIpQLSdswcDdmqv_kogN7mGkhr_1DJ6jDMLPVblqlz_BZyxizZrOSw/viewform?usp=sf_link) "due" Mon (11:59 PM; optional for EC; link also on Canvas)
# 
# Notes:
# - Campuswire
#     - post to main channel unless it really needs to be DM
#     - don't DM the same question to multiple people
#     - if you feel you haven't received a response, be sure post is marked as unresolved
#     - just a reminder you can post anonymously to your classmates there
# - Loops - difference between functions and loops?
#     - **function** - set of instructions for the burger
#     - **loops** - `for` loop: make burger for every member of the family in the car; `while` loop : make burgers until your shift is over

# **A3 Notes**
# 
# - There is a section giving you an `.append()` example - read that
# - student struggling with where and when to initialize a counter, empty list, etc.

# **Q&A**
# 
# Q: In the For Loops after the "if" statement do "not in" or "in" always have to follow?  
# A: Nope. Any statement that evaluates as a boolean can follow.
# 
# Q: Although in lecture you said we don't need to worry about the asterisk for range 1.4.1 does that mean we don't need to have it or just to put it before the range no matter what to run the code?  
# A: You do *not* put it in your code. 
# 
# Q: How do you do a nested "while" loop?  
# A: See answer key from CL5 - follow up in office hours/on campuswire if you have questions!
# 
# Q: Continue only helps us continue with a loop. What if we want to exit the loop completely and continue with the rest of the code?  
# A: `break`! The next part of the notes we didn't get to on Wednesday; will discuss today.
# 
# Q: is there any code similar to continue but can jump to any line?  
# A: No; you could use conditionals to control this...but your code would get confusing/unreadable very quickly, so you'd probably want a different design.
# 
# Q: When I append the list, sometimes the variable shows up in red, is this normal? AND why does 'break' turn red sometimes? my code still runs even if it is but i dont know why this happens
# A: This indicates you have an extra space somewhere...likely before the variable name/before `break`? 
# 
# Q: For 'while' loops does it only take numbers? If yes, then is 'for' the only one that accepts strings?  
# A: No. while loops only accepts conditions; for loops loop over collections (lists, tuples, dictionaries, etc.)
# 
# Q: Is range specifically only for numbers? I'm a bit confused since indexing works for both numbers and lists. Or is range only for loops?  
# A: `range` is only for numbers. And, it is most commonly used with loops.
# 
# Q: How does break and print statements in a loop differ in stoping the loop from running infinitely?  
# A: `break` breaks the loop. print statements simply print whatever you tell it to print to screen; does not affect the code running.
# 
# Q: how do you index a list in a loop without using range?  
# A: See the while loop example II for a case where we do this.
# 
# Q: 'break' of loops- Quite confusing when a topic in a due assignment is not mentioned at that day's lecture  
# A: A reminder that coding labs go throughout the entire day and there are staff there to answer questions like these; also, coding labs are graded on effort. If we didn't get to a topic in lecture, we won't deduct points for your not figuring it out on a lab.
# 
# Q: Can you explain the difference between 'pass' and 'continue'? 
# A: `pass` moves on to the next bit of code; `continue` goes to the next iteration of the loop...ignoring any code below it
# 
# Q: I can't see the lecture notes in datahub, I can only see the newest one is 07collection.  
# A: Be sure to click to update your lecture notes using the link at the top of the canvas home page
# 
# Q: What does n -= 1 and n += 1 notation mean?  
# A: This is shorthand....for example, `n += 1` is equivalent to `n = n + 1`
# 
# Q: I defined a list[2,4,6,8] and used the range function for item in range(0,4,1) print item. It just gives me 1,2,3,4 even though I have defined my list before using range function. How do we let python know the range refers to range in the list but not in general sense?  
# A: This is where you would use indexing `list[0:4:1]`
# 
# Q: With each assignment amount of question increasing, are they going to be more complex and longer each time? I understand that complex for sure , since we are studying a new concepts, A3 seems very long.    
# A: A1 and A2 are the shortest; A3, A4, and A5 are all similar in length/complexity.

# # Algorithms
# 
# What are the sorts of things that we should do with computers? What are things that are easy to compute? Hard to compute? Impossible to compute?

# ## Algorithms

# <div class="alert alert-success">
# An <b>algorithm</b> is a formal description of how to complete a procedure, typically taking inputs and returns some output.
# </div>

# If you can write the steps down, you can write an algorithm.
# 
# Algorithms are computable.

# Computers cannot read between the lines. They are very literal.

# ### Algorithm Example: Making a Sandwich

# Humans are pretty good at making sandwiches. Computers may struggle a bit.

# ### Algorithm Example: Sorting
# 
# Given a list of numbers, how can we sort it into the correct order?

# In[ ]:


# Define a list of numbers
list_of_numbers = [2, 1, 3]  


# #### Clicker Question #1

# Think about the specific steps needed to sort an array...
# - A) I have a specific set of steps 
# - B) I have some idea that might work
# - C) I have no idea

# **array**: a collection of items, where each item can be accessed by its index.

# Y'all Google is *really* good at sorting.
# 
# - ranking: rate a site as how related
# - sort: given a list of good sites, determine order to present to user
# 
# ...and do this on all the things

# ## `sort_array`
# 
# A version of a **selection sort**:
# - loop through current list
# - find lowest item
# - put that at the front of your sorted list
# - remove lowest item from current list
# - wash, rinse, repeat

# In[ ]:


def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to 
     
    while not is_sorted:

        lowest = None
        for item in array_to_sort:
            if lowest == None:         # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines use new methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
            is_sorted = True
    
    return sorted_array


# ## Using `sort_array`

# In[ ]:


# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# In[ ]:


# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)


# #### Clicker Question #2
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = ['a', 'c', 'b'] 
sort_array(data)


# - A) ['a', 'c', 'b']
# - B) ['a', 'b', 'c']
# - C) [97, 98, 99]
# - D) None
# - E) This code will fail

# ### How Python evaluates strings

# In[ ]:


'a' < 'b'


# In[ ]:


ord('a')


# In[ ]:


ord('b')


# #### Clicker Question #3
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = [True, False, True]
sort_array(data)


# - A) [False, True, True] 
# - B) [True, False, True] 
# - C) [0, 1, 1]
# - D) [True, True, False] 
# - E) This code will fail

# ### How Python evaluates Booleans

# In[ ]:


True < False


# In[ ]:


bin(True)


# In[ ]:


bin(False)


# #### Clicker Question #4
# 
# Using our `sort_array` function from above, what will the following code snippet print out:

# In[ ]:


data = [[1, 4], [1, 2]]
sort_array(data)


# - A) [[1, 4], [1, 2]]  
# - B) [1, 1, 2, 4] 
# - C) [[1, 2], [1, 4]]
# - D) None 
# - E) This code will fail

# ## SideNote: `sorted`

# In[ ]:


# Sort a list, with `sorted`
data = [7, 4, 6]
sorted(data)


# In[ ]:


# what about a list of strings?
sorted(['asdf','abcd'])


# In[ ]:


# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[1, 4], [1, 2]]))


# ## Algorithmic Complexity

# <div class="alert alert-success">
# The complexity of an algorithm characterizes the relationship between the input size and the number of steps of an algorithm.
# </div>

# ## Algorithmic Complexity 
# 
# Things we might care about:
# - The number of steps it takes to complete our algorithm
#     - Usually defined in relation of the size of the input
# - The amount of memory it will take to run our algorithm

# ## Properties of our sorting algorithm
# 
# - It will require $n^2$ steps, where $n$ is the length of the list
# - It will require ~double the memory of the original list

# ## Computability

# Things that computers can do are things that we can write down an algorithm to do.
# 
# Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.

# ## Variable Type Checking
# 
# **Note**: The rest of the noteook includes notes to answer a student's in class question. You will not be tested on this, but it will be helpful to understand and may be necessary for your final project.
# 

# To check on an input variable's type, you can use either of the following approaches:
# 
# ```python
# type(object) == type
# ```
# OR 
# 
# ```python
# isinstance(object, classinfo) 
# ```
# 
# `isinstance()` takes two parameters:
# - `object` : variable/object to be checked
# - `classinfo` : class, type, or tuple of classes and types

# For example, using the `string_manipulator` function from earlier, note that I've added the following two lines: 
# 
# ```python
# if not isinstance(string, str):
#     print("Warning: please provide a string as input")
# ```
# 
# This checks to see if the input is anything other than a string. If it is, the function prints a warning.

# In[ ]:


def string_manipulator(string):
    
    if type(string) != str:
        print("Warning: please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[ ]:


# use function with a string
string_manipulator('hello!')


# In[ ]:


# print warning if not a string
string_manipulator(5)


# However, sometimes, you want it to raise an error rather than just print something. Here we use `raise` instead of print. In this case, an error will be returned (with our specified message) to the user if the wrong variable type is provided:

# In[ ]:


def string_manipulator(string):
    
    if type(string) != str:
        raise ValueError("Please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output


# In[ ]:


# raise error instead of print message
string_manipulator(5)

