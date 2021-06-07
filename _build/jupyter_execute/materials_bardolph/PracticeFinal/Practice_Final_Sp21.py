# COGS 18 - Final Exam

This is the practice final exam for Spring 2021. It covers topics through the end of the course.

This exam is out of 0 points, but the real final will be worth 19 points (19% of your grade). 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~2-3h.
- There will be a 48+ hour window during which you can complete this exam.
- If it takes you longer than 3h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond (Campuswire, Discord, Chegg, any similar site)
    - viewing exam questions from a message board (as described above)
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 48+ hours straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

### Q0 - Honor Code

In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:

>I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.


### BEGIN SOLUTION
honor_code = True
### END SOLUTION

assert honor_code

## Part 1: Functions, Modules, & Code Style (10 points)

### Q1 - `chatbot` module (0.5 points)

Notice that in the folder with your exam there are two .py files provided. 

- `chatbot.py` includes a few functions for the module you'll be working with and editing throughout this exam. Go ahead and open this file now and take a glance at the code. Nothing you need to change yet. The exam will walk you through the steps needed.
- `chatbot_tests.py` will (eventually) include your test functions. We'll get to those later.

For now, import the `chatbot` module so that `chat.have_a_chat()` executes and allows you to have a chat. (Note that `'quit'` will allow you to end the chat.)

### BEGIN SOLUTION
import chatbot as chat
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your work (optional)

assert chat
### BEGIN HIDDEN TESTS
assert callable(chat.have_a_chat)
### END HIDDEN TESTS

chat.end_chat('this has quit in the middle')

### Q2 - `about_ucsd` function (2.5 points)

While our chatbot functions, it's pretty generic right now, so let's help make it a bit more interesting. Write a function in the cell below called `about_ucsd()`. 

This function will determine if the input is about UCSD.

- It should have a single parameter: `input_string`.
- The function should detect if the `input_string` contains any of the following: `'UCSD', 'ucsd', 'UC San Diego', or 'University of California, San Diego'`.
    - If it contains any of the above, the function should `return` `True`. 
    - otherwise, the function should `return` False.
    
Be sure to use good code style here.

### BEGIN SOLUTION
def about_ucsd(input_string):
    
    to_check = ['UCSD', 
               'ucsd', 
               'UC San Diego', 
               'University of California, San Diego']
    out = any(val in input_string for val in to_check) 
    
    return out
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your work (optional)

assert about_ucsd
### BEGIN HIDDEN TESTS
# returns false
assert not about_ucsd('hi')
### END HIDDEN TESTS

assert callable(about_ucsd)
### BEGIN HIDDEN TESTS
# returns True
assert about_ucsd('ucsd') 
assert about_ucsd('UCSD') 
assert about_ucsd('UC San Diego') 
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- defined correctly; single input (**0.25 points**)
- specified list (or other) to check correctly (**0.25 points**)
- checks list correctly to return boolean (**0.25 points**)
- has return statement (**0.25 points**)
- adheres to good code style (**0.5 points**)

=== END MARK SCHEME ===

### Q3 - `about_ucsd` to `chatbot` module (1 point)

Copy your `about_ucsd` function to the `chatbot` module. Save the changes to the `chatbot.py` file. 

Then, restart your kernel, and rerun your code from Q1 to `import` the module. 

Note, you do not need to write any code in this notebook for this question, but you can use the cell below to be sure you have accomplished the task correctly.

# BE SURE YOUR ANSWER IS IN THE MODULE
# but you can use this cell to test/execute/check your work (optional)

# tests to ensure Q3 is done correctly
### BEGIN HIDDEN TESTS
import chatbot as chat
assert not chat.about_ucsd('hi')
assert chat.about_ucsd('UCSD')
### END HIDDEN TESTS

### Q4 - Code Style (3.5 points)

At this point, you've got a few functions in your `chatbot` module; however, if you look at the code, you'll notice that some of the functions don't have very good code style. 

For this question, improve the code style, using what we discussed in class to improve the readiability and style of the `is_question()` and `end_chat()` functions.

Note, you do not need to write any code in this notebook for this question. All work will occur in `chatbot.py`

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

`is_question()`
- spacing around operators fixed (**0.5 points**)
- variable names improved (**0.5 points**)
- line spacing improved (**0.5 points**)
- if/else on separate lines (**0.5 points**)

=== END MARK SCHEME ===

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

`end_chat()`
- spacing around operators fixed (**0.5 points**)
- variable names improved (**0.5 points**)
- if/else on separate lines (**0.5 points**)

=== END MARK SCHEME ===

### Q5 - editing `return_message` and `have_a_chat` (2.5 points)

At this point, you've written your `about_ucsd()` function and moved it into the `chatbot` module; however, its functionality has not *yet* been incorporated into the chatbot. 

Be sure you understand the code of all of the functions provided. 

Then, within the `chatbot.py` module, edit `return_message()` using the following approach:

- has three input parameters: `out_msg`, `question`, `ucsd`
    - `ucsd` will be a boolean indicating `True` if the user mentioned UCSD and `False` otherwise
- has the same functionality as provided originally, *with the following addition*: 
    - if `question` is `False` and `about_ucsd()` is `True`, this function will `return` a response at random from the list of `ucsd_facts` provided below. 

Finally, in the `have_a_chat` function, edit `return_message` as needed and incorporate `about_ucsd()` such that if the user mentions UCSD (as specified in Q2), the chatbot will return a `ucsd_facts` at random.

Note: no code needs to be written in the notebook here. All changes will be made in `chatbot.py`

ucsd_facts = ['UCSD sits on the ancestral homelands of the Kumeyaay Nation.',
              'UCSD has more than 220,000 Eucalyptus trees on its campus.',
              'UCSD was founded in 1960.',
              'UCSD receives more than $1B in research funding annually.',
              'UCSD has more than 130 different majors and more than 40,000 students.'
             ]

# BE SURE YOUR ANSWER IS IN THE MODULE
# but you can use this cell to test/execute/check your work (optional)

# check that chatbot works with questions
### BEGIN HIDDEN TESTS
import chatbot as chat
assert chat.return_message(out_msg=None, question=True, ucsd=False) == "I'm too shy to answer questions. What do you want to talk about?"
### END HIDDEN TESTS

# check that chatbot works when UCSD is mentioned
### BEGIN HIDDEN TESTS
ucsd_facts = ['UCSD sits on the ancestral homelands of the Kumeyaay Nation.',
              'UCSD has more than 220,000 Eucalyptus trees on its campus.',
              'UCSD was founded in 1960.',
              'UCSD receives more than $1B in research funding annually.',
              "UCSD has more than 130 different majors and more than 40,000 students."
             ]
assert chat.return_message(out_msg=None, question=False, ucsd=True) in ucsd_facts
### END HIDDEN TESTS

## Part 2: Code Documentation (5 points)

### Q6 - Code Comments (2 points)

At this point, your chatbot is fully functional (for the purposes of this exam). Go through your module and be sure that all functions (both the ones provided and the ones your wrote/edited) have sufficient code comments.

Note: Nothing has to be done in this notebook. All changes will be in `chatbot.py`.

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- sufficient good code comments throughout module (**2 points**)
    - if *too* many comments (**-0.5 points**)  
    - if comments don't explain code's logic (**-1 point**)
    
=== END MARK SCHEME ===

### Q7 - `numpy`-style docstrings (3 points)

Add `numpy`-style docstrings to the `is_question`, `end_chat`, and `return_message` functions within `chatbot.py`

Note: Nothing has to be done in this notebook. All changes will be in `chatbot.py`.

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- all (3) functions have `numpy`-style docstrings (**3 points**)
    - if not numpy-style but has docstrings (-1.5)

=== END MARK SCHEME ===

## Part 3: Code Testing (4 points)

### Q8 - Code tests (4 points)

`chatbot_tests.py` has been provided for you, but it's empty. 

Add three test functions to test the functions: `is_question()`, `end_chat()`, and `return_message()` from the `chatbot` module.

Each test function should have at least three `assert` statements and should test the functionality of a single function.

Remember that you'll want to consider what needs to be `import`ed at the top of your `chatbot_tests.py` file.

Note: Nothing has to be done in this notebook. All changes will be in `chatbot_tests.py`.

# BE SURE TEST FUNCTIONS ARE IN `chatbot_tests` 
# but feel free to test out here

# tests to ensure test functions pass silently
# uses pytest
### BEGIN HIDDEN TESTS
out = !pytest chatbot_tests.py
assert out.grep("ERRORS") == []
assert out.grep("FAILED") == []
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- (3) test functions are there with correct name (**1 point**)
- each test function contains three asserts that test functionality (**1 point**)

=== END MARK SCHEME ===

### Final Exam complete!

Good work - you're done with the final exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.