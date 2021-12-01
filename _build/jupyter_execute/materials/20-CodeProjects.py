#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **A5** due Friday (11:59)
# - **Final exam/project** due next Mon (12/6; 11:59 PM)
#     - Practice Final will be released Mon afternoon; answer key posted Wed
#     - Final Exam will be released Friday afternoon
# - **CAPEs** - please fill out your [CAPEs](https://cape.ucsd.edu/) (+1% if >=85\% of class completes their CAPEs)
# - **[Post-Course Survey](https://docs.google.com/forms/d/e/1FAIpQLSfqwgORTqIj1h6Zb5MJB_StJnAVTgrOEboq60frGv4Z4xN3Wg/viewform?usp=sf_link)** ("due" 12/6 11:59 PM; link also on Canvas); ideally, fill out *after* taking final exam/completing final project
# - Demo Anaconda
# 

# **Q&A**
# 
# Q: Do the tests always have to be done on a text file or can they be done in the notebook   
# A: You can write them in the notebook to start, but we will be grading them in the project from a separate .py file. So, they'll have to be moved there.
# 
# Q: Does it matter if a comment is before or after the line of code that it is explaining?  
# A: Yes, it should come before.
# 
# Q: Will/When will we get a practice exam for the final exam?  
# A: Will be released this afternoon (Monday afternoon)
# 
# Q: When will we start our projects?  
# A: You should start them ASAP.
# 
# Q: How many documents should we submit for our project?  
# A: Minimal requirement: 1 notebook, 1 module/script, 1 test file
# 
# Q: Can toy go over the difference between isinstance and type again?  
# A: This is somewhat beyond the scope of this class. For our purposes, you can consider them equivaelent. But, I encourage you to use `type()` to avoid any confusion.
# 
# Q: Could you give more example on how we would use comments vs documentation in our code for example a class function?  
# A: Keep in mind documentation is for the *user*; comments are for the *developer*. See previous COGS 18 projects for more examples.
# 
# Q: What are some other python classes can we take after cogs 18? (Cogs 108 has a long waitlist...)  
# A: COGS 109, COGS 118 series, COGS 185, CSE courses, DSC 10, DSC 40, DSC 80
# 
# Q: When adding comments to our code, why do we use how and why instead of what?  
# A: Because your code typically demonstrates what.
# 
# Q: Will we have to write a unit test for each question in the final exam?  
# A: Not exactly. See practice midterm (posted later today) for an idea of how the layout will work.
# 
# Q: If I haven't started my project yet, am I still on track to do it? I've honestly felt a little intimidated to start it so I've been putting it off.   
# A: Yup! Hopefully today's lecture will help get you unstuck!
# 
# Q: For the project, if I use outside sources, lets say a list of the top ten most rated movies in the world from an article, how would I cite this?   
# A: https://cogs18.github.io/materials/Projects/faq.html#citations  
# Q: Who do we contact to learn how to use Anaconda?  
# A: I'll do a quick demo today, but you could ask in Office Hours and/or coding lab this week as well!
# 
# Q: Does my final project code have to run perfectly or can it still have some errors?  
# A: It can have errors; this will lose some points, but you'll certainly get credit for what's there.
# 
# Q: What is the grading distribution in this class? Is there extra credit for CAPE?  
# A: Yes, +1% to everyone's grades if >= 85% of class complete CAPEs. And, I use the standard grading scale. See syllabus.
# 
# Q: I do not know what is the difference between Test Coverage and unit tests.  
# A: Unit tests are the individual tests. Coverage is how much of your code is covered by tests. For example, if you had three functions and three tests, one for each of those functions, you would have 100% test coverage.

# # Code Projects
# 
# - modular design
# - minimal viable product
# - test-driven development
# - rapid prototyping
# - project organization
# - refactoring
# - code review

# ## Project Check-In
# 

# ### Modular Design

# <div class="alert alert-success">
# Modular design, like modular programming, is the approach of designing and building things as independent modules. 
# </div>

# ### Minimal Viable Product

# <div class="alert alert-success">
# A 'minimal viable product' is a product that contains the minimum amount of implemented features to use the code product - no more, no less.</div>

# ### Test-Driven Development

# <div class="alert alert-success">
# Writing the tests as soon as you have a plan & before you've written the code.
# </div>

# ### Rapid Prototyping

# <div class="alert alert-success">
# Rapid prototyping is an approach for developing things in which you work on minimal prototypes and iterate on them quickly. 
# </div>

# #### Some examples
# 
# - Chatbot: start and end a chat
# - Data Analysis: read a dataset in, make a basic plot
# - Car Inventory: object with method that adds a car to the Inventory
# - Artificial Agents: simple bot moves around randomly

# ## Project Organization

# - **Notebooks**: good for interactive development
#     - For when seeing the inputs and outputs of code running needs to be seen start to finish
#     - file ends in `.ipynb`
# - **Modules**: for storing mature Python code, that you can import
#     - you don't *use* the functions in there, just define them
#     - file ends in `.py`
# - **Scripts**: a Python file for executing a particular task
#     - this takes an input and does something start to finish
#     - file ends in `.py`

# ### Project Workflow

# Typical project workflow:
# 
# - Develop plan and write tests
# - Develop code interactively in a Jupyter notebook/text editor
# - As functions & classes become mature, move them to Python files that you then `import`
#     - As you do so, go back through them to check for code style, add documentation, and run your code tests
# - At the end of a project, (maybe) write a standalone script that runs the project

# #### Project Notes
# 
# 1. Design and write tests
# 2. Write some code
# 2. Test to make sure it works
# 3. Check code style (naming, spacing, etc.)
# 4. Add documentation
# 5. Move to module (if necessary)
# 6. Run all tests

# ### Project Design
# 
# - Idea: atbash encryption: return the capitalized, reverse alphabetical letter for each character in the input string
# 
# - Design:
#     - `atbash_encrypt()` : take input string and retrun atbash encrypted string
#         - inputs: `input_string` 
#         - returns: `atbash_string`
#     - `atbash_decrypt()` : take encrypted string and decrypt using atbash
#         - inputs: `atbash_string`
#         - returns: `decrypted_string`
#     - `atbash_wrapper()` : does either of the above, as specified with input parameter
#         - inputs: `input_string`, `method` (either 'encrypt' or 'decrypt', default: 'encrypt')
#         - returns `output_string`

# ### Adding Unit Tests

# In[ ]:


def test_atbash_encrypt():
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt('hello'), str)
    assert atbash_encrypt('HELLO') == 'SVOOL'
    assert atbash_encrypt('hello') == 'SVOOL'
    
def test_atbash_decrypt():
    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt('hello'), str)
    assert atbash_decrypt('SVOOL') == 'HELLO'
    assert atbash_decrypt('svool') == 'HELLO'

def test_atbash_wrapper():
    assert callable(atbash_wrapper)
    assert isinstance(atbash_wrapper('hello', method='encrypt'), str)
    assert atbash_wrapper('hello', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('HELLO', method='encrypt') == 'SVOOL'
    assert atbash_wrapper('SVOOL', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='decrypt') == 'HELLO'
    assert atbash_wrapper('svool', method='blargh') == "method should be either 'decrypt' or 'encrypt'"


# ...move to test file

# ### Writing Code

# #### `atbash_encrypt`

# In[1]:


def atbash_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    atbash_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            atbash_string += reverse_alpha[position]
        else:
            atbash_string = None
            break
        
    return atbash_string


# In[2]:


# smoke test
atbash_encrypt('Hello')


# ### Moving to a module...
# 
# - consider imports at the top

# Note on `imports`: If you want to be able to use modules (imports) within a module/script, be sure to import it at the top. This applies to test files as well.

# In[3]:


get_ipython().system('pytest test_atbash.py')


# #### `atbash_decrypt`

# In[ ]:


# reminder: consider code style! 
def atbash_decrypt(atbash_string):    
    ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    REVERSEALPHA='ZYXWVUTSRQPONMLKJIHGFEDCBA'
    atbash_string=atbash_string.upper()
    decrypted_string=''
    for l in atbash_string:
        if l in REVERSEALPHA:
            letterindex=REVERSEALPHA.find(l)
            decrypted_string=decrypted_string+ALPHA [letterindex]
        else: decrypted_string=decrypted_string+l
    return decrypted_string


# In[ ]:


# smoke test
atbash_decrypt('SVOOL')


# In[ ]:


get_ipython().system('pytest test_atbash.py')


# #### `atbash_wrapper`

# In[ ]:


def atbash_wrapper(input_string, method='encrypt'):
    
    if method == 'encrypt':
        output_string = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output_string = atbash_encrypt(input_string)
    else:
        output_string = "method should be either 'decrypt' or 'encrypt'"
    
    return output_string


# In[ ]:


# smoke test
atbash_wrapper('hello')


# In[ ]:


get_ipython().system('pytest test_atbash.py')


# ### Documentation
# 
# - Code in final project/exam requires:
#     - numpy-style docstrings
#     - code comments

# ### Putting it all together

# In[ ]:


from atbash import atbash_wrapper


# In[ ]:


atbash_wrapper('hello')


# In[ ]:


atbash_wrapper('svool', method='decrypt')


# In[ ]:


atbash_wrapper('hello', method='blargh')


# ### Refactoring

# <div class="alert alert-success">
# Refactoring is the process of restructuring existing computer code, without changing its external behaviour. 
# </div>

# Think of this as restructuring and final edits on your essay. 

# **Nesting Functions/Conditionals/Loops** - If you have a whole bunch of functions, if statements, and for/while loops together within a single function, you probably want (need?) to refactor.

# Clean functions accomplish a **single task**!

# **DRY**: Don't Repeat Yourself

# #### Refactoring Example: Chatbot

# In[ ]:


import random 

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        # Check if the input is a question
        input_string = msg
        if '?' in input_string:
            question = True
        else:
            question = False

        # Check for an end msg 
        if 'quit' in input_string:
            out_msg = 'Bye!'
            chat = False
            
        # If we don't have an output yet, but the input was a question, 
        # return msg related to it being a question
        if not out_msg and question:
            out_msg = "I'm too shy to answer questions. What do you want to talk about?"

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])

        print('OUTPUT:', out_msg)


# In[ ]:


have_a_chat()  


# #### Refactored Example: Chatbot

# What this function does:
# 
# 1. takes an input
# 2. checks if input is a question
# 3. checks if input is supposed to end the chat
# 4. return appropriate response if question, end chat, or other
# 
# That's four different things! Functions should do a single thing...

# In[ ]:


def get_input():
    """ask user for an input message"""
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg


# In[ ]:


def is_question(input_string):
    """determine if input from user is a question"""
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output


# In[ ]:


def end_chat(input_list):
    """identify if user says 'quit' in input and end chat"""
    
    if 'quit' in input_list:
        output = 'Bye'
        chat = False
    else:
        output = None
        chat = True
        
    return output, chat


# In[ ]:


def return_message(out_msg, question):
    """generic responses for the chatbot to return"""
        
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        out_msg = "I'm too shy to answer questions. What do you want to talk about?"

    # Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])
        
    return out_msg


# In[ ]:


def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get input message from the user
        msg, out_msg = get_input()
        
        # Check if the input is a question
        question = is_question(msg)
         
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
       
        # specify what to return
        out_msg = return_message(out_msg = out_msg, question = question)
        
        print('OUTPUT:', out_msg)


# In[ ]:


have_a_chat()  


# ## Code Review

# <div class="alert alert-success">
# Code reviews is a process for systematically reviewing someone else's code. 
# </div>

# This is what you'll have the chance to do in coding lab next week!
