---
interact_link: content/materials/04-Conditionals.ipynb
download_link: assets/downloads/04-Conditionals.ipynb.zip
pdf_link: assets/pdf/04-Conditionals.pdf
layout: materials
title: '04-Conditionals'
prev_page:
  url: /materials/03-Operators
  title: '03-Operators'
next_page:
  url: /materials/05-Collections
  title: '05-Collections'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### Course Announcements

- **A1** is due Mon (7/6; 11:59 PM)

**Now Available**
- **CL2** (due next Wed 7/8)
- **A2** (due Mon 7/13)
    - `append` - 1 or 2 places where you are asked to do something on an assignment not explicitly taught in class
    

### Survey Summary:

- Thank you!
- N = 89
- ~60% of class has never programmed before
    - 10% Python
    - 17% Java
    - 14% C/C++
- Common hobbies: reading, sports, video games, internships/work

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


#### Clicker Question #1

Replace `---` below with something that will print 'True'

- A) I did it!
- B) I think I did it!
- C) I tried but am stuck.
- D) I'm unsure where to start



{:.input_area}
```python
# can evaluate boolean expression with bool
bool(2 + 2 >= 4)
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


#### Clicker Question #2

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
language = "Perl"

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


#### Clicker Question #3

What will the following code snippet print out:



{:.input_area}
```python
beatle = True

if not beatle:
    print("John")
elif beatle:
    print("Paul")
elif beatle:
    print("George")
else:
    print("Ringo")
```


{:.output_stream}
```
Paul

```

- A) John 
- B) Paul, George, Ringo 
- C) Paul 
- D) Paul, George 
- E) Ringo

#### Clicker Question #4

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

#### Clicker Question #5

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

## A1: Clarification/Demo

- variables created in `%%writefile` will be stored in file
- these variables will overwrite variables created in test cells
- your assignments should run from top to bottom without you having to change anything



{:.input_area}
```python
%%writefile new_file.py
# You can ignore the line above - it is used to help check your code

a = 3
b = 'new'
print(status)
```




{:.input_area}
```python
status = True

%run -i new_file.py  
assert status == False
```


### Assignment Reminders

- To make life easier on your wonderful TAs:
    - Please don't change the assignment file name 
    - Please don't delete/modify cells in assignment (other than cells where you add code)
    - You can add cells and include `print()` statements to check your work.

- There are **hidden assert cells**
    - If you follow instructions and pass all the asserts provided, you will receive credit
    - We cannot give points back for typos

- You *must* **submit your assignment** for it to be graded.
    - best to "Kernel > Restart & Run All" before you submit
        - this executes code in your notebook from top to bottom
        - You can also use "Validate" button at top. Note that for A4 you *may* get an error b/c that notebook takes a while to run    
    - submit as many times as you like
        - most recent submission is graded
        - *but*, if you submit before deadline and again after, it will be late

- variables defined in `%%writefile` cells will overwrite variables in test (`assert`) cells
