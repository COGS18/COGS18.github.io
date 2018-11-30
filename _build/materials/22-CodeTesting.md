---
interact_link: content/materials/22-CodeTesting.ipynb
download_link: assets/downloads/22-CodeTesting.ipynb.zip
pdf_link: assets/pdf/22-CodeTesting.pdf
layout: materials
title: '22-CodeTesting'
prev_page:
  url: /materials/21-CodeStyle
  title: '21-CodeStyle'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Code Testing

### Clicker Question #1

Given the following code, which assert will fail?



{:.input_area}
```python
def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output
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

## The Best Argument for Writing Tests

<div class="alert alert-success">
Whenever you write new code, you will find yourself using little snippets of code to check it. Collect these snippets into a test function, and you get re-runnable tests for free.
</div>

## Example Test Code



{:.input_area}
```python
def add(num1, num2):
    return num1 + num2
```




{:.input_area}
```python
def test_add():
    """Tests for the `add` function."""
    
    # Test adding positve numbers
    assert add(2, 2) == 4
    
    # Test adding negative numbers
    assert add(-2, -2) == -4
    
    # Test adding floats
    assert add(2.7, 1.2) == 3.9
    
    # Test adding with 0
    assert add(2, 0) == 2
```


### Clicker Question #2



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
# And the following test function:
def test_divide_list():
    assert isinstance(divide_list([1, 2]), list)
    assert divide_list([1, 2, 4]) == [2, 2]
```


- A) These tests will pass, and this function is well tested
- B) These tests will pass, but this function needs more tests
- C) These tests will fail, but they cover the needed cases
- D) These tests will fail, and we should also have more tests

## PyTest

<div class="alert alert-info">
[pytest](https://docs.pytest.org/en/latest/) is a module that for writing and running test code. 
</div>

## Levels of Code Testing:

- Smoke Tests
- Unit Tests
- Integration Tests

## Test Driven Development

<div class="alert alert-success">
In software development, 'test-driven development' is a approach in which you write tests first -  and then write code to pass the tests. 
</div>

### Test Driven Development

- Ensures you go into writing code with a good plan / outline
- Ensures that you have a test suite, as you can not decide to neglect test code after the fact
- Note: when you write assignments for this class, you are effectively doing test-driven development

## Test Coverage

<div class="alert alert-success">
Test coverage is the proportion of a software project that is run by the test suite. 
</div>

# Writing Good Code

If you write code that is:
- Documented
- Well organized (follows a style guide)
- Tested

You are an above average coder for academic & research. 
