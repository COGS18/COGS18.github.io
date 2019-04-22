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
  url: /labs/CL1-ProgrammingI
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Course Announcements

- **A2 due tonight (11:59 PM)**
- **A3 due Monday 4/29 (11:59 PM)**
    - building from this assignment for final project is an option (chatbots)
- If you're stuck:
    - take a break
    - talk to a classmate
    - come talk to us (office hours!)
    - post on Piazza

## Points of Clarification

- `print()` statements vs variable assignment
- indexing
- for loops w/
    - lists
    - dictionaries

### Variable Assignment vs `print()` statements



{:.input_area}
```python
# print statements
print(3)
```




{:.input_area}
```python
# variable assignment
my_var = 3
```


### Indexing

Indexing allows you to access parts of a collection (list, tuple, dictionary, etc.). 

It is done with square brackets: `[]`



{:.input_area}
```python
list_a = [3, 4, 5]
list_b = [17, 18, 19]
```




{:.input_area}
```python
# index second value in the list
# we can just print that value
print(list_a[1])
```




{:.input_area}
```python
# or we can store that value in a variable
stored_val = list_a[1]
```




{:.input_area}
```python
# output from comparison operators can then be stored
# in a variable
stored_comparison = list_a[1] < list_b[2]
```


### Loops & `print()` statements



{:.input_area}
```python
# print statements help let you know what's going on
for number in range(2, 20, 2):
    print(number)
```




{:.input_area}
```python
# this won't print anything out
# but result is stored
result = 0

for number in range(2, 20, 2):
    result = result + number
```




{:.input_area}
```python
## you can assign and print in the same cell
result = 0

for number in range(2, 20, 2):
    result = result + number
    
print(result)
```


### Working with Dictionaries

- dictionaries are referred to by their keys
- indexing a dictionary by its key returns that key's value



{:.input_area}
```python
# defining a dictionary
dictionary = {
    'Alberto' : True,
    'Jaime' : False,
    'Jill' : True,
    'Mi Linh' : False,
}
```




{:.input_area}
```python
## intialize a list
output_list = []

# loop through keys in dictionary
for person in dictionary:
    
    ## check if value stored in key is True
    if dictionary[person] == True:
        continue
    else:
        ## add key to end of output_list
        output_list.append(person)
```




{:.input_area}
```python
## can look at outputs
print(output_list)
```


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



{:.input_area}
```python
# you've seen functions before
my_var = [3, 4, 5]
type(my_var)
```


Copy + Pasting the same/similar bit of code is to be avoided.

**Loops** were one way to avoid this.

**Functions** are a another!

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




{:.input_area}
```python
# the function len() doesn't depend on type()
# but they can both be used on the same variable
len(my_var)
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




{:.input_area}
```python
# equivalent function call
# without specifying parameter
print_value(6)
```




{:.input_area}
```python
## why is it printing None?
## lets look at return below
new_var = print_value(6)
print(new_var)
```


All this function is doing is printing the input. It's not actually *storing* any new information. To do that, we need to use `return`.



{:.input_area}
```python
# improving that function using return
def return_value(num):
    
    # do some operation
    output = num
    
    # return an asnwer
    return output
```




{:.input_area}
```python
# excecute that function
return_value(6)
```




{:.input_area}
```python
# execute function but assign output 
# store that output in variable new_val
new_val = return_value(6)
print(new_val)
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
# Execute our function again, on some other inputs
add_two_numbers(-1, 4)
```


## Function Example III

We aren't limited to a single operation within a function. We can use multiple operations and all of the concepts we've used previously (`if`, `elif`, `else` and conditionals).



{:.input_area}
```python
# determine if a value is even or odd
def evenOdd(value): 
    if (value % 2 == 0): 
        print("even")
    else: 
        print("odd")
```




{:.input_area}
```python
# Execute our function
# note that it's only printing the output
evenOdd(-1)
```




{:.input_area}
```python
# determine if a value is even or odd
# and return that value
def evenOdd(value): 
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
my_val = evenOdd(-1)
print(my_val)
```


With functions, the logic behind our code no longer requires it to be executed from top to bottom.

The cost of potential confusion is *definitely* offset by the benefits of writing functions and using modular code.

## Function Properties

- Functions are defined using `def` followed by `:`, which opens a code-block that comprises the function
    - Running code with a `def` block *defines* the function (but does not *execute* it)

- Functions are *executed* using parentheses - '()'
    - This is when the code inside a function is actually run

- Functions have their own namespace
    - They only have access to variables explicitly passed into them

- Inside a function, there is code that performs operations on the available variables

- Functions use the special operator `return` to exit the function, passing out any specified variables

- When you use a function, you can assign the output to a variable

## Clicker Question #1



{:.input_area}
```python
def remainder(number, divider):
    
    r = number % divider
    
    return r
```


Given the function above, what will the code below print out?



{:.input_area}
```python
ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

print(ans_1 + ans_2)
```


- A) 0
- B) 2
- C) 4
- D) '2r.2 + 1'
- E) ¯\\\_(ツ)\_/¯

## Clicker Question #2

Write a function `greet` that takes the parameter `name`. Inside the function, concatenate 'Hello', the person's name, and 'Good morning!". Assign this to `output` and return `output`.

- A) I did it!
- B) I think I did it...but I'm on paper
- C) I tried but am stuck
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


## Clicker Question #3



{:.input_area}
```python
an_int = 2
a_float = 11.5

def print_numbers(an_int, a_float):
    print(an_int, ',', a_float)
```


Assuming the cell above has been executed, what will the code below print out?



{:.input_area}
```python
print_numbers(5, 12.2)
```


- A) 5 , 11.5
- B) 2, 12.2 
- C) 2 , 11.5 
- D) 5 , 12.2
- E) None

## Clicker Question #4



{:.input_area}
```python
def string_manipulator(string):
    
    output = ''
    for char in string:
        if char == 'a' or char == 'e':
            char = 'z' 
        output = output + char
    
    return output
```


Given the function above, what will the following code print?



{:.input_area}
```python
variable = 'abcde'
manipulated_string = string_manipulator(variable)
print(manipulated_string)
```


- A) 'abcde' 
- B) 'zbcdz'
- C) 'zzzzz'
- D) 'azbcdez'
- E) ''
