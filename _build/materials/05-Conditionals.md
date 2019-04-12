---
interact_link: content/materials/05-Conditionals.ipynb
download_link: assets/downloads/05-Conditionals.ipynb.zip
pdf_link: assets/pdf/05-Conditionals.pdf
layout: materials
title: '05-Conditionals'
prev_page:
  url: /materials/04-Operators
  title: '04-Operators'
next_page:
  url: /labs/CL1-ProgrammingI
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<center><img src="img/CSSA.png" ></center>

# Conditionals

- `if`
- `elif`
- `else`

## Understanding Boolean logic

When first learning booleans, we sometimes *think* we know what we're asking the computer to do, but our logic can be flawed.

Let's look at an example that could trip you up now.


1. Python considers empty strings as having boolean value of `False`. Non-empty string as having boolean value of `True`.




{:.input_area}
```python
empty_string = ''
bool(empty_string)
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
nonempty_string = 'string has something in it'
bool(nonempty_string)
```





{:.output_data_text}
```
True
```



2.  For `and` operator if left value is `True`, then right value is checked and returned. If left value is `False`, then that left value is returned.




{:.input_area}
```python
True and False
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
bool('a')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'a' and 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'b' and 'a'
```





{:.output_data_text}
```
'a'
```



### Clicker Question #1

What would the following code cell return?



{:.input_area}
```python
'' and 'a'
```





{:.output_data_text}
```
''
```



- A) ''
- B) 'b'
- C) `True`
- D) `False`



{:.input_area}
```python
# the left value in parentheses is True
'a' == ('b' and 'a')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# the left value in parentheses is True
'a' == ('a' and 'b')
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# the left value in parentheses is False
'a' == ('' and 'a')
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# what we actually wanted python to do
# to look at a in a and b
'a' == 'a' and 'a' == 'b' 
```





{:.output_data_text}
```
False
```



3. For `or` operator if left value is `True`, then it is returned, otherwise if left value is `False`, then right value is returned.



{:.input_area}
```python
'a' or 'b'
```





{:.output_data_text}
```
'a'
```





{:.input_area}
```python
'' or 'b'
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'' or ''
```





{:.output_data_text}
```
''
```





{:.input_area}
```python
'b' or ''
```





{:.output_data_text}
```
'b'
```





{:.input_area}
```python
'a' == ('a' or 'b')
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'b' == ('a' or 'b')
```





{:.output_data_text}
```
False
```



### Clicker Question #2

What would the following code cell return?



{:.input_area}
```python
'a' == ('' or 'a')
```





{:.output_data_text}
```
True
```



- A) ''
- B) 'a'
- C) `True`
- D) `False`

## Identity Operators

 Identity operators are used to check if two values (or variables) are located on the same part of the memory.



{:.input_area}
```python
a = 927
b = a
c = 927
```




{:.input_area}
```python
print(a is b)
print(c is a)
```


{:.output_stream}
```
True
False

```



{:.input_area}
```python
print(id(a), id(b), id(c))
```


{:.output_stream}
```
4578650352 4578650352 4578650320

```

A **new object** is created each time we have a variable that makes reference to it, but there are *few notable exceptions*:

- some strings
- Integers between -5 and 256 (inclusive)
- empty immutable containers (e.g. tuples) - we'll get to these later

While these may *seem* random, they exist for memory optimization in Python implementation. 

Shorter and less complex strings are "interned" (share the same space in memory).

The rules behind this are a bit fuzzy, so we'll just go through a few examples here. But, if you want to read more about string interning and how Python handles this, you can read more [here](http://guilload.com/python-string-interning/).



{:.input_area}
```python
simple_string = 'string'
simple_string2 = 'string'
```




{:.input_area}
```python
simple_string is simple_string2
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
print(id(simple_string), id(simple_string2))
```


{:.output_stream}
```
4537041168 4537041168

```



{:.input_area}
```python
longer_string = 'really long string that just keeps going'
longer_string2 = 'really long string that just keeps going'
```




{:.input_area}
```python
longer_string is longer_string2
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
print(id(longer_string), id(longer_string2))
```


{:.output_stream}
```
4579331792 4579331696

```

Python implementation front loads an array of integers between -5 to 256, so these objects *already exist*.



{:.input_area}
```python
d = 5
e = 5
```




{:.input_area}
```python
print(id(d), id(e))
```


{:.output_stream}
```
4534097456 4534097456

```



{:.input_area}
```python
print(d is e)
```


{:.output_stream}
```
True

```



{:.input_area}
```python
# Python doesn't create a new object here
j = 5
k = 5
l = 'Hello'
m = 'Hello'

true_variable_integer = j is k
true_variable_string = l is m

print(true_variable_integer, true_variable_string)
```


{:.output_stream}
```
True True
False False

```



{:.input_area}
```python
# Python DOES create a new object here
n = 975 #greater than 256
o = 975
p = 'Hello!' #that exclamation point makes it more complex
q = 'Hello!'

false_variable_integer = n is o
false_variable_string = p is q

print(false_variable_integer, false_variable_string)
```


### Clicker #3


Using the variables provded below and identity operators replace `---` with code such that `true_variable` will return `True` and `false_variable` will return `False`. 

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
a = 5
b = 5
c = b
d = 'Hello!'
e = 'Hello!'
f = 567
g = 567

# EDIT CODE HERE
true_variable = ---
false_variable = ---

print(true_variable, false_variable)
```


{:.output_stream}
```
True False

```

# Conditionals

- `if`
- `elif`
- `else`

## Conditionals: if

<div class="alert alert-success">
Conditionals are statements that check for a condition, using the `if` statement, and then only execute a set of code if the condition evaluates as `True`.
</div>



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
```


{:.output_stream}
```
This code executes if the condition evaluates as True.

```

### Clicker Question #4

Replace `---` below with something that will print 'True'

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
math = ---

if math:
    print('True')
```


## Conditional: else

<div class="alert alert-success">
After an `if`, you can use an `else` that will run if the conditional(s) above have not run.
</div>



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')
```


{:.output_stream}
```
This code executes if the condition evaluates as True.

```

### Clicker Question #5

Replace `---` below with something that will print 'False'.

- A) I did it!
- B) I tried but am stuck.
- C) I'm unsure where to start



{:.input_area}
```python
my_value = ---

if my_value:
    print('True')
else: 
    print('False')
```


## Conditional: elif

<div class="alert alert-success">
After an if statement, you can have any number of `elif`'s (meaning 'else if') to check other conditions.
</div>



{:.input_area}
```python
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
```


{:.output_stream}
```
This code executes if both condition_1 and condition_2 evaluate as False

```

### `elif` without an `else`

An else statement is not required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.



{:.input_area}
```python
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
```


### `elif` *after* an `else` does not make sense

The order will alwas be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an erro).



{:.input_area}
```python
## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
```



{:.output_traceback_line}
```
  File "<ipython-input-55-c94763108fe2>", line 8
    elif condition_2:
       ^
SyntaxError: invalid syntax

```


## Conditionals With Value Comparisons

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>



{:.input_area}
```python
language = "Python"

if language == "Python":
    print("Yay!")
elif language == "Perl":
    print("Oh no.")
else:
    print("Get yourself a programming language!")
```


{:.output_stream}
```
Get yourself a programming language!

```



{:.input_area}
```python
# Exploring conditionals
number = 5

print('Before Conditional')
 
if number < 5:
    print('    if statement execution')
elif number > 5:
    print('    elif statement execution')

print('After Conditional')
```


{:.output_stream}
```
Before Conditional
After Conditional

```

### Clicker Question #6

What will the following code snippet print out:



{:.input_area}
```python
if False:
    print("John")
elif True:
    print("Paul")
elif True:
    print("George")
else:
    print("Ringo")
```


{:.output_stream}
```
Paul

```

- A) John 
- B) Paul, George, Ringo 
- C) Paul 
- D) Paul, George 
- E) Ringo

### Clicker Question #7

What will the following code snippet print out:



{:.input_area}
```python
if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")
```


{:.output_stream}
```
I did Math

```

- A) I did Math 
- B) I broke Math
- C) I didn't do math
- D) This code won't execute

### Clicker Question #8

What will the following code snippet print out:



{:.input_area}
```python
conditional = True
python = "great"

if conditional:
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")
```


{:.output_stream}
```
Yay Python!

```

- A) Yay Python!
- B) Oh no.
- C) I'm here.
- D) This code won't execute

## Properties of conditionals

- All conditionals start with an `if`, can have an optional and variable number of `elif`'s and an optional `else` statement
- Conditionals can take any expression that can be evaluated as `True` or `False`. 
- At most one component (`if` / `elif` / `else`) of a conditional will run
- The order of conditional blocks is always `if` then `elif`(s) then `else`
- Code is only ever executed if the condition is met

# Collections

## Collections: Lists

<div class="alert alert-success">
A list is a mutable collection of ordered items, that can be of mixed type. Lists are created using square brackets.
</div>

### List examples



{:.input_area}
```python
# Define a list
lst = [1, 'a', True]
```




{:.input_area}
```python
# Print out the contents of a list
print(lst)
```


{:.output_stream}
```
[1, 'a', True]

```



{:.input_area}
```python
# Check the type of a list
type(lst)
```





{:.output_data_text}
```
list
```



### Indexing

<div class="alert alert-success">
Indexing refers to selecting an item from within a collection. Indexing is done with square brackets.
</div>



{:.input_area}
```python
# Indexing: Count forward, starting at 0, with positive numbers
print(my_lst[2])# Define a list 
my_lst = ['Julian', 'Anne', 'Richard', 'George', 'Timmy']
```




{:.input_area}
```python
# Indexing: Count forward, starting at 0, with positive numbers
print(my_lst[2])
```





{:.output_data_text}
```
'Richard'
```





{:.input_area}
```python
# Indexing: Count backward, starting at -1, with negative numbers
print(my_lst[-1])
```


{:.output_stream}
```
Timmy

```



{:.input_area}
```python
# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(my_lst[2:4])
```


{:.output_stream}
```
['Richard', 'George']

```

### Index Practices



{:.input_area}
```python
# Define a list for the examples
example_lst = [1, 2, 3, 4, 5]
```




{:.input_area}
```python
example_lst[-3]
```





{:.output_data_text}
```
3
```





{:.input_area}
```python
example_lst[2]
```





{:.output_data_text}
```
3
```





{:.input_area}
```python
example_lst[1:3]
```





{:.output_data_text}
```
[2, 3]
```



### Clicker Question #9

What will be the output of the following piece of code:



{:.input_area}
```python
q1_lst = ['a', 'b', 'c','d']
q1_lst[-3:-1]
```





{:.output_data_text}
```
['b', 'c']
```



- a) 'a', 'b', 'c'
- b) 'c', 'b', 'a'
- c) 'c', 'b'
- d) 'b', 'c', 'd'
- e) 'b', 'c'

### Reminders

- Negative indices index backwards through a collection
- A sequence of indices (called a slice) can be accessed using start:stop
    - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
