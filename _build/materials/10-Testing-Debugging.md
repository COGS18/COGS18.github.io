---
interact_link: content/materials/10-Testing-Debugging.ipynb
download_link: assets/downloads/10-Testing-Debugging.ipynb.zip
pdf_link: assets/pdf/10-Testing-Debugging.pdf
layout: materials
title: '10-Testing-Debugging'
prev_page:
  url: /materials/09-FunctionsII
  title: '09-FunctionsII'
next_page:
  url: /materials/11-Classes
  title: '11-Classes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

**Upcoming Dates**
- **A3** due Monday (7/20)
- **CL4** due Wednesday (7/22)
- **E2** Thursday (7/23)

**General Notes**
- I'll release CL4 and A4 later today
- Prof Ellis will not have office hours _next_ week on Thurs (b/c of the exam)
    - Wed 4-6 PM instead
    - I'll send out a Piazza note
- My family is in town next week, so I'm going to be lecturing from our backyard. If the recording stinks or you have trouble hearing me at all, please let me know and I'll come up with a different plan!

# Debugging & Testing

- Errors
    - Syntax
    - Exceptions
- `try`/`except`
- Code Testing
    - smoke tests
    - unit tests
    - `pytest`

<div class="alert alert-success">
Debugging is the process of finding and fixing errors in a computer program.
</div>

Now that we're writing functions, debugging will become _really_ critical.

#### Clicker Question #1

Will I be able to define and execute this function?



{:.input_area}
```python
def example_function(input_list):
    
    running_sum = 0
    for item in input_list:
        running_sum = running_sum + item
    
    special_value = input_list[3]
    
    return running_sum + special_value
```




{:.input_area}
```python
example_function([1,2,3])
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-9-3d9cb7c5d23f> in <module>()
----> 1 example_function([1,2,3])

```

{:.output_traceback_line}
```
<ipython-input-7-a4fb5262d9d1> in example_function(input_list)
      5         running_sum = running_sum + item
      6 
----> 7     special_value = input_list[3]
      8 
      9     return running_sum + special_value

```

{:.output_traceback_line}
```
IndexError: list index out of range
```


- A) Yes 
- B) No
- C) Depends on the `input_list`
- D) There's no way to tell 
- E) I don't know



{:.input_area}
```python
### executing the function
```


## Errors

<div class="alert alert-success">
Errors are problems with code definition or execution that interrupt running Python code.
</div>

### Syntax Errors

- Syntax Errors
- Indentation Errors

<div class="alert alert-success">
Syntax & Indentation Errors reflect code that doesn't follow Python structure, and will necessarily fail. 
</div>

### Syntax Error Examples



{:.input_area}
```python
# will produce a syntax error
if True
    print('Yep.')
```



{:.output_traceback_line}
```
  File "<ipython-input-3-dfda8e0f217c>", line 2
    if True
           ^
SyntaxError: invalid syntax

```


Python does its best to tell you:
- what type of error it is
- and where it _thinks_ it occurred (`^`)



{:.input_area}
```python
# will produce a syntax error
# and specifically an indentation error
my_list = [1, 2]
for value in my_list:
print(value)
```



{:.output_traceback_line}
```
  File "<ipython-input-6-45596487aa45>", line 5
    print(value)
        ^
IndentationError: expected an indented block

```


Python gives you a readout about what it was expecting and where you appear to have gone wrong.

## Exceptions

<div class="alert alert-success">
Exceptions are errors that occur when a code is executed.
</div>

For these, there's nothing wrong with the _syntax_ or _structure_ of the code, but in your specific case and how you're trying to use it, Python says 'no'.

### ZeroDivisionError

ZeroDivisionError occurs when you try to divide by zero. 



{:.input_area}
```python
# produces ZeroDivisionError
1 / 0
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
<ipython-input-10-79e900a17bd3> in <module>()
      1 # produces ZeroDivisionError
----> 2 1 / 0

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```


Python specifies:
- the Exception and specific type / error
- points you to where the error occurred

### NameError

NameError occurs when you try to access a name that Python does not know.



{:.input_area}
```python
# Define a variable
variable = 12
```




{:.input_area}
```python
# If you typo a name, you will get a NameError
varaible
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-12-4acade15292f> in <module>()
      1 # If you typo a name, you will get a NameError
----> 2 varaible

```

{:.output_traceback_line}
```
NameError: name 'varaible' is not defined
```


While it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.



{:.input_area}
```python
# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
NameError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-15-4f05423dede6> in <module>()
      1 # You also get a name error if you try to use the wrong operator for assignment
----> 2 new_variable == 1

```

{:.output_traceback_line}
```
NameError: name 'new_variable' is not defined
```


### IndexError

IndexError occurs when you try to access an index that doesn't exist.



{:.input_area}
```python
my_list = [1, 2, 3]
my_list[5]
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-16-2c2a83518cf2> in <module>()
      1 my_list = [1, 2, 3]
----> 2 my_list[5]

```

{:.output_traceback_line}
```
IndexError: list index out of range
```




{:.input_area}
```python
# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
KeyError                                  Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-17-84a1c00e4833> in <module>()
      1 # Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
      2 my_dictionary = {'name1' : 1, 'name2' : 2}
----> 3 my_dictionary['name3']

```

{:.output_traceback_line}
```
KeyError: 'name3'
```


### ValueError

ValueError occurs when you try to use an illegal value for something.



{:.input_area}
```python
int('cat')
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-18-1c6b28888bbe> in <module>()
----> 1 int('cat')

```

{:.output_traceback_line}
```
ValueError: invalid literal for int() with base 10: 'cat'
```




{:.input_area}
```python
my_list = [1, 2, 3]
my_list.remove(0)
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-19-f00634ed638b> in <module>()
      1 my_list = [1, 2, 3]
----> 2 my_list.remove(0)

```

{:.output_traceback_line}
```
ValueError: list.remove(x): x not in list
```


### TypeError



{:.input_area}
```python
'a_string' + 12
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-20-57c293ee5895> in <module>()
----> 1 'a_string' + 12

```

{:.output_traceback_line}
```
TypeError: can only concatenate str (not "int") to str
```


## Error Recap

- Syntax Errors
    - `SyntaxError`
    - `IndentationError`
- Exceptions
    - `ZeroDivisionError` 
    - `NameError`
    - Index Errors
        - `IndexError`
        - `KeyError`
    - `ValueError`
    - `TypeError`


####  Errors: comprehension check

What type of error will each of the following produce?



{:.input_area}
```python
int('six')
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-21-196d25768c28> in <module>()
----> 1 int('six')

```

{:.output_traceback_line}
```
ValueError: invalid literal for int() with base 10: 'six'
```




{:.input_area}
```python
if num > 0
    print("Greater than 0")
```



{:.output_traceback_line}
```
  File "<ipython-input-25-ad228ac1793f>", line 1
    if num > 0
              ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
if num > 0:
    print("Greater than 0")
```


{:.output_stream}
```
Greater than 0

```

## Stack Trace

The trace (log) of what Python did as it went through your code. Gets printed out if Python runs into an error.



{:.input_area}
```python
running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        #+= allows you to add the value on the right to the variable on the left 
        # and assign it to the variable on the left
        running_sum += temp 
        # equivalent to:
        # running_sum = running_sum + temp
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
<ipython-input-27-215726ba149c> in <module>()
      5 
      6     if val % 2 == 0:
----> 7         temp = val / (val - 4)
      8         #+= allows you to add the value on the right to the variable on the left
      9         # and assign it to the variable on the left

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```


Sometimes these get really complex. We're here to get better at interpreting these traces.

Note that if external functions are being used, these will get longer. (.....I'm talking about A4, here.)

## Try / Except

<div class="alert alert-success">
Exceptions do not necessarily have to lead to breaking the program - they can be programmatically dealt with, using 'try' and 'except'. 
</div>

### Try / Except Block



{:.input_area}
```python
# Try / Except Block
try:
    # Tries to do this code
    pass # pass just says is not an operation; carry on
except:
    # If there is an error (an exception), keep going and do this instead
    pass
```


### Try / Except Example



{:.input_area}
```python
# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)
```


{:.output_stream}
```
Please type a number: shannon

my_num is:  shannon

```

### Example with Try / Except



{:.input_area}
```python
int('shannon')
```





{:.output_data_text}
```
5
```





{:.input_area}
```python
int(input('Number'))
```


{:.output_stream}
```
Numbershannon

```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-33-5c327d8444a1> in <module>()
----> 1 int(input('Number'))

```

{:.output_traceback_line}
```
ValueError: invalid literal for int() with base 10: 'shannon'
```




{:.input_area}
```python
try:
    int(input('Number'))
except:
    print("nahhh")
```


{:.output_stream}
```
Numbershannon
nahhh

```

#### Try / Except within a While Loop



{:.input_area}
```python
input("text")
```


{:.output_stream}
```
textadl;kjasldfkja;sldkjf

```




{:.output_data_text}
```
'adl;kjasldfkja;sldkjf'
```





{:.input_area}
```python
ask_for_num = True

while ask_for_num:
    try:
        my_num = int(input("Please enter a number: "))
        ask_for_num = False
    except ValueError:
        print("Oops!  That was no valid number. Try again!")
        
print('\nmy_num is: ', my_num)
```


{:.output_stream}
```
Please enter a number: as;kdfasdflkja
Oops!  That was no valid number. Try again!
Please enter a number: 29

my_num is:  29

```

### More Try / Except



{:.input_area}
```python
# define a function divide
def divide(num1, num2):
    return num1 / num2
```




{:.input_area}
```python
print(divide(2, 0))
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
<ipython-input-40-0cdf54a076ec> in <module>()
----> 1 print(divide(2, 0))

```

{:.output_traceback_line}
```
<ipython-input-39-62d4f4a69b89> in divide(num1, num2)
      1 # define a function divide
      2 def divide(num1, num2):
----> 3     return num1 / num2

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```




{:.input_area}
```python
# define a function safe_divide
def safe_divide(num1, num2):
    
    try:
        output = num1 / num2
    except ZeroDivisionError:
        output = None
    
    return output
```




{:.input_area}
```python
print(safe_divide(2, 0))
```


{:.output_stream}
```
None

```

## Raising Errors

<div class="alert alert-success">
You can also write code to raise an Exception if something unexpected happens.
</div>

### Raise Exception Examples

`raise` is a keyword that tells Python you want to create your own error.



{:.input_area}
```python
my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted an integer! :(')
    
print('My integer is: ', my_int) 
```


{:.output_stream}
```
An integer please: 9.4

```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-46-9e83f00ba183> in <module>()
      1 my_int = input('An integer please: ')
      2 if not my_int.isnumeric():
----> 3     raise ValueError('I wanted an integer! :(')
      4 
      5 print('My integer is: ', my_int)

```

{:.output_traceback_line}
```
ValueError: I wanted an integer! :(
```


#### Clicker Question #2

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.



{:.input_area}
```python
num1 = 6
num2 = 0

try:
    output = num1 / num2
except ZeroDivisionError:
    output = None
    
print(output)
```


{:.output_stream}
```
None

```

- A) I did it!
- B) I _think_ I did it...
- C) I'm totally lost.

## Code Testing

#### Clicker Question #3

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
<ipython-input-61-c510c0c20682> in <module>()
      1 # Check if the function works on tuples
----> 2 assert extend((1, 2)) == (1, 2, 1, 2)

```

{:.output_traceback_line}
```
<ipython-input-51-e590b6fb4ff9> in extend(input_arg)
      1 def extend(input_arg):
----> 2     output = input_arg.copy()
      3 
      4     for element in input_arg:
      5         output.append(element)

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
assert add(2, 4) == 6
```




{:.input_area}
```python
add(2.7, 1.2)
```





{:.output_data_text}
```
3.9000000000000004
```





{:.input_area}
```python
assert add(2.7, 1.2) == 3.9
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AssertionError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-69-ce54740178c5> in <module>()
----> 1 assert add(2.7, 1.2) == 3.9

```

{:.output_traceback_line}
```
AssertionError: 
```




{:.input_area}
```python
import math

math.isclose(add(2.7, 1.2), 3.9)
```





{:.output_data_text}
```
True
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


#### Clicker Question #4

Given the function and test below, which of the following is true?



{:.input_area}
```python
for el1, el2 in zip([1, 2, 3], ['a', 'b', 'c']):
    print(el1)
    print(el2)
```


{:.output_stream}
```
1
a
2
b
3
c

```



{:.input_area}
```python
def divide_list(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list[0:-1]):
        output.append(el1 / el2)
    
    return output
```




{:.input_area}
```python
divide_list([1,2,0,4])
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
<ipython-input-96-4382c68cea57> in <module>()
----> 1 divide_list([1,2,0,4])

```

{:.output_traceback_line}
```
<ipython-input-90-f3742fc060b2> in divide_list(in_list)
      3 
      4     for el1, el2 in zip(in_list[1:], in_list[0:-1]):
----> 5         output.append(el1 / el2)
      6 
      7     return output

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```




{:.input_area}
```python
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
- **Tested**

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

#### Clicker Question #5

Write a test function that checks the following piece of code:

- A) I did it!
- B) I think I did it!
- C) I'm lost.



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
sum_list([2,3]) == 5
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# TEST FUNCTION HERE
def test_sum_list():
    assert sum_list([2,3]) == 5
    assert isinstance(sum_list[2,3], int)
```


Thought process:
1. Define test function `def test_...`
2. make `assert`ion within the test function
    - check that function sums the list (which was our expectation)
    - check that the input was a list (either in function or test function)
    - check the output is expected output / expected type



{:.input_area}
```python
# callable checks to see if the input is something that can be called/executed
callable(sum_list)
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
### POSSIBLE TEST
def test_sum_list():
    
    # write multiple asserts
    assert callable(sum_list)
    assert isinstance(sum_list([1, 2, 3, 4]), int)
    assert sum_list([1, 2, 3, 4]) == 10
```




{:.input_area}
```python
test_sum_list()
```


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
