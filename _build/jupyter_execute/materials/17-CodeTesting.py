**Course Announcements**

**Due Dates:**
- **CL7** due tonight (11:59 PM)
    - `open` does not work on datahub; can open file by clicking from Files tab
- **A5** due Mon of week 10 12/7 (11:59 PM) 

**Notes**
- No Class Friday & No OH Th-Sun (Happy Thanksgiving!)
- Final Exam Option: will have _at least_ 24h - will also be due Mon 11:59PM of finals week
- Final Project: 
    - Plan before you start writing code! 
    - What pieces (functions, classes) will you need? Which do you absoultely need to have a minimal viable project? Start there!
    - Requirements: >=3 unique functions/methods + >=3 tests 


# Code Testing

- smoke tests
- unit tests
- `pytest`

#### Clicker Question #1

Given the following code, which assert will fail?

def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output

# test here
extend((1, 2))

- A) `assert isinstance(extend([1, 2]), list)`
- B) `assert extend([1, 2]) == [1, 2, 1, 2]`
- C) `assert extend((1, 2)) == (1, 2, 1, 2)` 
- D) `assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']`
- E) `assert extend([]) == []`

### Clicker Question - Asserts

# Check that extend returns a list
assert isinstance(extend([1, 2]), list)

# Check that an input list returns the expected result
assert extend([1, 2]) == [1, 2, 1, 2]

# Check if the function works on tuples
assert extend((1, 2)) == (1, 2, 1, 2)

# Check that a different input list (different lengths / contents) returns expected result
assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']

# Check that an empty list executes, executing an empty list
assert extend([]) == []

## Code Testing

<div class="alert alert-success">
Code tests are code that runs and checks other code, to make sure it does what it is expected to do. 
</div>

## How to Write Tests

Given a function or class you want to test:
- You need to have an expectation for what it should do
- Write out some example cases, with known answers
- Use `assert` to check that your example cases do run as expected
- Collect these examples into test functions, stored in test files

## Why Write Tests

- To ensure code does what it is supposed to
- To have a system for checking things when you change things in the code

## The Best (Laziest) Argument for Writing Tests

Whenever you write new code, you will find yourself using little snippets of code to check it. 

Collect these snippets into a test function, and you get re-runnable tests for free.

## Example Test Code

def add(num1, num2):
    return num1 + num2

add(2.7, 1.2)

add(2.7, 1.2) == 3.9

import math
math.isclose(add(2.7, 1.2), 3.9)

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

# Run our test function
test_add()

#### Clicker Question #2

# Given the following function:
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output

divide_list([0,1,2])

# And the following test function:
def test_divide_list():
    assert isinstance(divide_list([1, 2]), list)
    assert divide_list([1, 2, 4]) == [2, 2]

test_divide_list()

- A) These tests will pass, and this function is well tested
- B) These tests will pass, but this function needs more tests
- C) These tests will fail, but they cover the needed cases
- D) These tests will fail, and we should also have more tests

divide_list((0,2,3))

## PyTest

<div class="alert alert-info">
<b><a href = 'https://docs.pytest.org/en/latest/'> PyTest </a></b> is a module that for writing and running test code. It is available from Anaconda and datahub.
</div>

## Levels of Code Testing:

- Smoke Tests
- **Unit Tests**
- Integration Tests
- System Tests

## Test Driven Development

<div class="alert alert-success">
In software development, <b>test-driven development</b> is an approach in which you write tests first -  and then write code to pass the tests. 
</div>

### Test Driven Development

- Ensures you go into writing code with a good plan / outline
- Ensures that you have a test suite, as you can not decide to neglect test code after the fact
- Note: when you complete (or at least write) assignments for this class, you are effectively doing test-driven development

## Test Coverage

<div class="alert alert-success">
<b>Test coverage</b> is the proportion of a software project that is run by the test suite. 
</div>

## Writing Good Code

All in all, write code that is:
- Documented
- Well organized (follows a style guide)
- Tested

And you will have understandable, maintainable, and trustable code. 

Why We Write Tests:

- ensure does does what it's supposed to
- system for checking things when you change / make updates in the future

Tests, when run, help identify code that will give an error if something has gone wrong. 

### Four general types

1. **Smoke tests** - preliminary tests to basic functionality; checks if something runs (but not necessarily if it does the right thing) (sanity check) 
2. **Unit tests** - test functions & objects to ensure that they code is behaving as expected
3. **Integration tests** - tests functions, classes & modules interacting
4. **System tests** - tests end-to-end behavior 

### Not tests, but related
- asserts - make a statement of fact about code 
- static checks - check your code as you go that it behaves as expected
- argument validation - checks to see if the input given to a function

### Unit Tests

- one test for each "piece" of your code (each function, each class, each module, etc)
- passes silently if true
- error if it fails
- consider "edge cases"
- help you resist the urge to assume computers will act how you think it will work 
- functions used with pytest start with `test_`

#### Clicker Question #3

Write a test function that checks the following piece of code:

- A) I did it!
- B) I think I did it!
- C) I'm lost.

Thought process:
1. Define test function `def test_...`
2. make `assert`ion within the test function
    - check that function sums the list (which was our expectation)
    - check that the input was a list (either in function or test function)
    - check the output is expected output / expected type

def sum_list(input_list):
    """add all values in a list/tuple - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output

### YOUR TEST
def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert isinstance(sum_list([1, 2, 3]), int)
    assert sum_list((1, 2, 3)) == 6

# test if input is what you expected (a list) on Wed

test_sum_list()

### `pytest`

- check if error raised when expected to be raised
- autorun all of your tests
- formal testing to your code/projects

#### Executing `pytest`

1. Look for any file called `test_...`
2. If everything works, silently moves along. 
4. For anything that fails, will alert you.

**Available from Anaconda and on datahub**

def sum_list(input_list):
    """add all values in a list - return sum"""
    
    # add in test for incorrect input
    if not isinstance(input_list, list):
        raise ValueError("Please provide the input as a list")
    else:
        output = 0

        for val in input_list:
            output += val
        
    return output

# see how function performs here
sum_list([1, 2, 3])
# this below would raise error
# sum_list(3)

### POSSIBLE TEST
def test_sum_list():
    
    # write multiple asserts
    assert callable(sum_list)
    assert isinstance(sum_list([1, 2, 3, 4]), int)
    assert sum_list([1, 2, 3, 4]) == 10
    
    # include approach where testing for error
    try: 
        sum_list(3)
    except ValueError:
        assert True

test_sum_list()

!pytest tests.py