**Course Announcements**

Due Dates:
- **CL8** due tonight
- **A5** due Monday

Notes:
- Scientific Computing Lecture on Canvas issue:
    - Have reuploaded lecture on Media Gallery (will be out of order)
- No Lecture/OH on Monday (Memorial Day Holiday)
- Folder for module/scripts practice: CL7_student_examples

# Documentation

- readability
- comments
- documentation
- versioning

## Code Readability (API)

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

Clear names are for humans. The computer doesn't care, but you and others reading your code do.

### Code comments & Documentation

Helpful comments and documentation take your code to the next level. The final piece in the trifecta of readable code! 

Good code has good documentation - but code documentation should _not_ be used to try and fix unclear names, or bad structure. 

Rather, comments should add any additional context and information that helps explain what the code is, how it works, and why it works that way. 

These will all be components of your final project grade.

#### Clicker Question #1

What does the following code do?

def ff(jj):
    oo = list(); jj = list(jj) 
    for ii in jj: oo.append(str(ord(ii)))
    return '+'.join(oo)
ff('Hello World.')

- A) Returns unicode code points, as a list
- B) Encodes a string as a cypher, returning a string of alphabetical characters
- C) Returns unicode code points, as a string
- D) Encodes inputs alphabetical characters, returned as a list
- E) This code will fail

Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code

list('Hello World.')

def return_unicode(input_list):
    string = list()
    input_list = list(input_list)
      
    for character in input_list: 
        string.append(str(ord(character)))
        
    output_string = '+'.join(string)
    return output_string

return_unicode('Hello World.')

- A) Returns unicode code points, as a list
- B) Encodes a string as a cypher, returning a string of alphabetical characters
- C) Returns unicode code points, as a string
- D) Encodes inputs alphabetical characters, returned as a list
- E) This code will fail

Improvement Considerations:
- Structural considerations: indentations & spacing
- Improved naming: functions & variables
- Add Comments within code
- **Proper Documentation!**

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

# This is a loop that iterates over elements in a list
for element in list_of_elements:
    pass

#### Good Comments

# Because of X, we will use approach Y to do Z
for element in list_of_elements:
    # comment for code block
    pass

## Docstrings

<div class="alert alert-success">
<b>Docstrings</b> are in-code text that describe modules, classes and functions. They describe the operation of the code.
</div>

### Numpy style docs
[Numpy style docs](https://numpydoc.readthedocs.io/en/latest/format.html) are a particular specification for docstrings. 

### Example Docstring

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
    answer : int or float
        The result of the addition. 
    """
    
    answer = num1 + num2
    
    return answer

Docstrings

- multi-line string that describes what's going on
- starts and ends with triple quotes `"""`
- one sentence overview at the top - the task/goal of function
- **Parameters** : description of function arguments, keywords & respective types
- **Returns** : explanation of returned values and their types

**Docstrings** are available to you *outside* of the source code.

### Docstrings are available through the code

add?

# The `help` function prints out the `docstring` 
# of an object (module, function, class)
help(add)

### `__doc__`

# Docstrings get stored as the `__doc__` attribute
# can also be accessed from there
print(add.__doc__)

#### Clicker Question #2

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

1. Your original code definitely needs `numpy` docstrings (required)
2. It's best if all your main functions have docstrings (optional)
    - If you include functions from an assignment, go ahead document them
    - If you write a teeny tiny function to accomplish a super small task, no need to document

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

## Software Versioning

When you make changes to the software you've released into the world, you have to change the version of that software to let people know changes have occurred.

### Versioning Schemes

The rules, if you're new to this can be [dizzying](https://www.python.org/dev/peps/pep-0440/#version-scheme), so we'll [simplify](https://www.python.org/dev/peps/pep-0396/) for now:

- `<MAJOR>.<MINOR>`
    - i.e. 1.3
    
- `<MAJOR>.<MINOR>.<MAINTENANCE>`
    - i.e. 1.3.1

- `<MAJOR>` - increase by 1 w/ incompatible API changes
- `<MINOR>` - increase by 1 w/ added functionality in a backwards-compatible manner
- `<MAINTENANCE>` - (aka patch) increase by 1 w/  backwards-compatible bug fixes.

# see version information
import pandas as pd
pd.__version__

In Python package development... when `<MAJOR>` == 0, suggests a package in development

# see version information
!pip show lisc