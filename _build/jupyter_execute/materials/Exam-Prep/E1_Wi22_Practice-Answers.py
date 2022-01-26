#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Practice Exam 1
# 
# This is the Practice Exam 1 for Winter 2022. It covers topics through the Collections Lecture.
# 
# This exam is out 0 points and worth 0% of your grade, but the real thing will be out of 12.5 points, worth 12.5% of your grade.
# 
# **PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**
# 
# **PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

# ## Instructions
# 
# (Note: These are the instructions you'll see on the real exam)
# 
# #### Timing
# - The exam is designed to take you ~1h.
# - There will be a >24 hour window during which you can complete this exam.
# - If it takes you longer than 1h, you're free to use that time.
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


# ## Part 1: Variables & Operators

# ### Q1 - Variables
# 
# In the cell below, create three variables: `var_str`, `var_num`, and `var_col`. 
# 
# - `var_str` should store a string of length 7
# - `var_num` should be a single value that, if multiplied by itself, returns 36.
# - `var_col` should be a a mutable variable type storing three different elements.
# 
# The specific values you use to generate the variables are up to you, as long as they fulfill the criteria specified.

# In[3]:


### BEGIN SOLUTION
# actual values stored will differ
var_str = 'Shannon'
var_num = 6
var_col = [1, 2, 3]
### END SOLUTION


# In[4]:


# check variable exists
assert var_str is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_str, str)
assert len(var_str) == 7
### END HIDDEN TESTS


# In[5]:


assert var_num is not None
### BEGIN HIDDEN TESTS
assert var_num ** 2 == 36
### END HIDDEN TESTS


# In[6]:


assert var_col is not None
### BEGIN HIDDEN TESTS
assert isinstance(var_col, list)
assert len(var_col) == 3
### END HIDDEN TESTS


# ### Q2 - Math Operators
# 
# Use the variables provided in the cell below (`var_low`, `var_mid` and `var_high`) to generate the variables: `var_150` and `var_14` according to the following specifications:
# 
# - `var_150` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 150 
# - `var_14` | use the 3 variables provided once each and *at least two* of the math operators (`+`, `-`, `*`, `/`, `**`, `//`, `%`) to store the value 14

# In[7]:


# these variables provided for you
# this cell is read-only (cannot be changed)
var_low = 5
var_mid = 10
var_high = 20


# In[8]:


### BEGIN SOLUTION
# actual operations will differ
var_150 = (var_high - var_low) * var_mid
var_14 = (var_high // var_low) + var_mid

print(var_150, var_14)
### END SOLUTION


# In[9]:


assert var_150 is not None
### BEGIN HIDDEN TESTS
assert var_150 == 150
### END HIDDEN TESTS


# In[10]:


assert var_14 is not None
### BEGIN HIDDEN TESTS
assert var_14 == 14
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - correct operators used (0.15)
# - variables referenced; did not hard-code numbers (0.15)  
# 
# Note: It's ok if they also referenced additional values other than the variables provided.
# 
# === END MARK SCHEME ===
# 

# ### Q3 - Comparison Operators 
# Store your favorite number in the variable `fav_num`. 
# 
# Then, store another number between 1 and 1000 in the variable `comparison_num`
# 
# Finally, referencing both `fav_num` and `comparison_num` *and* using at least one comparison operator, define two variables: `true_comp` and `false_comp`
# 
# These variables must satisfy the following requirements:
# 
# 1. Each variable must be defined using one comparison operator (`<`,`>`,`<=`,`>=`,`!=`,`==`).
# 2. Each variable must use and refer to `fav_num` and `comparison_num` (and no other values or variables)
# 4. `true_comp` should evaluate as the boolean `True`; `false_comp` should evaluate as the boolean `False`

# In[11]:


### BEGIN SOLUTION
fav_num = 3 # specific values will differ
comparison_num = 29

true_comp = fav_num < comparison_num
false_comp = fav_num == comparison_num
### END SOLUTION


# In[12]:


assert true_comp is not None
### BEGIN HIDDEN TESTS
assert true_comp
### END HIDDEN TESTS


# In[13]:


assert false_comp is not None
### BEGIN HIDDEN TESTS
assert not false_comp
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - both variables reference `fav_num` and `comparison_num` (**0.25 pts**)
# - both variables reference use at least one comparison operator (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q4 - Membership Operators
# 
# Define an *immutable* variable of length 7 called `my_var`, such that when you check whether 'COGS' is a member of `my_var` it returns `True`, but if you check whether 'holiday' is a member of `my_var` it returns `False`

# In[14]:


### BEGIN SOLUTION
# students could define *either* a string OR a tuple here
my_var = 'COGS18!'
# or
my_var = ('COGS', 'b', 'c', 'd', 'e', 'f', 'g')
### END SOLUTION


# In[15]:


assert my_var is not None
### BEGIN HIDDEN TESTS
assert type(my_var) in [tuple, str]
### END HIDDEN TESTS


# In[16]:


# hidden tests to check length
### BEGIN HIDDEN TESTS
assert len(my_var) == 7
### END HIDDEN TESTS


# In[17]:


# hidden tests to check conditions specified in instructions
### BEGIN HIDDEN TESTS
assert 'COGS' in my_var
### END HIDDEN TESTS


# In[18]:


# hidden tests to check conditions specified in instructions
### BEGIN HIDDEN TESTS
assert 'holiday' not in my_var
### END HIDDEN TESTS


# ### Q5 - String Concatenation
# 
# In this question, you'll specify how you've been feeling since returning to in-person learning. 
# 
# Define the variable `my_feeling` such that it stores the string `Returning to in-person learning has been ---.` , where the `---` is replaced by one of the values in `feelings` (provided below).
# 
# Notes: 
# - Your answer should reference (meaning: use) the variable `feelings`. You should NOT simply type one of the words from the list in your answer.
# - Spacing, captialization, and punctuation all matter. Be sure your resulting string matches what's specified in the instructions (including the period at the end of the sentence; note there is NO extra space in the string. It ends with a period.). 

# In[19]:


# these variables provided for you
# this cell is read-only (cannot be changed)
feelings = ['exciting', 'nerve-wracking', 'boring', 'fun']


# In[20]:


### BEGIN SOLUTION
my_feeling = "Returning to in-person learning has been " + feelings[0] + '.'
print(my_feeling)
### END SOLUTION


# In[21]:


assert my_feeling is not None
### BEGIN HIDDEN TESTS
assert isinstance(my_feeling, str)
### END HIDDEN TESTS


# In[22]:


# hidden test checking for correct string
### BEGIN HIDDEN TESTS
assert my_feeling in ['Returning to in-person learning has been exciting.',
                      'Returning to in-person learning has been nerve-wracking.',
                      'Returning to in-person learning has been boring.',
                      'Returning to in-person learning has been fun.']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - if hard-coded (doesn't reference variable/use indexing, remove autograder credit from cell above (-0.4)
# 
# === END MARK SCHEME ===

# ## Part 2: Collections & Indexing

# ### Q6 - Lists & Indexing
# 
# The list `burritos` has been provided in the cell below for you.
# 
# ***Use the `burritos` variable and indexing*** to generate each of the four variables at left below, so that each stores the output at right below. For example, `burritos_a` should refer to `burritos` in its answer and use indexing to store the string 'Cali'.
# 
# - `burritos_a` | `'Cali'`
# - `burritos_b` | `['Adobada', 'Bean and Cheese', 'Steak Ranchero', 'Carnitas']`
# - `burritos_c` | `['Cali', 'Steak Ranchero']`
# - `burritos_d` | `['Chicken', 'Chile Verde', 'Adobada', 'Steak Ranchero']`

# In[23]:


# this variables provided for you
# this cell is read-only (cannot be changed)
burritos = ['Chicken', 'Carne Asada', 'Chile Verde', 'Cali', 
            'Adobada', 'Bean and Cheese', 'Steak Ranchero',
            'Carnitas']


# In[24]:


### BEGIN SOLUTION
# actual values will differ
burritos_a = burritos[3]
burritos_b = burritos[-4:]
burritos_c = burritos[3::3]
burritos_d = burritos[::2]
### END SOLUTION


# In[25]:


assert burritos_a
### BEGIN HIDDEN TESTS
assert burritos_a == 'Cali'
### END HIDDEN TESTS


# In[26]:


assert burritos_b
### BEGIN HIDDEN TESTS
assert burritos_b == ['Adobada', 'Bean and Cheese', 'Steak Ranchero', 'Carnitas']
### END HIDDEN TESTS


# In[27]:


assert burritos_c
### BEGIN HIDDEN TESTS
assert burritos_c == ['Cali', 'Steak Ranchero']
### END HIDDEN TESTS


# In[28]:


assert burritos_d
### BEGIN HIDDEN TESTS
assert burritos_d == ['Chicken', 'Chile Verde', 'Adobada', 'Steak Ranchero']
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - if hard-coded (doesn't use indexing & reference `burritos`), remove autograder credit
# 
# === END MARK SCHEME ===
# 

# ### Q7 - Tuples
# 
# In the cell below, describe a situation where you would store information in a tuple (give an example). Be clear about the information or values you would store in a tuple and why that variable type would be appropriate for your situation. 
# 
# Note: you do not *have* to write any python code here; we're looking for a written explanation.

# 

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - example provided includes multiple pieces of information being stored (**0.25 pts**)
# - information being stored would reasonably NOT want to be changed (**0.50 pts**)
# - student explanation links immutability to their example (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q8 - Collections: Indexing & Mutating
# 
# Professor Ellis is trying to learn more about the colleges at UCSD (even though she's been here since 2019), so she's pulled together a list of the colleges. Unfortunately, she's got some bad information. Using code constructs discussed in class, replace any element in `ucsd_colleges` that is NOT a college at UCSD with an empty string. Your updated list should be stored in the same variable: `ucsd_colleges`.
# 
# Note: Prof Ellis is NOT trying to trip you up on spelling or anything here, so you don't have to check each college's spelling or anything like that.

# In[29]:


# this variable provided for you
# this cell is read-only (cannot be changed)
ucsd_colleges = ['Revelle',
                 'John Muir',
                 'Thurgood Marshall',
                 'Sarah Marshall',
                 'Earl Warren',
                 'Eleanor Roosevelt',
                 'Sixth',
                 'Torrey Pines',
                 'Seventh']


# In[30]:


### BEGIN SOLUTION
ucsd_colleges[3] = ''
ucsd_colleges[7] = ''
### END SOLUTION


# In[31]:


assert ucsd_colleges is not None
### BEGIN HIDDEN TESTS
assert ucsd_colleges[3] == ''
### END HIDDEN TESTS


# In[32]:


# hidden test
### BEGIN HIDDEN TESTS
assert ucsd_colleges[7] == ''
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - if hard-coded (doesn't use indexing/conditionals & does not reference `ucsd_colleges`), remove autograder credit
# 
# === END MARK SCHEME ===
# 

# ## Part 3: Conditionals, Functions, & Debugging

# ### Q9 - Conditionals
# 
# You're working on software that's supposed to determine whether a speeding ticket should be written. 
# 
# For this you have to consider both *where* the person is driving *and* how fast they're going. If the person should receive a ticket, the variable `ticket` should store the boolean `True`; otherwise, `ticket` should store `False`.
# 
# More specifically, you have to write a conditional that references the three variables provided below and considers the following logic:
# 
# It should specify that a ticket should be written under the following three conditions:
# 1. If the person's `zone` is 'private' and their `speed` is greater than the `private_mph` (defined below)
# 2. If the person's `zone` is 'local' and their `speed` is greater than the `local_mph` (defined below)
# 3. If the person's `zone` is 'highway' and their `speed` is greater than the `hwy_mph` (defined below)
# 
# Otherwise, the person should not be written a ticket.
# 
# Note: `zone` and `speed` have been defined below for you. You can (and should) try out other values for those variables to make sure your logic is working as expected; however, when you're done be sure `zone` has the value 'private' and `speed` the value `20`.

# In[33]:


# these variables provided for you
# this cell is read-only (cannot be changed)
private_mph = 5
local_mph = 25
hwy_mph = 65


# In[34]:


zone = 'private'
speed = 20

### BEGIN SOLUTION
if zone == 'private' and speed > private_mph:
    ticket = True
elif zone == 'local' and speed > local_mph:
    ticket = True
elif zone == 'highway' and speed > hwy_mph:
    ticket = True
else:
    ticket = False
### END SOLUTION


# In[35]:


assert ticket is not None
### BEGIN HIDDEN TESTS
assert ticket
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# - uses `if`/`elif`/`elif`/`else` syntax correctly; half credit if `if`/`if`/`if`/`else` used (**0.4 points**)
# - conditionals correct 
#     - references variables (`private_mph`, `local_mph`, `hwy_mph`) and doesn't hard-code (**0.2 points**)
#     - references `zone` (**0.1 points**)
#     - uses `>` and `and`/`&` correctly  (**0.2 points**)
# - `ticket` assigned a boolean value (even if logic is incorrect) (**0.1 points**)
# 
# === END MARK SCHEME ===

# ### Q10 - Code Style
# 
# **Part I**
# 
# The following function executes without issue...but the code style isn't great. Consider what we've discussed about code style for variables, operators, conditionals, functions, and edit the code style in the cell below.
# 
# Do not change the name of the function or what the function does/accomplishes. Your changes/edits should only change the code style.
# 
# The original function provided:
# 
# ```python
# def new_password(pwd,name):
#     if len(pwd)<8 or name in pwd:need_new=True
#     else:need_new=False
#     return need_new
# ```

# In[6]:


def new_password(pwd,name):
    if len(pwd)<8 or name in pwd:need_new=True
    else:need_new=False
    return need_new
### BEGIN SOLUTION
def new_password(pwd, name):
    
    if len(pwd) < 8 or name in pwd:
        need_new = True
    else:
        need_new = False
        
    return need_new
### END SOLUTION


# In[37]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# **Part II**
# 
# In your own words, describe what the function above accomplishes overall and how the code in the function specifically accomplishes this. This will likely incclude specific explanations of lines of code provided.

# Replace this with your response to Part II

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# Part I
# - spacing between parameters 
# - considers spacing around operators
# - conditionals on separate lines
# - considers line spacing
# 
# Part II
# - explanation describes what function accomplishes
# - addresses parameters
# - explains conditionals
# - describes output will be returned
# 
# === END MARK SCHEME ===

# ### Q11 - `wear_mask()` 
# 
# While the rules have and will continue to change, we want a function that will help us determine if a mask should be worn.
# 
# This function `wear_mask` will have three parameters:
# - `group_size`, which will have no default value
# - `location`, which should take the default value 'indoors' (a string)
# - `vaccinated`, which should take the default value `True` (a boolean)
# 
# This function will `return` the string specified below using the following logic:
# - if `vaccinated` is `False` (regardless of other parameter values),: `return`s 'Masking required.'
# - if `vaccinated` is True:
#     - ...and if `location` is 'outdoors', and `group_size` is any value: `return`s 'Masking encouraged.'
#     - ...and if `location` is 'indoors' and `group_size` is > 1: `return`s 'Masking required.'
#     - ...and any other condition: `return`s 'Mask requirement uncertain.'
# 
# Note that the string returned must match exactly to string provided above. Likely best to copy + paste to avoid typos.
# 
# For example:
# - `wear_mask(group_size=10, location = 'indoors')` would `return` `'Masking required.'`
# - `wear_mask(group_size=10, location='outdoors')` would `return` `Masking encouraged.'`
# - `wear_mask(group_size=10, location='outdoors', vaccinated=False)` would `return` `'Masking required.'`
# - `wear_mask(group_size=1, location='indoors')` would `return` 'Mask requirement uncertain.'

# In[39]:


### BEGIN SOLUTION
def wear_mask(group_size, location='indoors', vaccinated=True):
    if not vaccinated:
        output = 'Masking required.'
    else:
        if location == 'outdoors':
            output = 'Masking encouraged.'

        elif location == 'indoors' and group_size > 1:
            output = 'Masking required.'
        else:
            output = 'Mask requirement uncertain.'
    
    return output
### END SOLUTION


# In[40]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your thinking (optional)


# In[41]:


assert wear_mask
### BEGIN HIDDEN TESTS
assert wear_mask(group_size=10, location='outdoors', vaccinated=False) == 'Masking required.'
### END HIDDEN TESTS


# In[42]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check indoors
assert wear_mask(group_size=10, location='indoors') == 'Masking required.'
### END HIDDEN TESTS


# In[43]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check default values
assert wear_mask(1) == 'Mask requirement uncertain.'
### END HIDDEN TESTS


# In[44]:


# hidden test to check functionality
### BEGIN HIDDEN TESTS
# check outdoors, but state vaccinated explicitly
assert wear_mask(group_size=1, location='outdoors', vaccinated=True) == 'Masking encouraged.'
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# Check if points lost on autograder above: 
# - `def` correct with 3 parameters password (**0.1 pts**)
# - `location` and `vaccinated` take default values correctly (**0.1 pts**)
# - condition for `not vaccinated` correct (**0.2 pts**)
# - condition for `location` correct (**0.2 pts**)
# - `else` condition for 'Mask requirement uncertain.' included (**0.2 pts**)
# - includes `return` statement (**0.1 pts**)
# 
# Note: if only issue is `return` statement is missing, return autograder credit lost and only deduct for `return` statement missing
# === END MARK SCHEME ===

# ### Q12 - `provide_info()` 
# 
# Write a function `provide_info` that takes three parameters: `name`, `year`, and `school` .
# 
# Set the default value for `school` to be 'UCSD'.
# 
# This function should `return` the string "Hi. I'm `name`. I am a `year` at `school`." (where the variable names are replaced by the values input to the function upon execution).
# 
# For example, one possible execution of this function could return "Hi! I'm Shannon. I am a sophomore at UCSD."
# 
# Note: Be sure punctuation and spacing match that specified in the instructions.

# In[45]:


### BEGIN SOLUTION
def provide_info(name, year, school='UCSD'):
    output = "Hi. I'm " + name + '. I am a ' + year + ' at ' + school + '.'
    return output
### END SOLUTION


# In[46]:


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)


# In[47]:


assert callable(provide_info)

### BEGIN HIDDEN TESTS
assert provide_info(name = 'Taylor', year = 'junior', school = 'UCLA') == "Hi! I'm Taylor. I am a junior at UCLA." or provide_info(name='Taylor', year='junior', school = 'UCLA') == "Hi. I'm Taylor. I am a junior at UCLA."
### END HIDDEN TESTS


# In[48]:


# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure defaul parameter is correct
assert provide_info(name = 'Taylor', year = 'junior') == "Hi! I'm Taylor. I am a junior at UCSD." or provide_info(name='Taylor', year='junior') == "Hi. I'm Taylor. I am a junior at UCSD."
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# 
# === BEGIN MARK SCHEME ===
# 
# partial credit for answer above:
# 
# - function defined correctly (**0.5 points**)
# - 3 parameters specified (**0.5 points**)
# - default parameter specified correctly (**0.5 points**)
# - string concatenation attempted correctly (even if typos in string) (**1 point**)
# - `return` statement included (**0.3 points**)
# 
# === END MARK SCHEME ===

# ### Submit on Datahub
# 
# Good work - you're done!
# 
# Check your work, and then when you're ready, **submit on datahub**.
# 
# We will not have your exam until you click submit and see this show up under 'submitted assignments'.
