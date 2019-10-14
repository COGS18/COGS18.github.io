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
  url: /materials/07-Loops
  title: '07-Loops'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Course Announcements
- A1 due tonight by 11:59 PM
- A2 due next Friday (11:59 PM)
- Double check office hours on syllabus

## Assignment Reminders

- To make life easier on your wonderful TAs:
    - Please don't change the assignment file name 
    - Please don't delete/modify cells in assignment (other than cells where you add code)
    - You can add cells and include `print()` statements to check your work.

- There are **hidden assert cells**
    - If you follow instructions and pass all the asserts provided, you will receive credit
    - We cannot give points back for typos

- You *must* **submit your assignment** for it to be graded.
    - best to "Kernel > Restart & Run All" before you submit
        - this executes code in your notebook from top to bottom
        - You can also use "Validate" button at top. Note that for A4 you *may* get an error b/c that notebook takes a while to run    
    - submit as many times as you like
        - most recent submission is graded
        - *but*, if you submit before deadline and again after, it will be late

- variables defined in `%%writefile` cells will overwrite variables in test (`assert`) cells

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
# can determine type in list
type(my_lst[2])
```





{:.output_data_text}
```
str
```





{:.input_area}
```python
my_lst[2:-1]
```





{:.output_data_text}
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
# slicing by skipping a value [start:stop:step]
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


- A) ['a', 'b', 'c']
- B) ['c', 'b', 'a']
- C) ['c', 'b']
- D) ['b', 'c', 'd']
- E) ['b', 'c']

Note: The following was added after class due to a student question. You are not expected to know this. Including as an FYI.

You *can* return ['c','b'] but it combines two different concepts.

1. the `start:stop` now refers to indices in the reverse.
2. `-1` is used as the step to reverse the output.

More details about `step`:  
`step`: the amount by which the index increases, defaults to 1. If it's negative, you're slicing over the iterable in reverse.



{:.input_area}
```python
# slice in reverse
q2_lst[-2:-4:-1]
```





{:.output_data_text}
```
['c', 'b']
```





{:.input_area}
```python
# you can use forward indexing
# makes this a little clearer
q2_lst[2:0:-1]
```





{:.output_data_text}
```
['c', 'b']
```



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
- A sequence of indices (called a slice) can be accessed using `start:stop`
    - In this contstruction, `start` is included then every element until `stop`, not including `stop` itself
    - To skip values in a sequence use `start:stop:step`

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
The <code>in</code> operator asks whether an element is present inside a collection, and returns a boolean answer. 
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
#searching partial strings
'cogs' in practice_lst
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
lst_update = [1, 2, 3, 0, 5]
lst_update[3] = 4 
```


- A) replace 0 with 4 in `lst_update`
- B) replace 4 with 0 in `lst_update`
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
<ipython-input-47-6b0fd3f24bc7> in <module>()
      1 # Tuples are immutable - meaning after they defined, you can't change them
      2 # This code will produce an error.
----> 3 tup[2] = 1

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

## Aside: Aliases

Note: This was introduced in the Variables lecture.



{:.input_area}
```python
# Make a variable, and an alias
a = 1
b = a
print(b)
```


{:.output_stream}
```
1

```

Here, the value 1 is assigned to the variable `a`.  

We then make an **alias** of `a` and store that in the variable `b`. 

Now, the same value (1) is stored in both `a` (the original) and `b` (the alias).

What if we change the value of the original variable (`a`) - what happens to `b`?

### Clicker #7

After executing the following code, what will the values stored in `a` and `b` be?



{:.input_area}
```python
# Make a variable & an alias
# change value of original variable
a = 1
b = a
a = 2

print(a)
print(b)
```


{:.output_stream}
```
2
1

```

- A) `a` and `b` both store 1
- B) `a` and `b` both store 2
- C) `a` stores 2 `b` stores 1
- D) `a` stores 1 `b` stores 2
- E) No clue

Reminder: integers are **immutable**.

### Alias: mutable types

What happens if we make an alias of a **mutable** variable, like a list?



{:.input_area}
```python
first_list = [1, 2, 3, 4]
alias_list = first_list
alias_list
```





{:.output_data_text}
```
[1, 2, 3, 4]
```





{:.input_area}
```python
#change second value of first_list
first_list[1] = 29
first_list
```





{:.output_data_text}
```
[1, 29, 3, 4]
```





{:.input_area}
```python
# check alias_list
alias_list
```





{:.output_data_text}
```
[1, 29, 3, 4]
```



For *mutable* type variables, when you change one, both change.

### Clicker #8

After executing the following code, what will the second value stored in `second_tuple`?



{:.input_area}
```python
# Make a variable & an alias
# change value of original variable
my_tuple = (1, 2, 3, 4)
second_tuple = my_tuple
my_tuple[1] = 29 
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
<ipython-input-55-7a44f310718f> in <module>()
      3 my_tuple = (1, 2, 3, 4)
      4 second_tuple = my_tuple
----> 5 my_tuple[1] = 29

```

{:.output_traceback_line}
```
TypeError: 'tuple' object does not support item assignment
```


- A) 1
- B) 2
- C) 29
- D) This will Error
- E) I'm lost.

### Why allow aliasing?

Aliasing can get confusing and be difficult to track, so why does Python allow it?

Well, it's more efficient to point to an alias than to make an entirely new copy of a a very large variable storing a lot of data. 

Python allows for the confusion, in favor of being more efficient.

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
<ipython-input-74-9139cc40aa38> in <module>()
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




{:.input_area}
```python
counter = counter + 1
print(counter)
```




{:.input_area}
```python
counter = counter + 1
print(counter)
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


<pre> A) 0   B) 1   C) 2   D) 3   E) 4 </pre>

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


<pre> A) EndMatch   B) Overlap   C) Length   D) Overlap & Match   E) None </pre>
