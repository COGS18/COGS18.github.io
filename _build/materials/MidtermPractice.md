---
interact_link: content/materials/MidtermPractice.ipynb
download_link: assets/downloads/MidtermPractice.ipynb.zip
pdf_link: assets/pdf/MidtermPractice.pdf
layout: materials
title: 'MidtermPractice'
prev_page:
  url: /materials/Midterm-Review
  title: 'Midterm-Review'
next_page:
  url: /materials/PythonParty
  title: 'PythonParty'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Practice Questions

To practice for the midterm, read through each of these questions and try and answer the question _before_ you run the code.

Since this is a notebook, you can also then run this code to check what it does. 

Make sure you understand why each thing does what it does!

## Variables & Operators

For each of the following cells, after executing the code, what will the value of `var_a` be?



{:.input_area}
```python
# Variables-1
var_b = 2
var_a = var_b = 2%3
```




{:.input_area}
```python
# Variables-2
var_b = False 
var_c = True
var_d = True
var_a = var_b or var_c or var_d
```




{:.input_area}
```python
# Variables-3
var_b = 2**3
var_c = 2
var_a = float(var_b/var_c)
```




{:.input_area}
```python
# Variables-4
var_a = 5**2 <= 30 or 25%4 > 1
```


## Indexing

Given the following list:



{:.input_area}
```python
my_lst = ['Python', True, 12, 'Java', False, None, 23, 'C++']
```


What will each of the following code cells print out?



{:.input_area}
```python
len(my_lst)
```




{:.input_area}
```python
my_lst[1:4]
```




{:.input_area}
```python
my_lst[-3:]
```




{:.input_area}
```python
my_lst[1::2]
```




{:.input_area}
```python
my_lst[1:6:2]
```


## Conditionals

### Conditionals 1

What will the following code print out?



{:.input_area}
```python
if True and not False:
    print('Yay')
elif False or not False:
    print('Also yay')
```


### Conditionals 2

What will the following code print out?

a) 1  b) 2  c) broken d) 3 e) This code won't execute



{:.input_area}
```python
if 10%2 == 5:
    print('1')
elif True and False or False:
    print('2')
elif 5/0:
    print('broken')
else:
    print('3')
```


## Loops

### Loops 1

What will the following code print out:

A) 0 | B) 1 | C) 2 | D) 3 | E) 4



{:.input_area}
```python
counter = 0
my_lst = [True, 3, False, False]
for item in my_lst:
    if item:
        continue
    else:
        counter = counter + 1
        break
```


### Loops 2

What will the following code print out:

A) 1 4 9 16 | B) 1 2 3 4| C)9 16 25 | | D) 1 4 9



{:.input_area}
```python
my_lst = [1, 2, 3, 4, 5]

for item in my_lst[0:-2]:
    print(item**2)
```


### Loops 3

What will the following code print out:



{:.input_area}
```python
index_outer = 1
while index_outer < 4:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
```


## Functions & Algorithms

### Functions 1

What will the following code print: 

A) ‘abcde’	B) ‘zzcde’	C) ‘zzzzz’	D) ‘zz’	E) ‘’



{:.input_area}
```python
def string_manipulator(string):
    
    output = ''
    for char in string:
        if char is 'a' or char is 'b':
            char = 'z'
            output = output + char
    return output

variable = 'abcde'
manipulated_string = string_manipulator(variable)
print(manipulated_string)
```


### Functions 2

What will the following piece of code print out?



{:.input_area}
```python
def manipulate_three(num1, num2, num3):

    answer = num1**num2%num3

    return answer

manipulate_three(3, 2, 5)
```


### Functions 3

What will the following piece of code print out?

A) 0 | B) 1 | C) 2 | D) 3 | E) 4



{:.input_area}
```python
def count_bool(list_of_bools):
    
    counter = 0
    
    for it in list_of_bools:
    
        if isinstance(it, bool):
            counter = counter + 1
    
    return counter

count_bool([True, 3, None, False, False])
```


## Errors

For each of the following, answer:
    - What kind of error will the following code raise? 
    - How would you fix it?

### Errors 1

A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 



{:.input_area}
```python
my_string = "My favourite number is " + 27
```


### Errors 2

A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 



{:.input_area}
```python
print('My favorite number is' + str(3+5)
```


### Errors 3

A) Syntax Error| B) Type Error | C) Name Error | D) Code will work 



{:.input_area}
```python
my_list = [1, 3, max]
```


## More Errors

Each of the code blocks below have something wrong with them. 

Name the type of error that will result when python tries to execute each example. 

When you've identified the error, figure out how you would fix this could to run properly.



{:.input_area}
```python
print'5 plus six')
```




{:.input_area}
```python
int('six')
```




{:.input_area}
```python
100/0
```




{:.input_area}
```python
my_list = [4,5,2]
print(my_list[3])
```




{:.input_area}
```python
my_dict = {'this':100, 'that':200}
my_dict['there']
```


## Objects

### Objects 1

Given the following object:

- Identify which parts are a class attribute, an instance attribute, and class method. 



{:.input_area}
```python
class Tom():
    
    current_job = 'instructor'
    
    def __init__(self, current_project):
        self.current_project = current_project
    
    def do_new_thing(self, new_thing):
        self.current_project = new_thing
        print("I have a new project now!")
        
    def print_project(self):
        print("My current project is: ", self.current_project)        
```


Using the object from above, what will each of the following code cells (executed in order) do / print out?



{:.input_area}
```python
tom = Tom('Teaching')
```




{:.input_area}
```python
tom.print_project()
```




{:.input_area}
```python
tom.do_new_thing('Research')
```




{:.input_area}
```python
tom.print_project()
```


### Combining Things: Flow Control with Booleans

We're going to define a few functions that return booleans. 



{:.input_area}
```python
def foo1():
    return True

def foo2():
    return False

def foo3(val):
    result = val > 10
    return result
```


For each of the following cells, given the function above, what will they print out?



{:.input_area}
```python
result1 = (True and foo1()) or (False or foo2())
print(result1)
```




{:.input_area}
```python
result2 = (False and foo1()) or (True or foo2())
print(result2)
```




{:.input_area}
```python
result3 = (False and foo1()) or (False or foo2()) or (True and foo3(11))
print(result3)
```




{:.input_area}
```python
result4 = (False and foo1()) or (False or foo2()) or (True and foo3(1))
print(result4)
```

