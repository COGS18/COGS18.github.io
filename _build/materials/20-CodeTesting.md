---
interact_link: content/materials/20-CodeTesting.ipynb
download_link: assets/downloads/20-CodeTesting.ipynb.zip
pdf_link: assets/pdf/20-CodeTesting.pdf
layout: materials
title: '20-CodeTesting'
prev_page:
  url: /materials/19-CodeStyle
  title: '19-CodeStyle'
next_page:
  url: /materials/21-CodeProjects
  title: '21-CodeProjects'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

- Final Project Due 6/12 (11:59 PM)
- Please fill out your CAPEs

# Code Testing

- smoke tests
- unit tests
- `pytest`

#### Clicker Question #1

Given the following code, which assert will fail?



{:.input_area}
```python
def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output
```




{:.input_area}
```python
# test here
extend([1,2,3,4])
```





{:.output_data_text}
```
[1, 2, 3, 4, 1, 2, 3, 4]
```



- A) `assert isinstance(extend([1, 2]), list)`
- B) `assert extend([1, 2]) == [1, 2, 1, 2]`
- C) `assert extend((1, 2)) == (1, 2, 1, 2)` 
- D) `assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']`
- E) `assert extend([]) == []`

### Clicker Question - Asserts



{:.input_area}
```python
# Check that extend returns a list
assert isinstance(extend([1, 2]), list)
```




{:.input_area}
```python
# Check that an input list returns the expected result
assert extend([1, 2]) == [1, 2, 1, 2]
```




{:.input_area}
```python
# Check if the function works on tuples
assert extend((1, 2)) == (1, 2, 1, 2)
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AttributeError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-6-c510c0c20682> in <module>()
      1 # Check if the function works on tuples
----> 2 assert extend((1, 2)) == (1, 2, 1, 2)

```

{:.output_traceback_line}
```
<ipython-input-1-a3ca5f93bd43> in extend(input_arg)
      1 def extend(input_arg):
----> 2     output = input_arg.copy()
      3     for element in input_arg:
      4         output.append(element)
      5     return output

```

{:.output_traceback_line}
```
AttributeError: 'tuple' object has no attribute 'copy'
```




{:.input_area}
```python
# Check that a different input list (different lengths / contents) returns expected result
assert extend(['a', 'b', 'c']) == ['a', 'b', 'c', 'a', 'b', 'c']
```




{:.input_area}
```python
# Check that an empty list executes, executing an empty list
assert extend([]) == []
```


## Code Testing

<div class="alert alert-success">
Code tests is code that runs and checks other code, to make sure it does what it is expected to do. 
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



{:.input_area}
```python
def add(num1, num2):
    return num1 + num2
```




{:.input_area}
```python
add(2.7, 1.2) == 3.9
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
import math

def test_add():
    """Tests for the `add` function."""
    
    # Test adding positve numbers
    assert add(2, 2) == 4
    
    # Test adding negative numbers
    assert add(-2, -2) == -4
    
    # Test adding floats
    # assert add(2.7, 1.2) == 3.9
    assert math.isclose(add(2.7, 1.2), 3.9)
    
    # Test adding with 0
    assert add(2, 0) == 2
```




{:.input_area}
```python
# Run our test function
test_add()
```


#### Clicker Question #2



{:.input_area}
```python
# Given the following function:
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output
```




{:.input_area}
```python
divide_list((0,2,3))
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ZeroDivisionError                         Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-27-c91f35be7f5f> in <module>()
----> 1 divide_list((0,2,3))

```

{:.output_traceback_line}
```
<ipython-input-18-1f783ab343a3> in divide_list(in_list)
      4 
      5     for el1, el2 in zip(in_list[1:], in_list[0:-1]):
----> 6         output.append(el1 / el2)
      7 
      8     return output

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```




{:.input_area}
```python
# And the following test function:
def test_divide_list():
    assert isinstance(divide_list([1, 2]), list)
    assert divide_list([1, 2, 4]) == [2, 2]
```




{:.input_area}
```python
test_divide_list()
```


- A) These tests will pass, and this function is well tested
- B) These tests will pass, but this function needs more tests
- C) These tests will fail, but they cover the needed cases
- D) These tests will fail, and we should also have more tests

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

# Writing Good Code

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

### `pytest`

- check if error raised when expected to be raised
- autorun all of your tests
- formal testing to your code/projects

#### Executing `pytest`

1. Look for any file called `test_...`
2. If everything works, silently moves along. 
4. For anything that fails, will alert you.

**Available from Anaconda and on datahub**

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



{:.input_area}
```python
def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output
```




{:.input_area}
```python
### YOUR TEST
def test_sum_list():
    assert sum_list([1, 2, 3]) == 6

```




{:.input_area}
```python
test_sum_list()
```




{:.input_area}
```python
### POSSIBLE TEST
def test_sum_list():
    
    # write multiple asserts
    assert callable(sum_list)
    assert isinstance(sum_list([1, 2, 3, 4]), int)
    assert sum_list([1, 2, 3, 4]) == 10
    
test_sum_list()
```

