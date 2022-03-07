#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# Due Dates:
# - **CL8** due Wed 3/9 
# - **A5** due Fri 3/11
# - **Final exam/project** due Mon 3/14
# 
# Notes:
# - Practice Final Exam now available on datahub
# - Please fill out your [CAPEs](https://cape.ucsd.edu/)! (+1% if >=85% of the class completes; currently: ~33%)
# - Staff office hours end this Friday; Prof Ellis will hold OH on Mon of finals week by appt - 10 min slots; details coming soon on how to sign up.

# **Q&A**
# 
# Q: Should there be a Docstring for every function that I write?  
# A: Your original code (3 required methods/functions) need docstrings. Beyond that, best to document all functions but not required
# 
# Q: Im still confused on how to get files to the right place so you can import them  
# A: This can be done at the terminal using `mv` (move) or by clicking to the left of the filename on datahub and selecting move at top/specifying where to move it to. If still unsure, this is absolutely something you want to get cleared up ASAP, so do attend office hours if this explanation does not help.
# 
# Q: Can you use docstrings and code comments or would that be too many comments?  
# A: You *should* have both docstrings and code comments. Comments are for people actually looking at your code. Docstrings are for users, people who just want to use your code.
# 
# Q: will I get docked point on the final exam if my coding style is different from what we've been doing?  
# A: Not necessarily. If you have good code style that is consistent throughout, you won't get docked points.
# 
# Q: I am unsure of what "\n"  and "\n\t" mean.
# A: "\n" is a newline character, so it will add a line break to your string; "\t" is a tab character; it will add a tab to your string.
# 
# Q: When do we need code documentation in our code? Is it optional or necessary?   
# A: In a code project at an internship/job, almost always. In your final project, see first QA from today. In final exam, when we specify to add docstrings.
# 
# Q: If we have a really long comment or want to explain something in detail, could we instead use a markdown cell?  
# A: If you're in a .py file, no...as there are no markdown cells. If you're in a notebook, absolutely.
# 
# Q: Why doesn't python automatically cut off a line at a certain point instead of allowing scrolling from left to right?  
# A: Great question. Lots of development environments do that for you and have that as a setting...and there *may* be a way to add on to jupyter to accomplish that, but it's not a setting in Jupyter by default.
# 
# Q: on the final exam, will there be functions in a package that we never gone over?  
# A: Nope. The final exam will require you to use `pandas` functions/methods, but you will have seen them all previously (lecture, coding lab, or A5).
# 
# Q: Other than making it easier to read, what other reasons are there to have good code style?   
# A: None. That's it! It makes it easier for the humans. (And trust me it may *feel* trivial, but it makes a *huge* difference...especially when you're "new" to the code or coming back to old code after having been a way for a bit)
# 
# Q: Is A5 the last assignment we have?  
# A: Yes.
# 
# Q: if I have 2 classes, can I add 2 docstrings. Also, if I think that my function is self-explanatory and if I ask you or the TAs if you can understand what it does, is it okay if I don't add a docstring for it?   
# A: Yes. And, yes. But, do be sure at least three methods/functions of your unique code have full docstrings.
# 
# Q: Just thinking of previous lectures, why is 'self' used in classes and methods?   
# A: Because it's the only place where we have attributes/data "attached" to an object. The use of `self` allows one to refer back to these "attached" attributes throughout the class.
# 
# Q: will we be strictly graded on code style for out final project?  
# A: You will be graded...but not strictly.
# 
# Q: what is df.method()?  
# A: This is the general format for how to call a pandas method. There will be some dataframe (`df` in the example code) and some method (`method()`).

# # Code Testing
# 
# - smoke tests
# - unit tests
# - `pytest`

# ## Writing Good Code

# All in all, write code that is:
# 
# - Well organized (follows a style guide)
# - Documented
# - **Tested**
# 
# And you will have understandable, maintainable, and trustable code. 

# #### Clicker Question #1
# 
# Given the following code, which assert will fail?

# In[ ]:


def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output


# In[ ]:


# test here


# - A) `assert isinstance(extend([1, 2]), list)`
# - B) `assert extend([1, 2]) == [1, 2, 1, 2]`
# - C) `assert extend((1, 2)) == (1, 2, 1, 2)` 
# - D) `assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']`
# - E) `assert extend([]) == []`

# ### Clicker Question - Asserts

# In[ ]:


# Check that extend returns a list
assert isinstance(extend([1, 2]), list)


# In[ ]:


# Check that an input list returns the expected result
assert extend([1, 2]) == [1, 2, 1, 2]


# In[ ]:


# Check if the function works on tuples
assert extend((1, 2)) == (1, 2, 1, 2)


# In[ ]:


# Check that a different input list (different lengths / contents) returns expected result
assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']


# In[ ]:


# Check that an empty list executes, executing an empty list
assert extend([]) == []


# ## Code Testing

# <div class="alert alert-success">
# Code tests are code that run and check other code, to make sure it does what it is expected to do. 
# </div>

# ### Levels of Code Testing:
# 
# - Smoke Tests
# - **Unit Tests**
# - Integration Tests
# - System Tests

# #### Four general types
# 
# 1. **Smoke tests** - preliminary tests to basic functionality; checks if something runs (but not necessarily if it does the right thing) (gut check) 
# 2. **Unit tests** - test functions & objects to ensure that they code is behaving as expected
# 3. **Integration tests** - tests functions, classes & modules interacting
# 4. **System tests** - tests end-to-end behavior 

# #### Unit Tests
# 
# - one test for each "piece" of your code (each function, each class, each module, etc)
# - passes silently if true
# - error if it fails
# - consider "edge cases"
# - help you resist the urge to assume computers will act how you think it will work 
# - functions used with pytest start with `test_`

# ### Not tests, but related
# - `assert`s - make a statement of fact about code 
# - static checks - check your code as you go that it behaves as expected
# - argument validation - checks to see if the input given to a function

# ## Why Write Tests

# - To ensure code does what it is supposed to
# - To have a system for checking things when you change things in the code

# Tests, when run, help identify code that will give an error if something has gone wrong. 

# ## The Best (Laziest) Argument for Writing Tests
# 
# Whenever you write new code, you will find yourself using little snippets of code to check it. 
# 
# Collect these snippets into a test function, and you get re-runnable tests for free.

# ![](img/code_testing.png)
# 
# Source: https://twitter.com/jimhester_/status/1361697676832739328

# ## How to Write Tests

# Given a function or class you want to test:
# - You need to have an expectation for what it should do
# - Write out some example cases, with known answers
# - Use `assert` to check that your example cases do run as expected
# - Collect these examples into test functions, stored in test files

# ## Example Test Code
# 
# What function should do: add two inputs together

# In[ ]:


# import math

def test_add():
    """Tests for the `add` function."""
    
    # Test adding positve numbers
    assert add(2, 2) == 4
    
    # Test adding negative numbers
    assert add(-2, -2) == -4
    
    # Test adding floats
    assert add(2.7, 1.2) == 3.9
    # assert math.isclose(add(2.7, 1.2), 3.9)
    
    # Test adding with 0
    assert add(2, 0) == 2


# In[ ]:


def add(num1, num2):
    return num1 + num2


# In[ ]:


# Run our test function
test_add()


# #### Clicker Question #2
# 
# If you were asked to write a function `remove_punctuation` that removed all the punctuation from a given input string...what are some things that would be `True` of the output of that function?
# 
# - A) I've got some ideas!
# - B) I tried but I'm stuck.
# - C) I'm lost/don't understand what we're supposed to be doing.

# Brainstorm here...

# In[ ]:


# assert statements here


# In[ ]:


# test function here


# In[ ]:


# function here


# #### Clicker Question #3

# In[ ]:


# Given the following function:
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output


# In[ ]:


# And the following test function:
def test_divide_list():
    assert isinstance(divide_list([1, 2]), list)
    assert divide_list([1, 2, 4]) == [2, 2]


# In[ ]:


test_divide_list()


# - A) These tests will pass, and this function is well tested
# - B) These tests will pass, but this function needs more tests
# - C) These tests will fail, but they cover the needed cases
# - D) These tests will fail, and we should also have more tests

# In[ ]:


divide_list((0,2,3))


# ## Test Driven Development

# <div class="alert alert-success">
# In software development, <b>test-driven development</b> is an approach in which you write tests first -  and then write code to pass the tests. 
# </div>

# ### Test Driven Development

# - Ensures you go into writing code with a good plan / outline
# - Ensures that you have a test suite, as you can not decide to neglect test code after the fact
# - Note: when you complete (or at least write) assignments for this class, you are effectively doing test-driven development

# ## Test Coverage

# <div class="alert alert-success">
# <b>Test coverage</b> is the proportion of a software project that is run by the test suite. 
# </div>

# #### Clicker Question #4
# 
# Write a test function that checks the following piece of code:

# In[ ]:


def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output


# - A) I did it!
# - B) I think I did it!
# - C) I'm lost.

# Thought process:
# 1. Define test function `def test_...`
# 2. make `assert`ion within the test function
#     - check that the function is callable
#     - check the output is expected output / expected type
#     - check that function sums the list (which was our expectation)

# In[ ]:


### YOUR TEST


# In[ ]:


test_sum_list()


# In[ ]:


### POSSIBLE TEST
def test_sum_list():
    
    # write multiple asserts
    assert callable(sum_list)
    assert isinstance(sum_list([1, 2, 3, 4]), int)
    assert sum_list([1, 2, 3, 4]) == 10
    
test_sum_list()


# ## Testing Code: when `input()` is used

# In[ ]:


def get_input():
    """ask user for an input message
    
    Returns
    -------
    msg : str
        text specified on input by user
    out_msg : None
        always returns None; subsequent functions would return a more specific out_msg
    """
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg


# In[ ]:


get_input()


# In[ ]:


import mock
import builtins

def test_get_input():
    # specify after lambda what you want function to use as "input"
    with mock.patch.object(builtins, 'input', lambda _: 'Hello'):

        # execute function and specify something that asserts True
        msg, out_msg = get_input()
        assert msg == 'Hello'
        assert out_msg == None


# In[ ]:


test_get_input()


# ## PyTest

# <div class="alert alert-info">
# <b><a href = 'https://docs.pytest.org/en/latest/'> PyTest </a></b> is a module that for writing and running test code. It is available from Anaconda and datahub.
# </div>

# ### `pytest`
# 
# - check if error raised when expected to be raised
# - autorun all of your tests
# - formal testing to your code/projects
# 
# #### Executing `pytest`
# 
# 1. Look for any file called `test_...`
# 2. If everything works, silently moves along. 
# 4. For anything that fails, will alert you.
# 
# **Available from Anaconda and on datahub**
