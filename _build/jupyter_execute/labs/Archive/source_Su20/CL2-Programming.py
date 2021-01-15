# Coding Lab 2: Programming


Welcome to the second coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but you'll each still have fill out your own notebook for submission.

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! If you explore something beyond what is required in the notebook, you're encouraged to leave that exploratory code in the notebook you submit.

If you have a question about how something works / what something does - try it out, and see what happens! If you can't figure it out, reach out to your instructional staff - we're here to help!

**Reminder**: You may *not* be able to complete all of this in 2 hours, particularly the "challenges."  These are meant to help you gain mastery and provide additional practices, not to stress you out a ton. Make a concerted effort. Do your best to complete it. But, if you don't figure it all out, that's why we post answers for these!

## Part 1: Variables

Variables are used in Python to store values. 

### Defining Variables

Declare a int, float, string, and boolean. Fill them with with any values you want. 

Call them `my_int`, `my_float`, `my_string` and `my_boolean`. 



Use the following cells to check the types of the variables you write are as expected

type(my_int)

type(my_float)

type(my_string)

type(my_boolean)

## Part 2: Operators & Comparisons

Operators are used in Python to do things with variables. 

### Operator Questions

First - explore using Python operators. Make sure you can add and subtract numbers, concatenate strings, do boolean comparisons, etc.

## Do some exploring!



Once you have explored using operators, try to answer some quesions using them. 

Let's start with an example: is the multiplication of 13 and 15 greater than 200?

13 * 15 > 200

Similar to that example, try to answer the following questions using Python variables & comparisons:
- Is the remainder of dividing 323 by 13 greater than 6?
- Is 7 to the power of 3 greater than or equal to 300?
- Is 49 squared greater than 2500 or (boolean comparison) is 14 to the power of 3 greater than 2500
- Is 49 modulus 9 equal to 67 modulus 9 and (boolean comparison) is the sum 49 & 67 modulus 9 greater than 7





### Operator Challenges

The following are more challenging operator related questions. If they seem too tricky for now, just skip ahead to the next section.

Some more comparisons, with variable assignment:
- Set the variable `comp_1` to the result of whether 17 squared is not the same as 867 divided by 3
- Set the variable `comp_2` to the result of whether 4^3 is less than 3^4 **and** also greater than the remainder of dividing 1234 by 99

Bonus: both of the above questions can be written in (at least) two ways. 

If you found an answer to them, see if you can update the construction, changing at least one operator, to answer the question in a different way. 

Note: x^y indicates 'x to the power of y'





### Operator Explorations.

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- If you divide a float by an int, what is the type of the outcome? What about dividing an int by a float?
- What happens if you multiply a string with a number?
- The `+` sign works if you for adding numbers and for concatenating strings. Can you use `+` with a number and string in the same operation?
- Since you can use `+` and `*` with strings, what happens if you try to substract two strings using `-`?





## Part 3: Asserts

You will notice, through the coding labs and assignments, code that looks somehing like `assert True`, in which the assert statement is used.

Using assert basically says to `assert that the following code is True`.

Or, slightly more formally `assert that the following code evaluates as True`.

If the asserted code does not evaluate as True, it raises an error - meaning it interrupts the code execution because something went wrong.

This can be used as a way to test that code does what you expect it to do - and is therefore part of how we will text your code programmatically. 

Because the use of `assert` will be common in course materials, let's take a moment to explore how it works and what happens when we use it.

# Declare a variable called `boolean` that  has type boolean, and passes the assert in the next cell


# Check that there is variable called `boolean` that is a boolean
assert type(boolean) == bool

# Check that the variable called `boolean` passes the assert
assert boolean

boolean

###  Assert Explorations

Now, explore using assert. What happens if you assert an integer, or a string? 

What happens if you assert None?

Find at least one integer that raises an assertion error. 

## EXPLORATION CODE HERE




## Part 4: Collection types

Collections are Python variable types than can store a 'collection' of items.

### Collection Questions

Create a list and a tuple. Fill them with with any values you want. 

Call them `my_list` and `my_tuple`.



Use the following cells to check the types of the variables you write are as expected

type(my_list)

type(my_tuple)

#### Declaring Collections

Note that there can be more than one way to declare collections. 

As well as declaring them with '[]' and '()', we can use the list & tuple constructors, as shown below. 

# Run me! - This creates another list & tuple, using the list & tuple constructors
some_list = list([1, 2, 3, 4, 5])
some_tuple = tuple(["peanut", "butter", "and", "jelly"])

print("'some_list' contains: \t", some_list)
print("'some_tuple' contains: \t", some_tuple)

Compare the types of these variables to your equivalent variables to confirm.

In the cell below, write in the type of the objects that you expect them to be, and make sure the asserts pass. 

# Fill in `_WRITE_IN_TYPE_HERE` with the type you expect each variable to be
assert isinstance(some_list, _WRITE_IN_TYPE_HERE_)
assert isinstance(some_tuple, _WRITE_IN_TYPE_HERE_)

### Indexing

Given the following list, do the following operations:
- Get the length of the list (assign this to a variable `lst_len`)
- Get the 1st element of the list (call the selection `ind1`)
- Get the last element of the list (call the selection `ind2`)
- Get the second to the fourth element of the list (call the selection `ind3`)
- Get from the fifth element, to the end of the list (call the selection `ind4`)
- Get every second element of the list, starting at the first element (call the selection `ind5`)
- Get every second element of the list, starting at the second element (call the selection `ind6`)

my_lst = ['a', True, 12, 'tomato', False, None, 23, 'python', [], 5.5]



## Part 5: Conditionals

Conditionals a form of control flow for executing certain code if a specific condition is met. 

### Conditional Questions

In this part, we will re-visit some questions about conditionals, and start combining them together with collections. 

Make sure you can use if/elif/else statements to control which code blocks are run.

#### Controlling Output With Conditionals I

Using the code below, keep updating the variable value to make sure you can make the conditional return each of the possibilities. 

# ToDo: Update value to control what gets executed
value = 10

# This code provided
if isinstance(value, int):
    if value < 10:
        result = 'small value'
    if value >= 10:
        result = 'big value'
else:
    result = 'false value'

print(result)

#### Controlling Output With Conditionals II

In the cell below, first write something into each result assignment related to  for example, it could be "B1 is False & B2 is True"). 

Then make sure you can change values of b1 & b2 to make the program execute each option. 

# ToDo: Update b1 & b2 to control what gets executed
b1 = False
b2 = False

# Next, try this out
if b1 and not b2:
    result = ''
elif not b1 and b2:
    result = ''
elif b1 and b2:
    result = ''
else:
    result = ''

print(result)

### Conditional Challenges

The following are more challenging questions relating to conditional statements. If they seem too tricky for now, just skip ahead to the next section.

#### Conditional Challenge #1

Write a conditional that prints "Found it" if a given `val_2` is a multiple of 10, otherwise prints "Nope."




#### Conditional Challenge #2

Input: assumes a variable `val_1`, that can be either a string or an integer

Output: based on the conditions, this code block will assign a variable called `output` to be a boolean

Use conditions to check whether `val_1` is a string or an integer object:
- If it is a string, check whether it's length is greater then 8
    - If so, set the value `output` to True
- If it is an integer, compare whether it is less than 100
    - If so, set the value `output` to True
- Else, set output to False



### Operator Explorations

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- Can you include multiple conditions in an if statement?
    - If think so, write an if statement that tests multiple conditions.
- What happens if you put an if statement inside an if statement? When would such a statement run?
    - To explore this, write an if statement that has an embedded if statement in it. 


## YOUR EXPLORATIONS HERE




## Part 6: Loops

We will now explore two ways to iterate over data in Python - `for` and `while` loops. 

Each type of loop performs its respective code block until certain conditions are met. Here, we will explore what those conditions are. 

Note: "iterate" means to perform an action repeatedly 

Note: Sometimes, we accidentally make loops that never end. 
- If that happens, "break" the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

#### Loops Q1

First, declare a variable called `counter` that has type int and value zero.

Then write a while loop that runs 10 times and use 'counter' to track how many times the loop runs. 



# Check that (after the loop runs) that there is a variable called `counter` that has value 10
assert counter == 10

#### Infinite Loops

The while loop below will run indefinitely unless someone puts a stop to it! 

Add your own code that causes the loop to exit when the `counter` variable reaches 10. You can use `break` to do this. 

Note: Sometimes, we accidentally make loops that never end - try that by running the cell below before adding 

If that happens, interrupt the cell by selecting it and then pressing "ctrl+c". Alternatively, press the "stop" button (square icon) in the Jupyter toolbar. 

counter = 0

while True:
    
    print("the value of 'counter' = {}".format(counter))
    counter +=1
    
    ## YOUR CODE HERE


###  Loop Explorations

Now, explore using for and while loops and breaks. 

Here are some things to try, and questions to ask - each of which you should explore in code. 
- What happens if you use 'break' all by itself?
- What are some different ways to loop through a list? tuple?
- Write these combinations: 
    - a `for` loop with a `break`, a `for` loop with a `continue`
    - a `while` loop with a `break`, a `while` loop with a `continue`
- Write some loops that loop across lists:
    - Write a loop that loops across, and prints out, all the elements of a list
    - Write a loop that loops across, and prints out, every second element of a list
    - Write a loop that loops across, and prints out, every element of a list in reverse order
    - Write a loop that loops across, and prints out, the first half of a list
- Write a loop with a conditional inside it.
- Can you have loops inside loops? If you think so, try and write a nested loop. 

# YOUR CODE EXPLORATIONS HERE




### Nested Loop Challenge

Using nested loops, you will print out a pattern that looks like this:

1 <br>
1 2 <br>
1 2 3 <br>
1 2 3 4 <br>
1 2 3 4 5 <br>
1 2 3 4 5 6 <br>
1 2 3 4 5 6 7

Hints:
- You can do this with two while loops, one inside the other.
- You will have two indices counters, one for each loop. 
- For the print statement, it will look something like `print(index_inner, end=" ")`



If you get the above pattern working, try manipulating the code to print out different patterns, and with different symbols. 



## The End!

This is the end of this Coding Lab!

Be sure you've made a concerted effort to complete all the tasks specified in this lab. Then, go ahead and submit on datahub!