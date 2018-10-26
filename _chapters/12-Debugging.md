---
download_link: assets/downloads/12-Debugging.ipynb.zip
pdf_link: assets/pdf/12-Debugging.pdf
title: '12-debugging'
permalink: '/chapters/12-Debugging'
previouschapter:
  url: /chapters/11-FunctionsII
  title: '11-functionsii'
nextchapter:
  url: /chapters/A1-Syntax
  title: 'A1-syntax'
redirect_from:
  - '/chapters/12-debugging'
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
    for item in input_list
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




{:.input_area}
```python
my_list = [1, 2]
for value in my_list:
print(value)
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


### Clicker Question #2

How are we feeling about Python. 

- a) Make total.
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


### Try / Except Examplem



{:.input_area}
```python
# Example: we want to get an input number from the user

my_num = input("Please type a number: ")

print('\nmy_num is: ', my_num)
```


### Example with Try / Except



{:.input_area}
```python
while True:
    try:
        my_num = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number. Try again!")
        
print('\nmy_num is: ', my_num)
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




{:.input_area}
```python
print(safe_divide(2, 0))
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




{:.input_area}
```python
my_int = input('An integer please: ')
if not my_int.isnumeric():
    raise ValueError('I wanted a number! :(')
    
print('My integer is: ', my_int)
```


## Debugging Practice



{:.input_area}
```python
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1
    if input_1[0] = 0:
        answer = 0
    
    elif len(input_2) == 2:
        answer = input_2[1] / input_1[0]
        
    elif len(input_1) == len(input_2):
        answer = input_1[0] + input_2[0]
        
    print(answer)
```




{:.input_area}
```python
my_function([0, 1], [0])
```




{:.input_area}
```python
my_function([0], [0, 1])
```




{:.input_area}
```python
my_function([1], [1])
```




{:.input_area}
```python
my_function([1], ['1'])
```

