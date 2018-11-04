---
download_link: assets/downloads/materials/12-Debugging.ipynb.zip
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

# Debugging

<div class="alert alert-success">
Debugging is the process of finding and fixing errors in a computer program.
</div>

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


A) Yes | B) No | C) Depends on the Input List D) There's no way to tell E) I don't know

## Errors

<div class="alert alert-success">
Errors are problems with code definition or execution that interrupt running Python code.
</div>

### Syntax & Indentation Errors

<div class="alert alert-success">
Syntax & Indentation Errors reflect code that doesn't follow Python structure, and will necessarily fail. 
</div>

### Syntax Error Examples



{:.input_area}
```python
if True
    print('Yep.')
```



{:.output_traceback_line}
```
  File "<ipython-input-2-84adba9b209c>", line 1
    if True
           ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
my_list = [1, 2]
for value in my_list:
print(value)
```



{:.output_traceback_line}
```
  File "<ipython-input-3-6b38a7bbe4d8>", line 3
    print(value)
        ^
IndentationError: expected an indented block

```


## Exceptions

<div class="alert alert-success">
Exceptions are errors that occur when a code is executed.
</div>

### ZeroDivisionError

ZeroDivisionError occurs when you try to divide by zero. 



{:.input_area}
```python
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
<ipython-input-4-bc757c3fda29> in <module>()
----> 1 1 / 0

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```


### Name Error

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
<ipython-input-6-4acade15292f> in <module>()
      1 # If you typo a name, you will get a NameError
----> 2 varaible

```

{:.output_traceback_line}
```
NameError: name 'varaible' is not defined
```




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
<ipython-input-7-4f05423dede6> in <module>()
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
<ipython-input-8-2c2a83518cf2> in <module>()
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
<ipython-input-9-84a1c00e4833> in <module>()
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
<ipython-input-10-1c6b28888bbe> in <module>()
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
<ipython-input-11-f00634ed638b> in <module>()
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
<ipython-input-12-57c293ee5895> in <module>()
----> 1 'a_string' + 12

```

{:.output_traceback_line}
```
TypeError: must be str, not int
```


### Clicker Question #2

How are we feeling about Python. 

- a) Makes total sense.
- b) Getting there.
- c) A little fuzzy.
- d) Nope, no idea. 

## Stack Trace



{:.input_area}
```python
running_sum = 0
my_list = [1, 2, 3, 4, 5]

for val in my_list:
    
    if val % 2 == 0:
        temp = val / (val - 4)
        running_sum += temp
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
<ipython-input-13-08385b303fa2> in <module>()
      5 
      6     if val % 2 == 0:
----> 7         temp = val / (val - 4)
      8         running_sum += temp

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
```


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
    pass
except:
    # If there is an error, keep going and do this instead
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
Please type a number: 12

my_num is:  12

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
Numberdskg
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
Please enter a number: sg
Oops!  That was no valid number. Try again!
Please enter a number: 12

my_num is:  12

```

### More Try / Except



{:.input_area}
```python
def divide(num1, num2):
    return num1 / num2

def safe_divide(num1, num2):
    
    try:
        output = num1 / num2
    except ZeroDivisionError:
        output = None
    
    return output
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
<ipython-input-20-0cdf54a076ec> in <module>()
----> 1 print(divide(2, 0))

```

{:.output_traceback_line}
```
<ipython-input-19-2fcc9cd30b98> in divide(num1, num2)
      1 def divide(num1, num2):
----> 2     return num1 / num2
      3 
      4 def safe_divide(num1, num2):
      5 

```

{:.output_traceback_line}
```
ZeroDivisionError: division by zero
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



{:.input_area}
```python
my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int)
```


{:.output_stream}
```
An integer please: as

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
<ipython-input-22-bc64f24647db> in <module>()
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

