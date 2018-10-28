---
download_link: assets/downloads/labs/Coding Labs.ipynb.zip
layout: notebooks
title: 'Coding Labs'
prev_page:
  url: /materials/10-Algorithms
  title: '10-Algorithms'
next_page:
  url: /labs/CL1-ProgrammingI
  title: 'CL1-ProgrammingI'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Coding Lab 1: Programming I


Welcome to the first coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each fill out your own notebook, if you prefer. 

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 

If you have a question about how something works / what something does - try it out, and see what happens!

## Part 1: Variables

Variables are used in Python to store values. 

### Defining Variables

Declare a int, float, string, and boolean. Fill them with with any values you want. 

Call them `my_int`, `my_float`, `my_string` and `my_boolean`. 



{:.input_area}
```python
## YOUR CODE HERE

```


Use the following cells to check the types of the variables you write are as expected



{:.input_area}
```python
type(my_int)
```




{:.input_area}
```python
type(my_float)
```




{:.input_area}
```python
type(my_string)
```




{:.input_area}
```python
type(my_boolean)
```


## Part 2: Operators & Comparisons

Operators are used in Python to do things with variables. 

### Operator Questions

First - explore using Python operators. Make sure you can add and subtract numbers, concatenate strings, do boolean comparisons, etc.



{:.input_area}
```python
## Do some exploring!


```


Once you have explored using operators, try to answer some quesions using them. 

Let's start with an example: is the multiplication of 13 and 15 greater than 200?



{:.input_area}
```python
13 * 15 > 200
```


Similar to that example, try to answer the following questions using Python variables & comparisons:
- Is the remainder of dividing 323 by 13 greater than 6?
- Is 7 to the power of 3 greater than or equal to 300?
- Is 49 squared greater than 2500 or (boolean comparison) is 14 to the power of 3 greater than 2500
- Is 49 modulus 9 equal to 67 modulus 9 and (boolean comparison) is the sum 49 & 67 modulus 9 greater than 7



{:.input_area}
```python
## YOUR CODE HERE



```


### Operator Challenges

The following are more challenging operator related questions. If they seem too tricky for now, just skip ahead to the next section.

Some more comparisons, with variable assignment:
- Set the variable `comp_1` to the result of whether 17 squared is not the same as 867 divided by 3
- Set the variable `comp_2` to the result of whether 4^3 is less than 3^4 and also greater than the remainder of dividing 1234 by 99

Bonus: both of the above questions can be written in (at least) two ways. 

If you found an answer to them, see if you can update the construction, changing at least one operator, to answer the question in a different way. 

Note: x^y indicates 'x to the power of y'



{:.input_area}
```python
## YOUR CODE HERE



```


### Operator Explorations.

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- If you divide a float by an int, what is the type of the outcome? What about dividing an int by a float?
- What happens if you multiply a string with a number?
- The '+' sign works if you for adding numbers, and for concatenating strings. Can you use '+' with a number and string?
- Since you can use '+' and '*' with strings, can you use '-'?



{:.input_area}
```python
## EXPLORATION CODE HERE



```


## Part 3: Asserts

You will notice, through the coding labs and assignments, code that looks somehing like `assert True`, in which the assert statement is used.

Using assert basically says to `assert that the following code is True`.

Or, slightly more formally `assert that the following code evaluates as True`.

If the asserted code does not evaluate as True, it raises an error - meaning it interrupts the code execution because something went wrong.

This can be used as a way to test that code does what you expect it to do - and is therefore part of how we will text your code programmatically. 

Because the use of `assert` will be common in course materials, let's take a moment to explore how it works and what happens when we use it.



{:.input_area}
```python
# Declare a variable called `boolean` that  has type boolean, and passes the assert in the next cell

## YOUR CODE HERE

```




{:.input_area}
```python
# Check that there is variable called `boolean` that is a boolean
assert type(boolean) == bool
```




{:.input_area}
```python
# Check that the variable called `boolean` passes the assert
assert boolean
```




{:.input_area}
```python
boolean
```


###  Assert Explorations

Now, explore using assert. What happens if you assert an integer, or a string? 

What happens if you assert None?

Find at least one integer that raises an assertion error. 



{:.input_area}
```python
## EXPLORATION CODE HERE



```

