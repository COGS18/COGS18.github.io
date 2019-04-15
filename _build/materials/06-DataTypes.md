---
interact_link: content/materials/06-DataTypes.ipynb
download_link: assets/downloads/06-DataTypes.ipynb.zip
pdf_link: assets/pdf/06-DataTypes.pdf
layout: materials
title: '06-DataTypes'
prev_page:
  url: /materials/05-Conditionals
  title: '05-Conditionals'
next_page:
  url: /labs/CL1-ProgrammingI
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Course Announcements
- A1 due tonight by 11:59 PM
- Myles' Office Hours: Mondays 5-6 PM (Sun God Lounge)
- A2 due next Monday

# Review Time

### Review Clicker #1

What is the kernel?

- A) a list of the variables stored in Python memory
- B) where your code runs; your Jupyter notebook is connected to the kernel
- C) an object that returns a Boolean
- D) a way to specify that you are using math variables and not programming variables

### Review Clicker #2

What is the output of `my_var` after this code runs?



{:.input_area}
```python
my_var = 18

my_var = my_var + 2
print(my_var)
```


{:.output_stream}
```
20

```

- A) This code will not run
- B) 18
- C) 20
- D) 'my_var'

### Review Clicker #3

What type of variable is `var_a`?



{:.input_area}
```python
var_a = -15.8
```


- A) String
- B) Int
- C) Float
- D) Boolean
- E) None

### Review Clicker #4

What would be the output of running the following code?



{:.input_area}
```python
condition = 5 < 7

if condition: 
    print('SO GOOD!')
else:
    print('NOT SO GOOD.')
```


{:.output_stream}
```
SO GOOD!

```

- A) SO GOOD!
- B) NOT SO GOOD.
- C) True
- D) False
- E) SyntaxError

# Collections

- Lists
    - Indexing
    - Mutating
- Tuples

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



### Clicker Question #1

Which of the following specifies a list of 4 items?



{:.input_area}
```python
item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]
```


- A) item_A
- B) item_B
- C) item_C
- D) item_D
- E) item_E

### Indexing

<div class="alert alert-success">
Indexing refers to selecting an item from within a collection. Indexing is done with square brackets.
</div>



{:.input_area}
```python
# Define a list 
my_lst = ['Julian', 'Amal', 'Richard', 'Juan', 'Xuan']
```




{:.input_area}
```python
# Indexing: Count forward, starting at 0, with positive numbers
print(my_lst[1])
```


{:.output_stream}
```
Amal

```



{:.input_area}
```python
# Indexing: Count backward, starting at -1, with negative numbers
print(my_lst[-1])
```


{:.output_stream}
```
Xuan

```



{:.input_area}
```python
# Indexing: Grab a group of adjacent items using `start:stop`, called a slice
print(my_lst[2:4])
```


{:.output_stream}
```
['Richard', 'Juan']

```



{:.input_area}
```python
# indexing to end of list
print(my_lst[2:])
```


{:.output_stream}
```
['Richard', 'Juan', 'Xuan']

```



{:.input_area}
```python
# Indexing from beginning of list
print(my_lst[:4])
```


{:.output_stream}
```
['Julian', 'Amal', 'Richard', 'Juan']

```



{:.input_area}
```python
# slicing by skipping a value
print(my_lst[0:4:2])
```


{:.output_stream}
```
['Julian', 'Richard']

```

### Index Practices



{:.input_area}
```python
# Define a list for the examples
example_lst = [1, 2, 3, 4, 5]
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
example_lst[-3]
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



### Clicker Question #2

What will be the output of the following piece of code:



{:.input_area}
```python
q2_lst = ['a', 'b', 'c','d']
q2_lst[-3:-1]
```





{:.output_data_text}
```
['b', 'c']
```



- A) ['a', 'b', 'c']
- B) ['c', 'b', 'a']
- C) ['c', 'b']
- D) ['b', 'c', 'd']
- E) ['b', 'c']

### Clicker Question #3

What would be the appropriate line of code to return `['butter', '&', 'jelly']`?



{:.input_area}
```python
q3_lst = ['peanut', 'butter', '&','jelly']
```


- A) `q3_lst[2:4]`
- B) `q3_lst[1:3]`
- C) `q3_lst[:-2]`
- D) `q3_lst[-3:]`
- E) `q3_lst[1:4:2]`

### Reminders

- Python is zero-based (The first index is '0')
- Negative indices index backwards through a collection
- A sequence of indices (called a slice) can be accessed using start:stop
    - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself

### SideNote: But why is it like this...

<div class="alert alert-success">
Starting at zero is a convention (some) languages use that comes from how variables are stored in memory
, and 'pointers' to those locations.
</div>

### Length of a collection



{:.input_area}
```python
# Define a new list
another_lst = ['Peter', 'Hind', 'Jack', 'Pam', 'Barbara', 'Colin', 'Felix']

# Get the length of the list, and print it out
len(another_lst)
```





{:.output_data_text}
```
7
```



## The `in` Operator

<div class="alert alert-success">
The `in` operator asks whether an element is present inside a collection, and returns a boolean answer. 
</div>



{:.input_area}
```python
# Define a new list to work with
lst_again = [True, 13, None, 'apples']
```




{:.input_area}
```python
# Check if a particular element is present in the list
True in lst_again
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# The `in` operator can also be combined with the `not` operator
'19' not in lst_again
```





{:.output_data_text}
```
True
```



### Practice with `in`



{:.input_area}
```python
# Define a list to practice with
practice_lst = [1, True, 'alpha', 13, 'cogs18']
```




{:.input_area}
```python
13 in practice_lst
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
False in practice_lst
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
'True' in practice_lst
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
'cogs18' not in practice_lst
```





{:.output_data_text}
```
False
```



### Clicker #4

After executing the following code, what will be the value of `output`?



{:.input_area}
```python
ex2_lst = [0, False, 'ten', None]

bool_1 = False in ex2_lst
bool_2 = 10 not in ex2_lst

output = bool_1 and bool_2

print(output)
```


{:.output_stream}
```
True

```

- a) True
- b) False
- c) This code will fail
- d) I don't know

### Reminder

- The `in` operator checks whether an element is present in a collection, and can be negated with `not`

## Mutating a List

<div class="alert alert-success">
Lists are mutable, meaning after definition, you can update and change things about the list.
</div>



{:.input_area}
```python
# Define a list
updates = [1, 2, 3]
```




{:.input_area}
```python
# Check the contents of the list
print(updates)
```


{:.output_stream}
```
[1, 2, 3]

```



{:.input_area}
```python
# Redefine a particular element of the list
updates[1] = 0
```




{:.input_area}
```python
# Check the contents of the list
print(updates)
```


{:.output_stream}
```
[1, 0, 3]

```

### Clicker Question #5

What would the following code accommplish?



{:.input_area}
```python
lst_update = [1,2,3,0,5]
lst_update[3] = 4 
```


- A) replace 5 with 4 in `lst_update`
- B) replace 4 with 5 in `lst_update`
- C) no change to `lst_update`
- D) produce an error
- E) I'm not sure

## Collections: Tuples

<div class="alert alert-success">
A tuple is an <b>immutable</b> collection of ordered items, that can be of mixed type. Tuples are created using parentheses.
</div>

### Tuple Examples



{:.input_area}
```python
# Define a tuple
tup = (2, 'b', False)
```




{:.input_area}
```python
# Print out the contents of a tuple
print(tup)
```


{:.output_stream}
```
(2, 'b', False)

```



{:.input_area}
```python
# Check the type of a tuple
type(tup)
```





{:.output_data_text}
```
tuple
```





{:.input_area}
```python
# Index into a tuple
tup[0]
```





{:.output_data_text}
```
2
```





{:.input_area}
```python
# Get the length of a tuple
len(tup)
```





{:.output_data_text}
```
3
```



### Tuples are Immutable



{:.input_area}
```python
# Tuples are immutable - meaning after they defined, you can't change them
# This code will produce an error.
tup[2] = 1
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
<ipython-input-44-f3cf3fcad4b2> in <module>()
      1 # Tuples are immutable - meaning after they defined, you can't change them
----> 2 tup[2] = 1

```

{:.output_traceback_line}
```
TypeError: 'tuple' object does not support item assignment
```


### Clicker Question #6

Which of the following specifies a tuple of 4 items?



{:.input_area}
```python
item_A = [0, 'string', 18]
item_B = (0, 'string', 18, 'name')
item_C = [0, 'string', 18, 'name']
item_D = (0, 'string', 18)
item_E = [1234]
```


- A) item_A
- B) item_B
- C) item_C
- D) item_D
- E) item_E

## Strings as Collections

<div class="alert alert-success">
Strings act similarly to ordered collections of homogenous elements - specifically characters. But, they are <b>immutable</b>.
</div>



{:.input_area}
```python
# Define a string
my_str = 'TheFamousFive'
```




{:.input_area}
```python
# Index into a string
my_str[2]
```





{:.output_data_text}
```
'e'
```





{:.input_area}
```python
# Ask if an item is in a string
'Fam' in my_str
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Check the length of a string
len(my_str)
```





{:.output_data_text}
```
13
```





{:.input_area}
```python
# Index into a string
# This code will produce an error
my_str[1:3] = 'HE'
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
<ipython-input-79-9139cc40aa38> in <module>()
      1 # Index into a string
      2 # This code will produce an error
----> 3 my_str[1:3] = 'HE'

```

{:.output_traceback_line}
```
TypeError: 'str' object does not support item assignment
```


### SideNote: using counters



{:.input_area}
```python
# Initialize a counter variable
counter = 0 
print(counter)
```


{:.output_stream}
```
0

```



{:.input_area}
```python
counter = counter + 1
print(counter)
```


{:.output_stream}
```
1

```



{:.input_area}
```python
counter = counter + 1
print(counter)
```


{:.output_stream}
```
2

```

## Pulling it Together: Collections, Membership & Conditionals

### Clicker Question #7

What will be the value of `counter` after this code is run?



{:.input_area}
```python
things_that_are_good = ['python', 'data', 'science', 'tacos']

counter = 0

if 'python' in things_that_are_good:
    counter = counter + 1

if len(things_that_are_good) == 4:
    counter = counter + 1
    
if things_that_are_good[2] == 'data':
    counter = counter + 1 
    
print(counter)
```


{:.output_stream}
```
2

```

<pre> A) 0   B) 1   D) 2   D) 3   E) 4 </pre>

### Clicker Question #8

What will be printed out from running this code?



{:.input_area}
```python
lst = ['a', 'b', 'c']
tup = ('b', 'c', 'd')

if lst[-1] == tup[-1]:
    print('EndMatch')
elif tup[1] in lst:
    print('Overlap')
elif len(lst) == tup:
    print('Length')
else:
    print('None')
```


{:.output_stream}
```
Overlap

```

<pre> A) EndMatch   B) Overlap   C) Length   D) Overlap & Match   E) None </pre>

# Control Flow - Loops

- `while`
- `for`

## Loops

<div class="alert alert-success">
A loop is a procedure to repeat a piece of code.
</div>

## While Loops

<div class="alert alert-success">
A while loop is a procedure to repeat a piece of code while some condition is still met. 
</div>

## While Loops

While loops always have the structure

```
while condition:
    # Loop contents
```

While condition is true, execute the code contents. 

Repeat until condition is no longer True. 

### While Loops



{:.input_area}
```python
number = 5
while number < 0:
    print(number)
    number = number + 1
```


### While Loop Example I



{:.input_area}
```python
connected = False

while not connected:
    
    # Try and establish connection (placeholder code)
    print('Establishing Connection...')
    
    break
```


{:.output_stream}
```
Establishing Connection...

```

### While Loop Example II



{:.input_area}
```python
has_user_input = False

while not has_user_input:
    
    # Ask for user input (placeholder code)
    print('Asking for user input...')
    
    break
```


{:.output_stream}
```
Asking for user input...

```

## Clicker Question #9

What will be the value of `counter` after this loop is run:



{:.input_area}
```python
keep_looping = True
counter = 0

while keep_looping:

    counter = counter + 1
    
    if counter > 3:
        keep_looping = False

print(counter)
```


{:.output_stream}
```
4

```

<pre> A) 0 | B) 2 | C) 3 | D) 4 | E) Infinite </pre> 

### Stepping Through the Loop



{:.input_area}
```python
keep_looping = True
counter = 0

while keep_looping:
    print('START LOOP')
    print('\tStart counter: ', counter)

    counter = counter + 1
    
    print('\tMid counter: ', counter)
    
    if counter > 3:
        keep_looping = False
        
    print('\tEnd counter: ', counter)

print('\nFinal counter: ', counter)
```


{:.output_stream}
```
START LOOP
	Start counter:  0
	Mid counter:  1
	End counter:  1
START LOOP
	Start counter:  1
	Mid counter:  2
	End counter:  2
START LOOP
	Start counter:  2
	Mid counter:  3
	End counter:  3
START LOOP
	Start counter:  3
	Mid counter:  4
	End counter:  4

Final counter:  4

```
