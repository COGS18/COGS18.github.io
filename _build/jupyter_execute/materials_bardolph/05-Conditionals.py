**Course Announcements**

**Due Dates**
- CL2 due tonight (11:59 PM)
- A1 due Monday (11:59 PM)

**Survey (N=262)** 
- You should have gotten an email reply from me with a PS specific to you
- Time zones: 81% in PDT (UTC -7/8); 10% in Eastern Asia
- 68% have never programmed before
- Hobbies: Gaming, hang with friends, baking/cooking, reading, music, beach, family
- Futures: psychologist, researcher, grad school, engineer, undecided, happy, successful

**Q&A**

Q: The "slay the dragon" example was confusing/too difficult.  
A: That sounds really normal! Take time to think about new problems, attend Coding Lab & office hours and ask questions, and realize that knowledge comes mostly from *practice.*  

Q: What is the purpose of Boolean logic? What can we use it for?  
A: One place where we will use Booleans is with conditionals - covered in this lecture. You will see more uses for comparisons and Boolean logic as your code becomes more complex.  

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

#### Poll Question #1

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

#### Poll Question #2

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

#### Poll Question #3

What will the following code snippet print out?

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

#### Poll Question #4

What will the following code snippet print out?

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

#### Poll Question #5

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