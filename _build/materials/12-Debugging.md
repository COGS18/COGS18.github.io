---
interact_link: content/materials/12-Debugging.ipynb
download_link: assets/downloads/12-Debugging.ipynb.zip
pdf_link: assets/pdf/12-Debugging.pdf
layout: materials
title: '12-Debugging'
prev_page:
  url: /materials/11-FunctionsII
  title: '11-FunctionsII'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- A3 due tonight (11:59 PM)
- A4 due next Monday (11:59 PM)
    - functions, Classes & objects
    - builds up to an 'Artificial Agent' (bot)
- Midterm next Friday in class

### Functions: Points of Clarification

1. `def` defines a function
2. function_name() - parentheses are required to execute a function
3. function_name(input1) - input parameters are specified within the function parentheses 
4. function_name(input1, input2) - functions can take multiple parameters as inputs
    - `input1` and `input2` can then be used within your function when it executes
5. To store the output from a function, you'll need a `return` statement

#### For example....

If you write a function called `is_odd()` which takes an input `value`, 



{:.input_area}
```python
def is_odd(value):
    if value % 2 != 0:
        answer = True
    else:
        answer = False
    
    return answer
```


to use that function, you would execute `is_odd(value)` ....something like `is_odd(value=6)`



{:.input_area}
```python
is_odd(6)
```


Later on, if you wanted to use that function _within another function_, you still have to pass an input to the function.



{:.input_area}
```python
def new_function(my_list):
    output = []
    for val in my_list:
        if is_odd(val):
            output.append('yay!')
    return output
            
```




{:.input_area}
```python
new_function([1,2,4])
```


**Q10**: The instructions use the word append. They don't tell you to use the method `append()`. Remember:

- `append()` is a list method (_not_ a string method)
- append (the word) just means add to the end 
- concatenation is how to add to the end of a string

## Clicker Question #0

Notes: 
1. Material covered this week _IS_ on next week's exam
2. A4 covers functions, Classes, & Objects

_Hypothetically_: Would it be helpful if I pushed the due date for A4 back by a week? (This would make the exam next Friday and the assignment due the following Monday.)

- A) No
- B) Yes
- C) No opinion

# Debugging

- Errors
    - Syntax
    - Exceptions
- `try`/`except`

<div class="alert alert-success">
Debugging is the process of finding and fixing errors in a computer program.
</div>

Now that we're writing functions, debugging will become _really_ critical.

### Clicker Question #1

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


While it's annoying, it's helpful that Python doesn't just _guess_ that you _meant_ 'variable'....because sometimes Python would guess wrong. It's better for Python to just give us the error.



{:.input_area}
```python
# You also get a name error if you try to use the wrong operator for assignment
new_variable == 1
```


### IndexError

IndexError occurs when you try to access an index that doesn't exist.



{:.input_area}
```python
my_list = [1, 2, 3]
my_list[5]
```




{:.input_area}
```python
# Relatedly, 'KeyError' occurs if you ask for a dictionary key that doesn't exist
my_dictionary = {'name1' : 1, 'name2' : 2}
my_dictionary['name3']
```


### ValueError

ValueError occurs when you try to use an illegal value for something.



{:.input_area}
```python
int('cat')
```




{:.input_area}
```python
my_list = [1, 2, 3]
my_list.remove(0)
```


### TypeError



{:.input_area}
```python
'a_string' + 12
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


### Clicker Question #2

What type of error will the following code produce?



{:.input_area}
```python
int('six')
```


- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

### Clicker Question #3

What type of error will the following code produce?



{:.input_area}
```python
if num > 0
    print("Greater than 0")
```


- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

### Clicker Question #4

What type of error will the following code produce?



{:.input_area}
```python
if num > 0:
    print("Greater than 0")
```


- A) Syntax 
- B) Name
- C) Type
- D) Index
- E) Value

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
```


Sometimes these get really complex. We're here to get better at interpreting these traces.

Note that if external functions are being used, these will get longer.

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


### Example with Try / Except



{:.input_area}
```python
try:
    int(input('Number'))
except:
    print("nahhh")
```


#### Try / Except within a While Loop



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




{:.input_area}
```python
# define a function save_divide
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
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int)
```


### Clicker Question #5

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.



{:.input_area}
```python
num1  = ---
num2 = ---

try:
    output = --- / ---
except ZeroDivisionError:
    output = None
    
print(output)
```


- A) I did it!
- B) I _think_ I did it...
- C) I'm totally lost.
