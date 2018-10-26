---
download_link: assets/downloads/assignments/A3-Chatbots.ipynb.zip
layout: notebooks
title: 'A3-Chatbots'
prev_page:
  url: /assignments/A2-Ciphers
  title: 'A2-Ciphers'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Assignment 3: Chatbots

## Overview

This assignment covers Functions & Algorithms, and builds up to the application of Chatbots. 

This assignment is out of 8 points, worth 8% of your grade.

Make sure your completed assignment passes all the asserts. This assignment also has hidden tests - which means that passing all the asserts you see does not guarantee that you have the correct answer! Make sure to double check and re-run your code to make sure it does what you expect, and that the variables you define end up with values you'd expect. 

### Quick Tips

Make sure you execute your code to define the functions you write, and then add a new cell to apply your function to different inputs, and check that you get the outputs you expect. 

If you're not sure where to start, look at the code in the test cases (in the asserts) for examples for what kind of inputs and outputs the function should take, and what kind of behaviour it should have.

Keep in mind that each question is mostly independent from every other - so if you get stuck on something, you can always move on to the next one, and come back to any that you have trouble with later.

## Setup

#### Code Imports

You must run the following cell before proceeding with the last part of the assignment. 



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

If you get stuck on anything, come back here, and talk to the Zen chatbot, to relax :)

Note: in this, and other, chatbot lines, running this code will start an open-ended while loop, that will interupt your code flow, until you explicity quit out of the conversation. If you want to be able to run all your code (from kernel `restart & run all`), then comment these lines back out when you are finished exploring them. 



{:.input_area}
```python
# Uncomment and run this cell to talk to a Zan Chatbot
#nltk.chat.zen.demo()
```


## Part 1: Functions

This part covers the basics of writing and using functions.

### Function Examples

The following are a couple examples of functions provided to you. 



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
# Test out using `basic_function`
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
# Test out using `more_complicated_function`
print(more_complicated_function('ab45b'))
```


### Q1 - Find max value  (0.5 points)

Write a function called `find_max`, that takes in a single parameter called `random_list`, which should be a list. 

This function will find the maximum (max) value of the input list, and return it. 

In particular this function will assume the list is composed of only positive numbers.

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


### Q2 - Square Everything  (0.5 points)

Write a function called `square_all` that takes an input called `collection` that you assume to be a list or tuple of numbers. 

This function should return a new `list`, which contains the square of each value in `collection`. 

To do so, you will write a loop inside the function, and also use the `append` method. 



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


## Part 2: Refactoring Code to Use Functions

'Refactoring' is the process of updating existing computer code, to keep the same outputs, but with a better internal organization and/or properties. 

We have already written a lot of code in previous assignments. However, since we did not yet have functions at our disposal, a lot of that code is not very easy to re-use. In this section we will refactor some code - rewriting (and extending) some code from previous assignments as functions, that will be easier to re-use. 

### Q3 - Calculator (0.5 points)

Let's start with the calculator functions that we did in a previous assignment. 

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

The goal of using functions is to be able to re-use them, as well as to apply and combine functions together. 

The cell below shows a couple examples of using our calculator functions that we have now defined. 



{:.input_area}
```python
# Add the multiplication of 2 and 3 to the multiplication of 3 and 4
number1 = multiplication(2, 3)
number2 = multiplication(3, 4)
output1 = summation(number1, number2)
print('Output1: \t', output1)

print('')

# Note that we can use functions as inputs to other functions too
#   Therefore, the above construction is equivalent to the following:
output2 = summation(multiplication(2, 3), multiplication(3, 4))
print('Output2: \t', output2)

# When we have something like above the functions as inputs gets evaluated first:
#   So, `multiplication(2, 3)` evaluates as 6, and `multiplication(3, 4)` evaluales as 12
#   This then reduces to calling `summation(6, 12)`
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

In practice, this will look like writing small and specific function to do particular things, and then using those functions in bigger functions.

### Q6 - Functions for Even & Positive Numbers (0.5 points)

Recall Q13 from A2, when we wanted to check a series of conditions across items in a list. 

We can consider that checking each of these conditions is really a separate task. 

When writing modular code, these separate tasks should therefore be organized as separate functions.

For question, write two functions, one called `is_even`, and the other `is_positive`. 

Each function should take in a single parameter, a number called `value`. 

- `is_even` will check if that number is even, and return `True` if so, and `False` otherwise. 
- `is_positive` will check if that number is positive, and return `True` if so, and `False` otherwise. 
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


## Part 3: Algorithms

This part covers working with algorithms.

### Q8 - Algorithms (0.5 points)

For each of the tasks below, indicate whether you think it is something that a human or a computer would be better at doing. 

- a) Recognize whether a sentence is supposed to be sarcastic or ironic. 
    - Answer in a variable called algo_q_a
- b) Reply to a question with information about a topic, with the exact wording from a wikipedia article
    - Answer in a variable called algo_q_b
- c) Keep answering messages for an arbitrarily long period of time, without demonstrating fatigue
    - Answer in a variable called algo_q_c
- d) Interpret the tone of what was said, to infer if someone is angry. 
    - Answer in a variable called algo_q_d
    
For each, try to think through if and how you could write an algorithm to do this task - and if you could not, what about it is hard to formalize. Use these questions to start to think through what might be easy and hard to program our chatbot to do. 



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

This part is an application of all the tools we have covered so far, to the problem of creating variations of traditional chatbots. 

A chatbot is a piece of software that tries to have a conversation with a human. While today's chatbots are powerful learners, traditional chatbots are much simpler. 

Traditional chatbots follow a "rule-based" approach that is defined for them (by you, the programmer). These rules can be very simple to very complex. These types of chatbots can handle simple entries but tend to fail with more complex ones.

#### Chatbot functions

In order to make our chatbot, we will create a series of functions that our eventual chatbot will use together to try and chat with a user. 

At the end, we will test that these functions do indeed allow us to have simple conversations with our chatbot.

Below are some more example chatbots to talk to. Remember to comment these lines back out if you want to be able to `Restart and Run All`.

### Example Chatbot - Eliza

The following demo is from the Natural Language ToolKit (nltk), a Python package available through Anaconda. 

Uncomment the line below, and run the code to be able to have a chat with Eliza. 



{:.input_area}
```python
# Run a demo of a chatbot, with Eliza
#nltk.chat.eliza.demo()
```


### Example Chatbot - Iesha

The following is another demo chatbot from nltk, this one called Iesha. 

As you check out the chatbot demos with Eliza and Iesha, see if you can notice any patterns that might help you figure out how they work (what kind of programming structures they use). 



{:.input_area}
```python
# Run a demo of a chatbot, with Iesha
#nltk.chat.iesha.demo()
```


### Q9 - Is It a Question (0.5 points)

The first thing we might want to know, given an input to a chatbot, is if the input is a question. 

We are going to use a very simple heuristic to check this: we will consider any input that has a question mark ('?') in it to be a question. 

Write a function called `is_question`, that takes as input a string called `input_string`. 

If there is a '?' in `input_string`, this function should return True, otherwise it should return False. 



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

To do so, write a function called `remove_punctuation`, which takes an input called `input_string`. 

This function should:
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


### Q11 - Preparing Text (0.5 points)

Now we want a more general function to prepare out text data for processing. 

Write a function called `prepare_text`, that takes as input `input_string`. 

Inside this function, using string methods and our new `remove_punctuation` function, this function should:
- make the string all lower case (use a string method called `lower`)
- remove all punctuation from the string (use your new function `remove_punctuation`)
- split the string into words (look for and use a string method called `split`)



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


### Q12 - Echo a Response (0.5 points)

Define a function, called `respond_echo`, that will return a string a specified number of times, with a given separator. 

This function should have the following inputs & outputs:

Inputs
* `input_string` - string, or None
* `number_of_echoes` - an integer
* `spacer` - a string

Output
* `echo_output` - string, or None

Because we will be using this function with our chatbot, we will also want to deal with the case where `input_string` is None. 

Inside this function:
- if `input_string` is not `None`:
    - set a variable `echo_output` to be  `input_string`, repeated the number of times specified by `number_of_echoes`, joined by the  `spacer`.
        - To do this, remember what '*' does to strings
- otherwise (if `input_string` is None), set `echo_output` to be `None`
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


### Example: random.choice

We want our chatbot to have some variation in it's responses - not only anwering the same thing.

So, want to be able to choose an output from a list of options, and we will use the `random.choice` function to so.

An example of using `random.choice` is offered below.



{:.input_area}
```python
# Given a list of inputs, randomly choose and return one of them
random.choice(['first option', 'second option', 'third option'])
```


### Q13 - Selector (0.5 points)

Next we will write a function that will help us select an output for the chatbot, based on the input it got.

The overall goal of this function is to take a list of words that we got as input, a list of words to check for if they appear in the input, and a list of possible outputs to return if something from the list to check is in the input list. 

Define a function, called `selector`, with the following inputs and outputs. 

Inputs:
* `input_list` - list
* `check_list` - list
* `return_list` - list

Output:
* `output` - string, or None

Inside this function:
- Initialize `output` to `None`
- Loop through each element in input_list
- Use a conditional to check if this element is in `check_list`
    - If it is, assign `output` as the returned value of calling the `random.choice` function on `return_list`
    - Also, break out of the loop
- At the end of the function, return `output`



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


### Q14 - String Concatenator Function (0.5 points)

Create a function that will concatenate two strings, combining them with a specified separator. 

To do so, write a function called `string_concatenator` which takes three parameters `string1`, `string2` and `separator` (all will be strings). 

Inputs
* `string1` - string
* `string2` - string
* `separator` - string

Output
* `output` - string, or None

Inside the function:
- Concatenate `string1` to `string2` with `separator` in between them. 
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


### Q15 - List to String (0.5 points)

Since we are often dealing with a list of strings, it would be useful to have a function to turn a list of string back into one single concatenated string. 

Write a function called `list_to_string` that takes two inputs: a list called `input_list` and a string called `separator`. 

This function will return a string that is each element of `input_list` concatenated together with each separated by the string `seperator`. 

For example, the following function call:
`list_to_string(['This', 'is', 'fun'], ' ')`

shoud return: 'This is fun'

Inputs
* `input_list` - list
* `separator` - string

Output
* `output` - string

Inside the function:
- Initialize `output` to be the first (index 0) element from `input_list`
- Loop through the rest of `input_list`, looping through the 2nd element (index 1), to the end
    - Within the loop, use `string_concatenator` to combine `output` with the current element, separated by `separator`
        - Assign the output of this to be the new value of `output`
- return `output`, which should now be a list of the elements of `input_list`, joined together into a string, separated by `separator`



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


### Q16 - End Chat (0.5 points)

The last thing we need is a way to end the chat with our chatbot. 

We will use the same convention that `nltk` uses - namely, that we will end the conversation if the word `quit` appears.

To be able to do so, write a function called `end_chat`, that will take as input a variable called `input_list`, and return `output`, which will be a boolean. 

`end_chat` should return True if the string 'quit' is in the list of strings, `input_list`, and return False otherwise. 



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
# This cell defines a collection of input and output things our chatbot can say and respond to

GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

COMP_IN = ['python', 'code', 'turing', 'computer']
COMP_OUT = ["Python is my mother.", \
            "Did you know I'm made of code!?", \
            "Computers are so magical", \
            "Do you think I'll pass the Turing test?"]

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I cannot talk about"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"
```


## Talking to our Chatbot

If everything has gone well with writing all the pieces of our chatbot above, the cell below should let us chat to our bot!

You don't have to write anything in the code block below. 

Do read through it though, to see how our chatbot works, and to see how all the functions you just wrote are used to create the chatbot. You don't have to understand everything about what happens here (this code is provided for you, and you don't have to add anything to it), but try to check through to see how it works, and how everything comes together. 

If anything seems to go weird, note that you can always interrupt the code from running with chat with kernel - interrupt from the menu. If this happens, it probably means there is some issue with one of the functions you wrote for the chatbot. 



{:.input_area}
```python
# Run this cell to talk to our chatbot

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
        outs = []
        
        # Check if the input looks like a greeting, return a greetings output if so
        outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))
        
        # Check if the input looks like a computer thing, return a computer related output if so
        outs.append(selector(msg, COMP_IN, COMP_OUT))
        
        # Check if the input looks like a joke, repeat a joke output if so
        outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))
        
        # Check if the input has some words we don't want to talk about, say that, if so
        #   Note: the last part of this is just a way to get which `NONO` word was used in msg
        #     You can ignore exactly how it does that, for now
        outs.append(string_concatenator(selector(msg, NONO_IN, NONO_OUT), [el for el in msg if el in NONO][0], ' '))
        
        # IF YOU WANT TO ADD MORE TOPICS TO RESPOND TO, YOU CAN ADD THEM IN HERE

        # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
        #   If so, we are going to randomly select an output from the set of outputs that are not None
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


### Extending Our Chatbot

You might notice that our chatbot, right now, is pretty limited in how many things it can respond to. It 

After you've explored chatting to the chatbot, you are done!

## The End!

This is the end of the assignment!
Have a look back over your answers, and also make sure to Restart & Run All from the kernel menu to double check that everything is working properly. 

When you are ready to submit your assignment, upload it to TritonED under Assignment-3.
