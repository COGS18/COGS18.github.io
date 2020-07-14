---
interact_link: content/materials/08-FunctionsI.ipynb
download_link: assets/downloads/08-FunctionsI.ipynb.zip
pdf_link: assets/pdf/08-FunctionsI.pdf
layout: materials
title: '08-FunctionsI'
prev_page:
  url: /materials/07-Dictionaries
  title: '07-Dictionaries'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

Due dates:
- **CL3** due Wednesday (11:59 PM)
- **A3** due Monday (11:59 PM)

# Functions I

- defining a function
    - `def`
    - `return`
- executing a function
    - parameters
    - separate namespace
- algorithms
    - `sorted()`

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
    
    # return an answer
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
add_two_numbers(-1, 4)
```




{:.input_area}
```python
# Execute our function again, on some other inputs
output = add_two_numbers(-1, 4)
print(output)
```


## Function Example III

We aren't limited to a single operation within a function. We can use multiple operations and all of the concepts we've used previously (including loops and conditionals).



{:.input_area}
```python
# determine if a value is even or odd
# only prints output; cannot store
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


Given the function above, what will the code below print out?



{:.input_area}
```python
ans_1 = remainder(12, 5)
ans_2 = remainder(2, 2)

ans_1 + ans_2
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


## Algorithms

<div class="alert alert-success">
An <b>algorithm</b> is a formal description of how to complete a procedure, typically taking inputs and returns some output.
</div>

If you can write the steps down, you can write an algorithm.

Algorithms are computable.

Computers cannot read between the lines. They are very literal.

## Algorithm Example: Making a Sandwich

#### Clicker Question #3

Can you write an algorithm to make a ham and cheese sandwich. 

- A) Yes 
- B) No
- C) I don't know

## Algorithm for making a ham & cheese sandwich



Humans are pretty good at making sandwiches. Computers may struggle a bit.

## Algorithm Example: Sorting

Given a list of numbers, how can we sort it into the correct order?

Y'all Google is *really* good at sorting.

- ranking: rate a site as how related
- sort: given a list of good sites, determine order to present to user

...and do this on all the things



{:.input_area}
```python
# Define a list of numbers
list_of_numbers = [2, 1, 3]  
```


#### Clicker Question #4

**array**: a collection of items, where each item can be accessed by its index.

Can you write an algorithm to sort an array?

- A) Yes 
- B) No
- C) I don't know

## `sort_array`

A version of a **selection sort**:
- loop through current list
- find lowest item
- put that at the front of your sorted list
- remove lowest item from current list
- wash, rinse, repeat



{:.input_area}
```python
def sort_array(array_to_sort):
    """A function to sort an array."""

    is_sorted = False    # Keeps track of when we are done sorting
    sorted_array = []    # A new list that we will use to 
     
    while not is_sorted:

        lowest = None
        for item in array_to_sort:
            if lowest == None:         # If not defined (first element) set the current element as lowest
                lowest = item
            if item < lowest:
                lowest = item
        
        # these next two lines use new methods
        sorted_array.append(lowest)    # Add the lowest value to our sorted array output
        array_to_sort.remove(lowest)   # Drop the now sorted value from the original array

        if len(array_to_sort) == 0:    # When `array_to_sort` is empty, we are done sorting
            is_sorted = True
    
    return sorted_array
```


## Using `sort_array`



{:.input_area}
```python
# Sort an array of integers
unsorted_array = [12, 7, 19, 12, 25]
sorted_array = sort_array(unsorted_array)
print(sorted_array)
```




{:.input_area}
```python
# Sort an array of floats
unsorted_array = [21.3, 56.7, 2.3, 2.9, 99.9]
sorted_array = sort_array(unsorted_array)
print(sorted_array)
```


#### Clicker Question #5

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = ['a', 'c', 'b'] 
sort_array(data)
```


- A) ['a', 'c', 'b']
- B) ['a', 'b', 'c']
- C) [97, 98, 99]
- D) None
- E) This code will fail

### How Python evaluates strings



{:.input_area}
```python
'a' < 'b'
```




{:.input_area}
```python
ord('a')
```




{:.input_area}
```python
ord('b')
```


#### Clicker Question #6

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [True, False, True]
sort_array(data)
```


- A) [False, True, True] 
- B) [True, False, True] 
- C) [0, 1, 1]
- D) [True, True, False] 
- E) This code will fail

### How Python evaluates Booleans



{:.input_area}
```python
True < False
```




{:.input_area}
```python
bin(True)
```




{:.input_area}
```python
bin(False)
```


#### Clicker Question #7

Using our `sort_array` function from above, what will the following code snippet print out:



{:.input_area}
```python
data = [[1, 4], [1, 2]]
sort_array(data)
```


- A) [[1, 4], [1, 2]]  
- B) [1, 1, 2, 4] 
- C) [[1, 2], [1, 4]]
- D) None 
- E) This code will fail

## SideNote: `sorted`



{:.input_area}
```python
# Sort a list, with `sorted`
data = [7, 4, 6]
sorted(data)
```




{:.input_area}
```python
# what about a list of strings?
sorted(['asdf','abcd'])
```




{:.input_area}
```python
# Sort different data types
print(sorted(['a', 'c', 'b']))
print(sorted([True, False, True]))
print(sorted([[1, 4], [1, 2]]))
```


## Algorithmic Complexity

<div class="alert alert-success">
The complexity of an algorithm characterizes the relationship between the input size and the number of steps of an algorithm.
</div>

## Algorithmic Complexity

Things we might care about:
- The number of steps it takes to complete our algorithm
    - Usually defined in relation of the size of the input
- The amount of memory it will take to run our algorithm

## Properties of our sorting algorithm

- It will require $n^2$ steps, where $n$ is the length of the list
- It will require ~double the memory of the original list

## Computability

Things that computers can do are things that we can write down an algorithm to do.

Things that we can write an algorithm to do are things that we can define a specific set of steps to complete.

## Extra Notes: Variable Type Checking

**Note**: The rest of the noteook includes a common student question. You are not expected to know this, but you are free to learn and use the information!


To check on an input variable's type, you can use the following approach:

```python
isinstance(object, classinfo) 
```

`isinstance()` takes two parameters:
- `object` : variable/object to be checked
- `classinfo` : class, type, or tuple of classes and types

For example, using the `string_manipulator` function from earlier, note that I've added the following two lines: 

```python
if not isinstance(string, str):
    print("Warning: please provide a string as input")
```

This checks to see if the input is anything other than a string. If it is, the function prints a warning.



{:.input_area}
```python
def string_manipulator(string):
    
    if not isinstance(string, str):
        print("Warning: please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output
```




{:.input_area}
```python
# use function with a string
string_manipulator('hello!')
```




{:.input_area}
```python
# print warning if not a string
string_manipulator(5)
```


However, sometimes, you want it to raise an error rather than just print something. Here we use `raise` instead of print. In this case, an error will be returned (with our specified message) to the user if the wrong variable type is provided:



{:.input_area}
```python
def string_manipulator(string):
    
    if not isinstance(string, str):
        raise ValueError("Please provide a string as input")
    else:
        output = ''
        for char in string:
            if char == 'a' or char == 'e':
                char = 'z' 
            output = output + char
    
        return output

```




{:.input_area}
```python
# raise error instead of print message
string_manipulator(5)
```

