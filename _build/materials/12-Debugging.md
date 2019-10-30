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
  url: /materials/13-Objects
  title: '13-Objects'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- A3 due Friday (11:59 PM)
- Exam scores posted
    - Score on back of exam is out of 60
    - Grade posted on Canvas out of 15 (Median: 12.7/15 ; 84.6%)
    - Will be available to look over:
        - Wednesday in CodingLab
        - regrades will be handled by Prof Ellis

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




{:.input_area}
```python
# will work
example_function([1, 2, 3, 4])
```





{:.output_data_text}
```
14
```





{:.input_area}
```python
# will not work
example_function(['s', 'h', 'a', 'n'])
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
<ipython-input-3-6a097b693a7c> in <module>()
----> 1 example_function(['s', 'h', 'a', 'n'])

```

{:.output_traceback_line}
```
<ipython-input-1-a4fb5262d9d1> in example_function(input_list)
      3     running_sum = 0
      4     for item in input_list:
----> 5         running_sum = running_sum + item
      6 
      7     special_value = input_list[3]

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```


- A) Yes 
- B) No
- C) Depends on the `input_list`
- D) There's no way to tell 
- E) I don't know



{:.input_area}
```python
### executing the function
example_function([2, 3, 4, 5.7, 8.2])
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
  File "<ipython-input-5-a91490a26c37>", line 2
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
<ipython-input-7-79e900a17bd3> in <module>()
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
<ipython-input-9-4acade15292f> in <module>()
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
<ipython-input-10-4f05423dede6> in <module>()
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
<ipython-input-11-2c2a83518cf2> in <module>()
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
<ipython-input-12-84a1c00e4833> in <module>()
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
<ipython-input-13-1c6b28888bbe> in <module>()
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
<ipython-input-14-f00634ed638b> in <module>()
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
<ipython-input-15-57c293ee5895> in <module>()
----> 1 'a_string' + 12

```

{:.output_traceback_line}
```
TypeError: must be str, not int
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
<ipython-input-16-196d25768c28> in <module>()
----> 1 int('six')

```

{:.output_traceback_line}
```
ValueError: invalid literal for int() with base 10: 'six'
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



{:.output_traceback_line}
```
  File "<ipython-input-17-ad228ac1793f>", line 1
    if num > 0
              ^
SyntaxError: invalid syntax

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
<ipython-input-18-2ff8076b6898> in <module>()
----> 1 if num > 0:
      2     print("Greater than 0")

```

{:.output_traceback_line}
```
NameError: name 'num' is not defined
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
<ipython-input-21-5d11a706076f> in <module>()
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


{:.output_stream}
```
Please type a number: shannon

my_num is:  shannon

```

### Example with Try / Except



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
Please enter a number: shannon
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
<ipython-input-29-0cdf54a076ec> in <module>()
----> 1 print(divide(2, 0))

```

{:.output_traceback_line}
```
<ipython-input-28-62d4f4a69b89> in divide(num1, num2)
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
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int) 
```


{:.output_stream}
```
An integer please: shannon

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
<ipython-input-33-bc64f24647db> in <module>()
      1 my_int = input('An integer please: ')
      2 if not my_int.isnumeric():
----> 3     raise ValueError('I wanted a number! :(')
      4 
      5 print('My integer is: ', my_int)

```

{:.output_traceback_line}
```
ValueError: I wanted a number! :(
```


### Clicker Question #5

Edit the code below (replacing `---` with either values or variable names) so that when executed, this cell returns `None`.



{:.input_area}
```python
num1  = 1
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
