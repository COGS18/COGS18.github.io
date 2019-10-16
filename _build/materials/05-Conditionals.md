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
  url: /materials/06-DataTypes
  title: '06-DataTypes'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Course Announcements

- A1 is due Friday (10/11; 11:59 PM)
- Week 1 CodingLab and Lecture participation posted on Piazza
- A2 now available; due next Friday (10/18)

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


{:.output_stream}
```
This code executes if the condition evaluates as True.

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





{:.output_data_text}
```
True
```





{:.input_area}
```python
math = True

if math:
    print('True')
```


{:.output_stream}
```
True

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


{:.output_stream}
```
This code executes if the condition evaluates as False

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





{:.output_data_text}
```
False
```





{:.input_area}
```python
bool(None)
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
bool('')
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
my_value = 0

if my_value:
    print('True')
else: 
    print('False')
```


{:.output_stream}
```
False

```

## Conditional: `elif`

<div class="alert alert-success">
After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
</div>



{:.input_area}
```python
# what if you use all if statements
# will/can evaluate all print statements
condition_1 = True
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
if condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
if condition_1 and condition_2: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
```


{:.output_stream}
```
This code executes if condition_1 evaluates as True.
This code executes if condition_1 did not evaluate as True, but condition_2 does.
This code executes if both condition_1 and condition_2 evaluate as False

```



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


{:.output_stream}
```
This code executes if condition_1 did not evaluate as True, but condition_2 does.

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



{:.output_traceback_line}
```
  File "<ipython-input-28-aedfc0cec5db>", line 9
    elif condition_2:
       ^
SyntaxError: invalid syntax

```


## Conditionals With Value Comparisons

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>



{:.input_area}
```python
language = "R"

if language == "Python":
    print("Yay!")
elif language == "Perl" or language == "R":
    print("Oh no.")
else:
    print("Get yourself a programming language!")
```


{:.output_stream}
```
Oh no.

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


{:.output_stream}
```
Before Conditional
    if statement execution
After Conditional

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


{:.output_stream}
```
Paul

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


{:.output_stream}
```
I did Math

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


{:.output_stream}
```
I'm here.

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
