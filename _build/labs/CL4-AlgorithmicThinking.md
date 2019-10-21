---
interact_link: content/labs/CL4-AlgorithmicThinking.ipynb
download_link: assets/downloads/CL4-AlgorithmicThinking.ipynb.zip
layout: notebooks
title: 'CL4-AlgorithmicThinking'
prev_page:
  url: /labs/CL3B-Answers
  title: 'CL3B-Answers'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# CL4: Algorithmic Thinking

Welcome to the fourth coding lab!

In this CodingLab we will be thinking and working on functions and algorithms. 

The first part is more abstract - thinking about algorithms and functions, and sketching out some pseudocode. 

After that, we'll move to more practice with functions. 

## Part I: PseudoCode

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

You can also write pseudocode, that is much closer to Python, including Python syntax, but that is more of a template / outline. 

PseudoCode like this is sometimes just a work-in-progress that is just not yet finished. 

Note the use of the `pass` keyword - `pass` is just a placeholder keyword, that does nothing.



{:.input_area}
```python
# PseudoCode for a function to email a list of emails, and return a log of what was sent
def sent_emails(list_of_emails):

    emails_sent = {}  # Define an output variable for the logging

    for email in list_of_emails:

        # Send email to current student
        pass

        # Add logging information that email was sent
        email_sent[email] = True

    return emails_sent
```


## Part II: Computation &  Algorithms

Both computers and humans are good at some things, and bad at others. However, it tends to be different things that computers and humans are good at. 

Here is a list of possible tasks that a human and/or computer could try and do:

- Given a list of 100K values, find the average and range of the list
- Sort an array of randomly generated numbers from smallest to largest
- Recognize the saddest part of a movie
- Recall specific facts, like answering 'which day of the week was the 1st of June, 1997
- Identify the likely country of origin of a person from their accent
- Create a meme
- Sort a list of 10,000 names alphabetically
- Rank memes in order of how funny they are
- Given two locations, figure out the best route to drive to get between them
- Recognize the emotional state of a person
- Flexibly change strategy, based on cues in the environment
- Write and perform a winning rap battle 
- Learn and be able to understand a human language
- Learn and be able to understand a programming language
- Play tic-tac-toe
- Write a review of a movie
- Play chess
- Play PACMAN

### Instructions

For the tasks above, we want to try and decide whether it is a task that computers would be better at, that humans would be better at, or if it would be a tie.

In small groups (2 or 3 people), pick 3 or 4 examples from the list of tasks above, have a quick discussion about the task and hand and try to answer the question of who (computers and/or humans) this task would be easier for. 

For each task, try to imagine how you might try and do this in Python. 

Use pseudocode to sketch out an outline of the procedure. 
- If you think it is something computers can do well, your pseudocode should roughly cover the whole process.
- If you think think it is more of a human thing, try to identify which part of the process, in particular, is difficult to specify within a formal algorithm. 

As you work through a few examples, make sure you talk through at least one of each of 'computer better' and 'human better' task. 

Note: as a rule of thumb, computers can do, and are good at anything we can write down an algorithm to complete. 

So one way to think of this task is to think through if and how you can think of writing an algorithm to complete this task.

Below is an example, with an answer for the first listed task.

#### Example: Given a list of 100K values, find the average and range of the list

This is a task that is easier for computers because we can write down a clear set of steps to complete this task (we can write an algorithm). 

Humans would not be good at completing this task, as there are a lot of steps to complete, and it would be slow, and we might not have the memory to do it.  



{:.input_area}
```python
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
```




{:.input_area}
```python
## Make some notes & write some pseudocode for you chosen tasks here


```


## Part III: Functions

Functions are a way to organize code into a procedure that we can repeat and use whenever we want. 

### Function Questions

#### Write a function that takes one input, multiplies it by two and returns the result

This function has been started for you, with the name `mult_two`.

Add some more code to finish this function. 



{:.input_area}
```python
def mult_two(input_number):
    
    # YOUR CODE HERE
```




{:.input_area}
```python
# Check that you can use the function
mult_two(2)
```




{:.input_area}
```python
# Check this function returns the correct outputs
assert mult_two(2) == 4
assert mult_two(3) == 6
```


### Write a function that takes two inputs, adds them together, and returns the result

Call this function `add_two`.



{:.input_area}
```python
def add_two(_FILL_IN_INPUTS_):
    # YOUR CODE HERE
```




{:.input_area}
```python
# Check that you can use the function
add_two(2, 2)
```




{:.input_area}
```python
# Check this function returns the correct number
assert add_two(2, 2) == 4
assert add_two(3, 2) == 5
```


### Write a function with a conditional inside it

You can decide what this function does. 

It could, for example, take a boolean, and print out a status if the input is True. 



{:.input_area}
```python
# YOUR CODE HERE

```


### Write a function with a loop inside it

You can decide what this function does. 

It could, for example, take a list of numbers, and add 1 to each element, and return the new list. 



{:.input_area}
```python
# YOUR CODE HERE

```


### Write a function with a loop and a conditional inside it

You can decide what this function does. 

It could, for example, take a list of booleans, and count how many elements are True, returning a count of `True` values. 



{:.input_area}
```python
# YOUR CODE HERE

```

