# CL5: Debugging

Welcome to the fourth coding lab!

In this CodingLab we will be thinking and working on debugging & objects. 

We will also start thinking about exploring all of the Python resources and tools that are available, with an eye towards starting to think about the projects.

ANSWERS: There may be many valid answers to the questions in this coding lab, so it's fine if your answers differ to those provided here, if they have the right output. 

## Part I: (More) Functions 

### Reverse a string Function

Write a function `reverse_string` that will take a string as an input and `return` the reverse of that string as its output. (For example, if the input were 'apple' the function woudl return 'elppa'

Note that there are multiple ways in which to approach this. One possible approach would use the logic laid out in this pseudocode:

```python
# define function with input
    
    # generate empty string
    # start counter at the length of the input string
    
    # while the counter is more than zero
        # add the letter at index into the input string starting at end of input string to growing string
        # decrease counter by 1
    
    # return string 
```

def reverse_string(input_string):
    
    rev = ''
    counter = len(input_string) 
    
    while counter > 0: 
        rev = rev + input_string[counter - 1]
        counter = counter - 1
    
    return rev

assert reverse_string('apple') == 'elppa'

### Palindrome Function

Write a function `check_palindrome` that takes a string as an input and within that function determines whether the input string is a palindrome or not (a word or phrase that is read the same forward as it is backward - i.e. kayak, dad, etc.). 

If it is a palindrome, `return` 'Hey! That's a palindrome!'

If it is not a palindrome, `return` 'Bummer. Not a palindrome.'

Remember that you created a function that can reverse a string above.

def check_palindrome(input_string):
    rev = reverse_string(input_string)

    if rev == input_string:
        out = "Hey! That's a palindrome!"
    else:
        out = "Bummer. Not a palindrome."
    
    return out

assert check_palindrome('kayak') == "Hey! That's a palindrome!"
assert check_palindrome('blargh') == 'Bummer. Not a palindrome.'

## Part II: Debugging Questions

### Creating Errors
For each of the follow Exceptions, write a small piece of code that will cause it to happen:
- ZeroDivisionError
- SyntaxError
- IndentationError
- TypeError
- IndexError
- KeyError
- ValueError
- NameError

# Zero Division Answer
1/0

# Syntax Answer
for el in [1, 2]
    print(el)

# Indentation Error
for el in [1, 2]:
print(el)

# Type error
(1, 2) + (2)

# Index Error
lst = [1, 2]
lst[2]

# Key Error
my_dict = {'a': 1, 'b':2}
my_dict['c']

# Value Error
int('a')

# Name Error
a

### Fixing Errors

For each of the following cells, try to debug the code to fix any errors, and get it running. 

if True
    print('It worked')
# Answer: add a ':' to open the conditional code block

age_string = "My favourite number is " + 27
# Answer: typecase int to string, `+ str(27)`

my_list = [1, a, 24]
# Answer: assuming `a` was supposed to be a string, update to 'a'

my_list2 = ['1st', '2nd', '3rd', '4th', '5th']
print('Printing the 3rd element of my list ' + my_list2(2))
# Answer: wrong syntax to index, replace with '[]'

print('Three plus five equals' + str(3+5)
# Answer: Missing closing parenthesis - add ')' at the end

## Part III: Debugging Challenges

### Debugging A Function

The following function has a series of issues with it. 

Work through debugging this function, fixing it up to be able to run with all the inputs below. 

def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1
        if input_1[0] = 0:
        answer = 0
    
    elif len(input_2) == 2:
        answer = input_2[1] / input_1[0]
        
    elif len(input_1) == len(input_2):
        answer = input_1[0] + input_2[0]
        
    print(answer)

# ANSWER: Fixed version
def my_function(input_1, input_2):
    """A long function that might error."""
    
    if len(input_1) > 1:
        if input_1[0] == 0:
            answer = 0
    
    elif len(input_2) == 2:
        try:
            answer = input_2[1] / input_1[0]
        except ZeroDivisionError:
            answer = None
        
    elif len(input_1) == len(input_2):
        try:
            answer = input_1[0] + input_2[0]
        except TypeError:
            answer = None
        
    print(answer)

my_function([0, 1], [0])

my_function([0], [0, 1])

my_function([1], [1])

my_function([1], ['1'])

## Exploring Code

One of the great things about Python is how many tools, utilities and examples there are out there.

Let's start exploring what is available. GitHub is a website that people use to save and present code, below we have some notebooks that are hosted on GitHub showing the projects that they have made. Take time to look at one of the notebooks below that intrests you and read the explination as well as getting an understanding of what is being performed in each of the code cells. 

- https://anaconda.org/jbednar/census/notebook - Demographic data plotted out on maps of the US, showing differences in racial segregation/integration in different cities.
- https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#linguistics-and-text-mining - Mining text to learn trends in bodies of text.
- https://anaconda.org/jbednar/nyc_taxi/notebook - NYC taxi data plotted out on cities of NYC
- https://www.fullstackpython.com/ - for advanced python user, next level guideline

<div class="alert alert-info">
Go and explore <a href="https://github.com">GitHub</a>, and search for some Python projects. And/or check out this list of interesting <a href="https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks">Jupyter Notebooks</a>. 
</div>