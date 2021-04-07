**Course Announcements**

**Due Dates**
- CL2 due tonight (11:59 PM)
- A1 due Monday (11:59 PM)

**Survey (N=115)** 
- You should have gotten an email reply from me with a PS specific to you
- Time zones: 80% in PST; 9% in Eastern Asia
- 67% have never programmed before
- Hobbies: Reading, gaming, Netflix/TV/movies, beach, sleep, music, art
- Futures: psychologist, happy, successful, content, physician, entrepreneur

**Q&A**

Q: In the lecture notes, it was mentioned that operators "and", "or", and "not" will return the booleans "True" and "False." Based on this, why does the code " 'a' and 'b' " not return a boolean when we are using the "and" operator?  
A: Great question - this was a mistake! I will fix this in the notes to read "Python has <code>and</code>, <code>or</code> and <code>not</code> for boolean logic. These operators often return booleans, but can return any Python value." Apologies for error.

Q: when using `%%writefile`  to create a new file, is it possible to correct the mistake without making another file ?  
A: So, when you re-run that cell, it will not create a new file. It will update what was previously in that file with the new code....storing it in the same file.

Q: How am I able to delete a cell after adding it in the wrong spot? Also, how can I switch a code cell(the default for mine) to a markdown cell?  
A: Keyboard shortcuts can be really helpful here. To delete a cell, click to the left of the cell you want to delete to select it and then type "D" twice on your keyboard. To toggle a code cell to markdown, select the cell by clicking to the left of the cell and typing "M" once on your keyboard. For the reverse (markdown -> code), it's "Y" on your keyboard. (Alternatively, you can select the cell and choose from the drop-down menu along the top to choose markdown or code. For deleting a cell, this is in the Edit menu at top.)

Q: We've learned a lot of operations already so how do you recommend we organize this information for exams and assignments? A list? Chart?  
A: Honestly, I'd recommend learning them/committing them to memory so that you don't have to look them up each time you want to use them. But, of course that takes time, If it were me (and there are lots of possible solutions), I would make a "cheat sheet" - a single paper (or single screen on a computer) where all of the opertaors are organized with generally what they do. These sorts of [cheat sheets](https://www.pythoncheatsheet.org/) exist...but sometimes students learn best by making their own!

# Conditionals

- `if`
- `elif`
- `else`

## Conditionals: `if`

<div class="alert alert-success">
Conditionals are statements that check for a condition, using the <code>if</code> statement, and then only execute a set of code if the condition evaluates as <code>True</code>.
</div>

condition = True

if condition:
    print('This code executes if the condition evaluates as True.')

# equivalent to above
if condition == True:
    print('This code executes if the condition evaluates as True.')

#### Clicker Question #1

Replace `---` below with something that will print 'True'

- A) I did it!
- B) I think I did it!
- C) I tried but am stuck.
- D) I'm unsure where to start

math = ---

if math:
    print('True')

## Conditional: `else`

<div class="alert alert-success">
After an <code>if</code>, you can use an <code>else</code> that will run if the conditional(s) above have not run.
</div>

condition = False

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')

#### Clicker Question #2

Replace `---` below with something that will print 'False'.

- A) I did it!
- B) I think I did it!
- C) I tried but am stuck.
- D) I'm unsure where to start

my_value = ---

if my_value:
    print('True')
else: 
    print('False')

## Conditional: `elif`

<div class="alert alert-success">
After an <code>if</code> statement, you can have any number of <code>elif</code>`s (meaning 'else if') to check other conditions.
</div>

condition_1 = False
condition_2 = True

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')

### `elif` without an `else`

An else statement is not required, but if both the `if` and the `elif` condtions are not met (both evaluate as `False`), then nothing is returned.

condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')

### `elif` *after* an `else` does not make sense

The order will always be `if`-`elif`-`else`...with only the `if` being required. If the `elif` is at the end...it will never be tested, as the `else` will have already returned a value once reached (and thus Python will throw an error).

## THIS CODE WILL PRODUCE AN ERROR
condition_1 = False
condition_2 = False

if condition_1:
    print('This code executes if condition_1 evaluates as True.')
else: 
    print('This code executes if both condition_1 and condition_2 evaluate as False')
elif condition_2:
    print('This code executes if condition_1 did not evaluate as True, but condition_2 does.')

## Conditionals With Value Comparisons

<div class="alert alert-success">
Any expression that can be evaluated as a boolean, such as value comparisons, can be used with conditionals.
</div>

language = "s"

if language == "Python" or language == "R":
    print("Yay!")
elif language == "Perl":
    print("Hmmmmmmm")
else:
    print("Get yourself a programming language!")

# Exploring conditionals
number = 4

print('Before Conditional')
 
if number < 5:
    print('    if statement execution')
elif number > 5:
    print('    elif statement execution')

print('After Conditional')

#### Clicker Question #3

What will the following code snippet print out:

condition = False

if condition:
    print("John")
elif not condition:
    print("Paul")
elif not condition:
    print("George")
else:
    print("Ringo")

- A) John 
- B) Paul, George, Ringo 
- C) Paul 
- D) Paul, George 
- E) Ringo

#### Clicker Question #4

What will the following code snippet print out:

if 1 + 1 == 2:
    print("I did Math")
elif 1/0:
    print("I broke Math")
else:
    print("I didn't do math")

- A) I did Math 
- B) I broke Math
- C) I didn't do math
- D) This code won't execute

#### Clicker Question #5

What will the following code snippet print out:

conditional = False
python = "great"

if conditional:
    if python == "great":
        print("Yay Python!")
    else:
        print("Oh no.")
else:
    print("I'm here.")

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