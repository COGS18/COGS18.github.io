# CL5: Functions

Welcome to the fifth coding lab!

Part I is more abstract - thinking about algorithms and functions, and sketching out some pseudocode. After that, we'll move to more practice with writing functions in Part II and finish with a return to debugging in the context of functions in Part III. 

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

## Part 2: Functions

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
def count_bool(list_of_bools):
    
    counter = 0
    
    for it in list_of_bools:
    
        if isinstance(it, bool):
            counter = counter + 1
    
    return counter

# Check the function
count_bool([True, None, False, 12])
### END SOLUTION

### Function Challenge

The World Health Organization has contacted Professor Ellis to ask for her help sorting between people that should be quarantined and people that shouldn’t. Unfortunately, she’s too busy grading assignments, exams, and coding labs. As such, your task is to help Professor Ellis accomplish this!

Write a function called `to_quarantine`. This function should take two input parmeters: a dictionary(`input_dict`) and `quarantine`. The default value for `quarantine` should be `True`.

Within this function, if `quarantine` is `True`, return all the keys from the input `quarantine_dict` whose values are `True` in a list. If `quarantine` is `False`, return all the keys from the input `quarantine_dict` whose values are `False` in a list.

# you could use this dictionary to test your function
test_dict = {'King Triton': True,
             'Racoon One': True,
             'Sun God': False,
             'Racoon Two': False,
             'Cole Slaw': False,
             'Racoon Three': True,
             'Dr. Py T. Hon': True
            }

### BEGIN SOLUTION

# def to_quarantine(input_dict, quarantine=True):
    
#     do_quarantine = []
#     dont_quarantine = []

#     for person in input_dict:
#         if input_dict[person]:
#             do_quarantine.append(person)
#         else:
#             dont_quarantine.append(person)
    
#     if quarantine:
#         output = do_quarantine
#     else:
#         output = dont_quarantine

#     return output

# OR 

# def to_quarantine(input_dict, quarantine=True):
#     out = []
    
#     if quarantine:
#         for person in input_dict:
#             if input_dict[person]:
#                 out.append(person)
#     else:
#         for person in input_dict:
#             if not input_dict[person]:
#                 out.append(person)    

#     return out

# OR

def to_quarantine(input_dict, quarantine=True):
    new_list = []
    for x in input_dict:
        if input_dict[x] == quarantine:
            new_list.append(x)

    return new_list
### END SOLUTION

assert to_quarantine(input_dict={'A': True, 'B': False, 'C': True, 'D': False}) == ['A', 'C']
assert to_quarantine({'A': True, 'B': False, 'C': True, 'D': False}, quarantine=False) == ['B', 'D']

## Part III: Debugging Questions

### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 

my_list = [1, a, 24]

### BEGIN SOLUTION
# Answer: assuming `a` was supposed to be a string, update to 'a'
my_list = [1, 'a', 24]
### END SOLUTION

my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
print('Printing the 3rd element of my list ' + my_list2(2))

### BEGIN SOLUTION
# Answer: wrong syntax to index, replace with '[]'
print('Printing the 3rd element of my list ' + my_list2[2])

### END SOLUTION

### Debugging a Function

The following function has a series of issues with it. 

Work through debugging this function, fixing it up to be able to run with all the inputs below. 

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

### BEGIN SOLUTION
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1:
        if input_1[0] == 0:
            answer = 0
    
    elif len(input_2) == 2:
        try:
            answer = input_2[1] / input_1[0]
        except ZeroDivisionError:
            answer = None
        
    elif len(input_1) == len(input_2):
        try:
            answer = input_1[0] + input_2[0]
        except TypeError:
            answer = None
        
    return answer 
### END SOLUTION

my_function([0, 1], [0])

my_function([0], [0, 1])

my_function([1], [1])

my_function([1], ['1'])

## Exploring Code

One of the great things about Python is how many tools, utilities and examples there are out there.

Let's start exploring what is available:

GitHub is a website that people use to save and present code. Below we have listed some some notebooks that are hosted on GitHub showing some particular projects, as well as a link to Github in general, and a curated list of interesting Jupyter notebooks. 

Take time to look at at least one of the notebooks mentioned below. See if you can get, to a first approximation, a sense of what the notebook is doing, and how the Python code does it. 

Also go and search through Github and/or the list of notebooks, to see if you can find some code projects that interest you. See if you can get any ideas for things that you could do in your project for this class. 

Don't worry if you don't understand all the code you see - this is just a start, to see what is out there, and you will understand more and more of it as we go along. 

- https://anaconda.org/jbednar/census/notebook - Demographic data plotted out on maps of the US, showing differences in racial segregation/integration in different cities.
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#linguistics-and-text-mining - Mining text to learn trends in bodies of text.
- https://anaconda.org/jbednar/nyc_taxi/notebook - NYC taxi data plotted out on cities of NYC
- https://www.fullstackpython.com/ - for advanced python user, next level guideline

<div class="alert alert-info">
Go and explore <a href="https://github.com">GitHub</a>, and search for some Python projects. And/or check out this list of interesting <a href="https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks">Jupyter Notebooks</a>. 
</div>