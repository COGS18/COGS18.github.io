---
interact_link: content/materials/19-Documentation.ipynb
download_link: assets/downloads/19-Documentation.ipynb.zip
pdf_link: assets/pdf/19-Documentation.pdf
layout: materials
title: '19-Documentation'
prev_page:
  url: /materials/18-ScientificComputing
  title: '18-ScientificComputing'
next_page:
  url: /materials/20-CodeStyle
  title: '20-CodeStyle'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

### Clicker Warm Up

**Debugging a function**

You want to write a function that returns the keys from a dictionary in a list. You want these keys to be sorted (either numerically or alphabetically), with the option to reverse the order. Your first attempt at writing this function is below...

Think through the logic of this code or run the code for the following function in your notebook. Think about how you would go about editing/testing this code so that it will (1) execute and (2) do what you want.

1. Test it - define the function; try to call the function
2. Look at the error - try to fix code (`get.keys` -> `keys()`)
3. Iterate through - re-run
4. Test out all scenarios
5. Edit until it does what you want.



{:.input_area}
```python
def sort_keys(dictionary, reverse_it = False):
    
    keys = dictionary.keys()
    sorted_keys = sorted(keys, reverse = reverse_it)

    return sorted_keys
```




{:.input_area}
```python
sort_keys({'A': 3, 'C': 2, 'B': 3})
```





{:.output_data_text}
```
['A', 'B', 'C']
```



- A) I have a plan!
- B) I think I've got a plan!
- C) I'm stuck.

iclicker Frequency Code: CA

## Project Notes

1. Zip file with proposed project structure on website
2. Datahub vs. Locally
3. Creating a module:
    - Create a text file in your project directory. 
    - Save with .py extension
    - Add a function/class to file
    - Save changes
    - `import` to Jupyter notebook
    - use function
4. Turn in as a zip file of your project directory

# Documentation

- readability
- comments
- documentation

### Zen of Python

- 20 guidelines (the 20th is missing)
- sometimes contradictory in favor of flexibility



{:.input_area}
```python
# a hidden easter egg
import this
```


{:.output_stream}
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

## Clicker Question #1

Read through and think about the statements in the Zen of Python Which do you think is the most important? 

The one I think is most important is in...

- A) 1-5
- B) 6-10
- C) 11-15
- D) 16-19
- E) ¯\\_(ツ)_\/¯

Tim Peters -- the author of the Zen of Python -- is a software developer and was a major contributor to the Python Programming language.

## A Brief Note

The Zen of Python is a set of guidelines for Python.

There are arguments for and against any of these.

Different languages take different approaches.

Language Wars are stupid.

**Fun fact**: Python is named after the British TV show Monty Python (not the snake).



## Code Readability

"Code is more often read than written" - Guido van Rossum

So: code should be written to be readable by humans.

Note: one of those humans is future you.

### Writing Readable Code

So how do we write good code for humans?

- Use good structure
- Use good naming
- Use code comments and include documentation

### Good Structure

If you design your program using separate functions for each task, avoid copying + pasting (functions and loops instead), and consider structure beforehand, you'll be set up for success

### Good Naming

We discussed this in the API lecture. Clear names are for humans. The computer doesn't care, but you and others reading your code do.

### Code comments & Documentation

Helpful comments and documentation take your code to the next level. The final piece in the trifecta of readable code! 

Good code has good documentation - but code documentation should _not_ be used to try and fix unclear names, or bad structure. 

Rather, comments should add any additional context and information that helps explain what the code is, how it works, and why it works that way. 

These will all be components of your final project grade.

### Clicker Question #2

What does the following code do?



{:.input_area}
```python
def ff(jj):
    oo = list(); jj = list(jj) 
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
ff('Hello World.')
```





{:.output_data_text}
```
'72+101+108+108+111+32+87+111+114+108+100+46'
```



- A) Returns unicode code points, as a list
- B) Encodes a string as a cypher, returning a string of alphabetical characters
- C) Returns unicode code points, as a string
- D) Encodes inputs alphabetical characters, returned as a list
- E) This code will fail

Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code



{:.input_area}
```python
# let's improve...
def return_unicode(input_list):
    string = list()
    input_list = list(input_list)
      
    for character in input_list: 
        string.append(str(ord(character)))
        
    output_string = '+'.join(string)
    return output_string

return_unicode('Hello World.')
```


Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code
- **Proper Documentation!**



{:.input_area}
```python
# Let's fix this code!
def convert_to_unicode(input_string):
    """Converts an input string into a string containing the unicode code points.
    
    Parameters
    ----------
    input_string : string
        String to convert to code points
        
    Returns
    -------
    output_string : string
        String containing the code points for the input string.
    """
    
    output = list()

    # Converting a string to a list, to split up the characters of the string
    input_list = list(input_string)
    
    for character in input_list:
        
        temp = ord(character)
        output.append(temp)

    output_string = '+'.join(output)
        
    return output_string
```


## Code Documentation

<div class="alert alert-success">
Code documentation is text that accompanies and/or is embedded within a software project, that explains what the code is and how to use it. 
</div>

Stuff written for humans in human language to help the humans.

## Code Comments vs. Documentation

#### Comments

Comments are string literals written directly in the code, typically directed at developers - people reading and potentially writing the code. 

#### Documentation

Documentation are descriptions and guides written for code users. 

## Inline Comments

Code comments should use `#`, and be written at the same indentation level of the code it describes. 

How to use comments:
- Generally:
    - focus on the *how* and *why*, over literal 'what is the code'
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
    # comment for code block
    pass
```


## Docstrings

<div class="alert alert-success">
<b>Docstrings</b> are in-code text that describe modules, classes and functions. They describe the operation of the code.
</div>

### Numpy style docs
[Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. 

### Example Docstring



{:.input_area}
```python
def add(num1, num2):
    """Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer
```


Docstrings

- multi-line string that describes what's going on
- starts and ends with triple quotes `"""`
- one sentence overview at the top - the task/goal of function
- **Parameters** : description of function arguments, keywords & respective types
- **Returns** : explanation of returned values and their types

**Docstrings** are available to you *outside* of the source code.

### Docstrings are available through the code



{:.input_area}
```python
add?
```




{:.input_area}
```python
# The `help` function prints out the `docstring` 
# of an object (module, function, class)
help(add)
```


{:.output_stream}
```
Help on function add in module __main__:

add(num1, num2)
    Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition.


```

### `__doc__`



{:.input_area}
```python
# Docstrings get stored as the `__doc__` attribute
# can also be accessed from there
print(add.__doc__)
```


{:.output_stream}
```
Add two numbers together. 
    
    Parameters
    ----------
    num1 : int or float
        The first number, to be added. 
    num2 : int or float
        The second number, to be added.
    
    Returns
    -------
    answer : float
        The result of the addition. 
    

```

### Clicker Question #3

What should be included in a docstring?

1) Input arguments and their types  
2) A brief overview sentence about the code  
3) A copy of the `def` line  
4) Returned variables and their types  
5) A step by step description of the procedure used in the code  

- A) 1, 4 
- B) 2, 3, 5
- C) 3, 5 
- D) 1, 2, 4 
- E) 1, 2, 3, 4, 5

### Projects & Documentation

**Do *all* of my functions need `numpy` documentation?**

1. Your original code definitely needs `numpy` docstrings
2. It's best if all your main functions have docstrings
    - If you include functions from an assignment, document them
    - If you write a teeny tiny function to accomplish a sumer small task, no need to document

## Documentation for a Software Project

Documentation Files:
- A `README` is a file that provides an overview of the project to potential users and developers
- A `LICENSE` file specifies the license under which the code is available (the terms of use)
- An `API Reference` is a collection of the docstrings, listing public interfaces, parameters and return values
- Tutorials and/or Examples show examples and tutorials for using the codebase

## Documentation Sites

<div class="alert alert-success">
Documentation sites are a host of a package's documentation, for code users. 
</div>

### Example: Function Documentation
`numpy.array` :
https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html

### Example: Package Documentation
**scikit learn** (`sklearn`) : https://scikit-learn.org/stable/index.html

# Open Source

<div class="alert alert-success">
Open source software is software for which the source code is openly available.
</div>

The Source Code for Python (which is actually written in C) is all available.

Open Source Software is free. (free = freedom)

Open source software is software that the user can:

- use and install the software
- view the source code of the project
- distribute the software
- change the source code of the project

Scientific research is often done in an exclusively open source environment.
