---
interact_link: content/assignments/A1-GettingStarted-answers.ipynb
download_link: assets/downloads/A1-GettingStarted-answers.ipynb.zip
layout: notebooks
title: 'Assignments'
prev_page:
  url: /labs/CL4-Exploring
  title: 'CL4-Exploring'
next_page:
  url: /assignments/A1-GettingStarted-answers
  title: 'A1-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Assignment 1: Getting Started

This assignment covers Variables, Operators & Conditionals.

This assignment is out of 10 points, worth 10% of your grade.

## How to complete assignments

Whenever you see:

```
# YOUR CODE HERE
raise NotImplementedError()
```

You need to replace this section with some code that answers the questions and meets the specified criteria. Make sure you remove the 'raise' line when you do this (or your notebook will raise an error, regardless of any other code, and thus fail the grading tests).

You should write the answer to the questions in those cells (the ones with `# YOUR CODE HERE`), but you can also add extra cells to explore / investigate things if you need / want to. 

Any cell with 'assert' statements in it is a test cell. You should not try to change or delete these cells. Note that there might be more than one assert that tests a particular question. 

If a test does fail, reading the error that is printed out should let you know which test failed, which may be useful for fixing it.

Note that some cells, including the test cells, may be read only, which means they won't let you edit them. If you cannot edit a cell - that is normal, and you shouldn't need to edit that cell.

## Tips & Tricks

The following are a couple tips & tricks that may help you if you get stuck on anything.

### Printing Variables

A reminder that you can (and should) print and check variables as you go.

This allows you to check what values they hold, and fix things if anything unexpected happens.



{:.input_area}
```python
# Define a variable
math_result = 2 * 4

# Print out the value(s) of a variable.
print(math_result)
```


### Restarting the Kernel

A reminder that sometimes if you run cells out of order, you can end up over-writing things in your namespace. 

If things seem to go weird, a good first step is to restart the kernel, which you can do from the kernel menu above.

Even if everything seems to be working, it's a nice check to 'Restart & Run All', to make sure everything runs properly in order.

## Example Question

Define a variable called `my_int` that stores the value 17. 



{:.input_area}
```python
# YOUR CODE HERE
my_int = 17
```




{:.input_area}
```python
# This is a test cell. It checks that the code you wrote does what it's supposed to
assert  my_int                     # This tests that a variable exists
assert  isinstance(my_int, int)    # This tests that a variable is of a particular type
assert  my_int == 17               # This tests that a variable has a specified value
```


## SETUP

Run the following cell before you start working on the assignment. 

This is going to make a helper folder on your computer, for some of the grading and checking things in this assignment. 

You do not need to interact with this folder maunally at all - everything is automatic.



{:.input_area}
```python
import os
if not os.path.exists('A1Code'):
    os.mkdir('A1Code')
```


## Part I - Defining Variables

First, we will start by defining some Python variables. 

### Q1 - Create Variables (1 point)

Create the following variables:
- a variable called `number` that stores the value 23
- a variable called `decimal` that stores the value 12.5
- a variable called `word` that stores the value 'cogs18'
- a variable called `truth` that stores the value True



{:.input_area}
```python
# Create the variables

# YOUR CODE HERE
number = 23
decimal = 12.5
word = "cogs18"
truth = True
```




{:.input_area}
```python
## TESTS FOR Q1

# Check that variable `number` is an int, and has the correct value
assert isinstance(number, int)
assert number == 23
```




{:.input_area}
```python
## TESTS FOR Q1

# Check that variable `decimal` is a float, and has the correct value
assert isinstance(decimal, float)
assert decimal == 12.5
```




{:.input_area}
```python
## TESTS FOR Q1

# Check that variable `words` is a string, and has the correct value
assert isinstance(word, str)
assert word == "cogs18"
```




{:.input_area}
```python
## TESTS FOR Q1

# Check that variable `truth` is a boolean, and has the correct value
assert isinstance(truth, bool)
assert truth == True
```


## Part II - Operations

### Q2 - Python as a Calculator (0.75 points)

Do the following calculations:
- Set `ans_1` as the result of int_1 multiplied by int_2
- Set `ans_2` as the result of float_1 divided by float_2, with int_2 then added
- Set `ans_3` as the result of the remainder of int_1 divided by int_2



{:.input_area}
```python
# These variables provided for you
int_1 = 47
int_2 = 12

float_1 = 47.5
float_2 = 19.0
```




{:.input_area}
```python
# YOUR CODE HERE
ans_1 = int_1 * int_2
ans_2 = float_1 / float_2 + int_2
ans_3 = int_1 % int_2
```




{:.input_area}
```python
## TESTS FOR Q2  [Note: Includes Hidden Tests]

assert isinstance(ans_1, int)

```




{:.input_area}
```python
## TESTS FOR Q2  [Note: Includes Hidden Tests]

assert isinstance(ans_2, float)

```




{:.input_area}
```python
## TESTS FOR Q2  [Note: Includes Hidden Tests]

assert isinstance(ans_3, int)

```


### Q3 - String Manipulations (0.75 points)

Using the strings provided, concatenate them together into the string `Python is fun!`. 

Save this result to a variable called `str_output`. 

Note: make sure to add spaces between words when concatenating together. 



{:.input_area}
```python
# These variables provided for you
str_1 = "Python"
str_2 = "is"
str_3 = "fun!"
```




{:.input_area}
```python
# YOUR CODE HERE
str_output = str_1 + ' ' + str_2 + ' ' + str_3
```




{:.input_area}
```python
## TESTS FOR Q3

assert isinstance(str_output, str)
assert str_output == "Python is fun!"
```


### Q4 - Boolean Comparisons (1 point)

Using the variables provided, do the following boolean logical comparisons:
- Define `bool_comp_1` to be the logical `and` of `bool_1` and `bool_2`
- Define `bool_comp_2` to be the logical `or` of  `bool_1` and `bool_2`



{:.input_area}
```python
# These variables provided for you
bool_1 = True
bool_2 = False
```




{:.input_area}
```python
# YOUR CODE HERE
bool_comp_1 = bool_1 and bool_2
bool_comp_2 = bool_1 or bool_2
```




{:.input_area}
```python
## TESTS FOR Q4 [Note: Includes Hidden Tests]
assert isinstance(bool_comp_1, bool)

```




{:.input_area}
```python
## TESTS FOR Q4 [Note: Includes Hidden Tests]
assert isinstance(bool_comp_2, bool)

```


### Q5 - Value Comparisons (1 point)

Do the following value comparisons:
- Check if the value stored in `comp_val_1` is less than or equal to the value stored in `comp_val_2`
    - Store the result of this comparison to variable called `comp_1`


- Check if the value stored in `comp_val_3` is not equal to (is different from) the value stored in `comp_val_4`
    - Store the result of this comparison to variable called `comp_2`



{:.input_area}
```python
# These variables provided for you
comp_val_1 = 13
comp_val_2 = 17
comp_val_3 = 23
comp_val_4 = 22
```




{:.input_area}
```python
# YOUR CODE HERE
comp_1 = comp_val_1 <= comp_val_2
comp_2 = comp_val_3 != comp_val_4
```




{:.input_area}
```python
## TESTS FOR Q5 [Note: Includes Hidden Tests]
assert isinstance(comp_1, bool)

```




{:.input_area}
```python
## TESTS FOR Q5 [Note: Includes Hidden Tests]
assert isinstance(comp_2, bool)

```


## Part III - Conditionals

### Q6 - Conditionals With Booleans (1 point)

Write a conditional that tests a boolean variable `status`, specifically:
- if `status` evaluates as `True`, set the variable `output` as the string "GOOD"
- else (meaning `status` must evaluate as `False`), set the variable `output` as the string "BAD"



{:.input_area}
```python
%%writefile A1Code/q6_code.py
# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if status:
    output = "GOOD"
else:
    output = "BAD"
```




{:.input_area}
```python
## TESTS FOR Q6

# Set stats - check for True case
status = True

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q6_code.py  
assert output == "GOOD"
```




{:.input_area}
```python
## TESTS FOR Q6

# Set stats - check for False case
status = False

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q6_code.py  
assert output == "BAD"
```


### Q7 - Conditionals With Comparisons (1 point)

Consider a case in which you are running an experiment, with multiple groups of subjects, including young subjects and old subjects. 

Based on the subjects age group, you want to do a different analysis - specifically if they are in the old group.

Write a conditional with an `if` and an `else`:
- The `if` should check if the variable `subj_age` has the value `'old'` (a string).
    - If so, it should set the variable `change_analysis` to the value `True` (a boolean)
    
    
- Else, the variable `change_analysis` should be set to False (a boolean)



{:.input_area}
```python
%%writefile A1Code/q7_code.py
# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if subj_age == 'old':
    change_analysis = True
else:
    change_analysis = False
```




{:.input_area}
```python
## TESTS FOR Q7

# Set subj_age to old
subj_age = 'old'

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q7_code.py  

# Check that code 
assert change_analysis
assert isinstance(change_analysis, bool)
```




{:.input_area}
```python
## TESTS FOR Q7

# Change subj_age
subj_age = 'young'

# Re-run code and make sure the conditional still works
%run -i ./A1Code/q7_code.py
assert not change_analysis
assert isinstance(change_analysis, bool)
```


### Q8 - Conditionals With Multiple Options (1 point)

Sometimes we may need to check multiple conditions, with many (more than two) possibilities.

Create a conditional with the following outline:
- If `check_1` and `check_2` variables are both True, it should set the value of a variable `outcome` to the string 'BOTH'
- Elif `check_1` is True and `check_2` is False, it should set the value of a variable `outcome` to the string 'ONE'
- Elif `check_1` is False and `check_2` is True, it should set the value of a variable `outcome` to the string 'TWO'
- Else (meaning both must be False), it should set the value of a variable `outcome` to the string 'NEITHER'



{:.input_area}
```python
%%writefile A1Code/q8_code.py
# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if check_1 and check_2:
    outcome = 'BOTH'
elif check_1 and not check_2:
    outcome = 'ONE'
elif not check_1 and check_2:
    outcome = 'TWO'
else:
    outcome = 'NEITHER'
```




{:.input_area}
```python
## TESTS FOR Q8

# Check 'BOTH' case
check_1 = True
check_2 = True

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q8_code.py
assert outcome == 'BOTH'
```




{:.input_area}
```python
## TESTS FOR Q8

# Check 'ONE' case
check_1 = True
check_2 = False

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q8_code.py
assert outcome == 'ONE'
```




{:.input_area}
```python
## TESTS FOR Q8

# Check 'TWO' case
check_1 = False
check_2 = True

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q8_code.py
assert outcome == 'TWO'
```




{:.input_area}
```python
## TESTS FOR Q8

# Check 'NEITHER' case
check_1 = False
check_2 = False

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q8_code.py
assert outcome == 'NEITHER'
```


## Part IV - Putting it all together

### Q9 - Multiple Cases: Experiment Example (1 point)

Lets revisit the setup of Q7 - in which we wanted to set a variable to indicate if a subject in an experiment was in a particular group, and thus required different processing. In this question we will extend that premise, by writing a set of conditionals to mark an interaction between subject's age and score. 

For example, it is common for behavioural performance to decrease with age. However, some subjects do not seem to show this behavioural deficit with age. Investigating such 'super-ages' could be useful for learning about the cognitive decline of aging.

Write a conditional that does the following:
- If the variable `subj_age` has the value `old` and the variable `score` is greater than 25:
    - set the variable `subj_status` to the string 'Super Ager'
    
    
- Elif the variable `subj_age` has the value `old` and the variable `score` is less than or equal to 25:
    - set the variable `subj_status` to the string 'Normal Ager'
    
    
- Elif the variable `subj_age` has the value `young` and the variable `score` is greater than 25:
    - set the variable `subj_status` to the string 'Normal Youth'
    
    
- Elif the variable `subj_age` has the value `young` and the variable `score` is less than or equal to 25:
    - set the variable `subj_status` to the string 'Bad Youth'



{:.input_area}
```python
%%writefile A1Code/q9_code.py
# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if subj_age == 'old' and score > 25:
    subj_status = 'Super Ager'
elif subj_age == 'old' and score <=25:
    subj_status = 'Normal Ager'
elif subj_age == 'young' and score > 25:
    subj_status = 'Normal Youth'
elif subj_age == 'young' and score <= 25:
    subj_status = 'Bad Youth'
```




{:.input_area}
```python
## TESTS FOR Q9

subj_age = 'old'
score = 28

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q9_code.py
assert subj_status == 'Super Ager'
```




{:.input_area}
```python
## TESTS FOR Q9

subj_age = 'old'
score = 22

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q9_code.py
assert subj_status == 'Normal Ager'
```




{:.input_area}
```python
## TESTS FOR Q9

subj_age = 'young'
score = 29

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q9_code.py
assert subj_status == 'Normal Youth'
```




{:.input_area}
```python
## TESTS FOR Q9

subj_age = 'young'
score = 21

# This line is a way to run & re-run the code you wrote
%run -i ./A1Code/q9_code.py
assert subj_status == 'Bad Youth'
```


### Q10 - Creating a Calculator (1.5 points)

Finally we will write a flexible calculater program, that performs multiple operations (addition, subtraction, multiplication and division) on pairs of numbers. To do so, the code will use a string variable `operation` that indicates with operation to perform, and two numerical values, `num1` and `num2`, upon which the operation is performed. The calculator will assign the output of it's calculation to a variable called `answer`. 

To create this calculater, we will be using conditionals. 

In particular, create a calculator such that:
- if `operation` has the value 'add', then `answer` gets set as the sum of `num1` and `num2`
- elif `operation` has the value 'subtract', then `answer` gets set as the substraction of `num2` from `num2`
- elif `operation` has the value 'multiply', then `answer` gets set as the multiplication of `num1` and `num2`
- elif `operation` has the value 'divide', then `answer` gets set as the division of `num1` by `num2`

For an example, with the following variables to start with:

```
operation = 'multiply'
num1 = 2
num2 = 3
```
We should expect our program to execute and set the variable `answer` to be `6`.



{:.input_area}
```python
%%writefile A1Code/q10_code.py

# YOUR CODE HERE
if operation == 'add':
    answer = num1 + num2
elif operation == 'subtract':
    answer = num1 - num2
elif operation == 'multiply':
    answer = num1 * num2
elif operation == 'divide':
    answer = num1 / num2
else:
    answer = None
```




{:.input_area}
```python
# Set numbers for tests
num1 = 21
num2 = 3
```




{:.input_area}
```python
## TESTS FOR Q10

# Test for sum
operation = 'add'
%run -i ./A1Code/q10_code.py
assert answer == 24
```




{:.input_area}
```python
## TESTS FOR Q10

# Test for subtract
operation = 'subtract'
%run -i ./A1Code/q10_code.py
assert answer == 18
```




{:.input_area}
```python
## TESTS FOR Q10

# Test for multiply
operation = 'multiply'
%run -i ./A1Code/q10_code.py
assert answer == 63
```




{:.input_area}
```python
## TESTS FOR Q10

# Test for divide
operation = 'divide'
%run -i ./A1Code/q10_code.py
assert answer == 7
```




{:.input_area}
```python
## TESTS FOR Q10

# Test unrecognized operation
operation = 'not a thing'
%run -i ./A1Code/q10_code.py
assert answer == None
```


## The End!

This is the end of the assignment!

Have a look back over your answers, and also make sure to `Restart & Run All` from the kernel menu to double check that everything is working properly. When you are ready to submit your assignment, validate and submit on DataHub!
