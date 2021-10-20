#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# **Due Dates**:
# - **CL3** due tonight (11:59 PM)
# - **A2** ...we'll see how far we get today
# 
# **Notes**:
# - **A1** scores posted (8 is full credit; score on Canvas; feedback on datahub)
# - **CL2** scores posted (2 is full credit)
# - Eena's OH changed to Zoom for rest of quarter (Zoom link on Canvas homepage)

# - **E1** will be made available Friday late afternoon/early evening. 
#     - Announcement on campuswire/email when posted.
#     - Must be submitted by 11:59 PM Monday 10/18
#     - designed to take ~1 h (most students will likely spend 2h)
#     - will cover material through *loops* lecture
#     - **NO lecture** Mon 10/18
#     - Practice exam (datahub) & materials (Exam-Prep folder on datahub/section on website) now available (answer keys posted Friday)

# **Q&A**
# 
# Q: How to search the keyword, just like in docx and pdf, in our Jupyter Notebook?  
# A: cmd/ctrl + f works or Edit > Find & Replace
# 
# Q: Are there instances where we need an infinite loop  
# A: No.
# 
# Q: How to avoid writing an infinite loop ?  
# A: Be sure when writing while loop, that the condition following `while` will at *some point* evaluate as False. For a `for` loop, be sure that you're not extending the list you're looping through infinitely.
# 
# Q: honestly im still confused on when to use loops and the format of them  
# A: Whenever you want to repeat some bit of code multiple times, consider using a loop. As for the format, hopefully today clears that up!
# 
# Q: So any set of numbers starts counting at 0 right?  Whether it be a list, a tuple or a string?  
# A: Correct! Python is zero-based as a language, so that carries across everything in Python.
# 
# Q: Are counters strictly called counters? Or, is counter just a variable name that can be switched to a different name?  
# A: Great question. The variable name can be *anything*. The concept is that they are a counter b/c they are keeping track, but the variable name could be anything at all.
# 
# Q: One of the things that was interesting for me was the range function. When writing for loops in R, to use a range, you would just do 1:7 for a range of 1 to 7 for instance. If anything I think the range function in python is similar to the seq (sequence) function in R.  
# A: Yes! there are certain aspects of loops in R that are more straightforward ...but then the syntax in python is more "clear" at first glance. But this is a good mapping of concepts between the languages!
# 
# Q: What are assertion errors and how do I resolve them?  
# A: Assertion errors let you know which `assert` statement "failed" ....meaning that whatever followed `assert` is not True (and it should be). So, you have to figure out why the `assert` is not True given the code you've written. If unsure after reading this, understanding `assert`s will be *really* helpful throughout this course, so definitely ask in coding lab/office hours for further clarification if unsure still!
# 
# Q: Can you incorporate an "if" statement within a "while" statement and vice versa?  
# A: Yup! We'll get to this soon. But all of the "code constructs" we're learning about can be combined.
# 
# Q: My remaining question is, if "a" and "b" both point to the same place in memory, then how do they have different values. I assume that a new place is created in memory for the altered value of 'a", while b remains "pointing" to the old memory location, but I am not sure this is true.  
# A: Yes! When you change the value for `a`, it's place in memory changes. You can "see" this if you check `id(a)` and `id(b)` prior to and after changing the value.
# 
# Q: I find an interesting thing that's slightly off the topic but I don't know why: `int(True)` equals to 1 and `int(False)` equals to 0.  
# A: This is somewhat historical. Specifically, Python didn't have booleans when the language was first developed. If you wanted to indicate "True", you'd use a 1 and "False", a 0. So, when booleans were introduced, they became a subtype of integers. Beyond the scope of this class, but interesting nonetheless!
# 

# **Course Announcements (Wed 10/20)**
# 
# **Due Dates**:
# - **CL4** due tonight (11:59 PM)
# - **A2** due Friday (11:59 PM)
# - **A3** now available; deadline now Mon 11/1 (this is a change; syllabus and Canvas have been updated)
# 
# **Notes**:
# - **CL3** scores posted
# - **E1** grading is underway

# Q: Where and what day are Hannah, Janice and Yvonne’s office hours? What is the course code on campus wire? Why wasn’t this on the syllabus? Why don’t all the IAs list their email or canvas email enabled?  
# A: Hannah, Janice, and Yvonne do not have weekly office hours. If you feel there isn't enough help throughout the week betwen avaialable office hours and coding labs all day on Wednsday, let me know and we'll see what we can do! The course code for campuswire is not on the syllabus b/c the syllabus is public-facing and we want campuswire to only be accessible to those in our course. Thus, the code for campuswire is on Canvas. Any "private" code (zoom link, campuswire code, etc.) will always be on the home page for our course on Canvas. Emails are not provided on the syllabus, as campuswire allows for direct messaging.
# 

# Q: When creating a loop when would we use a break?  
# A: Most often in testing. If you're trying to figure out why your loop isn't "working" you can add a `print()` statement followed by a `break`. This way what you want to check will be printed and then the loop will terminate and you can move onto debugging the next part of the loop.
# 
# Q: I'm still confused about what's immutable and mutable and how do we know which type is either immutable or mutable.
# A: Mutable are variables that allow you to change part of the variable after the variable has been defined. The only one discussed so far are lists. Today, we'll also discuss dictionaries (which are mutable). Everything else (integers, strings, booleans, Nonetype, floats, and tuples) are all immutable.

# # Encodings & Dictionaries
# 
# - symbols & representations
# - Encodings
# - Dictionaries
# - `ord` & `chr`

# What is a human representaion? human encoding? 
# 
# How do computers encode information?

# #### Clicker Question #1
# 
# What is a symbol?
# 
# - A) A character that can be typed on a computer
# - B) Something that can stand in the place of something else
# - C) Something that looks like something else
# - D) A character or sign used to represent something arbitrary
# - E) I have no idea

# ## Symbols

# <div class="alert alert-success">
# Symbols are characters (or 'signs') of arbitrary shape, that can refer to (or represent) something. 
# </div>

# ##  Representation

# <div class="alert alert-success">
# To represent means to stand in for something.
# </div>

# - **iconic representation** : the object looks like the thing it represents (i.e. a picture)
# - **symbolic representation** : the symbol does *not* look like the thing it represents (i.e. letters, numbers) 
# 

# ### Symbol Examples : concepts
# 
# - The symbol `2` represents the concept of `two-ness`. 
#     - This is arbitrary: there is nothing 'two-like' about `2`
#     - We need not use this symbol. The symbol `II` also represent `two-ness`.
#     - `2` and `II` are two different representations for the concept of two.
# - The symbol `b`, in english represents the sound `buh` (sort of). 
#     - There is nothing 'buh' like about the symbol `b`

# ### Symbol Examples : rules
# 
# Given the symbol `2`, or `b` we have systematic rules of things we can do with them. 
# - We can take `2` and add `1` and get a new symbol which represents the concept of `the value one bigger than two`
# - We can concatenate some, but not all, other letters (symbols) to `b` to start making rules
# - These rules are agnostic to what `2` or `b` represent, they are simply manipulations we can do with these symbols

# ## Digital Computers
# 
# Computers don't care about what the symbols look like. They don't care what symbols you use.
# 
# But, once a rule is established for a certain symbol, the computer will always follow that rule. 

# <div class="alert alert-success">
# Computation is symbol manipulation - using formal rules to manipulate symbols. 
# </div>

# Whenever we have symbols, and rules to manipulate them, we can do computation. 
# 
# When we use these symbols that represent meaningful things, we can use computers to make meaningful inferences.
# 
# Everything you think of as a computer (laptop, cell phone, etc.) works as a digital computer.

# ##  Encoding & Decoding

# <div class="alert alert-success">
# Encoding can be thought of as the process of 'changing representation', and decoding as the process of changing it back. 
# </div>

# Changing back and forth between using the symbol '2' and 'II' to represent the concept of two is an example of "changing representation."

# ## Aside: Binary
# 
# Fundamentally, digital computers can represent two states. Because of this, we say computers are / use binary. 
# 
# From binary, we can build up to store other things, that reduce down to binary representations.
# 
# We can then encode any value we would like to represent on our computer.  

# ### Binary in Code

# In[ ]:


## The `bin` operator returns the binary representation of an integer
# encoding an integer
print(bin(1))


# In[ ]:


print(bin(78))


# In[ ]:


#possible to encode Booleans in binary
#encoding a boolean
bin(False)


# In[ ]:


print(bool(0b0))


# In[ ]:


# We can also convert binary back to integers with 
# decoding from binary
int(0b1011)


# ## Character Encodings

# Character encodings are a set of rules of how to represent a broad range of characters (symbols) in computers. 
# 
# We already have a way to represent numbers in binary.  
# 
# Using numbers, we can build a general procedure to encode characters as numbers.
# 
# We then have a way to represent characters, that we can reduce all the way to binary, that we can use that on computers.

# ## Example: Character Encoding

# As a simple example, let's assign a number to a series of characters we want to be able to represent. 
# 
# Every time we see that number, we can evaluate it to replace it with the character it represents. 

# ### Character Encoding in Code

# In[ ]:


# Set the value we want to encode
character_encoding = 0

# Use conditional to interpret the character as a particular symbol
if character_encoding == 0:
    print('ñ')
elif character_encoding == 1:
    print('é')
elif character_encoding == 2:
    print('¿')


# ## Dictionaries
# 

# <div class="alert alert-success">
# A dictionary is mutable collection of items, that can be of mixed-type, that are stored as key-value pairs.
# </div>

# ### Dictionaries as Key-Value Collections

# In[ ]:


# Create a dictionary
dictionary = {'key_1' : 'value_1', 'key_2' : 'value_2'}


# In[ ]:


# Check the contents of the dictionary
print(dictionary)


# In[ ]:


# Check the type of the dictionary
type(dictionary)


# In[ ]:


# Dictionaries also have a length
# length refers to how many pairs there are
len(dictionary)


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


# #### Clicker Question #2
# 
# Which of the following would create a dictionary of length 3?
# 
# - A) `{'Student_1' : 97, 'Student_2'}`
# - B) `{'Student_1', 'Student_2', 'Student_3'}`
# - C) `['Student_1' : 97, 'Student_2': 88, 'Student_3' : 91]`
# - D) `{'Student_1' : 97, 'Student_2': 88, 'Student_3' : 91}`
# - E) `('Student_1' : 97, 'Student_2': 88, 'Student_3' : 91)`
# 

# #### Clicker Question #3
# 
# Fill in the '---' in the code below to return the value stored in the second key.

# In[ ]:


height_dict = {'height_1' : 60, 'height_2': 68, 'height_3' : 65, 'height_4' : 72}
height_dict[---]


# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# ### Example Dictionaries

# In[ ]:


student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : 'ada@analyticengine.com',
    'Alan Turing' : 'aturing@thebomb.gov',
    'Grace Hopper' : 'ghopper@navy.usa'
}

student_emails


# In[ ]:


completed_coding_lab = {
    'A1234' : True,
    'A5678' : False,
    'A9123' : True
}

completed_coding_lab


# In[ ]:


mixed_types = {
    True  : [1, 2, 3],  
    False : None
}

mixed_types


# #### Clicker Question #4
# 
# Write the code that would create a dictionary `car` that stores values about your dream car's `make`, `model`, and `year`.
# 
# - A) I did it
# - B) I think I did it...
# - C) I tried and am stuck
# - D) No clue where to start...

# In[1]:


# YOUR CODE HERE


# ### Dictionaries are mutable
# 
# This means that dictionaries, once created, values *can* be updated.

# In[ ]:


# remember what dictionary we created above
completed_coding_lab


# In[ ]:


# change value of specified key
completed_coding_lab['A5678'] = True
completed_coding_lab


# Because dictionaries are mutable, key-value pairs can also be removed from the dictionary using `del`.

# In[ ]:


print(completed_coding_lab)
len(completed_coding_lab)


# In[ ]:


## remove key-value pair using del
del completed_coding_lab['A5678']

print(completed_coding_lab)
len(completed_coding_lab)


# ### Dictionaries and operators
# 
# The operators we've discussed previously can be used when working with dictionaries.
# 
# To determine if a specified key is present in a dictionary we can use the `in` operator:

# In[ ]:


if 'A1234' in completed_coding_lab:
    print('Yes, that student is in this class')


# #### Clicker Question #5
# 
# What will the value of `result` be after this code has run?

# In[ ]:


dictionary = {'alpha' : [8, 12], 
              'beta'  : [13, 30], 
              'theta' : [4, 8]}

check = 10

for item in dictionary:
    temp = dictionary[item]
    if temp[0] <= check <= temp[1]:
        result = item
        
print(result)


# - A) alpha
# - B) [8, 12] 
# - C) beta 
# - D) theta 
# - E) alpha beta

# ### Additional Dictionary Properties
# 
# - Only one value per key. No duplicate keys allowed. 
#     - If duplicate keys specified during assignment, the last assignment wins.

# In[ ]:


# Last duplicate key assigned wins
{'Student' : 97, 'Student': 88, 'Student' : 91}


# - **keys** must be of an immutable type (string, tuple, integer, float, etc)
# - Note: **values** can be of any type

# In[ ]:


# lists are not allowed as key types
# this code will produce an error
{['Student'] : 97}


# - Dictionary keys are case sensitive.
# 

# In[ ]:


{'Student' : 97, 'student': 88, 'STUDENT' : 91}


# #### Clicker Question #6
# 
# Why does the following code produce an error?

# In[ ]:


student_emails = {
    'Betty Jennings' : 'bjennings@eniac.org',
    'Ada Lovelace' : ['ada@analyticengine.com'],
    'Ada Lovelace' : 'aturing@thebomb.gov',
    ['Grace Hopper'] : 'ghopper@navy.usa'
}


# - A) duplicate keys
# - B) mutable key specified
# - C) keys are case sensitive 
# - D) mutable value specified 
# - E) ¯\\\_(ツ)\_/¯

# ## Character Encodings with Dictionaries

# In[ ]:


# Define some character encodings
character_encodings = {
    0 : 'ñ',
    1 : 'é',
}


# In[ ]:


# Use character encodings to use symbols we want - example 1
my_sentence = 'no hablo espa' + character_encodings[0] + 'ol'
print(my_sentence)


# In[ ]:


# Use character encodings to use symbols we want - example 2
my_sentence = 'yo hablo ingl' + character_encodings[1] + 's'
print(my_sentence)


# ## Unicode

# <div class="alert alert-success">
# Unicode is a system of systematically and consistently representing characters. 
# </div>

# Every character has a unicode `code point` - an integer that can be used to represent that character. 
# 
# If a computer is using unicode, it displays a requested character by following the unicode encodings of which `code point` refers to which character. 

# ### ORD & CHR

# <div class="alert alert-success">
# <code>ord</code> returns the unicode code point for a one-character string.
# </div>
# 
# <div class="alert alert-success"> 
# <code>chr</code> returns the character encoding of a code point. 
# </div>

# ### ord & chr examples

# In[ ]:


print(ord('a'))


# In[ ]:


print(chr(97))


# ### Inverses
# 
# `ord` and `chr` are inverses of one another. 

# In[ ]:


inp = 'b'
out = chr(ord(inp))

assert inp == out
print('Input: \t', inp, '\nOutput: ', out)


# ## Extra Practice

# ### Extra Practice #1
# 
# Generate a dictionary called `about_me` that meets the following criteria:
# 
# - has three keys: 'name', 'favorite_game', and 'height'
# - stores _your_ `name` (string), `favorite_game` (string), and `height` (int) in inches as each key's value
# 

# In[ ]:


# YOUR CODE HERE


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.

# ### Extra Practice #2
# 
# Store your name in the variable `my_name`. Then, encode your  name, such that each letter is first replaced by the unicode code point for that letter plus 500 and then turned back into a character using `chr`. Store the new output in `out_name`.

# In[ ]:


# YOUR CODE HERE


# - A) I did it!
# - B) I think I did it.
# - C) I started but am now stuck.
# - D) I have no idea where to start.
