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
  url: /materials/10-Algorithms
  title: '10-Algorithms'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Functions I

## Functions

<div class="alert alert-success">
A function is a re-usable piece of code that performs operations on a specified set of variables, and returns the result.
</div>

## Modular Programming

<div class="alert alert-success">
Modular programming is an approach to programming that focuses on building programs from indendent modules ('pieces'). 
</div>

## Functions for Modular Programming

- Functions allow us to flexibly re-use pieces of code
- Each function is independent of every other function, and other pieces of code
- Functions are the building blocks of programs, and can be flexible combined and executed in specified orders
    - This allows us to build up arbitrarily complex, well organized programs

## Function Example



{:.input_area}
```python
def add_two_numbers(num1, num2):
    
    aa = '1'
    print('aa:', aa)
    
    # Do some operations on the input variables
    answer = num1 + num2
    
    # Return the answer
    return answer, aa
```




{:.input_area}
```python
# Execute our function again, on some other inputs
add_two_numbers(-1, 4)
```


{:.output_stream}
```
3

```

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
    
    remainder = number % divider
    
    return remainder
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

A) 0 | B) 1 | C) 2 | D) 3 | E) None

## Function Namespace I



{:.input_area}
```python
# Remember, you can check defined variables with `%whos`
%whos
```


{:.output_stream}
```
Variable          Type        Data/Info
---------------------------------------
add_two_numbers   function    <function add_two_numbers at 0x111bc57b8>
ans_1             int         2
ans_2             int         0
my_answer         NoneType    None
remainder         function    <function remainder at 0x111bc5730>

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
check_function_namespace(True)
```


{:.output_stream}
```
{'function_input': True}

```

## Function Namespaces III



{:.input_area}
```python
# Names used inside a function are independent of those used outside
my_var = 'I am a variable'

check_function_namespace(my_var)

print(my_var)
```


{:.output_stream}
```
{'function_input': 'I am a variable'}
I am a variable

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
my_var = 'I am a variable'

print('Outside, before function: \t', my_var)

print('Outside, after function: \t', my_var)
```


{:.output_stream}
```
Outside, before function: 	 I am a variable
Outside, after function: 	 I am a variable

```

## Clicker Question #2



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


{:.output_stream}
```
5 , 12.2

```

A) 5 , 11.5 | B) 2, 12.2 | C) 2 , 11.5 | D) 5 , 12.2 | E) None

## Clicker Question #3



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


{:.output_stream}
```
zbcdz

```

A) 'abcde' | B) 'zbcdz' | C) 'zzzzz' | D) 'azbcdez' | E) ''
