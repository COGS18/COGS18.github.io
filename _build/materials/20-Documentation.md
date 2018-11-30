---
interact_link: content/materials/20-Documentation.ipynb
download_link: assets/downloads/20-Documentation.ipynb.zip
pdf_link: assets/pdf/20-Documentation.pdf
layout: materials
title: '20-Documentation'
prev_page:
  url: /materials/19-OpenSource
  title: '19-OpenSource'
next_page:
  url: /materials/21-CodeStyle
  title: '21-CodeStyle'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Documentation

## Code Readability

"Code is more often read than written" - Guido van Rossum

So: code should be written to be readable by humans.

Note: one of those humans is future you.

### Writing Readable Code

So how do we write good code for humans?

- Use good structure
- Use good naming
- Use code comments and include documentation

Good code has good documentation - but code documentation should not be used to try and fix unclear names, or bad structure. 

Rather, comments should add any additional context and information that helps explain what the code is, how it works, and why it works that way. 

### Clicker Question #1

What does the following code do:



{:.input_area}
```python
def ff(jj):
    oo = list(); jj = list(jj)
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
ff('Hello World.')
```


- A) Returns unicode code points, as a list
- B) Encodes a string as a cypher, returning a string of alphabetical characters
- C) Returns unicode code points, as a string
- D) Encodes inputs alphabetical characters, returned as a list
- E) This code will fail



{:.input_area}
```python
# Let's fix this code!
def ff(jj):
    oo = list(); jj = list(jj)
    for ii in jj: oo.append(ord(ii))
    return oo
ff('Hello World.')
```


## Code Documentation

<div class="alert alert-success">
Code documentation is text that accompanies and/or is embedded within a software project, that explains what the code is and how to use it. 
</div>

## Code Comments vs. Documentation

#### Comments

Comments are string literals written directly in the code, typically directed at developers - people reading and potentially writing the code. 

#### Documentation

Documentation are descriptions and guides written for code users. 

## Inline Comments

Code comments should use `#`, and be written at the same indentation level of the code it describes. 

How to use comments:
- Generally:
    - focus on the how and why, over literal 'what is the code'
    - explain any context needed to understand the task at hand
    - give a broad overview of what approach you are taking to perform the task
    - if you're using any unusual approaches, explain what they are, and why you're using them
- Comments need to be maintained - make sure to keep them up to date

#### Bad Comments



{:.input_area}
```python
# This is a loop that iterates over elements in a list
for element in list_of_elements:
    pass
```


#### Good Comments



{:.input_area}
```python
# Because of X, we will use approach Y to do Z
for element in list_of_elements:
    pass
```


## Docstrings

<div class="alert alert-success">
Docstrings are in code text that describe modules, classes and functions. They describe the operation of the code.
</div>

<div class="alert alert-info">
[Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. 
</div>

### Example Docstring



{:.input_area}
```python
def add(num1, num2):
    """Add two numbers together. 
    
    Parameters
    ----------
    num1 : float
        The first number, to be added. 
    num2 : float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer
```


### Docstrings are available through the code



{:.input_area}
```python
# The `help` function prints out the `docstring` of an object (module, function, class)
help(add)
```


{:.output_stream}
```
Help on function add in module __main__:

add(num1, num2)
    Add two numbers together. 
    
    Parameters
    ----------
    num1 : float
        The first number, to be added. 
    num2 : float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition.


```

### `__doc__`



{:.input_area}
```python
# Docstrings get stored as the `__doc__` attribute, and can also be accessed from there
print(add.__doc__)
```


{:.output_stream}
```
Add two numbers together. 
    
    Parameters
    ----------
    num1 : float
        The first number, to be added. 
    num2 : float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    

```

### Clicker Question #2

What should be included in a docstring?

- 1) Input arguments and their types
- 2) A brief overview sentence about the code
- 3) A copy of the `def` line
- 4) Returned variables and their types
- 5) A step by step description of the procedure used in the code

A) 1, 4 | B) 2, 3, 5 | C) 3, 5 | D) 1, 2, 4 | E) 1, 2, 3, 4, 5

## Project Documentation

Project Documentation Files:
- A `README` is a file that provides an overview of the project to potential users and developers
- A `LICENSE` file specifies the license under which the code is available (the terms of use)
- An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
- Tutorials and/or Examples show examples and tutorials for using the codebase

## Documentation Sites

<div class="alert alert-success">
Documentation sites are a host of a package's documentation, for code users. 
</div>

<div class="alert alert-info">
For an example of a documentation site, check out the [neurodsp](https://voytekresearch.github.io/neurodsp/), docsite, as well as the source code (with comments), on [Github](https://github.com/voytekresearch/neurodsp/).
</div>
