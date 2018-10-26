---
download_link: assets/downloads/codingLabs/CL2-ProgrammingII.ipynb.zip
layout: notebooks
title: 'CL2-ProgrammingII'
prev_page:
  url: /codingLabs/CL1b-Answers
  title: 'CL1b-Answers'
next_page:
  url: /codingLabs/CL2b-Answers
  title: 'CL2b-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Coding Lab 2: Programming II

Welcome to the second coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each fill out your own notebook, if you prefer. 

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 

If you have a question about how something works / what something does - try it out, and see what happens!

## Part 1: Collection types

Collections are Python variable types than can store a 'collection' of items.

### Collection Questions

Create a list and a tuple. Fill them with with any values you want. 

Call them `my_list` and `my_tuple`.



{:.input_area}
```python
## YOUR CODE HERE

```


Use the following cells to check the types of the variables you write are as expected



{:.input_area}
```python
type(my_list)
```




{:.input_area}
```python
type(my_tuple)
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


Compare the types of these variables to your equivalent variables to confirm.

In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 



{:.input_area}
```python
# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert isinstance(some_list, _WRITE_IN_TYPE_HERE_)
assert isinstance(some_tuple, _WRITE_IN_TYPE_HERE_)
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

```


## Part 2: Conditionals

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


### Conditional Challenges

The following are more challenging questions relating to conditional statements. If they seem too tricky for now, just skip ahead to the next section.

#### Conditional Challenge #1

Write a conditional that prints "Found it" if a given `val_2` is a multiple of 10, otherwise prints "Nope."



{:.input_area}
```python
## YOUR CODE HERE


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
## YOUR EXPLORATIONS HERE



```


## Part 3: Loops

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

```


###  Loop Explorations

Now, explore using for and while loops and breaks. 

Here are some things to try, and questions to ask - each of which you should explore in code. 
- What happens if you use 'break' all by itself?
- What are some different ways to loop through a list? tuple?
- Write these combinations: 
    - a `for` loop with a `break`, a `for` loop with a `continue`
    - a `while` loop with a `break`, a `for` loop with a `continue`
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

```


If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 
