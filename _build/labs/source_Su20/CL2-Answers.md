---
interact_link: content/labs/source_Su20/CL2-Answers.ipynb
download_link: assets/downloads/CL2-Answers.ipynb.zip
title: 'CL2-Answers'
prev_page:
  url: /labs/source_Su20/CL1-Tooling
  title: 'CL1-Tooling'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Coding Lab 2: Programming I - Answers


Welcome to the second coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each fill out your own notebook, if you prefer. 

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 

If you have a question about how something works / what something does - try it out, and see what happens! If you can't figure it out, reach out to your instructional staff - we're here to help!

**Reminder**: You may *not* be able to complete all of this in 2 hours, particularly the "challenges."  These are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for these!

## Part 1: Variables

Variables are used in Python to store values. 

### Defining Variables

Declare a int, float, string, and boolean. Fill them with with any values you want. 

Call them `my_int`, `my_float`, `my_string` and `my_boolean`. 



{:.input_area}
```python
## YOUR CODE HERE
my_int = 12
my_float = 56.3
my_string = 'hello'
my_boolean = True
```


Use the following cells to check the types of the variables you write are as expected



{:.input_area}
```python
type(my_int)
```





{:.output_data_text}
```
int
```





{:.input_area}
```python
type(my_float)
```





{:.output_data_text}
```
float
```





{:.input_area}
```python
type(my_string)
```





{:.output_data_text}
```
str
```





{:.input_area}
```python
type(my_boolean)
```





{:.output_data_text}
```
bool
```



## Part 2: Operators & Comparisons

Operators are used in Python to do things with variables. 

### Operator Questions

First - explore using Python operators. Make sure you can add and subtract numbers, concatenate strings, do boolean comparisons, etc.



{:.input_area}
```python
## Do some exploring!

# Add & subtract numbers
print(1 + 2)
print(2 - 2)

# Concatenate string
print('ab' + 'cd')

# Boolean comparisons
print(True and True)
print(False or True)
```


{:.output_stream}
```
3
0
abcd
True
True

```

Once you have explored using operators, try to answer some quesions using them. 

Let's start with an example: is the multiplication of 13 and 15 greater than 200?



{:.input_area}
```python
13 * 15 > 200
```





{:.output_data_text}
```
False
```



Similar to that example, try to answer the following questions using Python variables & comparisons:
- Is the remainder of dividing 323 by 13 greater than 6?
- Is 7 to the power of 3 greater than or equal to 300?
- Is 49 squared greater than 2500 or (boolean comparison) is 14 to the power of 3 greater than 2500
- Is 49 modulus 9 equal to 67 modulus 9 and (boolean comparison) is the sum 49 & 67 modulus 9 greater than 7



{:.input_area}
```python
## YOUR CODE HERE
```




{:.input_area}
```python
323 % 13 > 6
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
7 **3 >= 300
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
49**2 > 2500 or 14**3 > 2500
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
49%9 == 67%9 and (49 + 67) % 9 > 7
```





{:.output_data_text}
```
True
```



### Operator Challenges

The following are more challenging operator related questions. If they seem too tricky for now, just skip ahead to the next section.

Some more comparisons, with variable assignment:
- Set the variable `comp_1` to the result of whether 17 squared is not the same as 867 divided by 3
- Set the variable `comp_2` to the result of whether 4^3 is less than 3^4 **and** also greater than the remainder of dividing 1234 by 99

Bonus: both of the above questions can be written in (at least) two ways. 

If you found an answer to them, see if you can update the construction, changing at least one operator, to answer the question in a different way. 

Note: x^y indicates 'x to the power of y'



{:.input_area}
```python
## YOUR CODE HERE
comp_1 = not 17**2 == 289/3
comp_1 = 17**2 != 289/3

comp_2 = (3**4) > (4**3) > (1234 % 99)
comp_2 = ((3**4) > (4**3)) and ((4**3)) > (1234 % 99)
```


### Operator Explorations.

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- If you divide a float by an int, what is the type of the outcome? What about dividing an int by a float?
- What happens if you multiply a string with a number?
- The `+` sign works if you for adding numbers and for concatenating strings. Can you use `+` with a number and string in the same operation?
- Since you can use `+` and `*` with strings, what happens if you try to substract two strings using `-`?



{:.input_area}
```python
## EXPLORATION CODE HERE
```




{:.input_area}
```python
print(type(12.0/2))
print(type(12/2.0))

# Dividing with a float and an int, in either order, returns a float
```


{:.output_stream}
```
<class 'float'>
<class 'float'>

```



{:.input_area}
```python
'hodor ' * 8

# Multiplying a string by a number repeats that string number times
```





{:.output_data_text}
```
'hodor hodor hodor hodor hodor hodor hodor hodor '
```





{:.input_area}
```python
12 + 'str'

# No, this code fails. You cannot use '+' with a number and a string
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
<ipython-input-17-0810b46a83be> in <module>()
----> 1 12 + 'str'
      2 
      3 # No, this code fails. You cannot use '+' with a number and a string

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```




{:.input_area}
```python
'abc' - 'a' 

# No, this code fails. You cannot use '-' with strings
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
<ipython-input-18-9a45216ae503> in <module>()
----> 1 'abc' - 'a'
      2 
      3 # No, this code fails. You cannot use '-' with strings

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```


## Part 3: Asserts

You will notice, through the coding labs and assignments, code that looks somehing like `assert True`, in which the assert statement is used.

Using assert basically says to `assert that the following code is True`.

Or, slightly more formally `assert that the following code evaluates as True`.

If the asserted code does not evaluate as True, it raises an error - meaning it interrupts the code execution because something went wrong.

This can be used as a way to test that code does what you expect it to do - and is therefore part of how we will text your code programmatically. 

Because the use of `assert` will be common in course materials, let's take a moment to explore how it works and what happens when we use it.



{:.input_area}
```python
# Declare a variable called `boolean` that  has type boolean, and passes the assert in the next cell

## YOUR CODE HERE
boolean = True
```




{:.input_area}
```python
# Check that there is variable called `boolean` that is a boolean
assert type(boolean) == bool
```




{:.input_area}
```python
# Check that the variable called `boolean` passes the assert
assert boolean
```




{:.input_area}
```python
boolean
```





{:.output_data_text}
```
True
```



###  Assert Explorations

Now, explore using assert. What happens if you assert an integer, or a string? 

What happens if you assert None?

Find at least one integer that raises an assertion error. 



{:.input_area}
```python
assert 12

# Asserting an integer asserts as True
```




{:.input_area}
```python
assert 'hello'

# Asserting a string asserts as True
```




{:.input_area}
```python
assert None

# Asserting None asserts as False
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
<ipython-input-25-98092c377a2c> in <module>()
----> 1 assert None
      2 
      3 # Asserting None asserts as False

```

{:.output_traceback_line}
```
AssertionError: 
```




{:.input_area}
```python
assert 0

# The integer 0 asserts as False (it gets interpreted as False)
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
<ipython-input-26-86e0797498a7> in <module>()
----> 1 assert 0
      2 
      3 # The integer 0 asserts as False (it gets interpreted as False)

```

{:.output_traceback_line}
```
AssertionError: 
```


## Part 4: Collection types

Collections are Python variable types than can store a 'collection' of items.

### Collection Questions

Create a list and a tuple. Fill them with with any values you want. 

Call them `my_list` and `my_tuple`.



{:.input_area}
```python
## YOUR CODE HERE
my_list = [1, 2, 3]
my_tuple = ('a', 'b', 'c')
```


Use the following cells to check the types of the variables you write are as expected



{:.input_area}
```python
type(my_list)
```





{:.output_data_text}
```
list
```





{:.input_area}
```python
type(my_tuple)
```





{:.output_data_text}
```
tuple
```



#### Declaring Collections

Note that there can be more than one way to declare collections. 

As well as declaring them with '[]' and '()', we can use the list & tuple constructors, as shown below. 



{:.input_area}
```python
# Run me! - This creates another list & tuple, using the list & tuple constructors
some_list = list([1, 2, 3, 4, 5])
some_tuple = tuple(["peanut", "butter", "and", "jelly"])

print("'some_list' contains: \t", some_list)
print("'some_tuple' contains: \t", some_tuple)
```


{:.output_stream}
```
'some_list' contains: 	 [1, 2, 3, 4, 5]
'some_tuple' contains: 	 ('peanut', 'butter', 'and', 'jelly')

```

Compare the types of these variables to your equivalent variables to confirm.

In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 



{:.input_area}
```python
# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert isinstance(some_list, list)
assert isinstance(some_tuple, tuple)
```




{:.input_area}
```python
# ANSWER
assert isinstance(some_list, list)
assert isinstance(some_tuple, tuple)
```


### Indexing

Given the following list, do the following operations:
- Get the length of the list (assign this to a variable `lst_len`)
- Get the 1st element of the list (call the selection `ind1`)
- Get the last element of the list (call the selection `ind2`)
- Get the second to the fourth element of the list (call the selection `ind3`)
- Get from the fifth element, to the end of the list (call the selection `ind4`)
- Get every second element of the list, starting at the first element (call the selection `ind5`)
- Get every second element of the list, starting at the second element (call the selection `ind6`)



{:.input_area}
```python
my_lst = ['a', True, 12, 'tomato', False, None, 23, 'python', [], 5.5]
```




{:.input_area}
```python
# YOUR CODE HERE
lst_len = len(my_lst)
ind1 = my_lst[0]
ind2 = my_lst[-1]
ind3 = my_lst[1:5]
ind4 = my_lst[4:]
ind5 = my_lst[0::2]
ind6 = my_lst[1::2]
```


## Part 5: Conditionals

Conditionals a form of control flow for executing certain code if a specific condition is met. 

### Conditional Questions

In this part, we will re-visit some questions about conditionals, and start combining them together with collections. 

Make sure you can use if/elif/else statements to control which code blocks are run.

#### Controlling Output With Conditionals I

Using the code below, keep updating the variable value to make sure you can make the conditional return each of the possibilities. 



{:.input_area}
```python
# ToDo: Update value to control what gets executed
value = 10

# This code provided
if isinstance(value, int):
    if value < 10:
        result = 'small value'
    if value >= 10:
        result = 'big value'
else:
    result = 'false value'
```




{:.input_area}
```python
print(result)
```


{:.output_stream}
```
big value

```

#### Controlling Output With Conditionals II

In the cell below, first write something into each result assignment related to  for example, it could be "B1 is False & B2 is True"). 

Then make sure you can change values of b1 & b2 to make the program execute each option. 



{:.input_area}
```python
# ToDo: Update b1 & b2 to control what gets executed
b1 = False
b2 = False

# Next, try this out
if b1 and not b2:
    result = ''
elif not b1 and b2:
    result = ''
elif b1 and b2:
    result = ''
else:
    result = ''
```




{:.input_area}
```python
print(result)
```


{:.output_stream}
```


```

### Conditional Challenges

The following are more challenging questions relating to conditional statements. If they seem too tricky for now, just skip ahead to the next section.

#### Conditional Challenge #1

Write a conditional that prints "Found it" if a given `val_2` is a multiple of 10, otherwise prints "Nope."



{:.input_area}
```python
## YOUR CODE HERE

# Set a test value for `val_2`
val_2 = 100

if val_2 % 10 == 0:
    print('Found it')
else:
    print('Nope')
```


{:.output_stream}
```
Found it

```

#### Conditional Challenge #2

Input: assumes a variable `val_1`, that can be either a string or an integer

Output: based on the conditions, this code block will assign a variable called `output` to be a boolean

Use conditions to check whether `val_1` is a string or an integer object:
- If it is a string, check whether it's length is greater then 8
    - If so, set the value `output` to True
- If it is an integer, compare whether it is less than 100
    - If so, set the value `output` to True
- Else, set output to False



{:.input_area}
```python
## YOUR CODE HERE

# Set a test value for `val_1`
val_1 = 'string'

if isinstance(val_1, str):
    output = True
elif isinstance(val_1, int):
    output = True
else:
    output = False

# Check the output
print(output)
```


{:.output_stream}
```
True

```

### Operator Explorations

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- Can you include multiple conditions in an if statement?
    - If think so, write an if statement that tests multiple conditions.
- What happens if you put an if statement inside an if statement? When would such a statement run?
    - To explore this, write an if statement that has an embedded if statement in it. 




{:.input_area}
```python
v1 = True
v2 = False

if v1 == True and v2 == False:
    print('YES!')

# Yes, you can include multiple conditions in an if statement
```


{:.output_stream}
```
YES!

```



{:.input_area}
```python
if v1 == True:
    if v2 == False:
        print('Also YES!')
        
# Yes, you can have an if statement within an if statement
#   The embedded if will end up running if both conditions of both if's are True
```


{:.output_stream}
```
Also YES!

```

## Part 6: Loops

We will now explore two ways to iterate over data in Python - `for` and `while` loops. 

Each type of loop performs its respective code block until certain conditions are met. Here, we will explore what those conditions are. 

Note: "iterate" means to perform an action repeatedly 

Note: Sometimes, we accidentally make loops that never end. 
- If that happens, "break" the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

#### Loops Q1

First, declare a variable called `counter` that has type int and value zero.

Then write a while loop that runs 10 times and use 'counter' to track how many times the loop runs. 



{:.input_area}
```python
## YOUR CODE HERE
counter = 0
while counter < 10:
    counter = counter + 1
```




{:.input_area}
```python
# Check that (after the loop runs) that there is a variable called `counter` that has value 10
assert counter == 10
```


#### Infinite Loops

The while loop below will run indefinitely unless someone puts a stop to it! 

Add your own code that causes the loop to exit when the `counter` variable reaches 10. You can use `break` to do this. 

Note: Sometimes, we accidentally make loops that never end - try that by running the cell below before adding 

If that happens, interrupt the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 



{:.input_area}
```python
counter = 0

while True:
    
    print("the value of 'counter' = {}".format(counter))
    counter +=1
    
    ## YOUR CODE HERE
    if counter >= 10:
        break
```


{:.output_stream}
```
the value of 'counter' = 0
the value of 'counter' = 1
the value of 'counter' = 2
the value of 'counter' = 3
the value of 'counter' = 4
the value of 'counter' = 5
the value of 'counter' = 6
the value of 'counter' = 7
the value of 'counter' = 8
the value of 'counter' = 9

```

###  Loop Explorations

Now, explore using for and while loops and breaks. 

Here are some things to try, and questions to ask - each of which you should explore in code. 
- What happens if you use 'break' all by itself?
- What are some different ways to loop through a list? tuple?
- Write these combinations: 
    - a `for` loop with a `break`, a `for` loop with a `continue`
    - a `while` loop with a `break`, a `while` loop with a `continue`
- Write some loops that loop across lists:
    - Write a loop that loops across, and prints out, all the elements of a list
    - Write a loop that loops across, and prints out, every second element of a list
    - Write a loop that loops across, and prints out, every element of a list in reverse order
    - Write a loop that loops across, and prints out, the first half of a list
- Write a loop with a conditional inside it.
- Can you have loops inside loops? If you think so, try and write a nested loop. 



{:.input_area}
```python
# YOUR CODE EXPLORATIONS HERE
```




{:.input_area}
```python
break

# `break` all by itself causes an error, because it needs to be run inside a loop
```



{:.output_traceback_line}
```
  File "<ipython-input-22-a88ccf7b8003>", line 1
    break
         ^
SyntaxError: 'break' outside loop

```




{:.input_area}
```python
my_list = [1, 2]
my_tuple = ('a', 'b')

# Loop through list with for - same goes for tuple
for el in my_list:
    print(el)

print('')
    
# Loop through tuple using indexing - same goes for list
for ind in range(2):
    print(my_tuple[ind])
    
# You can loop through lists or tuples directly, or with indexes
```


{:.output_stream}
```
1
2

a
b

```



{:.input_area}
```python
#- Write these combinations: 
#    - a `for` loop with a `break`, a `for` loop with a `continue`
#    - a `while` loop with a `break`, a `for` loop with a `continue`

letter_list = ['a', 'c', 'e']

for it in letter_list:
    if it == 'c':
        break

for it in letter_list:
    if it == 'a':
        continue
        
# For loops with break and continue
```




{:.input_area}
```python
ind = 0

while ind < 5:
    if ind == 2:
        break
    ind = ind + 1

while ind < 5:
    ind = ind + 1
    if ind == 2:
        continue

# While loops with break and continue
```




{:.input_area}
```python
another_list = [1, 2, 3, 4]

print('Print all elements list:')
for it in another_list:
    print(it)
print('')
    
print('Print every second element list:')
for it in another_list[1::2]:
    print(it)
print('')

print('Print reversed list:')
for it in another_list[::-1]:
    print(it)
print('')

print('Print first half:')
half_index = int(len(another_list)/2)
for it in another_list[0:half_index]:
    print(it)
print('')

# These are loops using indexing, to grab different elements of the list
```


{:.output_stream}
```
Print all elements list:
1
2
3
4

Print every second element list:
2
4

Print reversed list:
4
3
2
1

Print first half:
1
2


```



{:.input_area}
```python
for it in [True, False]:
    if it == True:
        print('Yay.')
        
# Loop with a conditional in it
```


{:.output_stream}
```
Yay.

```



{:.input_area}
```python
for a_val in [1, 2, 3]:
    for b_val in ['a', 'b', 'c']:
        print(a_val, b_val)

# Yes, you can have a loop inside a loop
```


{:.output_stream}
```
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c

```

### Nested Loop Challenge

Using nested loops, you will print out a pattern that looks like this:

1 <br>
1 2 <br>
1 2 3 <br>
1 2 3 4 <br>
1 2 3 4 5 <br>
1 2 3 4 5 6 <br>
1 2 3 4 5 6 7

Hints:
- You can do this with two while loops, one inside the other.
- You will have two indices counters, one for each loop. 
- For the print statement, it will look something like `print(index_inner, end=" ")`



{:.input_area}
```python
# YOUR CODE HERE

index_outer = 1
while index_outer < 8:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
```


{:.output_stream}
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
1 2 3 4 5 6 7 

```

## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!
