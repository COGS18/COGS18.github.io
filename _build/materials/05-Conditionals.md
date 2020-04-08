---
interact_link: content/materials/05-Conditionals.ipynb
download_link: assets/downloads/05-Conditionals.ipynb.zip
pdf_link: assets/pdf/05-Conditionals.pdf
layout: materials
title: '05-Conditionals'
prev_page:
  url: /materials/04-Operators
  title: '04-Operators'
next_page:
  url: /
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Course Announcements

- A1 is due Mon (4/13; 11:59 PM)
- Coding Lab today!
    - Submit CL2 by 11:59 PM tonight
    - The 9 AM coding lab a _tad_ too crowded last week 

### CALPIRG

Looking to get involved this spring?? [Volunteer or Intern with CALPIRG](https://actionnetwork.org/forms/volunteerinternship-opportunities-with-calpirg-students-at-ucsd?source=direct_link&) Students at UCSD! 

CALPIRG is our statewide student-directed and student-funded organization. For over 45 years we’ve worked to protect our environment and fight climate change, address food insecurity, and help students vote. Students have the power to shape the future we will inherit. We organize on UC campuses and statewide to win real, concrete victories.


We know things are hectic right now, but we are still here to help and fight on behalf of the public interest! If you want to get involved this spring- you can! We have VIRTUAL internships and volunteer opportunities!  

This Spring, we are working to:

- turn out the youth vote in the 2020 elections to make sure we get our voices heard on the issues we care about. We are the largest and most diverse generation alive and we have the power to elect the next generation of leaders who will fight for our vision for the future.
- Protect our oceans from single use plastics by passing AB 1080 and SB 54 in the state legislature 
- Make textbooks affordable 
- Work on our COVID-19 Rapid Response Campaign, currently focused on calling for more testing. 

Informational Video here: https://drive.google.com/file/d/1K9GWwr1OSjOa8CgBQ6S1RVFPN9EBFLjD/view

If you want to make a difference and learn skills, consider volunteering or taking an internship with CALPIRG! [Fill out this form!!!](https://actionnetwork.org/forms/volunteerinternship-opportunities-with-calpirg-students-at-ucsd?source=direct_link&)



# Conditionals

- `if`
- `elif`
- `else`

## Conditionals: `if`

<div class="alert alert-success">
Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
</div>



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
```


### Clicker Question #1

Replace `---` below with something that will print 'True'

- A) I did it!
- B) I think I did it!
- C) I tried but am stuck.
- D) I'm unsure where to start



{:.input_area}
```python
# can evaluate boolean expression with bool
bool(2 + 2)
```




{:.input_area}
```python
math = ---

if math:
    print('True')
```


## Conditional: `else`

<div class="alert alert-success">
After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
</div>



{:.input_area}
```python
condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')
```


### Clicker Question #2

Replace `---` below with something that will print 'False'.

- A) I did it!
- B) I think I did it!
- C) I tried but am stuck.
- D) I'm unsure where to start



{:.input_area}
```python
bool(0)
```




{:.input_area}
```python
bool(None)
```




{:.input_area}
```python
bool('')
```




{:.input_area}
```python
my_value = ---

if my_value:
    print('True')
else: 
    print('False')
```


## Conditional: `elif`

<div class="alert alert-success">
After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
</div>



{:.input_area}
```python
condition_1 = False
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
```


### `elif` without an `else`

An else statement is not required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.



{:.input_area}
```python
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
```


### `elif` *after* an `else` does not make sense

The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).



{:.input_area}
```python
## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
```


## Conditionals With Value Comparisons

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>



{:.input_area}
```python
language = "R"

if language == "Python" or language == "R":
    print("Yay!")
elif language == "Perl":
    print("Hmmmmmmm")
else:
    print("Get yourself a programming language!")
```




{:.input_area}
```python
# Exploring conditionals
number = 4

print('Before Conditional')
 
if number < 5:
    print('    if statement execution')
elif number > 5:
    print('    elif statement execution')

print('After Conditional')
```


### Clicker Question #3

What will the following code snippet print out:



{:.input_area}
```python
if False:
    print("John")
elif True:
    print("Paul")
elif True:
    print("George")
else:
    print("Ringo")
```


- A) John 
- B) Paul, George, Ringo 
- C) Paul 
- D) Paul, George 
- E) Ringo

### Clicker Question #4

What will the following code snippet print out:



{:.input_area}
```python
if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")
```


- A) I did Math 
- B) I broke Math
- C) I didn't do math
- D) This code won't execute

### Clicker Question #5

What will the following code snippet print out:



{:.input_area}
```python
conditional = False
python = "great"

if conditional:
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")
```


- A) Yay Python!
- B) Oh no.
- C) I'm here.
- D) This code won't execute

## Properties of conditionals

- All conditionals start with an `if`, can have an optional and variable number of `elif`'s and an optional `else` statement
- Conditionals can take any expression that can be evaluated as `True` or `False`. 
- At most one component (`if` / `elif` / `else`) of a conditional will run
- The order of conditional blocks is always `if` then `elif`(s) then `else`
- Code is only ever executed if the condition is met
