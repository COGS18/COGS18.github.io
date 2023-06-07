#!/usr/bin/env python
# coding: utf-8

# **Course Announcements**
# 
# - **CL9** due Wednesday (testing, documenting, refactoring)
# - **A5** due Friday
# - **Final Exam/Final Project** due Tuesday of finals week (6/13; 11:59 PM)
#     - Practice Final Available on datahub
# - Please complete your CAPEs!

# - Discuss getting template on datahub
#     - files that will be included in submission
# - Talk about what Canvas will show if you submit on datahub
# - review importing from a module vs running scripts (CL8 issues; lol @ car.py)

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

# #### Class Question #1
# 
# Given the following code, which assert will fail?

# In[2]:


def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output


# In[1]:


get_ipython().run_line_magic('pinfo', 'list.copy')


# In[7]:


assert type(extend([1, 2])) == list


# In[14]:


extend((1, 2))


# In[13]:


extend((1, 2)) == (1, 2, 1, 2)


# In[11]:


# test here
assert type(extend([1, 2])) == list
assert extend([1, 2]) == [1, 2, 1, 2]
# assert extend((1, 2)) == (1, 2, 1, 2)
assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']
assert extend([]) == []


# - A) `assert type(extend([1, 2])) == list`
# - B) `assert extend([1, 2]) == [1, 2, 1, 2]`
# - C) `assert extend((1, 2)) == (1, 2, 1, 2)` 
# - D) `assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']`
# - E) `assert extend([]) == []`

# ### Class Question - Asserts

# In[ ]:


# Check that extend returns a list
assert type(extend([1, 2])) == list


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
# - one test for each "piece" of your code (each function, each class, each method, etc)
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

# In[20]:


import math

def test_add():
    """Tests for the `add` function."""
    
    # Test adding positve numbers
    assert add(2, 2) == 4
    
    # Test adding negative numbers
    assert add(-2, -2) == -4
    
    # Test adding floats
#     assert add(2.7, 1.2) == 3.9
    assert math.isclose(add(2.7, 1.2), 3.9)
    
    # Test adding with 0
    assert add(2, 0) == 2


# In[17]:


def add(num1, num2):
    return num1 + num2


# In[19]:


add(2.7, 1.2)


# In[21]:


# Run our test function
test_add()


# #### Class Question #2
# 
# If you were asked to write a function `remove_punctuation` that removed all the punctuation from a given input string...what are some things that would be `True` of the output of that function?
# 
# - A) I've got some ideas!
# - B) I tried but I'm stuck.
# - C) I'm lost/don't understand what we're supposed to be doing.

# Brainstorm here...
# - output doesn't contain any punctuation
# - output should be a string 
# - output is shorter than or the the same length as the input

# In[ ]:


# assert statements here 
test_input = 'hello!@'
assert type(remove_punctuation(test_input)) == str
assert remove_punctuation(test_input) == 'hello'
assert len(remove_punctuation(test_input)) <= len(test_input)


# In[22]:


# test function here
def test_remove_punctuation():
    test_input = 'hello!@'
    assert type(remove_punctuation(input_string=test_input)) == str
    assert remove_punctuation(test_input) == 'hello'
    assert len(remove_punctuation(test_input)) <= len(test_input)


# In[26]:


test_remove_punctuation()


# In[25]:


# function here
from string import punctuation

def remove_punctuation(input_string):
    output_string = ''
    for ltr in input_string:
        if ltr in punctuation:
            continue
        else:
            output_string = output_string + ltr
    
    return output_string


# #### Class Question #3

# In[27]:


# Given the following function:
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output


# In[28]:


# And the following test function:
def test_divide_list():
    assert type(divide_list([1, 2])) == list
    assert divide_list([1, 2, 4]) == [2, 2]


# In[29]:


test_divide_list()


# - A) These tests will pass, and this function is well tested
# - B) These tests will pass, but this function needs more tests
# - C) These tests will fail, but they cover the needed cases
# - D) These tests will fail, and we should also have more tests

# In[30]:


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

# #### Class Question #4
# 
# Write a test function that checks the following piece of code:

# In[31]:


def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output


# Thought process:
# 1. Define test function `def test_...`
# 2. make `assert`ion within the test function
#     - check that the function is callable
#     - check the output is expected output / expected type
#     - check that function sums the list (which was our expectation)

# In[34]:


### YOUR TEST
def test_sum_list():
    assert callable(sum_list)
    assert type(sum_list([1,2])) == int
    assert sum_list([1, 2, 3]) == 6


# In[35]:


test_sum_list()


# In[ ]:


### POSSIBLE TEST
def test_sum_list():
    
    # write multiple asserts
    assert callable(sum_list)
    assert type(sum_list([1, 2, 3, 4])) == int
    assert sum_list([1, 2, 3, 4]) == 10
    
test_sum_list()


# ## Testing Code: when `input()` is used

# In[37]:


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


# In[38]:


get_input()


# In[39]:


import mock
import builtins

def test_get_input():
    # specify after lambda what you want function to use as "input"
    with mock.patch.object(builtins, 'input', lambda _: 'Hello'):

        # execute function and specify something that asserts True
        msg, out_msg = get_input()
        assert msg == 'Hello'
        assert out_msg == None


# In[40]:


test_get_input()


# <div class="alert alert-danger">
# If your function only has <code>print</code> statements as its output, it will *not* be testable. Consider this during development/planning!
# </div>

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
