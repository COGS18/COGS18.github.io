# CL4: Debugging & Loops

Welcome to the fourth coding lab!

In this Coding Lab we will start with debugging and then finish off with loops.

**Note**: You may *not* be able to complete all of this in 50 minutes, particularly the "challenges."  These are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for these!

## Part 1: Debugging Questions

### Creating Errors
For each of the follow Exceptions, write a small piece of code that will cause it to happen:
- ZeroDivisionError
- SyntaxError
- IndentationError
- TypeError
- IndexError
- ValueError
- NameError

# ZeroDividisionError

### BEGIN SOLUTION
# Zero Division Answer
1/0
### END SOLUTION

# SyntaxError

### BEGIN SOLUTION
# Syntax Answer
for el in [1, 2]
    print(el)
### END SOLUTION

# IndentationError

### BEGIN SOLUTION
# Indentation Error
for el in [1, 2]:
print(el)
### END SOLUTION

# TypeError

### BEGIN SOLUTION
# Type error
(1, 2) + (2)
### END SOLUTION

# IndexError

### BEGIN SOLUTION
# Index Error
lst = [1, 2]
lst[2]
### END SOLUTION

# ValueError

### BEGIN SOLUTION
# Value Error
int('a')
### END SOLUTION

# NameError

### BEGIN SOLUTION
# Name Error
a
### END SOLUTION

### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 

if True
    print('It worked')
    
### BEGIN SOLUTION
# Answer: add a ':' to open the conditional code block
if True:
    print('It worked')
### END SOLUTION

age_string = "My favorite number is " + 27

### BEGIN SOLUTION
# Answer: typecase int to string
age_string = "My favorite number is " + "27"
# OR
age_string = "My favorite number is " + str(27)
### END SOLUTION


print('Three plus five equals' + str(3+5)

### BEGIN SOLUTION
# Answer: Missing closing parenthesis - add ')' at the end
print('Three plus five equals' + str(3+5))

### END SOLUTION


## Part 2: Loops

We will now explore two ways to iterate over data in Python - `for` and `while` loops. 

Each type of loop performs its respective code block until certain conditions are met. Here, we will explore what those conditions are. 

Note: "iterate" means to perform an action repeatedly 

Note: Sometimes, we accidentally make loops that never end. 
- If that happens, "break" the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

#### Loops Q1

First, declare a variable called `counter` that has type int and value zero.

Then write a while loop that runs 10 times and use 'counter' to track how many times the loop runs. 

### BEGIN SOLUTION
counter = 0
while counter < 10:
    counter = counter + 1
### END SOLUTION

# Check that (after the loop runs) that there is a variable called `counter` that has value 10
assert counter == 10

#### Infinite Loops

The while loop below will run indefinitely unless someone puts a stop to it! 

Add your own code that causes the loop to exit when the `counter` variable reaches 10. You can use `break` to do this. 

Note: Sometimes, we accidentally make loops that never end - try that by running the cell below before adding 

If that happens, interrupt the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

counter = 0

while True:
    
    print("the value of 'counter' = {}".format(counter))
    counter +=1
    
### BEGIN SOLUTION
    if counter >= 10:
        break
### END SOLUTION


Now, rather than using `break`, edit the loop from above so that the condition following `while` will eventually evaluate as `False` (and thus terminate the loop).

### BEGIN SOLUTION
counter = 0

# edit condition
while counter < 10:
    
    print("the value of 'counter' = {}".format(counter))
    counter +=1
### END SOLUTION

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

### BEGIN SOLUTION
my_list = [1, 2]
my_tuple = ('a', 'b')

# You can loop through lists or tuples directly, or with indices
# Loop through list with for - same goes for tuple
for el in my_list:
    print(el)

print('')
    
# Loop through tuple using indexing - same goes for list
for ind in range(2):
    print(my_tuple[ind])

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

# While loops with break and continue
ind = 0

while ind < 5:
    if ind == 2:
        break
    ind = ind + 1

while ind < 5:
    ind = ind + 1
    if ind == 2:
        continue

# These are loops using indexing, to grab different elements of the list
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

# Loop with a conditional in it
for it in [True, False]:
    if it == True:
        print('Yay.')

# Yes, you can have a loop inside a loop
for a_val in [1, 2, 3]:
    for b_val in ['a', 'b', 'c']:
        print(a_val, b_val)


### END SOLUTION

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

### BEGIN SOLUTION
index_outer = 1
while index_outer < 8:
    
    index_inner = 1
    
    while index_inner <= index_outer:
        print(index_inner, end=" ")
        index_inner = index_inner + 1
        
    print("")
    index_outer = index_outer + 1
### END SOLUTION

If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 



## Part 2: PseudoCode

First, let's briefly consider the idea of pseudocode. 

Pseudocode is an informal, 'high-level' sketch or description of a program or algorithm. 

It will typically resemble the structure of a program, but the details to make it actually run have not been fleshed out. 

### Pseudocode Human Language

Some pseudocode is written in human level language, in a way that sketches out the tasks and general control flow. 

This highly abstract pseudocode is often not specific to any particular programming language. 

```
# PseudoCode for checking if a student got full credit on assignment

function that takes a list of student ids with student grades

    create an output object to collect full credit

    for student in list of grades

        if grade of student is equal to max grade
            add to list of full credits

    return list of students who got full credit
```

### Pseudocode in Python format

You can also write pseudocode, that is much closer to Python (including Python syntax) but maintains more of a template / outline. 

Pseudocode like this is sometimes just a work-in-progress that is just not yet finished. 

Note the use of the `pass` keyword - `pass` is just a placeholder keyword that does nothing.

# PseudoCode for a function to email a list of emails, and return a log of what was sent
def sent_emails(list_of_emails):

    emails_sent = {}  # Define an output variable for the logging

    for email in list_of_emails:

        # Send email to current student
        pass

        # Add logging information that email was sent
        email_sent[email] = True

    return emails_sent

## Part II: Computation &  Algorithms

Both computers and humans are good at some things, and bad at others. However, it tends to be different things that computers and humans are good at. 

Here is a list of possible tasks that a human and/or computer could try and do:

- Given a list of 100K values, find the average and range of the list
- Sort an array of randomly generated numbers from smallest to largest
- Recognize the saddest part of a movie
- Recall specific facts, like answering 'which day of the week was the 1st of June, 1997?'
- Identify the likely country of origin of a person from their accent
- Create a meme
- Sort a list of 10,000 names alphabetically
- Rank memes in order of how funny they are
- Given two locations, figure out the best route to drive to get from one to another
- Recognize the emotional state of a person
- Flexibly change strategies based on cues in the environment
- Write and perform a winning rap battle 
- Learn and be able to understand a human language
- Learn and be able to understand a programming language
- Play tic-tac-toe
- Write a review of a movie
- Play chess
- Play PACMAN

### Instructions

For each task above, we want to try and decide whether it is a task that computers would be better at, that humans would be better at, or if it would be a tie.

In small groups (2 or 3 people, or on your own if groups are not possible/you're not doing this in coding lab directly), pick 3 or 4 examples from the list of tasks above, have a quick discussion about the task at hand and try to answer the question of who (computers and/or humans) this task would be easier for. 

For each task, try to imagine how you might try and do this in Python. 

Use pseudocode to sketch out an outline of the procedure. 
- If you think it is something computers can do well, your pseudocode should roughly cover the whole process.
- If you think it is more of a human thing, try to identify which part of the process, in particular, is difficult to specify within a formal algorithm. 

As you work through a few examples, make sure you talk through at least one of both 'computer better' and 'human better' tasks. 

Note: as a rule of thumb, computers can perform (and are good at) anything we can write down an algorithm. 

So one way to approach this section is to think through if and how you would write an algorithm to complete each task.

Below is an example, with an answer for the first listed task. You will be asked to sketch out your own example under that.

#### Example: Given a list of 100K values, find the average and range of the list

This is a task that is easier for computers because we can write down a clear set of steps to complete this task (we can write an algorithm). 

Humans would not be good at completing this task, as there are a lot of steps to complete, and it would be slow, and we might not have the memory to do it.  

# Pseudocode for array statistics
def array_statistics():
    
    # Find the mean of the array. 
    pass
    # To do so:
        # Find the total sum of the array
        # Find the number of elements in the array
        # Divide the sum by the number of elements
        
    # Find the range of the array. 
    pass
    # To do so:
        # Find the maximum value of the array
        # Find the minimum value of the array
        # Calculate range by subtracting the max from the min for the array
    
    # Return the mean and range of the array
    return None

### Include sketch of (at least) one task

After brainstorming, include a sketch of your pseudocode for at least one of the tasks you brainstormed about earlier:

## Make some notes & write some pseudocode for you chosen task(s) here

## Part 3: Functions

Functions are a way to organize code into a procedure that we can repeat and use whenever we want. 

### Function Questions

#### Write a function that takes one input, multiplies it by two and returns the result

This function has been started for you, with the name `mult_two`.

Add some more code to finish this function. 

def mult_two(input_number):
    

### BEGIN SOLUTION
    answer = input_number * 2
    return answer
### END SOLUTION

# Check that you can use the function
mult_two(2)

# Check this function returns the correct outputs
assert mult_two(2) == 4
assert mult_two(3) == 6

#### Write a function that takes two inputs, adds them together, and returns the result

Call this function `add_two`.

def add_two(_FILL_IN_INPUTS_):
    
### BEGIN SOLUTION
def add_two(num1, num2):

    answer = num1 + num2
    return answer
### END SOLUTION

# Check that you can use the function
add_two(2, 2)

# Check this function returns the correct number
assert add_two(2, 2) == 4
assert add_two(3, 2) == 5

#### Write a function with a conditional inside it

You can decide what this function does. 

It could, for example, take in a boolean and print out a status if the given boolean is True. 

### BEGIN SOLUTION
def check_bool(input_bool):
    
    if input_bool == True:
        out = 'Status is True'
    else:
        out = 'Status is not True'
    
    return out
### END SOLUTION

#### Write a function with a loop inside it

You can decide what this function does. 

It could, for example, take a list of numbers, add 1 to each element, and return the new list. 

### BEGIN SOLUTION
def adder(in_list):

    out_list = []

    for it in in_list:
        out_list.append(it + 1)
        
    return out_list
### END SOLUTION

#### Write a function with a loop and a conditional inside it

You can decide what this function does. 

It could, for example, take a list of booleans, count how many elements are True, and return a count of `True` values. 

### BEGIN SOLUTION
# YOUR CODE HERE
def count_bool(list_of_bools):
    
    counter = 0
    
    for it in list_of_bools:
    
        if isinstance(it, bool):
            counter = counter + 1
    
    return counter

# Check the function
count_bool([True, None, False, 12])
### END SOLUTION