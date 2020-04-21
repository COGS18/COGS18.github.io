---
interact_link: content/labs/CL2-Answers.ipynb
download_link: assets/downloads/CL2-Answers.ipynb.zip
layout: notebooks
title: 'Coding Labs'
prev_page:
  url: /materials/Exam1-Practice
  title: 'Exam1-Practice'
next_page:
  url: /labs/CL2-Answers
  title: 'CL2-Answers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Coding Lab 2: Programming I - Answers


Welcome to the second coding lab!

CodingLab labs are meant to be interactive - so you should find another person to work together with on this notebook. For this lab, you can either work together on one notebook, or work together but each fill out your own notebook, if you prefer. 

CodingLabs are also meant to be exploratory. There are broad questions in the notebook that you should explore, and try to answer - but you are also very much encouraged to explore other related ideas as you go! 

If you have a question about how something works / what something does - try it out, and see what happens! If you can't figure it out, reach out to your instructional staff - we're here to help!

## Part 1: Variables

Variables are used in Python to store values. 

### Defining Variables

Declare a int, float, string, and boolean. Fill them with with any values you want. 

Call them `my_int`, `my_float`, `my_string` and `my_boolean`. 



{:.input_area}
```python
## YOUR CODE HERE
my_int = 12
my_float = 56.3
my_string = 'hello'
my_boolean = True
```


Use the following cells to check the types of the variables you write are as expected



{:.input_area}
```python
type(my_int)
```





{:.output_data_text}
```
int
```





{:.input_area}
```python
type(my_float)
```





{:.output_data_text}
```
float
```





{:.input_area}
```python
type(my_string)
```





{:.output_data_text}
```
str
```





{:.input_area}
```python
type(my_boolean)
```





{:.output_data_text}
```
bool
```



## Part 2: Operators & Comparisons

Operators are used in Python to do things with variables. 

### Operator Questions

First - explore using Python operators. Make sure you can add and subtract numbers, concatenate strings, do boolean comparisons, etc.



{:.input_area}
```python
## Do some exploring!

# Add & subtract numbers
print(1 + 2)
print(2 - 2)

# Concatenate string
print('ab' + 'cd')

# Boolean comparisons
print(True and True)
print(False or True)
```


{:.output_stream}
```
3
0
abcd
True
True

```

Once you have explored using operators, try to answer some quesions using them. 

Let's start with an example: is the multiplication of 13 and 15 greater than 200?



{:.input_area}
```python
13 * 15 > 200
```





{:.output_data_text}
```
False
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




{:.input_area}
```python
323 % 13 > 6
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
7 **3 >= 300
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
49**2 > 2500 or 14**3 > 2500
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
49%9 == 67%9 and (49 + 67) % 9 > 7
```





{:.output_data_text}
```
True
```



### Operator Challenges

The following are more challenging operator related questions. If they seem too tricky for now, just skip ahead to the next section.

Some more comparisons, with variable assignment:
- Set the variable `comp_1` to the result of whether 17 squared is not the same as 867 divided by 3
- Set the variable `comp_2` to the result of whether 4^3 is less than 3^4 **and** also greater than the remainder of dividing 1234 by 99

Bonus: both of the above questions can be written in (at least) two ways. 

If you found an answer to them, see if you can update the construction, changing at least one operator, to answer the question in a different way. 

Note: x^y indicates 'x to the power of y'



{:.input_area}
```python
## YOUR CODE HERE
comp_1 = not 17**2 == 289/3
comp_1 = 17**2 != 289/3

comp_2 = (3**4) > (4**3) > (1234 % 99)
comp_2 = ((3**4) > (4**3)) and ((4**3)) > (1234 % 99)
```


### Operator Explorations.

For each of the following questions, start by writing out a guess of what you think it might do. 

Then, test out each one by writing out some code. 

Finally, once you have answered the question, using some code, add a comment in the markdown here with the answer. 

Questions:
- If you divide a float by an int, what is the type of the outcome? What about dividing an int by a float?
- What happens if you multiply a string with a number?
- The `+` sign works if you for adding numbers and for concatenating strings. Can you use `+` with a number and string in the same operation?
- Since you can use `+` and `*` with strings, what happens if you try to substract two strings using `-`?



{:.input_area}
```python
## EXPLORATION CODE HERE
```




{:.input_area}
```python
print(type(12.0/2))
print(type(12/2.0))

# Dividing with a float and an int, in either order, returns a float
```


{:.output_stream}
```
<class 'float'>
<class 'float'>

```



{:.input_area}
```python
'hodor ' * 8

# Multiplying a string by a number repeats that string number times
```





{:.output_data_text}
```
'hodor hodor hodor hodor hodor hodor hodor hodor '
```





{:.input_area}
```python
12 + 'str'

# No, this code fails. You cannot use '+' with a number and a string
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-17-0810b46a83be> in <module>()
----> 1 12 + 'str'
      2 
      3 # No, this code fails. You cannot use '+' with a number and a string

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```




{:.input_area}
```python
'abc' - 'a' 

# No, this code fails. You cannot use '-' with strings
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-18-9a45216ae503> in <module>()
----> 1 'abc' - 'a'
      2 
      3 # No, this code fails. You cannot use '-' with strings

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for -: 'str' and 'str'
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
boolean = True
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





{:.output_data_text}
```
True
```



###  Assert Explorations

Now, explore using assert. What happens if you assert an integer, or a string? 

What happens if you assert None?

Find at least one integer that raises an assertion error. 



{:.input_area}
```python
assert 12

# Asserting an integer asserts as True
```




{:.input_area}
```python
assert 'hello'

# Asserting a string asserts as True
```




{:.input_area}
```python
assert None

# Asserting None asserts as False
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AssertionError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-25-98092c377a2c> in <module>()
----> 1 assert None
      2 
      3 # Asserting None asserts as False

```

{:.output_traceback_line}
```
AssertionError: 
```




{:.input_area}
```python
assert 0

# The integer 0 asserts as False (it gets interpreted as False)
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
AssertionError                            Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-26-86e0797498a7> in <module>()
----> 1 assert 0
      2 
      3 # The integer 0 asserts as False (it gets interpreted as False)

```

{:.output_traceback_line}
```
AssertionError: 
```

