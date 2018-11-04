---
download_link: assets/downloads/assignments/A3-Chatbots.ipynb.zip
layout: notebooks
title: 'A3-Chatbots'
prev_page:
  url: /assignments/A2B-Answers
  title: 'A2B-Answers'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Assignment 3: Chatbots

## Overview

This assignment covers Functions & Algorithms, and builds up to the application of Chatbots. 

This assignment is out of 8 points, worth 8% of your grade.

Make sure your completed assignment passes all the asserts. This assignment also has hidden tests - which means that passing all the asserts you see does not guarantee that you have the correct answer! Make sure to double check and re-run your code to make sure it does what you expect.

### Quick Tips

Make sure you execute your code to define the functions you write, and then add a new cell to apply your function to different inputs, and check that you get the outputs you expect. 

If you're not sure where to start, look at the code in the test cases (in the asserts) for examples for what kind of inputs and outputs the function you are writing should take, and what kind of behaviour it should have.

Keep in mind that each question is mostly independent from every other - so if you get stuck on something, you can always move on to the next one, and come back to any that you have trouble with later.

## Setup

#### Code Imports

You must run the following cell before proceeding with the assignment. 



{:.input_area}
```python
# Setup - run this cell before doing the next part of the assignment
#   This imports some extra code, making it available for us to use later
import string
import random
import nltk
```


### Zen Chatbot

In this assignment, we will be working our way up to building a chatbot.

To start with, we can have a quick chat with a zen chatbot, to see what these kinds of chatbots look like. 

Also, if you get stuck on anything, come back here, and talk to the Zen chatbot, to relax :)

Note: in this, and other, chatbot lines, running this code will start an open-ended while loop, that will interupt your code flow, until you explicity quit out of the conversation. If you want to be able to run all your code (from kernel `restart & run all`), then comment these lines back out when you are finished exploring them. 



{:.input_area}
```python
# Uncomment and run this cell to talk to a Zan Chatbot
#nltk.chat.zen.demo()
```


## Part 1: Functions

This part covers the basics of writing and using functions.

### Function Examples

The following are a couple examples of functions provided to you, so you can see their structure.

You don't need to do anything with these functions.



{:.input_area}
```python
def basic_function(input_number):
    """Multiplies an input number by 2."""
    
    # Multiple the input by 2
    output = input_number * 2 
    
    return output
```




{:.input_area}
```python
# Test using `basic_function`
print(basic_function(2))
print(basic_function(5))
```




{:.input_area}
```python
def more_complicated_function(input_string):
    """Counts how many letters are in a string."""

    letter_count = 0

    for item in input_string:
        
        # Uses the `isalpha` method to check if a character is from the alphabet
        if item.isalpha():
            
            # `+= 1` is a shortcut for `val = val + 1`
            letter_count += 1
            
    return letter_count
```




{:.input_area}
```python
# Test using `more_complicated_function`
print(more_complicated_function('ab45b'))
```


### Q1 - Find Max Value  (0.5 points)

Write a function called `find_max`, that takes in a single parameter called `random_list`, which should be a list. 

This function will find the maximum (max) value of the input list, and return it. 

This function will assume the list is composed of only positive numbers.

To find the max, within the function, use a variable called `list_max`, that you initialize to value 0. 

Then use a `for` loop, to loop through `random_list`. 

Inside the list, use a conditional to check if the current value is larger than `list_max`, and if so, re-assign `list_max` to store this new value.

After the loop, return `list_max`, which should now store the maximum value from within the input list. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(find_max)
assert isinstance(find_max([1,7,5]), int)
assert find_max([1,7,5]) == 7
```




{:.input_area}
```python
assert callable(find_max)

```


### Q2 - Square Everything  (0.5 points)

Write a function called `square_all` that takes an input called `collection` that you assume to be a list or tuple of numbers. 

This function should return a new `list`, which contains the square of each value in `collection`. 

To do so, inside the function, you will define a new list, use a loop to loop through the input list, use an operator to square the current value, and use the `append` method to add this to your output list. After the loop, return the output list.



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(square_all)
assert isinstance(square_all([1, 2]), list)
assert square_all((2, 4)) == [4, 16]
```




{:.input_area}
```python
assert callable(square_all)

```


## Part 2: Refactoring Code to Use Functions

'Refactoring' is the process of updating existing computer code, to keep the same outputs, but to have better internal organization and/or properties. 

We've written a lot of code in previous assignments. However, since we did not yet have functions at our disposal, a lot of that code is not very easy to re-use. 

In this section we will refactor some code - rewriting (and extending) some code from previous assignments as functions, to make it easier to re-use. 

### Q3 - Calculator (0.5 points)

Let's start with the calculator code that we worked on in A1.

Instead of using a conditional, like we did before, we will make a series of functions to do all the mathematical operations that we want to do. 

Define four functions, called `summation`, `subtraction`, `multiplication`, and `division`. 

Each of them will take two inputs `num1` and `num2` (that could be `int` or `float`), and use them as follows:
- `summation` will add `num1` to `num2` and return the result
- `subtraction` will subtract `num2` from `num1` and return the result
- `multiplication` will multiply `num1` by `num2` and return the result
- `division` will divide `num1` by `num2` and return the result



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(summation)
assert isinstance(summation(2, 2), int)
assert isinstance(summation(2.5, 1), float)
assert summation(1, 1) == 2

```




{:.input_area}
```python
assert callable(subtraction)
assert isinstance(subtraction(2, 2), int)
assert isinstance(summation(2.5, 0.5), float)
assert subtraction(1, 1) == 0

```




{:.input_area}
```python
assert callable(multiplication)
assert isinstance(multiplication(2, 2), int)
assert isinstance(multiplication(2.5, 2), float)
assert multiplication(1, 1) == 1

```




{:.input_area}
```python
assert callable(division)
assert isinstance(division(2, 2), float)
assert isinstance(division(2.5, 0.5), float)
assert division(1, 1) == 1

```


### Q4 - Extending our Calculator  (0.5 points)

Let's now add some more functions to our calculator: 

- Write a function called `squared` that takes one parameter, called `num`, and returns the square of it. 
- Write a function called `square_root` that takes one parameter, called `num`, and returns the square root of it. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(square)
assert isinstance(square(2), int)
assert square(5) == 25

```




{:.input_area}
```python
assert callable(square_root)
assert isinstance(square_root(4), float)
assert square_root(144) == 12

```


### Example: Chaining Functions Together

The goal of using functions is partly to be able to re-use code segments. 

It's also a way to able to flexibly apply and combine different functions together, to build up to more complex and interesting programs. 

The cell below shows a couple examples of using our calculator functions that we have now defined, in combination with each other. 



{:.input_area}
```python
# Add the multiplication of 2 and 3 to the multiplication of 3 and 4
number1 = multiplication(2, 3)
number2 = multiplication(3, 4)
output1 = summation(number1, number2)
print('Output1: \t', output1)

print('')

# Note that we can use the outputs of functions directly as inputs to other functions
#   Therefore, the above construction is equivalent to the following:
output2 = summation(multiplication(2, 3), multiplication(3, 4))
print('Output2: \t', output2)

# When we have something like above the functions that are inputs get evaluated first:
#   So, first, `multiplication(2, 3)` evaluates as 6, and `multiplication(3, 4)` evaluales as 12
#   This then reduces to calling `summation(6, 12)`, which returns our answer of 18
```


### Q5 - Using Our Calculator  (0.5 points)

Let's now use our new calculator functions to do some calculations!

- Add the square of 3 to the square root of 9
    - Save the result to a variable called `calc_a`
- Subtract the division of 12 by 3 from the the multiplication of 2 and 4
    - Save the result to a variable called `calc_b`
- Multiply the square root of 16 to the sum of 7 and 9
    - Save the result to a variable called `calc_c`
- Divide the square of 7 by the square root of 49
    - Save the result to a variable called `calc_d`



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert calc_a
assert isinstance(calc_a, float)

```




{:.input_area}
```python
assert calc_b
assert isinstance(calc_b, float)

```




{:.input_area}
```python
assert calc_c
assert isinstance(calc_c, float)

```




{:.input_area}
```python
assert calc_d
assert isinstance(calc_d, float)

```


### Calling Functions from Functions

In the example above, we were able to refactor our code into re-useable functions. 

We were then able to use these functions and chain them together to flexibly and extensibly do computation.

Next we'll dive into another aspect of writing good modular code: dividing complex tasks into independent functions and then using them together.

In practice, this will look like writing lots of and small and specific functions to do simple tasks.

We can then use these functions from within other functions build up to being able to do more complex tasks.

### Q6 - Functions for Even & Positive Numbers (0.5 points)

Recall Q13 from A2, when we wanted to check a series of conditions across items in a list. 

We can consider that checking each of these conditions is really a separate task. 

When writing modular code, these separate tasks should therefore be organized as separate functions.

For this question, write two functions, one called `is_even`, and the other called `is_positive`. 

Each function should take in a single parameter, a number called `value`:

- `is_even` will check if `value` is even, and return `True` if so, and `False` otherwise. 
- `is_positive` will check if `value` is positive, and return `True` if so, and `False` otherwise. 
    - Note: for our purposes here, 'positive' numbers are all numbers greater than 0 (so 0 is not considered positive).



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(is_even)
assert isinstance(is_even(3), bool)
assert is_even(3) == False

```




{:.input_area}
```python
assert callable(is_positive)
assert isinstance(is_positive(3), bool)
assert is_positive(-2) == False

```


### Q7 - Functions Using Functions (0.5 points)

In this section, your are going to recreate a function called `make_new_list` which takes a list called `data_list` as its input. 

This function will use `is_positive` and `is_even` to mimic the task from A2-Q13. 

That is, this function will  check each value in `data_list` to see if they are even or odd and whether they are positive or negative.
- If they are both positive and even, encode this as the number 1
- If they are both negative and odd, encode this as the the number -1
- Otherwise, encode this as the number 0

- Store the result for each value into a list called `output` and return it.



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(make_new_list)

data_list = [-1, 20, -100, -40, 33, 97, -101, 45, -79, 96]
assert isinstance(make_new_list(data_list), list)
assert(len(make_new_list(data_list)) == len(data_list))
```




{:.input_area}
```python
assert callable(make_new_list)

```


## Part 3: Algorithms

This part covers working with algorithms.

### Q8 - Algorithms (0.5 points)

For each of the tasks below, indicate whether you think it is something that a human or a computer would be better at doing.

Answer each question by setting each requested variable to the string either 'human' or 'computer'. 

Set the variable to reflect the answer of which of them you think would be better at the task.

- a) Recognize whether a sentence is sarcastic and/or ironic. 
    - Answer in a variable called `algo_q_a`
- b) Reply to a question with information about a topic, replying with the exact wording from a wikipedia article.
    - Answer in a variable called `algo_q_b`
- c) Keep answering messages for an arbitrarily long period of time, without demonstrating fatigue.
    - Answer in a variable called `algo_q_c`
- d) Interpret the tone of what was said, to infer if someone is angry. 
    - Answer in a variable called `algo_q_d`
    
For each, try to think through if and how you could write an algorithm to do this task - and if you could not, what about it is hard to formalize. 

We can use these questions to start to think through what might be easy and hard to program our chatbot to do. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert algo_q_a in ['human', 'computer']

```




{:.input_area}
```python
assert algo_q_b in ['human', 'computer']

```




{:.input_area}
```python
assert algo_q_c in ['human', 'computer']

```




{:.input_area}
```python
assert algo_q_d in ['human', 'computer']

```


## Part 4:  Chatbots

This part is an application of all the tools we have covered so far, to the problem of creating a chatbot.

A chatbot is a piece of software that tries to have a conversation with a human.

While today's chatbots are powerful learners, traditional chatbots are much simpler. 

Traditional chatbots follow a "rule-based" approach that is defined for them (by you, the programmer), usually without any learning. 

These rules can be very simple or sometimes quite complex - but everything is pre-defined. 

These types of chatbots can handle simple conversations but do tend to fail at more complex ones.

#### Chatbot functions

In order to make our chatbot, we will create a series of functions that our eventual chatbot will use together to try and chat with a user. 

At the end, we will test that these functions do indeed allow us to have simple conversations with our chatbot.

Below are some more example chatbots to talk to. Remember to comment these lines back out if you want to be able to `Restart and Run All`.

### Example Chatbot - Eliza

The following demo is from the Natural Language ToolKit (nltk), a Python package available through Anaconda. 

Uncomment the line below, and run the code to be able to have a chat with Eliza.

More information on Eliza: https://en.wikipedia.org/wiki/ELIZA



{:.input_area}
```python
# Run a demo of a chatbot, with Eliza
#nltk.chat.eliza.demo()
```


### Example Chatbot - Iesha

The following is another demo chatbot from nltk, this one called Iesha. 



{:.input_area}
```python
# Run a demo of a chatbot, with Iesha
#nltk.chat.iesha.demo()
```


As you try the chatbot demos with Eliza and Iesha, see if you can notice any patterns that might help you figure out how they work. 

That is, can you guess at what kind of programming structures these programs might use?

### Chatbots: Words & Rules

So, how do these kinds of chatbots work? Most broadly, they combine two simple but powerful approaches:
- Rule Based Artificial Intelligence (GOFAI)
- Bag-Of-Word Language Models

**Rule based AI**, sometimes called 'Good Old Fashion Artificial Intelligence', or 'GOFAI', is an approach to making artificial agents that tries to write down a set of rules to follow to perform some task. In practice, this often looks like using a lot of conditionals: if `X` happens, do `Y`. If we can write down enough logical procedures (call them algorithms) to follow to complete some task, then we can create an artificially intelligent agent (for that task).

**Bag-Of-Word language models** are an approach to language that takes the simple approach of saying 'lets try and figure out what someone is saying simply by checking and counting which words they use'. If someone says the word 'dog' three times in conversation, they are probably talking about dogs. This ignores many many things about language, and how it works, but is a good 'first guess' for what is being said. 

From our perspective, this means two things:
- We can broadly try to figure out the topic simply by checking which words are used
- We can choose a response based on a rule that defines what to do if and when we identify particular topics

In code then, this looks like:
- taking input as strings of continuous text, and splitting this up into lists that contain all the words we see
- use conditionals (if/elif/else) that choose an output based on what words appear in those lists

As we work through and create all the function in the next section to create our chatbot, try to think through how these functions relate to this approach.

### Q9 - Is It a Question (0.5 points)

One thing we might want to know, given an input to a chatbot, is if the input is a question. 

We are going to use a very simple heuristic to check this: we will consider any input that has a question mark ('?') in it to be a question. 

To do so, write a function called `is_question`. 

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_string` - string

Output(s):
* `output` - boolean

Procedure(s):
- if there is a '?' in `input_string`, set `output` to True
- otherwise, set output to False. 
- return output



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(is_question)
assert isinstance(is_question('abc'), bool)
assert is_question('what?') == True
```




{:.input_area}
```python
assert callable(is_question)

```


### Example: string.punctuation

When working with strings, it can be useful to check what kind of things particular characters are. 

To do things like this, Python offers some collections of items, that we can check against.

For example, we can ask if a particular character is a punctuation mark, by asking if it is in the collection of punctuation characters. 




{:.input_area}
```python
# Print out list of punctuation
print(string.punctuation)

print() # Print blank line

# Check if a particular symol is a punctuation mark
print('@' in string.punctuation)
```


### Q10 - Removing punctuation (0.5 points)

Once we know if an input is a question, we are going to get rid of all punctuation. 

To do so, write a function called `remove_punctuation`. 

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_string` - string

Output(s):
* `out_string` - string

Procedure(s):
- define a new variable `out_string` as an empty string
- loop through each character in `input_string`
    - if this character is not in `string.punctuation`
        - then append the current character to `out_string`
- return `out_string`



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(remove_punctuation)
assert isinstance(remove_punctuation('a'), str)
assert remove_punctuation("Hey! It's Tom!") == "Hey Its Tom"
```




{:.input_area}
```python
assert callable(remove_punctuation)

```


### Q11 - Preparing Text (0.5 points)

Now we want a more general function to prepare the text inputs for processing. 

Inside this function, we will use some string methods as well as our new `remove_punctuation` function.

Write a function called `prepare_text`.

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_string` - string

Output(s):
* `out_list` - list of string

Procedure(s):
- make the string all lower case (use a string method called `lower`)
    - note that you will have to assign the output to a variable. You can use a variable name like `temp_string`
- remove all punctuation from the string (use your new function `remove_punctuation`)
    - this can also assign out to `temp_string`
- split the string into words (look for and use a string method called `split`)
    - note that split will return a list of strings. Assign this as `out_list`
- return `out_list`



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(prepare_text)
assert isinstance(prepare_text('One two three.'), list)
assert prepare_text('Hi! Also, howdy.') == ['hi', 'also', 'howdy']
```




{:.input_area}
```python
assert callable(prepare_text)

```


### Q12 - Echo a Response (0.5 points)

We will define a function that will return a string that has been repeated a specified number of times, with a given separator. 

We will also want to deal with the case where the input to this function may be `None`. 

Write a function called `respond_echo`. 

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_string` - string, or None
* `number_of_echoes` - integer
* `spacer` - string

Output(s):
* `echo_output` - string, or None

Procedure(s):
- if `input_string` is not `None`:
    - set a variable `echo_output` to be  `input_string`, repeated the number of times specified by `number_of_echoes`, joined by the  `spacer`.
        - Hint: to do so, recall what "*" does to strings
- otherwise (if `input_string` is None)
    - set `echo_output` to `None`
- return `echo_output`

Note that a simple version of this version will end up appending the spacer to the end of the list as well. For our purposes here, implement that simple version.

So, for example, `respond_echo('bark', 2, '-')` should return: 'bark-bark-'



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(respond_echo)
assert isinstance(respond_echo('ha', 2, ' '), str)
assert respond_echo('meow', 3, '~') == 'meow~meow~meow~'
assert respond_echo(None, 2, '') == None
```




{:.input_area}
```python
assert callable(respond_echo)

```


### Example: random.choice

We want our chatbot to have some variation in it's responses - not only anwering the same thing.

So, we want to be able to choose an output from a list of options. 

We can use the `random.choice` function to so.

An example of using `random.choice` is offered below.



{:.input_area}
```python
# Given a list of inputs, randomly choose and return one of them (re-run this to see different outputs)
random.choice(['first option', 'second option', 'third option'])
```


### Q13 - Selector (0.5 points)

Next we will write a function that will help us select an output for the chatbot, based on the input it got.

The overall goal of this function is to take a list of words that we got as input, a list of words to check for if they appear in the input, and a list of possible outputs to return if something from the list to check is in the input list. 

Define a function, called `selector`.

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_list` - list of string
* `check_list` - list of string
* `return_list` - list of string

Output(s):
* `output` - string, or None

Procedure(s):
- Initialize `output` to `None`
- Loop through each element in `input_list`
- Use a conditional to check if the current element is in `check_list`
    - If it is, assign `output` as the returned value of calling the `random.choice` function on `return_list`
    - Also, break out of the loop
- At the end of the function, return `output`

Note that if we don't find any words from `input_list` that are in `check_list`, `output` will be returned as `None`.



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(selector)

assert selector(['in', 'words'], ['words'], ['yes']) == 'yes'
assert selector(['in', 'words'], ['out'], ['yes']) == None
```




{:.input_area}
```python
assert callable(selector)

```


### Q14 - String Concatenator Function (0.5 points)

Create a function that will concatenate two strings, combining them with a specified separator. 

To do so, write a function called `string_concatenator`. 

This function should have the following inputs, outputs and internal procedures:

Input(s)
* `string1` - string
* `string2` - string
* `separator` - string

Output(s)
* `output` - string, or None

Procedure(s):
- concatenate `string1` to `string2` with `separator` in between them. 
- return the result



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(string_concatenator)
assert isinstance(string_concatenator('hello', 'world', ' '), str)
assert string_concatenator('hello', 'world', ' ') == 'hello world'
```




{:.input_area}
```python
assert callable(string_concatenator)

```


### Q15 - List to String (0.5 points)

Since we are often dealing with a list of strings, it would be useful to have a function to turn a list of strings back into one single concatenated string. 

This function will return a string that is each element of `input_list` concatenated together with each separated by the string `seperator`. 

For example, the following function call:

    `list_to_string(['This', 'is', 'fun'], ' ')`

shoud return: 
    
    'This is fun'
    
To do this, write a function called `list_to_string`. 

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_list` - list of string
* `separator` - string

Output(s):
* `output` - string

Procedure(s):
- assign a variable called `output` to be the first (index 0) element from `input_list`
- loop through the rest of `input_list`, looping from the 2nd element (index 1) through to the end of the list
    - Within the loop, use `string_concatenator` to combine `output` with the current element, separated by `separator`
        - Assign the output of this to be the new value of `output`
- return `output`, which should now be a list of the elements of `input_list`, joined together into a a single string



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(list_to_string)
assert isinstance(list_to_string(['a', 'b'], '|'), str)
assert list_to_string(['a', 'b'], '|') == 'a|b'
```




{:.input_area}
```python
assert callable(list_to_string)

```


### Q16 - End Chat (0.5 points)

The last thing we need is a way to end the chat with our chatbot. 

We will use the same convention that `nltk` uses - namely, that we will end the conversation if the word `quit` appears.

To be able to do so, write a function called `end_chat`

This function should have the following inputs, outputs and internal procedures:

Input(s):
* `input_list` - list

Output(s):
* `output` - boolean

Procedure(s):
- This function should return `True` if the string 'quit' is in `input_list`, and return `False` otherwise. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(end_chat)
assert isinstance(end_chat(['a', 'b']), bool)
assert end_chat(['quit']) == True
```




{:.input_area}
```python
assert callable(end_chat)

```


## Pulling it all Together

If everything has gone well with writing everything above, then we are ready to pull all these functions together to create our chatbot.

The next few cells define a bunch of code, all provided for you. This code adds a couple more functions we can use and then defines some lists of inputs and outputs that our chatbot will know about. After that, there is a big function that pulls everything together and creates the procedure to use all of this code together as a chatbot. 

You don't have to write anything in the cells below (or in the rest of the assignment). 

Do have a quick read through the code though, to see how our chatbot works, and to see how all the functions you just wrote are used to create the chatbot. 

If you need, revisit the information at the beginning of this section about the logic our chatbot uses. 

You don't have to understand everything about what happens here, but try to have a first-pass look through it.

We will build up to understanding and writing this kind of code that brings a lot of things together as we continue through the course. 

If the code seems intimidating, just scroll down to the bottom, and test out talking to our chatbot. 



{:.input_area}
```python
# These are a couple more function, provided to you, to be used by our chatbot.

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None
```




{:.input_area}
```python
# This cell defines a collection of input and output things our chatbot can say and respond to

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.", \
            "Did you know I'm made of code!?", \
            "Computers are so magical", \
            "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I don't want to talk about"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"
```




{:.input_area}
```python
def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)
```


## Talking to our Chatbot

To talk to our chatbot, uncomment and run the cell below. 

If anything seems to go weird, note that you can always interrupt the code from running with chat with kernel - interrupt from the menu. 

If this happens, it probably means there is some issue with one of the functions you wrote for the chatbot. 



{:.input_area}
```python
# Talk to our chatbot
have_a_chat()
```


### Extending Our Chatbot

You might notice that our chatbot, right now, is pretty limited in how many things it can respond to.

To respond to more topics, we could re-use these same functions, adding more input & output options for our chatbot to respond to, using the basic approaches and functionality we have defined here. 

If you are interested in this topic, extending this chatbot (or ones like it) will be one of your project options. 

## The End!

After you've explored chatting to the chatbot, you are done!

Have a look back over your answers, and also make sure to Restart & Run All from the kernel menu to double check that everything is working properly. 

When you are ready to submit your assignment, upload it to TritonED under Assignment-3.
