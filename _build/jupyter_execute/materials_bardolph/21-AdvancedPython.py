**Course Announcements**

Due Dates:
- Final Project/Exam (Fri 6/11 at 11:59 PM)
    - Practice Final exam now available on datahub  (answer key will be posted this weekend)


Notes:
- Please fill out your CAPEs (+1% if >=85% response rate) - current: ~30%
- Coding Labs - nothing to turn in; ~OH; get your questions answered
- Additional OH will be Wed of Finals Week 
    - 10 min slot by appt
    - 9AM-noon; 2-3 PM
    - details are pinned on Piazza
    - will use a different zoom link than normal

**Q&A**

Q: Must we use the terminal in tandem with the notebook? Or can we simply use the notebook? What is the best way to go about this project?  
A: Yup - you can. You're encouraged to approach the project however you're most comfortable. Many students are most comfortable in the notebook, so we encourage you to start there (like we are doing in lecture) and move to a .py file from there. However, if you're more comfortable/have experience in a different environment, feel free to use that!

Q: Will you be creating new files for the exam or will they already be in the folder and we will have to be adding code inside of them?  
A: I will create them and have them in the folder for you. You will then add/edit code in them.

Q: From the project we were working on during lecture, would it have been possible to keep punctuations and have them be printed out in the output? Would we have just changed the part of the loop where we said it would be == None ?  
A: Yup! A conditional could be used to control this. At the end of the projects set of notes, we're going to discuss improvements. This is one of them! 

Q: I am curious on how extensive the final exam will be in terms of how many functions or classes will need to be written, since the example from this lecture only had 3 functions.  
A: It will be similar to example in class. You can expect to write 2 functions and debug/fix code style on a third. You will also have to write code tests. The code written on the final exam is *not* super extensive.

Q: I was confused about refactoring and if it only involves a chatbot or is that most commonly used?  
A: Refactoring is *not* specific to chatbots. Rather, it's specific to code - we'll discuss this more in today's lecture.

Q: When do we need to use numpy method, and when we can just use the normal python method?  
A: When you want to operate on matrices/arrays, you'll need `numpy`.

Q: Why do we need to use the terminal if we can use the notebook for most things? The purpose of the terminal is somewhat confusing.  
A: Notebooks are big and bulky. The terminal is faster and allows for streamlined organization. You won't *need* to use the terminal, but it can save you *a lot* of time.

Q: Do we have to use a separate file for the tests we write? Can we just include them in the Jupyter notebook?  
A: They must be in a separate file. We will be using `pytest` on that file.

Q: How do you create a new module and import the code on Jupyter?  
A: You create a .py file in the same directory as your notebook. You store code in that .py file. Then, you can import it into the notebook.

Q: For the atbash example, if we write those three functions in a module, would it be more efficient to write `from atbash import *` than `from atbash import atbash_encrypt, atbash_decrypt, atbash_wrapper`? 

A: While that would be more efficient, it would also be unclear in your code where those functions you're using came from. Instead, you could use `import atbash as ab` and then use `ab.` to refer to your functions in your code, if you prefer.

Q: How does running pytest in the terminal rather than the notebook differ?  
A: It doesn't. Anytime you start with `!` in the notebook, it's the same as running from the terminal.

Q: Do we get a feedback if we submit the project early and can we fix it again and resubmit? Thank you so much  
A: No sorry - we just won't have the capacity to do this for everyone; however, we could answer questions/look it over quickly in office hours?

Q: I'm confused how to figure out what tests to use.  
A: Think about what your function/class/method does or should do, and be sure you test that given an input, the expected output is returned. Those are the most important tests.

Q: How extensive should our tests be?  
A: They should test the functionality of your class/method/function. They do not have to consider all edge cases (if this were an intermediate python course, that answer would be different and tests would need to be more involved).

Q: I want to ask why my Sublime page looks different with our professor's Sublime. Also, I want to ask where should we save the sublime file?  
A: I have different settings specified to color my code the way I like it. You can Google how to change code highliting in Sublime to change your's too!

Q: Is it better to poorly refactor a code or to just leave it as is when it is totally functioning.?   
A: First priority: functioning code; Second priority: refactored, clean code.

Q: I am interested in finding more "assignments" to do to get more familiar with python after the conclusion of this class. Are there any public assignments from previous Cogs 18 courses that are viewable?  
A: Not really, *but* I'm going to be editing [this](https://shanellis.github.io/pythonbook/content/intro.html) over the summer to include lots of old COGS 18 examples in the exercises and to add an answer key, so there should be come Fall!

Q: For a first time coder how do you suggest I go about the coding project to not stress myself out entirely and question everything I am doing?   
A: Go in with a plan and *think* before doing. New programmers too often just "try everything" before stepping back and thinking about what they want to do and what they need to accomplish that.

Q: If we decide to do the final exam, will we have to do our own assertion tests?  
A: Yes.

Q: Are we allowed to use other imported functions in our code?  
A: Yup! On the final project, it's up to you!


# Advanced Python

- string formatting (`format`)
- sets
- `collections`
- args & kwargs
- list comprehensions
- map
- APIs
- Software versioning
- overloading operators

...or: a day of shortcuts

Note: Shortcuts make *your* life easier, but your code *less* understandable to beginners.

It's hard to search for things you don't know exist.

Today's goal : let you know these things exist.

NOT today's goal : teach you all the details.

You do *not* need to incorporate these into your project, but if they'll help you, go for it!

import antigravity

## String Formatting

Use the `format` method to manipulate and format strings.

name = "Shannon"
job = "Assistant Teaching Professor"
topic = "Python"

"Hello! My name is {}. My job is {}, and I work on {}".format(name, job, topic)

## Sets 

Sets are a variable type that store **only unique entries**.

my_set = set([1, 1, 2, 3, 4])
my_set

Like lists, they are iterable & mutable.

my_set.add(6)
my_set

#### Clicker Question #1

How many values would be in the following set?

clicker_set = set([1, 1, 2, 2, 3, 4])
clicker_set.add(6)
clicker_set.add(1)
clicker_set

- A) 0
- B) 4
- C) 5
- D) 6
- E) ¯\\\_(ツ)\_/¯

Reminder that if you add a value that is already in the set...the set will not change

## Collections

The `collections` module has a number of useful variable types, with special properties. 

"Special editions" of collections we've discussed before (lists, tuples, and dictionaries).

from collections import Counter

# count how many elements there are in collection
# return values in a dictionary
Counter([1, 0, 1, 2, 1])

import collections

collections.Counter([1, 0, 1, 2, 1])

# can count how many of each letter are in there
Counter("I wonder how many times I use the letter 'e'")

Think back to our encryption scheme! 

The most common letter in the English language is 'e'.

If you just move each letter over by 1 position, you can just use a Counter to crack the code.

Why we moved to a variable encoder!

## `any` & `all`

`any` and `all` evaluate collections for whether elements evaluate as True. 

my_bool_list = [True, False, True]

any(my_bool_list)

all(my_bool_list)

#### Clicker Question #2

What would the following return?

my_list = [True, True, False, True]
any(my_list)

- A) `True`
- B) `False`
- C) `[True, True, True]`
- D) `[False]`
- E) ¯\\\_(ツ)\_/¯

## `getattr` & `setattr`

`getattr` and `setattr` can be used to get and set attributes, respectively. 

Flexibly return and define instance attributes.

class MyClass():
    
    def __init__(self):        
        self.var_a = 'string'
        self.var_b = 12

# create instance 
instance = MyClass()

instance.var_a

# Get a specified attribute
# define var_a as an input
getattr(instance, 'var_a')

# Set a specified attribute
setattr(instance, 'var_b', 13)
print(instance.var_b)

## `args` & `kwargs`

- allow you to pass a variable number of arguments to a function
    - `*args` - allow any number of extra arguments (including zero)
    - `**kwargs` - allow any number of *keyword* arguments to be passed (as a dictionary)

### `*args`

# use *arguments to demonstrate args
def tell_audience(*arguments):
    for arg in arguments:
        print(arg)

tell_audience('asdf')

tell_audience("Hello!", 
              "My name is Shannon.", 
              "My job is Assistant Teaching Professor.")

### `**kwargs`

def tell_audience_kwargs(**info):
    print("type: ", type(info), '\n')
    
    for key, value in info.items():
        print("key: ", key)
        print("value: ", value, "\n")

tell_audience_kwargs(first='Shannon', 
                     last='Ellis', 
                     email='sellis@ucsd.edu')

## List Comprehensions

List comprehensions allow you to run loops and conditionals, *inside lists*.

The general format is :

`[ expression for item in list if conditional ]`


# NOT a list comprehension
# how we've been doing it
input_list = [0, 1, 2]
output_list = []

for ind in input_list:
    output_list.append(ind + 1)
    
# look at output
output_list

# This list comprehension is equivalent to the cell above
# note the square brackets on the outside
[ind + 1 for ind in [0, 1, 2]]

# You can also include conditionals inside a list comprehension
my_list = [1, 2, 3, 4, 5]
my_list2 = [val for val in my_list if val % 2 == 0]

print(my_list)
print(my_list2)

#### Clicker Question #3

What would the following return?

list1 = [3, 4, 5]
multiplied = [item * 3 for item in list1] 
multiplied

- A) `True`
- B) `False`
- C) `[9, 12, 15]`
- D) `15`
- E) ¯\\\_(ツ)\_/¯

Note: there are also tuple & dictionary comprehensions. They're just used less frequently.

## Regular Expressions

Regular expressions allow you to work with **specified patterns in strings**.

import re

my_string = "If 12 Python programmers try to complete 14 tasks in 16 minutes, why?"

# can just search for a letter
re.findall('o', my_string)

# but the patterns are where these shine
re.findall('\d\d', my_string)

## filter

`filter` is a function that takes in another function, and a collection object, and **filters the collection with the function**. 

def is_bool(val):
    if isinstance(val, bool):
        return True
    else:
        return False

#filter?

out = []

for val in [1, False, 's', True]:
    out.append(is_bool(val))

out

# apply function to every element of list
# function to apply is first input to filter
list(filter(is_bool, [1, False, 's', True]))

## Lambda Functions

Lambda functions are small, anonymous functions. 

Can define them in line.

increment = lambda a: a + 1

increment(1)

# not a lambda function
def lambda_equivalent(a):
    
    output = a + 1
    
    return output

lambda_equivalent(1)

#### Clicker Question #4

What would the following return?

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
new_list

- A) `[1, 5, 11, 3]`
- B) `[1, 3, 5, 11]`
- C) `[4, 6, 8, 12]`
- D) `[1, 5, 4, 6, 8, 11, 3, 12]`
- E) ¯\\\_(ツ)\_/¯

## map

`map` applies a given function to each element in a collection. 

# create a function
def double(val):
    return val * 2

# map function to each element of list
my_list = [1, 2, 3, 4]
list(map(double, my_list))

# Note - we can use lambda functions with map
list(map(lambda x: x *2, my_list))

## Conditional Assignment

You can use a conditional within an assignment, to manipulate what gets assigned given some condition. 

# variable assignment
condition = False
my_var = 1 if condition else 2

print(my_var)

## Unpacking

You can unpack collection objects with `*`, and key, value pairs with `**`. 

def my_func(xx, yy, zz):
    print(xx, yy, zz)

# create list
my_list = [1, 2, 3]

# this will error
my_func(my_list)

# unpack the list
my_func(*my_list)

# create dictionary
my_dict = {'xx' : 1, 'yy' : 2, 'zz' : 3}

# unpack the dictionary
my_func(**my_dict)

## Application Programming Interface

<div class="alert alert-success">
An <b>API</b> is a programmatic interface to an application - a software to software interface, or way for programs to talk to other programs. 
</div>

If you are pointing and clicking on computer applications, that is _not_ an API.

If you are writing code to interact with software and get information, that _IS_ an API.

### Module APIs

Modules have an API. Every time you write or use a set of functions and/or classes, you are writing or using an API. 

### Web APIs

APIs are an interface to interact with an application, _designed for programmatic use_ :
- They allow systematic, controlled access to (for example) an applications database and procedures
- They can be used to request data and/or to request that the the application perform some procedure

### RESTful API

(Representational State Transfer API) 

An approach to interact with web addresses

## Twitter API

# to use this on your computer
# uncomment and run following line
# !pip install tweepy

Then, follow the instructions [here](https://www.digitalocean.com/community/tutorials/how-to-authenticate-a-python-application-with-twitter-using-tweepy-on-ubuntu-14-04) for authetication of tweepy with Python.

# Accessing Twitter API from Python
#  Note: to run this, you will have to fill in stw.py with your OAuth credentials.
#    You can do that here: https://apps.twitter.com/

# Import tweepy to access API
import tweepy
from tweepy import OAuthHandler

# Import my API credentials
from stw import *

# Twitter API requires Authentification with OAuth
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # Create an API object to access Twitter
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    # Process a single status
    print(status.user.name)
    print(status.text, '\n')

## Overloading Operators

In other words: Nothing in Python is sacred.

Operators and special operations for objects are defined by double underscore methods, which we can overload to change how the object acts. 

class Language():
    
    def __init__(self, name):
        self.name = name.lower()
    
    # Overload what the printed representation of the object as a string
    def __repr__(self):
        return "The programming language " + self.name
    
    # Overload the greater than symbol
    def __gt__(self, other):
        return True if self.name == 'python' else False

Note: "dunder" is how we refer to those double underscore methods

python = Language('python')
perl = Language('perl')

print(python)

python > perl