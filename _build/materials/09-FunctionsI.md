---
interact_link: content/materials/09-FunctionsI.ipynb
download_link: assets/downloads/09-FunctionsI.ipynb.zip
pdf_link: assets/pdf/09-FunctionsI.pdf
layout: materials
title: '09-FunctionsI'
prev_page:
  url: /materials/08-Encodings
  title: '08-Encodings'
next_page:
  url: /materials/11-FunctionsII
  title: '10-FunctionsII'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

Due dates:
- **A2** due tonight (11:59 PM)
- **Exam I** on Friday <- covers through "Encodings" lecture

Notes:
- **CL4** now available (due Wed 4/22)
- **A3** now available (Mon 5/4)

## Exam Information

- Will be released on Datahub by 8AM PDT Friday (4/24) morning
    - Combination of autograding and manual grading
- Designed to take 50 min
    - Must be completed *and submitted* by 8AM PDT Sat morning (4/25)
    - So, you can take >50 min if you want
- No questions/clarifications allowed
    - Simply logistics
    - You can explain any of your thinking/confusion in the exam directly
- Open notes & Open Google
    - Not allowed to post exam questions anywhere
    - Not allowed to discuss with anyone via any communication channel

## COGS 18: Course Philosophy

- **Lecture**: Introduce Concepts (no pressure)
    - *just* learned the material seconds ago
    - clicker questions have to be "simpler"

- **CodingLab**: Get practice with concepts (low pressure)
    - have 50 minutes to explore and deepen understanding
    - challenge questions allow deeper exploration and understanding as we're not grading for completeness

- **Assignments**: Third time with the material and lots of time (medium pressure)
    - graded for completeness
    - but material has been seen before

- **Exams** (*typically*): Fourth time through with limited time (high pressure)
    - Due to limited time & limited help, difficulty also limited
    - Opportunity to solidify understanding of concepts

## Coding Lab Extras

Google Drive has docs and slides: https://drive.google.com/open?id=1_WJMMEZOvw7SdZyUzFfl3c76lSiHETa0

# Functions I

- defining a function
    - `def`
    - `return`
- executing a function
    - parameters
    - separate namespace

## Functions

<div class="alert alert-success">
A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
</div>

Copy + Pasting the same/similar bit of code is to be avoided.

**Loops** were one way to avoid this.

**Functions** are another!

## Modular Programming

<div class="alert alert-success">
Modular programming is an approach to programming that focuses on building programs from indendent modules ('pieces'). 
</div>

## Functions for Modular Programming

- Functions allow us to flexibly re-use pieces of code
- Each function is independent of every other function, and other pieces of code
- Functions are the building blocks of programs, and can be flexibly combined and executed in specified orders
    - This allows us to build up arbitrarily complex, well-organized programs



{:.input_area}
```python
# you've seen functions before
# here we use the type() function
my_var = [3, 4, 5]
type(my_var)
```





{:.output_data_text}
```
list
```





{:.input_area}
```python
# the function len() doesn't depend on type()
# but they can both be used on the same variable
len(my_var)
```





{:.output_data_text}
```
3
```



## Function Example I

When you use `def` you are creating a **user-defined function**.



{:.input_area}
```python
# define a function: print_value
# num is a parameter for the function
def print_value(num):
    
    # do some operation
    print(num)
```




{:.input_area}
```python
# excecute a function by calling function by name
# adding input within parentheses
print_value(num = 6) 
```


{:.output_stream}
```
6

```



{:.input_area}
```python
# equivalent function call
# without specifying parameter
print_value(6)
```


{:.output_stream}
```
6

```



{:.input_area}
```python
## why is it printing None?
## lets look at return below
new_var = print_value(6)
print(new_var)
```


{:.output_stream}
```
6
None

```

All this function is doing is printing the input. It's not actually *storing* any new information. To do that, we need to use `return`.



{:.input_area}
```python
# improving that function using return
def return_value(num):
    
    # do some operation
    output = num
    
    # return an answer
    return output
```




{:.input_area}
```python
# excecute that function
return_value(6)
```





{:.output_data_text}
```
6
```





{:.input_area}
```python
# execute function but assign output 
# store that output in variable new_val
new_val = return_value(6)
print(new_val)
```


{:.output_stream}
```
6

```

## Function Example II

Something more interesting than just printing or storing a single value



{:.input_area}
```python
def add_two_numbers(num1, num2):
    
    # Do some operations on the input variables
    answer = num1 + num2
    
    # Return the answer
    return answer
```




{:.input_area}
```python
add_two_numbers(-1, 4)
```





{:.output_data_text}
```
3
```





{:.input_area}
```python
# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)
```


{:.output_stream}
```
3

```

## Function Example III

We aren't limited to a single operation within a function. We can use multiple operations and all of the concepts we've used previously (including loops and conditionals).



{:.input_area}
```python
# determine if a value is even or odd
def even_odd(value): 
    if (value % 2 == 0): 
        print("even")
    else: 
        print("odd")
```




{:.input_area}
```python
# Execute our function
# note that it's only printing the output
even_odd(-1)

```


{:.output_stream}
```
odd

```



{:.input_area}
```python
# determine if a value is even or odd
# and return that value
def even_odd(value): 
    if (value % 2 == 0): 
        out = "even"
    else: 
        out = "odd"
    
    return out
```




{:.input_area}
```python
# Execute our function
# note that it's only printing the output
my_val = even_odd(-1)
print(my_val)
```


{:.output_stream}
```
odd

```

With functions, the logic behind our code no longer requires it to be executed from top to bottom of the notebook.

The cost of potential confusion is *definitely* offset by the benefits of writing functions and using modular code.

## Function Properties

- Functions are defined using `def` followed by `:`, which opens a code-block that comprises the function
    - Running code with a `def` block *defines* the function (but does not *execute* it)

- Functions are *executed* using parentheses - `()`
    - This is when the code inside a function is actually run

- Functions have their own namespace
    - They only have access to variables explicitly passed into them

- Inside a function, there is code that performs operations on the available variables

- Functions use the special operator `return` to exit the function, passing out any specified variables

- When you use a function, you can assign the output to a variable

#### Clicker Question #1



{:.input_area}
```python
def remainder(number, divider):
    
    r = number % divider
    w = number * divider
    
    return r, w
```




{:.input_area}
```python

a, b = remainder(12,6)
print(a)
print(b)
```


{:.output_stream}
```
0
72

```

Given the function above, what will the code below print out?



{:.input_area}
```python
ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

print(ans_1 + ans_2)
```


{:.output_stream}
```
2

```

- A) 0
- B) 2
- C) 4
- D) '2r.2 + 1'
- E) ¯\\\_(ツ)\_/¯

#### Clicker Question #2

Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.

- A) I did it!
- B) I think I did it.
- C) I tried but am stuck.
- D) Super duper lost



{:.input_area}
```python
## YOUR CODE HERE
```


## Function Namespace I



{:.input_area}
```python
# Remember, you can check defined variables with `%whos`
%whos
```


## Function Namespaces II



{:.input_area}
```python
def check_function_namespace(function_input):
    # Check what is defined and available inside the function
    print(locals())
```




{:.input_area}
```python
# Functions don't `see` everything
check_function_namespace(1)
```




{:.input_area}
```python
# Functions don't `see` everything
check_function_namespace(True)
```




{:.input_area}
```python
# using two different inputs to a function
def check_function_namespace2(function_input, other_name):
    # Check what is defined and available inside the function
    print(locals())
```




{:.input_area}
```python
# returning what each input is storing
check_function_namespace2(1, True)
```


## Function Namespaces III

Names defined inside a function only exist within the function.



{:.input_area}
```python
# Names used inside a function are independent of those used outside
# variables defined outside of functions are global variables
# global variables are always available
my_var = 'I am a variable'

check_function_namespace(my_var)

print(my_var)
```


## Function - Execution Order



{:.input_area}
```python
def change_var(my_var):
    my_var = 'I am something else'
    print('Inside function: \t\t', my_var)
```




{:.input_area}
```python
# my_var in the global namespace
my_var
```




{:.input_area}
```python
# my_var within the function
change_var(my_var)
```




{:.input_area}
```python
# my_var in the global namespace remains unchanged
my_var 
```




{:.input_area}
```python
print('Outside, before function: \t', my_var)
change_var(my_var)
print('Outside, after function: \t', my_var)
```

