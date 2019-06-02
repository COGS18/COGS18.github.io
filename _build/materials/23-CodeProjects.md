---
interact_link: content/materials/23-CodeProjects.ipynb
download_link: assets/downloads/23-CodeProjects.ipynb.zip
pdf_link: assets/pdf/23-CodeProjects.pdf
layout: materials
title: '23-CodeProjects'
prev_page:
  url: /materials/22-CodeTesting
  title: '22-CodeTesting'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- Final Projects due Wed of finals week (6/12) by 11:59 PM
- Normal office hours this week Friday 3-5 PM
- Please fill out your CAPEs!
- Please fill out TA/IA feedback!

## Clicker Warm Up

Write a test function that checks the following piece of code:

- A) I did it!
- B) I think I did it!
- C) I'm lost.



{:.input_area}
```python
def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output
```




{:.input_area}
```python
### YOUR TEST
```


## Project Check-In


Do you have an idea of what you want to do for your project?

- A) Absolutely no Idea
- B) Some idea, but not sure
- C) Sort of 
- D) Fairly good idea
- E) I know exactly what I want to do

How much code do you have written for your project? 

- A) None 
- B) A little or some pseudocode
- C) Some 
- D) A lot 
- E) Most (I'm mostly or completely done)

How confident do you feel about wht you need to do to finish the project? 

- A) I have no idea what to do from here 
- B) I have some idea of how to finish the project
- C) I have a reasonable idea of what to do from here
- D) I have a very good idea of what to do
- E) I completely know / am basically finished

## Code Testing Review

Tests, when run, help identify code that will give if something has gone wrong. 

Why We Write Tests:

- ensure does does what it's supposed to
- system for checking things when you change / make updates in the future

### Four general types

1. **Smoke tests** - preliminary tests to basic functionality; checks if something runs (but not necessarily if it does the right thing) (sanity check) 
2. **Unit tests** - test functions & objects to ensure that they code is behaving as expected
3. **Integration tests** - tests functions, classes & modules interacting
4. **System tests** - tests end-to-end behavior 

### Not tests, but related
- asserts - make a statement of fact about code 
- static checks - check your code as you go that it behaves as expected
- argument validation - checks to see if the input given to a function

### Test Driven Development

- Ensures you go into writing code with a good plan / outline
- Ensures that you have a test suite, as you can not decide to neglect test code after the fact
- Note: when you write assignments for this class, you are effectively doing test-driven development

### Unit Tests

- one test for each "piece" of your code (each function, each class, each module, etc)
- passes silently if true
- assertion error if it fails
- help you resist the urge to assume computers will act how you think it will work 
- functions used with pytest start with `test_`

### `pytest`

- check if error raised when expected to be raised
- autorun all of your tests
- formal testing to your code/projects

#### Executing `pytest`

1. Look for any file called `test_...`
2. If everything works, silently moves along. 
4. For anything that fails, will alert you.

# Code Projects

- modular design
- minimal viable product
- rapid prototyping
- Project Organization
- refactoring

### Modular Design

<div class="alert alert-success">
Modular design, like modular programming, is the approach of designing and building things as independent modules. 
</div>

### Minimal Viable Product

<div class="alert alert-success">
A 'minimal viable product' is a product that contains the minimum amount of implemented features to use the code product - no more, no less.</div>

### Rapid Prototyping

<div class="alert alert-success">
Rapid prototyping is an approach for developing things in which you work on minimal prototypes and iterate on them quickly. 
</div>

#### Some examples

- Chatbot: start and end a chat
- Data Analysis: read a dataset in, make a basic plot
- Car Inventory: object with method that adds a car to the Inventory
- Artificial Agents: simple bot moves around randomly

## Project Organization

### Organizing Code

- **Notebooks**: good for interactive development
    - For when seeing the inputs and outputs of code running needs to be seen start to finish
    - file ends in `.ipynb`
- **Modules**: for storing mature Python code, that you can import
    - you don't *use* the functions in there, just define them
    - file ends in `.py`
- **Scripts**: a Python file for executing a particular task
    - this takes an input and does something start to finish
    - file ends in `.py`

### Project Workflow

Typical project workflow:

- Develop code interactively in a Jupyter notebook
- As functions & classes become mature, move them to Python files that you then `import`
    - As you do so, go back through them to check for code style, add documentation, and write some code tests
- At the end of a project, write a standalone script that runs the project

## Code Review

<div class="alert alert-success">
Code reviews is a process for systematically reviewing someone else's code. 
</div>

This is what you'll have the chance to do in coding lab this week!

## Refactoring

<div class="alert alert-success">
Refactoring is the process of restructuring existing computer code, without changing its external behaviour. 
</div>

Think of this as restructuring and final edits on your essay. 

**Nesting Functions** - If you have a whole bunch of functions, if statements, and for/while loops together within a single function, you probably want (need?) to refactor.

Clean functions accomplish a **single task**!

**DRY**: Don't Repeat Yourself

### Refactoring Example: Chatbot

## Clicker Question #1
How many "things" does this function accomplish?

- A) 0
- B) 1
- C) 2
- D) 3
- E) 4



{:.input_area}
```python
import random 

def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        # Check if the input is a question
        input_string = msg
        if '?' in input_string:
            question = True
        else:
            question = False

        # Check for an end msg 
        if 'quit' in input_string:
            out_msg = 'Bye!'
            chat = False
            
        # If we don't have an output yet, but the input was a question, 
        # return msg related to it being a question
        if not out_msg and question:
            out_msg = "I'm too shy to answer questions. What do you want to talk about?"

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])

        print('OUTPUT:', out_msg)
```




{:.input_area}
```python
have_a_chat()
```


### Refactored Example: Chatbot

What this function does:

1. takes an input
2. checks if input is a question
3. checks if input is supposed to end the chat
4. return appropriate response if question, end chat, or other

That's four different things! Functions should do a single thing...



{:.input_area}
```python
def get_input():
    """ask user for an input message"""
    
    msg = input('INPUT :\t')
    out_msg = None
    
    return msg, out_msg
```




{:.input_area}
```python
def is_question(input_string):
    """determine if input from user is a question"""
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output
```




{:.input_area}
```python
def end_chat(input_list):
    """identify if user says 'quit' in input and end chat"""
    
    if 'quit' in input_list:
        output = True
        chat = False
    else:
        output = False
        chat = True
        
    return output, chat
```




{:.input_area}
```python
def return_message(out_msg, question):
    # If we don't have an output yet, but the input was a question, 
    # return msg related to it being a question
    if not out_msg and question:
        out_msg = "I'm too shy to answer questions. What do you want to talk about?"

    # Catch-all to say something if msg not caught & processed so far
    if not out_msg:
        out_msg = random.choice(['Good.', 'Okay', 'Huh?', 'Yeah!', 'Thanks!'])
        
    return out_msg
```




{:.input_area}
```python
def have_a_chat():
    """Main function to run our chatbot."""
    
    chat = True

    while chat:

        # Get input message from the user
        msg, out_msg = get_input()
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Check for an end msg 
        out_msg, chat = end_chat(msg)
      
        # specify what to return
        out_msg = return_message(out_msg = out_msg, question=question)
        
        print('OUTPUT:', out_msg)
```




{:.input_area}
```python
have_a_chat()
```

