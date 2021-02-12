# Exam 2 Review

- **Exam #2 is released next Wednesday** 
    - released at 8AM; 24h to complete and submit
    - must be **submitted on datahub by Thurs 2/18 at 8 AM**
- **A4 is due next Friday 2/19** (11:59 PM)
- No Class Monday (Holiday)
- No Coding Lab or Office Hours on Wednesday next week

## Exam II Plan (12.5 points)

Part I: **E1 Review** (3 points) 
- Q1: Variables, Operators, & Indexing (0.5 points)
- Q2: Conditionals & Loops (1.25 point)
- Q3: Loop to Complete a Task (1.25 points)

Part II: **Functions** (4.5 points)  
- Q4: Function execution (0.75 points)*
- Q5: Function I (1.25 points)*
- Q6: Function II (1.25 points)*
- Q7: Debugging (1.25 points)*

Part III: **Objects & Classes** (5 points)
- Q8: Classes I (2.5 point)*
- Q9: Classes II (2.5 points)*

\* : includes manual grading (partial credit)

**Note about `random`**

On the Practice midterm: there is a question that asks you to `import random`. There is a function from the `random` module called `choice()` that will choose an element from a list at random.

This will be required to do Q10 on the practice midterm.

*Note*: we have not covered imports or the `random` module yet; this question would NOT be fair game for your midterm.

### Reminder: 

There are two extra notebooks that you can use for review:

1. [A1-Syntax](https://cogs18.github.io/materials/A1-Syntax/)
2. [A2-Examples](https://cogs18.github.io/materials/A2-Examples/)

There are also a few Exam #2 Practice Problems [here](https://cogs18.github.io/materials/Exam2-Practice) and a practice exam on datahub.

### Questions?

## Functions

- `def`
    - `return`
- executing a function
    - parameters
        - keyword vs. positional
        - default values
    - have a separate namespace
- methods 
    - in place vs. not in place

#### Functions Question #1
Write, in real code, a function called `remainder` that takes two inputs, divides the first input by the second and returns the remainder.

## YOUR CODE HERE

#### Functions Question #2
Using the function `remainder` you wrote above, write the python code you would use to return the remainder of 10 divided by 4. Store the output in the variable `my_remainder`.

## YOUR CODE HERE

#### Functions Question #3
Assuming the following function has been defined, what would `sum_list([1, 2, 3])` return?

def sum_list(my_list):
    total = 0
    
    for item in my_list:
        total += item
        
    return total

## CODE TO TEST HERE

## Objects & Classes

- objects & `class`
    - attributes
    - methods
    - instances


#### Objects & Classes Question #1

**Part A**

We want to simulate a rocket ship for a game.

Write code that will create a class `Rocket`. 

This class should have two instance attributes: `x` and `y`. These will specify the x,y position of the rocket. Each attribute should be initialized with hte value 0. 

Your `Rocket` should also have the method `move_up()`. This method should increment the y-position of the rocket by 1. 

## YOUR CODE HERE

The exam question will be more involved than this example. It's meant to combine all the pieces we've learned this quarter (classes w/ methods, conditionals, etc).

**Part B**

Create an instance `my_rocket` of your Rocket object.

## YOUR CODE HERE

**Part C**

Update `my_rocket` so that `my_rocket` has the `y` position 3.

## YOUR CODE HERE

#### Objects & Classes Question #2

Fill in the blanks:

	What is the name of a function defined within a class: ______________

	In Python, everything is a(n) ______________. 


## Python & Jupyter Extras
- encodings (`chr` & `ord`)
- whitespace
- namespace
- kernel
- code comments
- magic functions

#### Extras Question #1
What will the following piece of code print out?

```print(chr(ord('A')))``` 
    
     _____________

#### Extras Question #2 

What is the magic function `%whos` used for?

#### Extras Question #3

For each of the following, indicate if the statement is True or False about Python and programming:

- True/False Whitespace matters in Python
- True/False Comments in Python start with '%' 					
- True/False You have to specify a data type when you define a variable
- True/False Every Python variable is available from every namespace		
- True/False `ls` is a shell command that creates a new file 		
- True/False `cd` returns your current working directory		
- True/False `print_name()` folles best practices for function naming

<h2><center>After the second exam:</center></h2>

<h3><center> We will focus on the Python ecosystem, and applications of Python. </center></h3>

<h3><center> We also become a project based course. </center></h3>