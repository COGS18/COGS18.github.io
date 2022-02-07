#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Exam 1
# 
# This is the first exam for Winter 2022. It covers topics through the Collections Lecture.
# 
# This exam is out of 12.5 points, worth 12.5% of your grade.
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

# ## Instructions
# 
# #### Timing
# - The exam is designed to take you ~1h.
# - There will be a >24 hour window during which you can complete this exam.
# - If it takes you longer than 1h, you're free to use that time.
# 
# #### The Rules
# - You are to complete this exam on your own.
# - This is open-notes & open-Google.
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
#     - Note: This policy is b/c we are incapable of responding for the entirety of the exam. This is the only way to make it fair across the board for students.

#  <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

# ### Q0 - Honor Code (0.15 points)
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


# ## Part 1: Variables & Operators (3.15 points)

# ### Q1 - Variables (0.75 points)
# 
# In the cell below, define three variables: `var_a`, `var_b`, and `var_c`. 
# 
# - `var_a` should be the variable type most appropriate to store a whole number
# - `var_b` should be a mutable collection type of length 3 useful for storing key-value pairs
# - `var_c` should be the immutable variable type most appropriate for storing information as characters
# 
# The specific values you use to generate the variables are up to you, as long as they fulfill the criteria specified.

# In[3]:


### BEGIN SOLUTION
# actual values stored will differ
var_a = 29
var_b = {'a' : 1, 'b' : 2, 'c' : 3}
var_c = 'Shannon'
### END SOLUTION


# In[4]:


# check variable exists
assert var_a is not None
### BEGIN HIDDEN TESTS
assert type(var_a) == int
### END HIDDEN TESTS


# In[5]:


assert var_b is not None
### BEGIN HIDDEN TESTS
assert type(var_b) == dict
assert len(var_b) == 3
### END HIDDEN TESTS


# In[6]:


assert var_c is not None
### BEGIN HIDDEN TESTS
assert type(var_c) == str
### END HIDDEN TESTS


# ### Q2 - Math Operators (1 point)
# 
# Define three integer values in `math_a`, `math_b`, and `math_c`.
# 
# Then, utilize the above variables to define two additional variables:
# - `neg_odd_val` | should store a negative, odd integer 
# - `pos_even_val` | should store a positive, even integer
# 
# Notes:
# - `neg_odd_val` and `pos_even_val` should *each* reference all three variables (`math_a`, `math_b` and `math_c`)
# - `neg_odd_val` and `pos_even_val` should *each* use *at least* two different math operators (such that *at least* four different math operators are used in total)
# - No other values other than `math_a`, `math_b`, and `math_c` should be used to generate `neg_odd_val` or `pos_even_val`

# In[7]:


### BEGIN SOLUTION
# specific values will differ
math_a = 2
math_b = 5
math_c = 10

# actual operations will differ
neg_odd_val = (math_b - math_c) + math_a
pos_even_val = math_a ** math_b * math_c

print(neg_odd_val, pos_even_val)
### END SOLUTION


# In[8]:


assert math_a is not None
assert math_b is not None
assert math_c is not None

### BEGIN HIDDEN TESTS
assert type(math_a) == int
assert type(math_b) == int
assert type(math_c) == int
### END HIDDEN TESTS


# In[9]:


assert neg_odd_val is not None
### BEGIN HIDDEN TESTS
def is_even(val):
    if val % 2 == 0:
        return True
    else:
        return False
    
assert neg_odd_val < 0
assert not is_even(neg_odd_val)
### END HIDDEN TESTS


# In[10]:


assert pos_even_val is not None
### BEGIN HIDDEN TESTS
assert pos_even_val > 0 
assert is_even(pos_even_val)
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - four different math operators used (**0.1 points**)
# - `neg_odd_val` and `pos_even_val` reference math_* variables; did not hard-code numbers (**0.1 points**)  
# - no other values used in definition (**0.1 points**)
# 
# === END MARK SCHEME ===
# 

# ### Q3 - Comparison Operators (1 point)
# 
# Professor Ellis started teaching at UCSD in Winter 2019. This means she has taught at UCSD for the following quarters: Wi19, Sp19, Fa19, Wi20, Sp20, Fa20, Wi21, Sp21, and Fa21. Of these, Sp20, Fa20, Wi21, and Sp21 were remote quarters. 
# 
# - Store the total number of quarters Prof Ellis has taught at UCSD in the variable `quarters_taught`.
# - Store the  number of remote quarters she has taught in the variable `remote_quarters`.
# 
# Then generate two variables (`true_var` and `false_var`) that satisfy the following requirements:
# 
# 1. Each variable must be defined using one comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
# 2. Each variable must use and refer to `quarters_taught` and `remote_quarters` (and no other values or variables)
# 4. `true_var` should evaluate as the boolean `True`; `false_var` should evaluate as the boolean `False`

# In[11]:


### BEGIN SOLUTION
quarters_taught = 9 
remote_quarters = 4

true_var = quarters_taught > remote_quarters
false_var = quarters_taught == remote_quarters
### END SOLUTION


# In[12]:


assert quarters_taught is not None
### BEGIN HIDDEN TESTS
assert quarters_taught == 9
### END HIDDEN TESTS


# In[13]:


assert remote_quarters is not None
### BEGIN HIDDEN TESTS
assert remote_quarters == 4
### END HIDDEN TESTS


# In[14]:


assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS


# In[15]:


assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - both variables reference `quarters_taught` and `remote_quarters` (**0.2 pts**)
# - both variables reference use at least one comparison operator (**0.2 pts**)
# - no other variables are referenced (**0.2 pts**)
# 
# === END MARK SCHEME ===

# ### Q4 - Membership Operators (0.4 points)
# 
# Define a **list of length 4** called `my_list`, such that when you check whether 'COGS18' is a member of `my_list` it returns `True`, but if you check whether 'COGS' is a member of `my_list` it returns `False`.

# In[16]:


### BEGIN SOLUTION
# specific list will vary, but at least one element has to be 'COGS18'
my_list = ['COGS18', 'is', 'the', 'best!']
### END SOLUTION


# In[17]:


assert my_list is not None
### BEGIN HIDDEN TESTS
assert type(my_list) == list
### END HIDDEN TESTS


# In[18]:


# hidden tests to check length
### BEGIN HIDDEN TESTS
assert len(my_list) == 4
### END HIDDEN TESTS


# In[19]:


# hidden tests to check conditions specified in instructions
### BEGIN HIDDEN TESTS
assert 'COGS18' in my_list
### END HIDDEN TESTS


# In[20]:


# hidden tests to check conditions specified in instructions
### BEGIN HIDDEN TESTS
assert 'COGS' not in my_list
### END HIDDEN TESTS


# ## Part 2: Collections & Indexing  (2.75 points)

# ### Q5 - Indexing (1 point)
# 
# The list `us_govt` has been provided in the cell below for you.
# 
# ***Use the `us_govt` list and indexing*** to generate each of the four variables at left below, so that each stores the output at right below. For example, `congress_minority` should refer to `us_govt` in its answer and use indexing to store the list `['Kevin McCarthy', 'Mitch McConnell']`.
# 
# - `congress_minority` | `['Kevin McCarthy', 'Mitch McConnell']`
# - `congress_majority` | `['Nancy Pelosi', 'Chuck Schumer']`
# - `executive` | `['Joe Biden', 'Kamala Harris']`
# - `president` | `'Joe Biden'` (note this is a string, not a list)

# In[21]:


# this variables provided for you
# this cell is read-only (cannot be changed)
us_govt = ['Joe Biden', 'Kamala Harris', 
           'Nancy Pelosi', 'Kevin McCarthy',
           'Chuck Schumer', 'Mitch McConnell']


# In[22]:


### BEGIN SOLUTION
# actual values will differ
congress_minority = us_govt[3::2]
congress_majority = us_govt[2::2]
executive = us_govt[0:2]
president = us_govt[0]
### END SOLUTION


# In[23]:


assert congress_minority is not None
### BEGIN HIDDEN TESTS
assert congress_minority == ['Kevin McCarthy', 'Mitch McConnell']
### END HIDDEN TESTS


# In[24]:


assert congress_majority is not None
### BEGIN HIDDEN TESTS
assert congress_majority == ['Nancy Pelosi', 'Chuck Schumer']
### END HIDDEN TESTS


# In[25]:


assert executive is not None
### BEGIN HIDDEN TESTS
assert executive == ['Joe Biden', 'Kamala Harris']
### END HIDDEN TESTS


# In[26]:


assert president is not None
### BEGIN HIDDEN TESTS
assert president == 'Joe Biden'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - if hard-coded (doesn't use indexing & reference `us_govt`), remove autograder credit
# 
# === END MARK SCHEME ===
# 

# ### Q6 - Dictionaries (1 point)
# 
# In the cell below, describe a situation where you would store information in a dictionary (give an example). Be clear about the information or values you would store in a dictionary, why that variable type would be appropriate for your situation, and whether or not this information could be changed after the dictionary is created. 
# 
# Note: you do not *have* to write any python code here; we're looking for a written explanation.
# 
# <span style="color:red">Be sure to include your text response in the cell below!</span>
# 

# 

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - example provided is something reasonably stored in a dictionary (**0.25 pts**)
# - information being stored makes sense/describes at least one key-value pair (**0.50 pts**)
# - student explanation addresses that dictionaries are mutable/can be updated (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q7 - Collections & Mutating  (0.75 points)
# 
# **Part I**
# 
# Define a dictionary `my_dict` which stores a dictionary related to the one you described in Q6. 
# 
# Be sure that this dictionary has a length of at least 3.
# 
# (Note, if the dictionary you described would have be really big, feel free to just store a couple of elements.)

# In[27]:


### BEGIN SOLUTION
# specific values will differ
my_dict = {'Make' : 'Hyundai',
           'Model' : 'Insight',
           'Year' : 2019,
           'Color' : 'black'}
### END SOLUTION


# In[28]:


assert my_dict is not None
### BEGIN HIDDEN TESTS
assert type(my_dict) == dict
### END HIDDEN TESTS


# In[29]:


# hidden test to check specifics of dictionary match instructions
### BEGIN HIDDEN TESTS
assert len(my_dict) >= 3

import copy
dict_copy = copy.deepcopy(my_dict)
### END HIDDEN TESTS


# **Part II**
# 
# Having already defined `my_dict`, write code that would *mutate* the value stored in the first position of your dictionary.
# 
# Note: the first position is the first element/thing stored in your dictionary.

# In[30]:


### BEGIN SOLUTION
# specific values will differ
my_dict['Make'] = 'Honda'
### END SOLUTION


# In[31]:


# hidden test
### BEGIN HIDDEN TESTS
assert list(my_dict.values())[0] != list(dict_copy.values())[0] 
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - if hard-coded (i.e. redefines dictionary rather than udpating/mutating), remove autograder credit
# 
# === END MARK SCHEME ===
# 

# ## Part 3: Control Flow - Conditionals, Functions, and Code Style  (6.45 points)

# ### Q8 - Function Execution & Code Style (2 points)
# 
# The following function executes without programmatic issue...but there are two things we need from you! We need you to  1) fix the funtion's poor code style (Part I) and 2) explain what the function is doing (Part II).
# 
# **Part I**
# 
# In Part I, consider what we've discussed about code style for variables, operators, conditionals, and functions, then edit the code style for the provided function in the cell below.
# 
# Do not change the name of the function or what the function does/accomplishes. Your changes/edits should only change the code style.
# 
# The original function provided:
# 
# ```python
# def introduce(name,year,school,major):output='Hi! my name is '+name+'. I am a '+year+' at '+school+' studying '+major+'.';return output
# ```
# 
# Include your function with good code style in the cell below.

# In[32]:


### BEGIN SOLUTION
def introduce(name, year, school, major):
    
    output = 'Hi! my name is ' + name + '. I am a ' + year + ' at ' + school + ' studying ' + major + '.'
    
    return output
### END SOLUTION


# In[33]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - added spacing between function arguments (**0.25 points**)
# - considers spacing around operators in string concatenation/assignment (**0.5 points**)
# - not all in a single line (**0.25 points**)
# 
# === END MARK SCHEME ===

# **Part II**
# 
# In your own words, describe what the function above accomplishes overall and how the code in the function specifically accomplishes this. This will likely incclude specific explanations of lines of code provided.
# 
# <span style="color:red">Be sure to include your text response in the cell below!</span>

# 

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - explanation describes what function accomplishes (**0.25 points**)
# - describes parameters are input (**0.25 points**)
# - explains string concatenation (**0.25 points**)
# - describes single string output will be returned (**0.25 points**)
# 
# === END MARK SCHEME ===

# ### Q9 - Functions + Conditionals (2 points)
# 
# As a semi-new prof, Prof Ellis is still trying to figure out the differences between the colleges. One thing she's noticed is that students discuss are the different math and writing requirements between the different colleges.
# 
# To help her out, you're going to write a function `determine_college()` that will take two input parameters: `math` and `writing`. 
# 
# Within this function, using the number of math and writing courses as inputs, you will `return` the college (listed at left), using the logic specified at right below:
# 
# - 'Muir' | 3 math courses; 2 writing courses
# - 'Thurgood Marshall' | 2 math courses; 0 writing courses
# - 'Earl Warren' | 0 math courses; 2 writing courses
# - 'Eleanor Roosevelt' | 0 math courses; 0 writing courses
# - 'Sixth' | 1 math course; 0 writing courses
# - 'Seventh' | 1 math course; 2 writing courses
# - 'cannot be determined' | output for any other combination of values
# 
# For example, if you were to execute your function: `determine_college(math=3, writing=2)`, the function would `return` 'Muir'.
# 
# Notes: 
# - Be sure the output strings do not have any typos and have the *same* capitalization as written above (may be best to just copy and paste strings from above to avoid any issues!)
# - If you disagree with these requirements in what's *actually* required, you may be correct. Prof Ellis only quickly looked at the GE requirements. For this question, use the values above...even if they're not quite "true" in reality.
# 

# In[34]:


### BEGIN SOLUTION
def determine_college(math, writing):
    
    if math == 3 and writing == 2:
        output = 'Muir'
    elif math == 2 and writing == 0:
        output = 'Thurgood Marshall'
    elif math == 0 and writing == 2:
        output = 'Earl Warren'
    elif math == 0 and writing == 0:
        output = 'Eleanor Roosevelt'
    elif math == 1 and writing == 0:
        output = 'Sixth'
    elif math == 1 and writing == 2:
        output = 'Seventh'
    else:
        output = 'cannot be determined'
    
    return output
### END SOLUTION


# In[35]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[36]:


assert callable(determine_college)
### BEGIN HIDDEN TESTS
assert determine_college(math=3,writing=2) == 'Muir'
assert determine_college(math=2,writing=0) == 'Thurgood Marshall'
assert determine_college(math=0,writing=2) == 'Earl Warren'
assert determine_college(math=0,writing=0) == 'Eleanor Roosevelt'
assert determine_college(math=1,writing=0) == 'Sixth'
assert determine_college(math=1,writing=2) == 'Seventh'
### END HIDDEN TESTS


# In[37]:


# hidden test to check for 'cannot be determined'
### BEGIN HIDDEN TESTS
assert determine_college(math=5,writing=5) == 'cannot be determined'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - function definition correct with two parameters (**0.25 points**)
# - uses `if`/`elif`s/`/`else` syntax correctly; half credit if `if`/`if`s/`else` used (**0.5 points**)
# - conditionals correct 
#     - references `math` `and` `writing` (**0.5 points**)
#     - uses `==` correctly  (**0.25 points**)
# - `return` statement inccluded (**0.15 points**)
# 
# === END MARK SCHEME ===

# ### Q10 - Accomplish a task (2.45 points)
# 
# With the four weeks of the quarter being completely online, the instructional staff has been regularly losing track of time...and they're also not particularly good at military time. To help us out, define a function `time_report()` that takes in two input parameters:
# - `name` : The name of the person executing the function (string)
# - `hour` : The hour in military time (integer)
# 
# The function will `return` a string that says either "Good morning", "Good afternoon", or "Good evening" depending on the `time` specified as input on execution. Specifically, We are using military (24 hour) time as input and converting it to am/pm (12 hour) time within the function. For the purposes of time keeping in this example, we are defining morning from 0:00-11:59, afternoon from 12:00-17:59, and evening from 18:00-23:59.
# 
# The string `return`ed from the function will be some variation of `'Good [morning/afternoon/evening], [name]! It's currently [time] [am/pm].` (where the values in brackets are determined by the inputs to the function and the operations carried out within the function.
# 
# For example: 
# 
# - `time_report('Sam', 8)` would `return` `"Good morning, Sam! It's currently 8 am."`
# - `time_report('Donovan', 14)` would `return` `"Good afternoon, Donovan! It's currently 2 pm."`
# - `time_report('Andrew', 20)` would `return` `"Good evening, Andrew! It's currently 8 pm."` 
# 
# 
# Notes/reminders: 
# - punctuation, spelling, capitalization and spacing matters, so be sure the string you output is exactly as you see above (with the correct inputs/values corresponding to your parameters, of course.)
# - To convert from military time to 12 hour time for any time 1PM (13:00) or later, remember you would need to subtract 12 from military time
# - If you want to convert an integer to a string, remember you can use the `str()` function to typecast the integer to a string. For example, `str(6)` returns the string `"6"`.

# In[38]:


### BEGIN SOLUTION
def time_report(name, hour):
    
    # determine if it's the morning
    if hour < 12:
        time_out = str(hour) + ' am'
        good = 'morning'
    # determine if it's the afternoon
    elif hour >= 12 and hour < 24:
        time_out = str(hour-12) + ' pm'
        
        # handle noon
        if hour == 12:
            time_out = str(hour)  + ' pm'
        
        # handle afternoon vs evening
        if hour >= 12 and hour < 18:
            good = 'afternoon'
        elif hour >= 18 and hour < 24:
            good = 'evening'
    else:
        print("not an actual time")
        return "cannout calculate"
    
    # concatenate string
    output = 'Good ' + good + ", " + name + "! It's currently " + time_out + "."

    return output

# OR 

def time_report(name, hour):
    # handle time
    if hour >= 13:
        time = hour - 12
    else: 
        time = hour
    
    # determine what string to generate 
    if hour >= 0 and hour < 12:
        output = "Good morning, " + name + "! It's currently " + str(time) + " am."
    elif hour >= 12 and hour < 18:
        output = "Good afternoon, " + name + "! It's currently " + str(time) + " pm."
    elif hour >= 18 and hour < 24:
        output = "Good evening, " + name + "! It's currently " + str(time) + " pm."    
    return(output)

# OR 

def time_report(name, hour):
    
    # determine if AM
    if hour >= 0 and hour < 12:
        output = "Good morning, " + name + "! It's currently " + str(hour) + ' am.'
    # determine if noon
    elif hour == 12:
        output = "Good afternoon, " + name + "! It's currently " + str(hour) + ' pm.'
    # determine if afternoon
    elif hour > 12 and hour < 18:
        output = "Good afternoon, " + name + "! It's currently " + str(hour - 12) + ' pm.'
    # determine if evening
    elif hour >= 18 and hour < 24:
        output = "Good evening, " + name + "! It's currently " + str(hour - 12) + ' pm.'
        
    return output
### END SOLUTION


# In[39]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[40]:


assert callable(time_report)
# hidden checks to make sure parameter names are correct
### BEGIN HIDDEN TESTS
# checks parameter names
assert time_report(name="Shannon", hour=12)
### END HIDDEN TESTS


# In[41]:


# hidden checks to make sure "am" or "pm" is correctly in string
### BEGIN HIDDEN TESTS
assert "am" in time_report("Shannon", 8)
assert "pm" in time_report("Shannon", 12)
assert "pm" in time_report("Shannon", 18)
### END HIDDEN TESTS


# In[42]:


# hidden checks to make sure output string is correct (morning)
### BEGIN HIDDEN TESTS
assert time_report("Andrew", 6) == "Good morning, Andrew! It's currently 6 am."
### END HIDDEN TESTS


# In[43]:


# hidden checks to make sure output string is correct (afternoon)
### BEGIN HIDDEN TESTS
assert time_report("Andrina", 12) == "Good afternoon, Andrina! It's currently 12 pm."
### END HIDDEN TESTS


# In[44]:


# hidden checks to make sure output string is correct (evening)
### BEGIN HIDDEN TESTS
assert time_report("Shivani", 20) == "Good evening, Shivani! It's currently 8 pm."
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - `time_report` defined with two parameters `name` and `hours` (**0.15 points**)
# - has conditional on `hours` (even if conditional incorrect) (**0.2 points**)
# - concatenates a string (even if concatenation incorrect) (**0.2 points**) 
# - has a `return` statement (**0.15 points**)  
# 
# === END MARK SCHEME ===

# ### Submit on Datahub
# 
# Good work - you're done!
# 
# Check your work, and then when you're ready, **submit on datahub**.
# 
# We will not have your exam until you click submit and see this show up under 'submitted assignments'.
