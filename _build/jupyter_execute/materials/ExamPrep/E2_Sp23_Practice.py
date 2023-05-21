#!/usr/bin/env python
# coding: utf-8

# Answer Key to in-class practice: https://docs.google.com/document/d/1YXiP1LR5dHu4wtQBuJMPYUnFQV2kMnrwyKVTHqoRQXM/edit?usp=sharing

# # COGS 18 - Practice Exam 2
# 
# This is the second practice exam for Spring 2023. It covers topics through the Command Line Lecture.
# 
# This is worth 0 points and worth 0% of your grade, but the real total exam (in-person + take-home) is out of 12.5 points, worth 12.5% of your grade. 
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.
# 
# <span style="color:red">Note: There are WAYYYYYY more questions on this practice exam than on the real exam. This is because a number of students have asked for additional practice problems. So, do not be intimidated by the length here, but feel free to use it for extra practice!</span>

# ## Instructions
# 
# #### Timing
# - The exam is designed to take you ~1-2h.
# - There will be a >24 hour window during which you can complete this exam.
# - If it takes you longer than 1-2h, you're free to use that time.
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Google
# - You may not talk to any humans about this exam. 
# - The following are all *prohibited*:
#     - text/phone/online chat communication
#     - posting questions to a message board where a human could respond (Campuswire, Discord, Chegg, any similar site)
#     - viewing exam questions from a message board (as described above)
#     - asking anyone via any form about a question on this test directly
# - Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
#     - Campuswire posts about the exam will not be answered and will be deleted. 
#     - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
#     - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
#     - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

#  <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

# ### Q0 - Honor Code
# 
# In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:
# 
# >I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.
# 

# In[1]:


### BEGIN SOLUTION
honor_code = True
### END SOLUTION


# In[2]:


assert honor_code


# ## Part 1: Methods, Debugging & Code Style

# ### Q1 - Method I
# 
# `isalpha()` is a string method that determines if all the characters in a string are in the alphabet (meaning letters or numbers: A-Z, a-z).
# 
# Use the `isalpha()` method on two strings (of your choosing) below to create two variables:
# - `true_var` | should store the value `True`
# - `false_var` | should store the value `False`

# In[3]:


### BEGIN SOLUTION
true_var = 'asdf'.isalpha()
false_var = '!!!!'.isalpha()
### END SOLUTION


# In[4]:


assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS


# In[5]:


assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `isalnum()` (**0.6 pts**)
# 
# === END MARK SCHEME ===

# ### Q2 - Method II 
# 
# `istitle()` is a string method that determines if the string follows the rules of a title (meaning the first letter of each distinct word is upper case while all other letters are lower case).
# 
# Use the `istitle()` method on two strings (of your choosing) below to create two variables:
# - `true_var` | should store the value `True`
# - `false_var` | should store the value `False`

# In[6]:


### BEGIN SOLUTION
true_var = 'My Title'.istitle()
false_var = 'MY TITLE'.istitle()
### END SOLUTIONs


# In[7]:


assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS


# In[8]:


assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `istitle()` syntax correctly (**0.35 pts**)
# 
# === END MARK SCHEME ===

# ### Q3 - Method III
# 
# Using the `count()` method, code constructs discussed in class, and referencing the `prof_day` variable provided below, generate a dictionary `prof_events`, whose keys are each of the unique elements in `prof_day` and whose corresponding values are the number of times each value shows up in `prof_day`.
# 
# 
# Notes:
# - `prof_day` has been defined for you below
# - `count()` is a list method that counts the number of appearances of a specified element in a list.
# - Do not hard-code. You should use code contructs to determine `prof_events`.

# In[9]:


# these variables provided for you
# you will not be able to edit this cell
prof_day = ['write one exam', 'write one exam', 'grade exam', 'answer email', 'office hours', 'staff meeting']


# In[10]:


# hidden test being used in grading
### BEGIN HIDDEN TESTS
# change one value in list to ensure code still executes (aka is not hard-coded)
prof_day = ['write one exam', 'write one exam', 'answer email', 'answer email', 'office hours', 'staff meeting']
### END HIDDEN TESTS


# In[11]:


### BEGIN SOLUTION
prof_events = {}

for ele in prof_day:
    prof_events[ele] = prof_day.count(ele)

prof_events
### END SOLUTION


# In[12]:


assert prof_events is not None
### BEGIN HIDDEN TESTS
# check that keys are all what they should be
assert all(elem in list(prof_events.keys())  for elem in ['write one exam', 'answer email', 'office hours', 'staff meeting'])
### END HIDDEN TESTS


# In[13]:


# hidden tests for task above
### BEGIN HIDDEN TESTS
# check that values are what they should be
assert sum(prof_events.values()) == 6
assert all(elem in list(prof_events.values()) for elem in [2,1])
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - initialized or created `prof_events` as a dictionary (**0.25 pts**)
# - Used count() method correctly (**0.25 pts**)
# - updated `prof_events` dictionary correctly (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q4 - Debugging & Code Style
# 
# In the cell below, there is a function that is not operating as anticipated *and* that has bad code style.
# 
# `count_consonants` is _supposed_ to take a string as input and count the number of each consonant in the `input_string` (input parameter), storing the output in a dictionary where the key is the consonant and the value is the number of times it appears in the input. 
# 
# Note that we want capitalization to be considered such that the capital and lower case letters are counted together, and the lower case letter is used as the key (i.e. 'A' and 'a' would both be counted under the key 'a')
# 
# Specifically, if the `input_string` were "Mohammed", the function ould return: `{'m': 3, 'h': 1, 'd': 1}`
# 
# Debug, edit, and test the function provided below so that it accomplishes the intended goal. 
# 
# ```python
# def count_consonants():
#     out={}
#     vowels=['a','e','i','o','u']
#     for char in input_string:
#         if char not in vowels:
#             if char not in out:
#                 out[char]=1
# 
# ```
# 
# *Then* be sure to **edit the function you generate so that it follows the code style guidelines** discussed in class.

# In[14]:


### BEGIN SOLUTION
def count_consonants(input_string):
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        char = char.lower()
        
        if char not in vowels:
            if char not in out:
                out[char] = 1
            else:
                out[char] += 1
    return out
### END SOLUTION


# In[15]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[16]:


assert count_consonants is not None

### BEGIN HIDDEN TESTS
assert count_consonants('Taylor') == {'t': 1, 'y': 1, 'l': 1, 'r': 1}
### END HIDDEN TESTS


# In[17]:


assert callable(count_consonants)

### BEGIN HIDDEN TESTS
assert count_consonants('AaBbCc') == {'b': 2, 'c': 2}
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Debugging:
# - input parameter included (**0.2 points**)
# - captitalization accounted for (**0.2 points**)
# - else condition (or equivalent) included (**0.2 points**)
# - return statement included (**0.2 points**)
# 
# Code Style: 
# - has reasonable spacing around operators
# - some reasonable line spacing introduced
# === END MARK SCHEME ===

# ### Q5 - Debugging & Code Style
# 
# In the cell below, there is a function that is not operating as anticipated *and* has bad code style.
# 
# `new_encrypt` is _supposed_ to take a string as input and return the reverse alphabetical string as output, meaning, given a character, return the capitalized character in the reverse position within the alphabet. 
# 
# For example, if the input character is 'B' or 'b', the function would store 'Y' in the output string. If the character is 'A' or 'a', the function would store 'Z'. (and vice versa: the input 'Z' or 'z' would store 'A').
# 
# Specifically, if the `input_string` were "ABc", the function would `return`: 'ZYX'
# 
# Debug, edit, and test the function provided below so that it accomplishes the intended goal.
# 
# ```python
# def new_encrypt():
#     alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     reverse_alpha='ZYXWVUTSRQPONMLKJIHGFEDCBA'
#     for char in input_string:
#         if char in alpha:
#             position=alpha.find(char)
#             output_string+=reverse_alpha[position]
#         else:
#             output_string=None
#             break
# ```
# 
# *Then* be sure to **edit the function you generate so that it follows the code style guidelines** discussed in class.

# In[18]:


### BEGIN SOLUTION
def new_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    output_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
        
    return output_string
### END SOLUTION


# In[19]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[20]:


assert new_encrypt
### BEGIN HIDDEN TESTS
assert new_encrypt('mohammed') == 'NLSZNNVW'
### END HIDDEN TESTS


# In[21]:


assert callable(new_encrypt)

### BEGIN HIDDEN TESTS
# will work even if they missed the .upper()
# has correct input parameter
assert new_encrypt(input_string='ABC') == 'ZYX'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Debugging:
# - `input_string` parameter included (**0.15 points**)
# - empty `output_string` initialized (**0.2 points**)
# - capitalization accounted for (**0.2 points**)
# - `return` statement included (**0.2 points**)
# 
# Code Style: 
# - has reasonable spacing around operators
# - some reasonable line spacing introduced
# 
# === END MARK SCHEME ===

# ### Q6 - Debugging (1.5 points)
# 
# The following not-totally-functioning `give_ticket()` function has been provided for you. The *goal* of this function, is given two inputs (`speed` and `zone`), the function should return the boolean True if the person should receive a ticket and the boolean False otherwise.
# 
# The rules for giving a ticket depend upon the driver's speed and the zone in which they were driving. They would get a ticket if: 1) they're in a 'private' `zone` and their speed is above 5, 2) they're in a 'local' `zone` and their speed is above 25, or 3) they're in a 'highway' `zone` and their speed is above 65. 
# 
# For example, if the driver's `speed` was 25 and their zone was 'local', the function would return `False`. However, if in the same zone, and their speed were 26, the function would return `True`. 
# 
# Consider the function provided below and then debug to accomplish the task specified above.:
# 
# ```python
# def give_ticket(self, speed, zone):
#     if zone = 'private' or speed > 5:
#         print(True)
#     elif zone = 'local' or speed > 25:
#         print(True)
#     elif zone = 'highway' or speed > 65:
#         print(True)
#     else:
#         print(False)
# ```
# 
# Note: Do not change the name of the function (`give_ticket`), and the parameter names provided in the instructions (`speed`, `zone`) must be used.

# In[1]:


### BEGIN SOLUTION
def give_ticket(speed, zone):

    if zone == 'private' and speed > 5:
        ticket = True
    elif zone == 'local' and speed > 25:
        ticket = True
    elif zone == 'highway' and speed > 65:
        ticket = True
    else:
        ticket = False

    return ticket
### END SOLUTION


# In[2]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[3]:


assert give_ticket
### BEGIN HIDDEN TESTS
assert give_ticket(speed=6, zone='private') 
assert give_ticket(speed=26, zone='local') 
assert give_ticket(speed=66, zone='highway') 
### END HIDDEN TESTS


# In[4]:


assert callable(give_ticket)
### BEGIN HIDDEN TESTS
assert not give_ticket(speed=5, zone='private') 
assert not give_ticket(speed=10, zone='local') 
assert not give_ticket(speed=45, zone='highway') 
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `self` removed as a parameter (**0.1 pts**)
# - fixed conditional operator `=` to `==` (**0.25 pts**)
# - `or` changed to `and` in conditional (**0.25 pts**)
# - `print()` statements changed to store variable (**0.25 pts**)
# - `reuturn` statement added (**0.15 pts**)
#                                                               
# === END MARK SCHEME ===

# ## Part 2: Loops & Functions
# 
# Note this section has *more* questions than your real exam will have. This is just to get you additional practice.

# ### Q7 - Function execution
# 
# The cell below includes a function that has been provided for you. After running the cell below (to define this function), execute (use) this function to create the following variables under the specified conditions:
# 
# 1. `square_default` | execute the `square_all` function using the default parameter such that the output will carry out the function on a list of input values containing the integers 2, 3, and 4. 
# 2. `power_three` | Use the same input values as above, but this time, use the `square_all` function provided to raise all input values to the power 3
# 3. `out_4` | Execute the `square_all` function such that `out_4` will store a list with 4 values, each of which is the integer 4.

# In[26]:


def square_all(collection, power=2):
    
    square_list = []
    for val in collection:
        square_list.append(val**power)
    
    return square_list


# In[27]:


# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)


# In[28]:


### BEGIN SOLUTION
square_default = square_all([2,3,4])
power_three = square_all([2,3,4], 3)
out_4 = square_all([2,2,2,2]) # this execution could differ
### END SOLUTION


# In[29]:


assert square_default is not None

### BEGIN HIDDEN TESTS
assert  square_default == [4,9,16]
### END HIDDEN TESTS


# In[30]:


assert power_three is not None

### BEGIN HIDDEN TESTS
assert power_three  == [8, 27, 64]
### END HIDDEN TESTS


# In[31]:


assert out_4 is not None

### BEGIN HIDDEN TESTS
assert out_4  == [4,4,4,4]
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# function executed appropriately for variable creation (aka not hard coded) (**1 point** ; 0.33 per function call)
# 
# === END MARK SCHEME ===

# ### Q8 - Function Execution
# 
# The function `count_sentences()` has been provided for you below. Note that `split()` is a string method that splits a string at the character specified within the parentheses of the method call.
# 
# **Part 1** 
# 
# First, in the cell provided below containing `YOUR ANSWER HERE`, describe what the `count_sentences()` function accomplishes. This should include both 1) the overall task accomplished and 2) how the specific code used accomplishes this task.

# In[32]:


def count_sentences(text):
    sentences = text.split('.')
    
    if sentences[-1]=='':
        num_sentences = len(sentences) - 1
    else:
        num_sentences = len(sentences)
        
    return num_sentences


# In[33]:


# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)


# Describe the `count_sentences()` function here.
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - explains task generally accurately (**0.25 pts**)
# - explains what `.split()` does in context accurately (**0.25 pts**)
# - explains what conditional does/why it's needed (**0.25 pts**)
# 
# === END MARK SCHEME ===

# **Part 2**
# 
# Execute the `count_sentences()` function such that it:
# - returns `2`; assign this output to the variable `out_2`.

# In[34]:


### BEGIN SOLUTION
out_2 = count_sentences('A sentence with words. A second sentence with words.')
### END SOLUTION


# In[35]:


assert out_2
### BEGIN HIDDEN TESTS
assert out_2 == 2
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - remove autograder credit above if function not executed
# 
# === END MARK SCHEME ===

# ### Q9 - `count_int` 
# 
# Write a function `count_int` that will take a tuple or list as the input and count the number (count) of integer values in that tuple/list, returning this value from the function. 
# 
# For example, if 3 of the values in the input list were integers, the function would return 3.
# 
# Note: You can assume the input to this function will be a tuple or list and do *not* need to write code to check whether or not this is true.

# In[36]:


### BEGIN SOLUTION
def count_int(col):
    count = 0
    
    for val in col:
        if type(val) == int:
            count += 1
    
    return count
### END SOLUTION


# In[37]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[38]:


assert callable(count_int)

### BEGIN HIDDEN TESTS
assert count_int((1,2,3,4,5,'string',4.4)) == 5
assert count_int([1,2,3,4,5,'string',4.4]) == 5
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - function defined correctly (**0.5 points**)
# - input parameter specified  (**0.5 points**)
# - counter initialized (**0.5 points**)
# - for loop (or equivalent) correct (**0.2 points**)
# - conditional (or equivalent) correct (**0.3 points**)
# - counter incremented correctly (**0.5 points**) 
# - `return` statement included (**0.5 points**)
# 
# === END MARK SCHEME ===

# ### Q10 - `modify_string`
# 
# 
# In this question, you're going to define a function called `modify_string()` that will change `input_string` using the key-value pairs in `new_language` (provided below), ultimately returning the updated name from the function.
# 
# Specifically, if any of the letters in your name (`input_string`) are keys in the dictionary `new_language` below, use that key's value in that letter's place in the string being output from the function. If the letter is not in `new_language`, add the original character from `input_string` to the string being output from the function.
# 
# For example, if `input_string` were 'Shannon', `modif_string()` would `return` 'Shӓnnðn' (the a and the o have the modified character from `new_language`)
# 
# 
# This function should have a single parameter: `input_string` - the string to be modified.

# In[43]:


new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð',
                'u' : 'û',
                'A' : 'Ӓ',
                'E' : 'ɛ',
                'O' : 'Ó',
                'U' : 'Ü'}


# In[44]:


### BEGIN SOLUTION
def modify_string(input_string):
    
    new_language = {'a': 'ӓ',
                    'e' : 'ɚ',
                    'i' : '¡',
                    'o' : 'ð',
                    'u' : 'û',
                    'A' : 'Ӓ',
                    'E' : 'ɛ', 
                    'O' : 'Ó', 
                    'U' : 'Ü'}
    
    modified_name = ''
    
    for letter in input_string:
        if letter in new_language:
            modified_name = modified_name + new_language[letter]
        else:
            modified_name = modified_name + letter

    return modified_name
                
### END SOLUTION


# In[45]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[46]:


assert modify_string

### BEGIN HIDDEN TESTS
assert modify_string('Taylor') == 'Tӓylðr'
### END HIDDEN TESTS


# In[47]:


assert callable(modify_string)

### BEGIN HIDDEN TESTS
# check functioning for capital letters
assert modify_string('AaBbCcEe') == 'ӒӓBbCcɛɚ'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - function defined correctly & input parameter specified (**0.1 points**)
# - for loop (or equivalent) correct (**0.1 points**)
# - conditional (or equivalent) correct (**0.1 points**)
# - string updated correctly (**0.1 points**) 
# - `return` statement included (**0.1 points**)
# 
# === END MARK SCHEME ===

# ### Q11 - `calculate_points`
# 
# Write a function `calculate_points` that has a single input parameter: `hand`. `hand` can be assumed to be a list of string values, where each string corresponds to a value in a deck of cards (2-10, J, Q, K, or A)
# 
# This function should calculate the total number of "pointer" cars in your hand, where ***a "pointer" is either a 10, J, Q, K, or A***. Each "pointer" is worth one point. All other cards are worth zero points. The function should `return` the total number of points in the `hand` as an integer.
# 
# For example, if your `hand` input was: 
# 
# ```python
# ['J', '10', '2', '5', 'K']
# ```
# 
# executing the `calculate_points()` function with the above list as the input to the `hand` parameter, the function would `return` the integer 3 (one point each for the `'J'`, `'10'`, and `'K'`.
# 
# If there are no pointers in the input `hand`, the function should return 0.

# In[48]:


### BEGIN SOLUTION
def calculate_points(hand):
    pointers = ['10', 'J', 'Q', 'K', 'A']
    counter = 0
    
    for card in hand:
        if card in pointers:
            counter += 1
        
    return counter
### END SOLUTION


# In[49]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[50]:


assert callable(calculate_points)

### BEGIN HIDDEN TESTS
# use default parameter
assert calculate_points(['K']) == 1
### END HIDDEN TESTS


# In[51]:


# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure returns zero if no pointers
assert calculate_points(['2', '7', '9']) == 0
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - function defined correctly with single parameter (**0.1 points**)
# - loop (or equivalent) correct (**0.1 points**)
# - conditional (or equivalent) correct (**0.1 points**)
# - counter incremented correctly (**0.1 points**)
# - `return` statement included (**0.1 points**)
# 
# === END MARK SCHEME ===

# ### Q12 - `to_taxes`
# 
# Here you will write a function that, given a salary as input, will `return` how much of that person's salary is going toward taxes.
# 
# To accomplish this, write a function `to_taxes()` that takes two parameters as input: `salary` and `tax_brackets`. The default value for the `tax_brackets` parameter should be the `default_brackets` dictionary provided below. Then, use code constructs discussed in class to accomplish the above goal.
# 
# Note that the dictionary `default_brackets` provided will have to be used to accomplish this goal. The keys in `default_brackets` are the proportion of an individual's salary that will go toward taxes if their salary is within the range in a given key's value (tuple). For example, an individual who makes \$10,000 would contribute 12\% of their salary in taxes, given the information in `tax_brackets` (specifically becasue 10000 falls between 9876 and 40125).
# 
# Accordingly, `to_taxes(salary=10000)` should `return` 1200.0 (which corresponds to 12\% of the input $10,000 salary).

# In[52]:


default_brackets = {0.10 : (0, 9875),
                    0.12 : (9876, 40125),
                    0.22 : (40126, 85525),
                    0.24 : (85526, 163300),
                    0.32 : (163301, 207350),
                    0.35 : (207351, 518400)
                   }


# In[53]:


### BEGIN SOLUTION
def to_taxes(salary, tax_brackets=default_brackets):
    for key in tax_brackets:
        if tax_brackets[key][0] <= salary <= tax_brackets[key][1]:
            output = key * salary
    
    return output
### END SOLUTION


# In[54]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[55]:


assert to_taxes
### BEGIN HIDDEN TESTS
assert callable(to_taxes)
assert to_taxes(10000) == 1200.0
assert to_taxes(207355) == 72574.25
### END HIDDEN TESTS


# In[56]:


# hidden test to check function accomplishes task
### BEGIN HIDDEN TESTS
# check for 22% bracket
# check that values on edges included
assert to_taxes(40126) == 8827.72
assert to_taxes(85525) == 18815.5
### END HIDDEN TESTS


# In[57]:


# hidden test to check default parameter correct
### BEGIN HIDDEN TESTS
# check for a different tax_brackets
assert to_taxes(100, tax_brackets={0.5: (0,1000)}) == 50.0
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - function defined correctly with `salary` parameter and default value for `tax_brackets` parameter (**0.25 pts**)
# - loops through dictionary (or equivalent) correctly (**0.2 pts**)
# - conditional accesses values in tuple correctly (**0.2 pts**)
# - conditional checks lower and upper bound of range (**0.2 pts**)
# - calculation correct (i.e. key * salary) (**0.2 pts**)
# - includes `return` statement (**0.2 pts**) 
# 
# === END MARK SCHEME ===

# ### Q13 - `write_tickets`
# 
# Here you will write a function `write_tickets()` that will take a dictionary as input (using the parameter `input_dict`) and determine who in that dictionary will receive  a ticket. The key in the `input_dict` will be the person's name, and the value will be a list of two values. The first value will be the person's zone ('private', 'local', or 'highway') and the second will be the speed at which the person was traveling. The output `return`ed from this function will be a dictionary of every person in the original dictionary's name as they keys. The value for each individual will be either the boolean `True` (if that person should receive a ticket) or `False` (if they should not). 
# 
# For example: `write_tickets({'Shannon' : ['local', 20], 'Josh' : ['highway', 80]})` should `return` the dictionary `{'Shannon' : False, 'Josh' : True}`
# 
# Note: You can assume that each key in the input dictionary only shows up one time. You do not need to worry about how to handle the same name showing up more than once.

# In[58]:


### BEGIN SOLUTION
def write_tickets(input_dict):
    output_dict = {}
    
    for key in input_dict:
        zone = input_dict[key][0]
        speed = input_dict[key][1]
        
        if zone == 'private' and speed > 5:
            output_dict[key] = True
        elif zone == 'local' and speed > 25:
            output_dict[key] = True
        elif zone == 'highway' and speed > 65:
            output_dict[key] = True
        else:
            output_dict[key] = False

    return output_dict
### END SOLUTION


# In[59]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[60]:


assert write_tickets
### BEGIN HIDDEN TESTS
# check provided example
assert write_tickets({'Shannon' : ['local', 20], 'Josh' : ['highway', 80]}) == {'Shannon': False, 'Josh': True}
### END HIDDEN TESTS


# In[61]:


# hidden test to check function accomplishes task
### BEGIN HIDDEN TESTS
# check for parameter name
assert write_tickets(input_dict = {'Shannon' : ['private', 20], 'Josh' : ['highway', 80]}) == {'Shannon': True, 'Josh': True}
### END HIDDEN TESTS


# In[62]:


# hidden test to check default parameter correct
### BEGIN HIDDEN TESTS
# check for a more than two values
assert write_tickets({'Shannon' : ['local', 20], 
                      'Kenny' : ['private', 20], 
                      'Josh' : ['highway', 80]}) == {'Shannon': False, 'Kenny': True, 'Josh': True}
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - function defined correctly with `input_dict` parameter (**0.1 pts**)
# - output_dict initialized (**0.2 pts**)
# - indexing into input_dict done correctly (**0.25 pts**)
# - loops through input_list correctly (or equivalent) (**0.15 pts**) 
# - conditionals included (even if incorrect) (**0.2 pts**)
# - output_dict updated correctly (**0.25 pts**)
# - includes `return` statement (**0.1 pts**) 
# 
# === END MARK SCHEME ===

# ## Part 3: Classes & Code Style
# 
# Note this section has *more* questions than your real exam will have. This is where students tend to struggle the most as the material is new and puts all the pieces we've talked about so far this quarter together, so I wanted you to have extra practice.

# ### Q14 - `Kingdom`
# 
# For this question (and the next one), imagine you want to create a video game with a handful of characters. You want this game to have a royal kingdom theme.
# 
# Here, define a class `Kingdom()`.
# 
# This class should have two instance attributes: `name` and `title`, which will be strings specifying the name and title of the character (in that order).
# 
# This class will also have a method `introduce()`. This method should `return` (*not* just `print`) a string, similar to:
# 
# ```
# 'Hello, my name is Ferdinand, and I am a King.' 
# ```
# 
# ...where 'Ferdinand' corresponds to whatever is stored in `Kingdom()` object's `name` attribute is and 'King' corresponds to whatever is stored in the `Kingdom()` object's `title` attribute.
# 

# In[63]:


### BEGIN SOLUTION
class Kingdom():
    
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def introduce(self):
        return 'Hello, my name is ' + self.name + ', and I am a ' + self.title + '.'
### END SOLUTION


# In[64]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[65]:


# Tests for the object
assert Kingdom

### BEGIN HIDDEN TESTS
queen = Kingdom('Elizabeth', 'Queen')
assert isinstance(queen, Kingdom)
assert queen.name == 'Elizabeth'
assert queen.title == 'Queen'
### END HIDDEN TESTS


# In[66]:


# Tests for introduce method
assert callable(Kingdom)

### BEGIN HIDDEN TESTS
assert callable(queen.introduce)
assert isinstance(queen.introduce(), str)
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - class defined correctly (**0.25 points**)
# - instance attributes initialized correctly with `self` + paramters (**0.25 points**)
# - `self` used correctly in instance attribute code block (**0.25 points**)
# - introduce method defined with `self` as parameter (**0.25 points**)
# - `return` statement returns a string (**0.25 points**)
# - `return` includes reference to `self.name` and `self.title` (**0.25 points**)
# 
# === END MARK SCHEME ===

# ### Q15 - `NewYear`
# 
# For this question, let's create a class to celebrate the Lunar New Year!
# 
# Here, define a class `NewYear()`.
# 
# This class should have:
# 
# - **one class attribute**: `zodiac_signs` that stores the dictionary specified in the cell below. This dictionary contains the zodiac sign as the key and the birth years that correspond to that sign.
# - **one instance attribute**:  `year` that takes the birth `year` as input from the user upon creation of a `NewYear` type object.
# 
# This class will also have a method `return_sign()`. This method should `return` (*not* just `print`) a string, similar to:
# 
# ```
# 'You were born in the year of the Dragon!' 
# ```
# 
# ...where 'Dragon' corresponds to the key from the `zodiac_signs` corresponding to the value stored in the `year` attribute. (Be sure captitalization and punctuation match the string specified here. The only thing that should change is the last word in the string.)
# 
# For example `NewYear(year=2021).return_sign()` should return 'You were born in the year of the Ox!', since 2021 is a value in the `zodiac_signs` dictionary for the key 'Ox'. 

# In[67]:


# provided for you
zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022], 
    'Rabbit' : [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023], 
    'Dragon' : [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024], 
    'Snake' : [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025], 
    'Horse' : [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026], 
    'Goat/Sheep' : [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027], 
    'Monkey' : [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028], 
    'Rooster' : [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029], 
    'Dog' : [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030], 
    'Pig' : [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031], 
    'Rat' : [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
} 


# In[68]:


### BEGIN SOLUTION
class NewYear():
    
    zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010], 
    'Rabbit' : [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023], 
    'Dragon' : [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024], 
    'Snake' : [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025], 
    'Horse' : [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026], 
    'Goat/Sheep' : [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027], 
    'Monkey' : [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028], 
    'Rooster' : [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029], 
    'Dog' : [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030], 
    'Pig' : [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031], 
    'Rat' : [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
    } 
    
    
    def __init__(self, year):
        self.year = year
    
    def return_sign(self):
        for key in self.zodiac_signs:
            if self.year in self.zodiac_signs[key]:
                out = key
                break # answer would be fine without break here
                
        return 'You were born in the year of the ' + out + '!'
### END SOLUTION


# In[69]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[70]:


# Tests for the object
assert NewYear
### BEGIN HIDDEN TESTS
dragon = NewYear(1988)
assert isinstance(dragon, NewYear)
### END HIDDEN TESTS


# In[71]:


assert callable(NewYear)
# Tests for classs attribute
### BEGIN HIDDEN TESTS
assert dragon.year ==  1988
### END HIDDEN TESTS


# In[72]:


# Tests for instance attribute
### BEGIN HIDDEN TESTS
assert isinstance(dragon.zodiac_signs, dict)
assert 'Ox' in dragon.zodiac_signs.keys()
### END HIDDEN TESTS


# In[73]:


# tests for method
# be sure punctuation matches instructions
### BEGIN HIDDEN TESTS
assert dragon.return_sign() == 'You were born in the year of the Dragon!'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - class defined correctly (**0.25 points**)
# - class attribute defined correctly (**0.25 points**)
# - instance attribute defined correctly (with `self` + parameter) (**0.15 points**)
# - method definition includes `self` (**0.1 points**)
# - method code loop/conditional correct. (**0.25 points**)
# - method code specifies self.name (**0.15 points**)
# - method includes `return` statement (**0.1 points**)
# 
# === END MARK SCHEME ===

# ### Q16 - `BasketballGame`
# 
# Generate a class called `BasketballGame`.
# 
# This class should have four instance attributes: `home_team`, `away_team`, `home_points`, and `away_points`
# 
# It should also have one method, `play_game()`. 
# 
# Within the `play_game` method, add code that would determine who the winner of the game is (determined by the team with the most points), returning Winner: ' and the winning team's name.
# 
# For ties, return: 'Winner: tie'

# In[74]:


### BEGIN SOLUTION
class BasketballGame():
    def __init__(self, home_team, away_team, home_points, away_points):
        self.home_team = home_team
        self.away_team = away_team
        self.home_points = home_points
        self.away_points = away_points
    
    def play_game(self):
        if self.home_points > self.away_points:
            out = 'Winner: ' + self.home_team
        elif self.away_points > self.home_points:
            out = 'Winner: ' + self.away_team
        else:
            out = 'Winner: tie'
        
        return out
### END SOLUTION


# In[75]:


# use this cell to test/execute/check your class (optional)


# In[76]:


assert callable(BasketballGame)

### BEGIN HIDDEN TESTS
game = BasketballGame(home_team='Warriors', away_team='Sixers', 
                      home_points=100, away_points=105)

# test attributes
assert game.home_team == 'Warriors'
assert game.away_team == 'Sixers'
assert game.home_points == 100
assert game.away_points == 105
### END HIDDEN TESTS


# In[77]:


assert callable(BasketballGame.play_game)

### BEGIN HIDDEN TESTS
# test method
assert game.play_game() == 'Winner: Sixers'
### END HIDDEN TESTS


# This "blank" cell included intentionally. Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# rubric for partial credit
# 
# === END MARK SCHEME ===

# ### Q17 - `ClassRoster`
# 
# Define a class `ClassRoster()` that meets the following specifications:
# 
# - has two instance attributes:
#     - `students`; initialized as an empty list
#     - `course`; which the user specifies when creating a `ClassRoster()` object
# - a single method `add_student()`, which will have `pid` and `name` as arguments, and will add these two inputs as a dictionary with `pid` as the key and the student's `name` as the value to the `students` list each time the method is called

# In[78]:


### BEGIN SOLUTION
class ClassRoster():
        
    def __init__(self, course):
        self.students = []
        self.course = course
        
    def add_student(self, pid, name):
        self.students.append({pid: name})
### END SOLUTION


# In[79]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[80]:


assert callable(ClassRoster)
my_course = ClassRoster('COGS 18')
### BEGIN HIDDEN TESTS
assert my_course.course == 'COGS 18'
### END HIDDEN TESTS


# In[81]:


# tests for instance attribute
assert my_course.students is not None
### BEGIN HIDDEN TESTS
assert my_course.students == []
### END HIDDEN TESTS


# In[82]:


# tests for method
assert callable(my_course.add_student)
### BEGIN HIDDEN TESTS
my_course.add_student(pid='A12345', name='Shannon')
my_course.add_student(pid='A56789', name='Josh')

assert my_course.students == [{'A12345':'Shannon'}, {'A56789': 'Josh'}]
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `class` defined correctly (**0.1 pts**)
# - instance attributes
#     - `def __init__(self)` correct (**0.2 pts**)
#     - `self` used within definition (**0.2 pts**)
#     - `students` attribute initialized correctly (empty list) (**0.2 pts**)
#     - `course` intialized correctly  (**0.2 pts**)
# - `add_student` method:
#     - method definition correct with `self`, `pid`, and `name` (**0.2 pts**)
#     - dictionary syntax correct  (**0.2 pts**)
#     - added to list correct (`append`) (**0.2 pts**)
# 
# Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly
# 
# === END MARK SCHEME ===

# ### Q18 - `ToDo` 
# 
# Define a class `ToDo()` to keep track of your to do list.
# 
# This should have a single instance attribute: `to_do`, which is initialized as an empty list.
# 
# It will then have two methods: `add_item` and `remove_item`.
# 
# `add_item()`:
# - will have two parameters `item`, and `top` (`top` takes the default value `True`)
# - if `top` is `True`:
#     the string in `item` will be added to the top of `to_do`:
# - if `top` is not true:
#     the string it `item` will be added to the end of `to_do`
# 
# `remove_item()`:
# - will have a single parameter `item`
# - will remove the item specified from `to_do`
# 
# Note: there is a list method `insert()`, which operates in place to add a value to a list at the index specified with the general syntax `my_list.insert(index, item_to_add)`.

# In[83]:


### BEGIN SOLUTION
class ToDo():
    
    def __init__(self):
        self.to_do = []
        
    def add_item(self, item, top=True):
        if top:
            self.to_do.insert(0, item)
        else: 
            self.to_do.append(item)
        
    def remove_item(self, item):
        self.to_do.remove(item)

### END SOLUTION


# In[84]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[85]:


assert callable(ToDo)
my_todo_list = ToDo()
### BEGIN HIDDEN TESTS
assert my_todo_list.to_do == []
### END HIDDEN TESTS


# In[86]:


# check add_item method
### BEGIN HIDDEN TESTS
my_todo_list.add_item('A')
my_todo_list.add_item('B')
assert my_todo_list.to_do == ['B','A']
### END HIDDEN TESTS


# In[87]:


# check add_item with non-default value
### BEGIN HIDDEN TESTS
my_todo_list.add_item('C', top=False)
assert my_todo_list.to_do == ['B','A', 'C']
### END HIDDEN TESTS


# In[88]:


# check remove_item
### BEGIN HIDDEN TESTS
my_todo_list.remove_item('A')
assert my_todo_list.to_do == ['B', 'C']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Check if points lost on autograder above: 
# - `class` defined correctly (**0.1 pts**)
# - instance attribute
#     - `def __init__(self)` correct (**0.2 pts**)
#     - `to_do` attribute initialized correctly (empty list) (**0.2 pts**)
# 
# - `add_item` method:
#     - method definition correct with `self`, `item`, and `top` (**0.15 pts**)
#     - `top` default value set to `True`
#     - conditional correct  (**0.15 pts**)
#     - extends list correctly (**0.15 pts**)
# 
# - `remove_item` method:
#     - method definition correct with `self` and `item` (**0.15 pts**)
#     - item removed correctly  (**0.15 pts**)
# 
# Note: autograder credit can be returned for portions above if particular aspect (class attribute, instance attribute, or method) were correct, but test failed because overall `class` was defined incorrectly
# 
# === END MARK SCHEME ===

# ### (Practice) Exam II complete!
# 
# Good work - you're done with the second (practice) exam!
# 
# A reminder that for the real thing you will need to submit on datahub. We will not have your exam until you click submit and see this show up under 'submitted assignments'.
