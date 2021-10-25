#!/usr/bin/env python
# coding: utf-8

# # COGS 18 - Exam 1
# 
# This is the first exam for Fall 2021. It covers topics through the Loops Lecture.
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
# - There will be a >24 hour window during which you can complete this exam (due Mon 11:59 PM).
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
#     - Note: This policy is b/c we are incapable of responding for 72h straight. This is the only way to make it fair across the board for students.

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


# ## Part 1: Variables & Operators (3.65 points)

# ### Q1 - Variables (0.75 points)
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


# ### Q2 - Math Operators (1 point)
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

# ### Q3 - Comparison Operators (1 point)
# 
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

# ### Q4 - Membership Operators (0.4 points)
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


# ### Q5 - String Concatenation (0.5 points)
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

# ## Part 2: Collections & Indexing  (2.5 points)

# ### Q6 - Lists & Indexing (1 point)
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

# ### Q7 - Tuples (1 point)
# 
# In the cell below, explain the information or values you would store in a tuple, and why that variable type would be appropriate for your situation. 
# 
# Note: you do not *have* to write any python code here; we're looking for a written explanation.

# Possible examples (important fact was that they wouldn't reasonably change): birthdays of immediate family members; social security numbers of specific set of people; constants in physics; etc.
# 
# Answer also had to mention immutability of tuples

# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# 
# - example provided includes multiple pieces of information being stored (**0.25 pts**)
# - information being stored would reasonably NOT want to be changed (**0.50 pts**)
# - student explanation links immutability to their example (**0.25 pts**)
# 
# === END MARK SCHEME ===

# ### Q8 - Collections & Indexing  (0.5 points)
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

# ## Part 3: Control Flow - Conditionals & Loops  (6.2 points)

# ### Q9 - Conditionals (1.6 points)
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

# ### Q10 - `for` loop (2.75 points)
# 
# Rather than determining whether one single car should have a ticket written (as you did in the previous question), now you have to use the same logic, but for a whole list of cars. Two variables have been defined for you below. `speeds` includes the speeds of 6 cars. `zones` includes the zones in which each of those 6 cars was driving. For example, the first car was going `29` mph in a `'private'` zone.
# 
# Your goal is to determine for each of these cars whether or not they should receive a ticket (where `True` indicates they deserve a ticket and `False` does not). These values should be stored in a list called `output_list`, such that at the end you have a list of six booleans in `output_list` corresponding to the six cars in `speeds`/`zones`.

# In[36]:


# these variables provided for you
# this cell is read-only (cannot be changed)
speeds = [29, 30, 60, 4, 15, 27]
zones = ['private', 'local', 'highway', 'private', 'local', 'highway']


# In[37]:


### BEGIN SOLUTION
output_list = []

for val in range(0, len(speeds)):
    
    zone = zones[val]
    speed = speeds[val]
    
    if zone == 'private' and speed > private_mph:
        ticket = True
    elif zone == 'local' and speed > local_mph:
        ticket = True
    elif zone == 'highway' and speed > hwy_mph:
        ticket = True
    else:
        ticket = False
    
    output_list.append(ticket)

output_list

# solution without using append:

# output_list = [None, None, None, None, None, None]
# for val in range(0, len(speeds)):
#     if zones [val] == 'private' and speeds[val] > private_mph:
#         output_list[val] = True
#     elif zones[val] == 'local' and speeds[val] > local_mph:
#         output_list[val] = True
#     elif zones[val] == 'highway' and speeds[val]> hwy_mph:
#         output_list[val] = True
#     else:
#         output_list[val]= False
### END SOLUTION


# In[38]:


assert output_list is not None
### BEGIN HIDDEN TESTS
assert len(output_list) == 6
assert all([isinstance(x, bool) for x in output_list])
### END HIDDEN TESTS


# In[39]:


# hidden test checking values in output_list
### BEGIN HIDDEN TESTS
assert output_list == [True, True, False, False, False, False]
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - `output_list` initialized with a value [] (**0.25 points**)
# - `for` loop thorugh `cars`/`zones`/range of len (**0.5 points**)
# - indexed to get value from list correctly (**0.5 points**)
# - conditionals included (not grading for correctness, as last question did) (**0.25 points**)
# - list appended correctly (**0.25 points**)
#     
# === END MARK SCHEME ===

# ### Q11 - Accomplishing a task (1.85 points)
# 
# Prof Ellis has a *lot* on her plate today, and she needs you to figure out if she has enough time to do it all. Assume that each of the `long_tasks` (defined below) takes 2 hours and each of the `short_tasks` (defined below) takes 1 hour to complete.
# 
# Today, Prof Ellis has to write two (2) exams, grade an exam, answer email, hold office hours, and hold a staff meeting. She wants to know approximately how many hours that will take. 
# 
# Write code that will determine how long her day will take. Store the number of hours in the variable `prof_hours`.
# 
# Note: Do not hard-code. Your answer should use code-construcs discussed in class to calculate `prof_hours`. In other words, if the specific tasks in a day were to change your `prof_hours` should still calculate correctly.

# In[40]:


# these variables provided for you
# this cell is read-only (cannot be changed)
long_tasks = ['write one exam', 'grade exam', 'prep lecture', 'office hours']
short_tasks = ['review lecture', 'grade assignment', 'staff meeting', 'answer email']


# In[41]:


### BEGIN SOLUTION
prof_day = ['write one exam', 'write one exam', 'grade exam', 'answer email', 'office hours', 'staff meeting']
prof_hours = 0 

for task in prof_day:
    if task in long_tasks: 
        prof_hours += 2
    elif task in short_tasks:
        prof_hours += 1 
    else:
        print('possible typo')

prof_hours
### END SOLUTION


# In[42]:


assert prof_hours is not None
### BEGIN HIDDEN TESTS
assert prof_hours == 10
### END HIDDEN TESTS


# **This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)
# 
# === BEGIN MARK SCHEME ===
# - `prof_hours` initialized (**0.25 points**)
# - `for` loop set up correctly (**0.25 points**)
# - conditional correct (references long_tasks; short_tasks) (**0.25 points**) 
# - `prof_hours` incremented correctly (**0.5 points**)  
# 
# === END MARK SCHEME ===

# ### Submit on Datahub
# 
# Good work - you're done!
# 
# Check your work, and then when you're ready, **submit on datahub**.
# 
# We will not have your exam until you click submit and see this show up under 'submitted assignments'.
