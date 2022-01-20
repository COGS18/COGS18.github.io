#!/usr/bin/env python
# coding: utf-8

# **Course Announcements (Wed 1/12)**
# 
# Due Dates:
# - **CL3** due tonight (11:59 PM)
# - **A1** accepted until late deadline w/o penalty (Thurs 1/20 11:59 PM)
# 
# Notes:
# - **A2** now available
# - **CL2** scores posted (out of 2 pts; concerted effort)
# - Review:
#     - copy + paste code vs. copy + pasting a whole cell
#     - must define/execute cell before you can use the variables
#     - avoid hard-coding

# Reminder: Do the greet clicker question!

# **Q&A**
# 
# Q: So only def and return are operators specific to functions?  
# A: Correct!
# 
# Q: But where do I go to find the answer keys for assignments and labs?  
# A: Lab answer keys are posted on the course website and on datahub in the Lectures-COGS18 folder...inside a folder called CL-Answers. Assignment answer keys aren't posted, but you'll get specific feedback about where points were lost. We'll discuss where to find this (on datahub assignments tab) after A1 is graded.
# 
# Q: In a function, can one of the two parentheses be a number and the other one be strings?  
# A: Yup! 
# 
# Q: Is the way we create the instructions for the function done with the # and then the command?  
# A: You can always add a comment with # before the code, but remember the computer ignores all commentes...so you'd definitely still need the code.
# 
# Q: When will the coding labs be graded by?   
# A: Typically, these are graded by Sunday night and I'll post grades Monday morning.
# 
# Q: What does "The source of the following cell has changed, but it should not have!": mean?  
# A: This typically means you copy+pasted an instruction cell on an assignment. This is something you can't delete but that we can fix when grading your assignment. Do your best to avoid copy+pasting whole cells on an assignment to avoid this.
# 
# Q: Just clarification regarding the fact that we can turn in assignment 1 late - is that a one time thing due to it being due on a weekend, or is it just a general one time situation for any of the assignments due?   
# A: This is a one time thing due to the holiday. Typically, assignments can be turned in up to 3 days late...but at a 25% penalty. This time, there will be no penalty applied.
# 
# Q: In the function examples given in the notes, the instructions usually define an operation first such as 'answer= num1+num2', and then return that operation such as 'return answer'. I'm curious about whether you can just write 'return num1+num2', or you have to define some kind of variable first and then return that variable to get the proper answer?  
# A: You can just return directly! I didn't do this in the notes so that it was clear to students what was happening...but feel free to condense to a single line.
# 
# Q: Can we use a function within a function? Specifically, ones that we defined prior to defining a new one?   
# A: Yes, you can use a function within a function; however, to execute a function, any functions used within it must already be defined.
# 
# Q: I know we went over this in class, but I'm still a bit confused on what the difference between return and print is. Is return only used for functions?  
# A: `return` specifies what the output from your function should be. It IS specific to function definitions. `print()` is a general statement to use any time you want to "check and see" what is stored in a variable.
# 
# Q: I saw the content of pseudocode in CL3. Do I miss this part in class or we haven't talked about it yet?  
# A: We won't discuss this in class explicitly, but the process is what we're doing every time we define a function.
# 
# Q: I need to know the difference between a parameter and an argument and how they affect each other.   
# A: For our purposes, we can use these terms interchangeably. 
# 
# Q: The homework is not enough for me. What other resources do I have to practice the material?   
# A: Check out the extra practice problems [here](https://shanellis.github.io/pythonbook/content/intro.html). Note that the Answers section has answers to the practice problems. 
# 
# Q: Please give us a challenging question at the end of each lecture to test our knowledge that we can discuss in office hours or in the beginning of the next lecture.   
# A: We'll do this more and more, time permitting.
# 
# Q: Is there any limitation on functions? Is there a maximum length that a function can be or any other things that limit how much or what you could write in a function?  
# A: No limits on functions theoretically, but we won't be writing functions that are too long/confusing. And, generally it's best for functions to do a single thing. If they get really long, there's probably a better approach - we'll get there!
# 
# Q: How widely can we use function in our code beyond mathematics equation solving given as example?  
# A: We'll use them a TON throughout this course. You'll see that they're the building block for code as we build on this concept! 
# 
# Q: Kinda peeking ahead, but while I know that technically we can use the same variable name within different functions (like having two functions return a variable my_var that was defined within each function), is it considered bad practice to do so?  
# A: Yea - anything that makes your code harder to understand should generally be avoided.
# 
# Q: When defining a function should we leave a blank line below the definition?  
# A: This is somewhat personal preference. I typically do...but it's not required.
# 
# Q: How come if lets say I have a=5 and b=4, and I create a new cell and just write a in line one and b in line two does it only output as 4 and not 5 and 4? Is the way to change this just to write print(a) print(b)? Thanks!   </br>
# A: Yup, `print()` will *always* print. The variable on its own will only be displayed if it's the last statement in a cell.
# 
# Q: I have a question from Assignment 1: In question 10, I would've loved to create a default value within my curve_grade function so that I didn't have to type out 0.03 for every student. I didn't want to mess with my original code, but in a situation like this, would the way to assign a default value be to go back to my original code, and add (points, curve = 0.03) to the parameters? Also, would this question have been better-directed to a private message on Campuswire?   
# A: Yup - this is a perfect message for Campuswire ...in fact, this could be a public message that way all students could benefit from the answer. So...*if* you knew that most of the time when you used this function the curve would be 0.03, yes, you would specify a default value within the function definition. However, in my thinking of this question, it was just *this* exam where we chose to do a 0.03 curve...so no need to edit the function definition. Hope that helps!
# 
# Q: When we concatenating strings, how to make space between each string in our output?   
# A: See the end of the operators lecture.
# 
# Q: Is the string can be only letters or letter+number? I'm still a little confused about the definition of string.  
# A: A string can be any character...that could be a letter, or a number, or a symbol, or a space. If it's in quotation marks...it's a string.

# # Conditionals
# 
# - `if`
# - `elif`
# - `else`

# ## Conditionals: `if`

# <div class="alert alert-success">
# Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
# </div>

# In[4]:


condition = True

if condition:
    print('This code executes if the condition evaluates as True.')


# In[5]:


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

# In[9]:


math = 3 < 4

if math:
    print('True')


# ## Conditional: `else`

# <div class="alert alert-success">
# After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
# </div>

# In[10]:


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

# In[12]:


my_value = 3 == 4

if my_value:
    print('True')
else: 
    print('False')


# ## Conditional: `elif`

# <div class="alert alert-success">
# After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
# </div>

# In[13]:


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

# In[14]:


condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')


# ### `elif` *after* an `else` does not make sense
# 
# The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

# In[15]:


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

# In[24]:


speed_limit = 65
speed = 70

if speed > speed_limit:
    ticket = True
else:
    ticket = False
    
ticket


# In[21]:


# string value comparisons also possible
a1 = 'completed'

if a1 == 'completed'
    action = 'grade'
elif a1 == 'in progress':
    action = 'wait'
elif a1 == 'not started':
    action = 'incomplete'
else:
    action = 'uncertain'


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

# ## Code Style: Conditionals
# 
# - avoid single line statements
# - a single conditional (if + elif + else) has no additional line spaces between statements

# ### Conditionals: Good Code Style

# In[2]:


value = 16

if value % 2 == 0:
    out = "even"
else:
    out = "odd"


# ### Conditionals: Code Style to Avoid

# In[3]:


if value%2==0:out="even" # avoid statement on same line as conditional
                         # avoid blank line between if and else
else:out="odd"           # don't forget about spacing around operators!                     


# ## Functions + Conditionals
# 
# Let's define a more interesting function than what we did in the functions lecture. Here we are using conditionals within our function.

# In[ ]:


# Determine if a value is even or odd
def even_odd(value): 

    if value % 2 == 0: 
        out = "even"
    else: 
        out = "odd"
        
    return out


# In[ ]:


# Execute our function to check that
# it is working according to our expectations
even_odd(-1)

