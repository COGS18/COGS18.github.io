**Course Announcements**

- **CL8** due next Wednesday (posted later today)
- **A5** due Monday of week 10 (5/31)

**Q&A**

Q: If you did the code differently from the autograder but still had functional code using a different method, will you still only get partial credit? 
A: On an assignment, you'd get credit. On an exam, if we specified that a certain method/object/function be used and it was not, you would only get partial credit.

Q: Does numpy only apply to making matrices?  
A: For the most part; it's really made for creating and operating on matrices.

Q: When indexing arrays or DataFrame objects, how can include a range of columns and/or rows? We talked about how we can do this for individual or all columns or rows, but what if I wanted to only find the values from rows 2-4 or columns 1-3?
A: This is where the `loc` method is quite helpful. `df.loc[2:5, 1:4]` would do what you're looking for!

Q: Does plotting only serve for drawing graphs?  
A: Hmmm....making plots is typically for creating lots of different types of graphs. Not sure what else you had in mind here, so do reach out if still unsure!

Q: I am curious on how often pandas are used for heterogenous data like the example from lecture on logging subject information from possibly some type of experiment. I always assumed people just used excel or spreadsheets to log this kind of data, but I was wondering how often Python is used to store this data, since it appears to be much faster?  
A: Python (and R, another programming language) are used *all* the time for operating on data. The reason is b/c 1) it is faster, but 2) it's reproducible. If I give you the data and the code, you can generate the results as well. With Excel that's not exactly possible unless you meticulously write down all the pointing and clicking you did.

Q: This is more so for my final project, but for the plotting section, can you use that to create a map in a sense?  
A: Yup! There is a package called `geopandas` that may be helpful for this purpose! 

Q: Is it always required to include the imported module name before using one of its methods?  
A: If you import the module/package directly `import module`, then yes, you always have to specify the module/package name before referring to a function from it. However if you import the function directly `from module import function`, then you can call `function` directly. The exception here is when we're talking about methods. Once an object of a particular class is created (DataFrame, numpy array, etc.), you can call the methods directly `df.method()` without the package/module name before it.

Q: Is there a website that introduces these packages, or if I want to use other packages, where can I find them?  
A: There is a lot of documentation on line. Searching the package name and python (`'pandas python`) will help you find the documentation! [PyP](https://pypi.org/project/pip/) is a searchable place for packages as well. 

Q: Pandas vs Scipy??
A: Pandas for getting the data into the format you need; Scipy (the package) is for analyzing those data after you get them into the format you need. 

Q: Can we invite tables from Excel into python?  
A: Yup! There are `read_` methods in pandas to read external files in.

Q: Will we be covering other major libraries?  
A: No this quarter.

Q: The plotting won't be on the exam correct?  
A: Correct. The plotting & stats (t-test) at the end were just shared for an FYI.

Q: Since packages like numpy use objects like arrays and pandas use objects like DataFrame, does that mean they can only be used with those packages?  
A: Kind of. These packages are often designed to work well together. So, while the DataFrame object is a pandas object, it sometimes borrows from other related packages. Happy to answer this question in more detail and discuss dependencies in office hours!

Q: will we incorporate these into our final project somehow, or is it just there as an option?  
A: Up to you if you use these in your final project; not required! DataFrames and matrices (and the methods we've discussed) are fair game for the final exam, however.

Q: How might we use these to facilitate something on our final project?  
A: If your project involves keeping track of information in rows and columns, consider a `numpy` array. If your project involves storing data and using it (analyzing, plotting, etc.), consider `pandas`.

# Code Testing

- smoke tests
- unit tests
- `pytest`

## Writing Good Code

All in all, write code that is:

- **Tested**
- Documented
- Well organized (follows a style guide)

And you will have understandable, maintainable, and trustable code. 

#### Clicker Question #1

Given the following code, which assert will fail?

def extend(input_arg):
    output = input_arg.copy()
    for element in input_arg:
        output.append(element)
    return output

# test here

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
Code tests is code that runs and checks other code, to make sure it does what it is expected to do. 
</div>

## Why Write Tests

- To ensure code does what it is supposed to
- To have a system for checking things when you change things in the code

Tests, when run, help identify code that will give an error if something has gone wrong. 

## The Best (Laziest) Argument for Writing Tests

Whenever you write new code, you will find yourself using little snippets of code to check it. 

Collect these snippets into a test function, and you get re-runnable tests for free.

![](img/code_testing.png)

Source: https://twitter.com/jimhester_/status/1361697676832739328

## How to Write Tests

Given a function or class you want to test:
- You need to have an expectation for what it should do
- Write out some example cases, with known answers
- Use `assert` to check that your example cases do run as expected
- Collect these examples into test functions, stored in test files

## Example Test Code

def add(num1, num2):
    return num1 + num2

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

# Run our test function
test_add()

add(2.7, 1.2) == 3.9

#### Clicker Question #2

# Given the following function:
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output

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

## Levels of Code Testing:

- Smoke Tests
- **Unit Tests**
- Integration Tests
- System Tests

### Four general types

1. **Smoke tests** - preliminary tests to basic functionality; checks if something runs (but not necessarily if it does the right thing) (sanity check) 
2. **Unit tests** - test functions & objects to ensure that they code is behaving as expected
3. **Integration tests** - tests functions, classes & modules interacting
4. **System tests** - tests end-to-end behavior 

### Unit Tests

- one test for each "piece" of your code (each function, each class, each module, etc)
- passes silently if true
- error if it fails
- consider "edge cases"
- help you resist the urge to assume computers will act how you think it will work 
- functions used with pytest start with `test_`

### Not tests, but related
- asserts - make a statement of fact about code 
- static checks - check your code as you go that it behaves as expected
- argument validation - checks to see if the input given to a function

#### Clicker Question #3

Write a test function that checks the following piece of code:

- A) I did it!
- B) I think I did it!
- C) I'm lost.

Thought process:
1. Define test function `def test_...`
2. make `assert`ion within the test function
    - check that the function is callable
    - check that function sums the list (which was our expectation)
    - check the output is expected output / expected type

def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output

### YOUR TEST

test_sum_list()

## PyTest

<div class="alert alert-info">
<b><a href = 'https://docs.pytest.org/en/latest/'> PyTest </a></b> is a module that for writing and running test code. It is available from Anaconda and datahub.
</div>

### `pytest`

- check if error raised when expected to be raised
- autorun all of your tests
- formal testing to your code/projects

#### Executing `pytest`

1. Look for any file called `test_...`
2. If everything works, silently moves along. 
4. For anything that fails, will alert you.

**Available from Anaconda and on datahub**