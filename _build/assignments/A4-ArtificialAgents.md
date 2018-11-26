---
interact_link: content/assignments/A4-ArtificialAgents.ipynb
download_link: assets/downloads/A4-ArtificialAgents.ipynb.zip
layout: notebooks
title: 'A4-ArtificialAgents'
prev_page:
  url: /assignments/A3-Chatbots
  title: 'A3-Chatbots'
next_page:
  url: /projects/ProjectIdeas
  title: 'Projects'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Assignment 4: Artificial Agents

## Overview

This assignment covers Classes & Objects, and builds up to the application of Artificial Agents.

This assignment is out of 8 points, worth 8% of your grade.

Make sure your completed assignment passes all the asserts. This assignment also has some hidden tests - which means that passing all the asserts you see does not guarantee that you have the correct answer! Make sure to double check and re-run your code to make sure it does what you expect.

## Setup

#### Code Imports

You must run the following cell before proceeding with the assignment. 



{:.input_area}
```python
# Setup - run this cell before doing the next part of the assignment
#   This cell imports some extra code, making it available for us to use later

import random
import string

from time import sleep
from IPython.display import clear_output
```


## Part 1: Functions & Methods (re-visited)

In this part, we will revisit and extend some work on using functions and methods.

We will also write some functions that we will use later in the assignment for the 'bots' application.

### Q1 - String Methods  (1 point)

First, we will explore some of methods from the `str` class.

#### a) `join`

During the last assignment you made a function that echoed a string several times with a seperator between each repetition. 

Here we will achieve a similar goal through the use of the `join()` method of the `str` class. 

When `join()` is called on a `str` object (let's call it `seperator`) with a `list` as its argument, it joins the elements of the `list`, seperating each one by `seperator`. 

Below we define a a list `my_list`. Use the `join()` method on the string you define as `seperator = '~'` to join the elements in `my_list` seperated by the `'~'` character. 

Save the output to a new variable called `joined_string`. The output should look as follows:

`'Python~is~so~much~fun'`



{:.input_area}
```python
# This variable provided for you
my_list = ['Python', 'is', 'so', 'much', 'fun']

# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(joined_string, str)
assert joined_string == 'Python~is~so~much~fun'
```


#### b) `replace`

Now try to use the `replace` method to update the string `statement` such that it replaces `UCLA` to `UCSD`. 

If you are unsure how use `replace` you can run `str.replace?` to look at documentation.

Note that using `replace` returns a new string that you need to assign to a variable if you want to keep a reference to it (`replace` is not 'inplace'). 

For this question, overwrite `statement` as the assignment to the output of the `replace` call.



{:.input_area}
```python
# This code provided for you
statement = 'UCLA is the best UC in Southern California.'

# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(statement, str)
assert statement == 'UCSD is the best UC in Southern California.'
```


#### c) `replace` for dropping characters

Use the `replace` method to remove all the exclamation points in the string `excessive`.

Assign the output of doing this to a variable called `fixed`.

Hint: you can drop characters with `replace` by 'replacing' them with an empty string.



{:.input_area}
```python
# This variable provided for you
excessive = 'using!!! excessive!!! exclamation points!! is the best!!!!!!'

# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(fixed, str)
assert fixed == 'using excessive exclamation points is the best'
```


#### d) Clearing all punctuation with `replace`

Now we want to generalize what we did in 'c)' to remove all punctuation using the `replace()` method.

Write a `for` loop to loop over every character in `string.punctuation`. Inside the loop, call `replace` on `too_much` with the current punctuation character to remove it, like we did in 'c)'.

To do this, inside the loop, re-assign `too_much` to be the ouput of calling `replace` on `too_much`, so that you are replacing `too_much` with it's updated version every time.



{:.input_area}
```python
# This variable provided for you
too_much = 'I, think th@at!! punctuation... may?>> be the bes$$$t th!ing thats: ever! been! invented!!!!!!'

# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(too_much, str)
assert too_much == 'I think that punctuation may be the best thing thats ever been invented'
```


### Example: Functions with Default Values

Note that functions can also have inputs with default values.

This means you don't necessarily need to provide an input with a specific value, since if you don't provide it explicitly, it will take on the default value. 

The following is an example of a function with a default value, provided to you, so you can see what it looks like.

You don't need to do anything with this function.



{:.input_area}
```python
def default_function(input_number, n_value=2):
    """Multiplies an input number n times. Default value for n=2
    
    Parameters
    ----------
    input_number : float
        Number to be multiplied.
    n_value : int, optional
        Number of times to multiply input.
        
    Returns
    -------
    output : float
        Result of the multiplication. 
    """
    
    # Multiple the input n times
    output = input_number * n_value
    
    return output
```




{:.input_area}
```python
# Test using `default_function`
print(default_function(2))
print(default_function(2, 10))
```




{:.input_area}
```python
# Function values can be also be defined by name
print(default_function(n_value=-1, input_number=2))
print(default_function(input_number=10, n_value=10, ))
```


### Q2 - Default Value Functions (0.5 points)

#### a) Sort Keys

Write a function called `sort_keys`, which will return a sorted version of the keys from an input dictionary. 

Input(s):
- `dictionary` : dictionary
- `reverse` : boolean, default: False

Output(s):
- `sorted_keys` : list

Procedure(s):
- Get the keys from the input `dictionary` using the `keys()` method (this will return a list of keys)
- Use the `sorted` function to sort the list of keys. Pass in `reverse` to `sorted` to set whether to reverse the sort order
- Return the sorted list of dictionary keys



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(sort_keys)
assert isinstance(sort_keys({'B': 2, 'A': 1}), list)
assert sort_keys({'B': 2, 'A': 1}) == ['A', 'B']
assert sort_keys({2: 'B', 1: 'A'}, reverse=True) == [2, 1]
```




{:.input_area}
```python
assert callable(sort_keys)

```


#### b) List Powers

Write a function called `list_powers`. 

This function will take a list, and return a new list where each element is exponentiated to a specified power. 

Input(s):
- `collection` - collection of numbers
- `power` - int, default value: 2

Output(s):
- `power_list` - list of numbers

Procedure(s):
- Initialize an empty list to be filled and returned
- Loop through each element in the input `collection`
    - Take the value to the power specified in `power`
    - Append the result to the output list
- Return the list of powers



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(list_powers)
assert isinstance(list_powers([1, 2]), list)
assert list_powers((2, 4)) == [4, 16]
assert list_powers([2, 4], 3) == [8, 64]
```




{:.input_area}
```python
assert callable(list_powers)

```


### Example: Zip

A reasonably common task in Python is to want to iterate across multiple collections items together.

To do so, we have the function `zip`, which takes in collection types, and let's you step across them together. 

This allows you to get, for example, the 0th item of each collection, and then the 1st item of each collection, etc.

Below is an example of using `zip`.



{:.input_area}
```python
# Define some collection objects
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Use zip, in a loop, to loop across both collections at the same time
for it1, it2 in zip(list1, list2):
    print(it1, it2)
```


### Q3 - Functions for Later (1 point)

In this section we will write a set of functions that will be useful for us to use later, with our artificial agents.

### a) Add Lists

Write a function called `add_lists`.

Input(s):
- `list1` - list of numbers
- `list2` - list of numbers

Output(s):
- `ouput` - list of numbers

Procedure(s):
- Initialize a new list `output`
- Using `zip`, loop through elements of both `list1` and `list2`
    - In each iteration, append the sum of the elements to `output`
- Return `output`



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(add_lists)
assert [1, 1] == add_lists([0, 0], [1, 1])
```




{:.input_area}
```python
assert callable(add_lists)

```


#### b)  Check Bounds

Write a function called `check_bounds`.

We will be using this function later in our bots. It checks whether a position, given as, for example [2, 3] is within the bounds of a grid of a particular size (say, a 4 x 4 square grid). 

Input(s):
- `position` - list of int
- `size` - int

Output(s):
- `boolean`

Procedure(s):
- Loop across each element in `position`.
    - Check if the element is less than 0, or greater than or equal to `size`
        - If so, return `False`
- Outside and after the loop, return `True`

Note that this means the function will return `False` if any element is outside the specified bounds. 

After checking all elements, if it hasn't returned yet, it returns `True` to indicate all elements are indeed within the bounds. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(check_bounds)
assert check_bounds([0, 0], 5)
assert not check_bounds([0, -1], 5)
assert not check_bounds([0, 5], 5)
```




{:.input_area}
```python
assert callable(check_bounds)

```


## Part 2: Classes

In this section we will be working with classes - building several classes to solve a variety of problems.

### Q4 - Creating a Class

We can start with a class object to make a 'schedule book' for our course Office Hours. 

Create a class called `OfficeHours`

- Class Attributes:
    - `course`, which has the value "COGS18"
- Instance Attibutes:
    - `name` : string
    - `day` : string
    - `time` : string
    - `place` : string
    - Note: all these attributes should be passed into the `__init__`, and attached to the object in there.
- Method
    - `check()`
        - This method should print out information, to look something like:
            - `Tom's office hours are on Tuesday at 12:30 in CSB115.`
            - Note that this should use the instance attributes to print out `name`, `day`, `time` & `place` of the particular instance. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert OfficeHours
assert OfficeHours('name', 'day', 'time', 'room')

name = "Instructor"
day = "Tuesday"
time = "12:30"
place = "CSB115"

test_oh = OfficeHours(name, day, time, place)
assert isinstance(test_oh, OfficeHours)

assert test_oh.course == "COGS18"
assert test_oh.name == name
assert test_oh.day == day
assert test_oh.time == time
assert test_oh.place == place
```


Here is a list of some office hours:
- Tom - Monday @ 12:30 in SDSC 212e
- Rob - Wednesday @ 2:00 in CSB 114
- Daril - Tuesday @ 10:00 in CSB 115
- Paolo - Friday @ 1:00 in CSB 106

Create a new instance of the OfficeHours class for each of the office hours listed above. 

Then store each of these instances together in a list called `all_office_hours`. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(all_office_hours, list)
assert len(all_office_hours) == 4
for item in all_office_hours:
    assert isinstance(item, OfficeHours)
    assert item.name in ['Tom', 'Rob', 'Daril', 'Paolo']
```


Now write a function called `check_all` that will take in a list of OfficeHour objects, and will call the `check` method on each one, using a loop to loop across each element in the input list. 

Call this function on your `all_office_hours` list to make sure that it works as expected. 

You should see that running this function prints out a string of information for each object, that looks like:

    Tom's office hours are on Monday at 12:30 in SDSC 212e.
    Rob's office hours are on Wednesday at 2:00 in CSB 114.
    Daril's office hours are on Tuesday at 10:00 in CSB 115.
    Paolo's office hours are on Friday at 1:00 in CSB 106.



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert callable(check_all)
```


### Q5 - Car Inventory

For this question you will create an object to store information on an inventory of cars.  

Create a class called `CarInventory`

- Instance Attibutes:
    - `n_cars` : int
    - `cars` : list
- Methods
    - `add_car()`
    - `compare()`

Details:
- The constructor (`__init__`) should take no inputs, but set `n_cars` to 0, and `cars` to be `[]` (an empty list). 

#### Method: `add_car`

Input(s):
- `manufacturer` : string
- `model` : string
- `year` : int
- `mpg` : float

Procedure(s):
- Create a dictionary from the values passed with the corresponding keys 'manufacturer', 'model', 'year' and 'mpg'
- Append this dictionary to the `cars` attribute
- Increment the `n_cars` attribute by 1

#### Method: `compare`

This method will compare all the cars on a specified `attribute` ('year', or 'mpg'), and find the highest and lowest values. It will return either the highest of lowest value, depending on the setting in a parameter `direction`. 

Input(s):
- `attribute` : string
- `direction` : string, default: 'highest'

Procedure(s):
- Initialize a variable called `lowest` to be the 0th element of `cars`, and another variable `highest` to be the same
- Loop through each car in cars
    - If the value of the attribute for the car is less than the car stored as `lowest`, replace `lowest` to be the current car
    - Similarly, if the value of the attribute for the car is greater than the car stored as `highest`, replace `highest` to be the current car
- After the loop, if the value of `direction` is 'highest', set a new variable `output` to be the variable `highest`
    - Else if the value of `direction` is 'lowest', set `output` to be `lowest`
- Return `output`



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
# Tests for the object
assert CarInventory
test_car_inv = CarInventory()
assert isinstance(test_car_inv, CarInventory)
assert test_car_inv.n_cars == 0
assert isinstance(test_car_inv.cars, list)
```




{:.input_area}
```python
# Tests for add_car method
test_inv = CarInventory()
test_inv.add_car('Toyota', 'Prius', 2012, 36)
assert test_inv.n_cars == 1
assert test_inv.cars[0] == {'manufacturer': 'Toyota', 'model': 'Prius', 'year': 2012, 'mpg':36}
```




{:.input_area}
```python
# Tests for compare method
test_inv = CarInventory()
test_inv.add_car('Toyota', 'Prius', 2012, 36)
test_inv.add_car('BMW', 'M3', 2017, 27)
assert test_inv.compare('mpg') == {'manufacturer': 'Toyota', 'model': 'Prius', 'year': 2012, 'mpg': 36}
assert test_inv.compare('year', 'lowest') == {'manufacturer': 'Toyota', 'model': 'Prius', 'year': 2012, 'mpg': 36}
```


#### b) Using our class

Using the `inventory` instance created for you in the cell below, do the following:

- Use `compare` to get the car with the highest mpg, and get the manufacturer of that car from the returned car
    - Store the answer in a variable called `highest_mpg`
- Use `compare` to get the car with the lowest year, and get the model of that car from the returned car
    - Store the answer in a variable called `oldest_car`



{:.input_area}
```python
# The following code provided for you
inventory = CarInventory()
inventory.add_car('Ford', 'Mustang', 2004, 20)
inventory.add_car('Honda', 'Civic', 2014, 40)
inventory.add_car('Toyota', 'Corrolla', 2010, 50)
inventory.add_car('Tesla', 'S', 2017, 1000)
```




{:.input_area}
```python
# Example: Get the least efficient car (lowest mpg)
inventory.compare('mpg', 'lowest')
```




{:.input_area}
```python
# Example: Get the newest car (highest year), and extract it's mpg
inventory.compare('year', 'highest')['mpg']
```




{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert isinstance(highest_mpg, str)
assert highest_mpg in ['Ford', 'Honda', 'Toyota', 'Tesla']

assert isinstance(oldest_car, str)
assert oldest_car in ['Mustang', 'Civic', 'Corrola', 'S']
```




{:.input_area}
```python
assert highest_mpg
assert oldest_car

```


### Example: Class Inheritance

The following is an extra example of class inheritance. 



{:.input_area}
```python
class TritonCourse:
    
    university = "UC San Diego"
    
    def __init__(self, department, code, title):
        """
        department: string
        code: int
        title: string
        """
    
        self.department = department
        self.code = code
        self.title = title
    
    def print_info(self):
        print(self.department + str(self.code) + ': ' + self.title)
```




{:.input_area}
```python
# By passing in `TritonCourse` to our new class, we create a derived class that inherits from `TritonCourse`
class TritonProgCourse(TritonCourse):

    def __init__(self, department, code, title, language):
        
        # Call the initializer from the class we inherited from
        #  `super` refers to the class that this class inherits from
        super().__init__(department, code, title)
        
        # Add a new instance attribute to our derived class
        self.language = language
```




{:.input_area}
```python
# Example: create an instance from our derived class
cogs18 = TritonProgCourse('COGS', 18, 'Introduction to Python', 'Python')
```




{:.input_area}
```python
# Note that our derived class inherits any class attributes & methods from the inherited class
print(cogs18.university)
cogs18.print_info()
```




{:.input_area}
```python
# Our derived class also has any extra and unique attributes and/or methods that we add to it
cogs18.language
```




{:.input_area}
```python
# We can check that our course is both an instance of 'TritonCourse', and of 'TritonProgCourse'
print(isinstance(cogs18, TritonCourse))
print(isinstance(cogs18, TritonProgCourse))
```


### Q6 - Extending our Class through Inheritance (0.5 points)

Create a `TritonCogsCourse` class that inherits from `TritonCourse`.

You can model your answer to this based on how we made `TritonProgCourse` above.

`TritonCogsCourse` should inherit from `TritonCourse` and calls it's super's `__init__`. 

In addition, in it's own `__init__`, it should take an extra parameter called `area`, which will store which area of Cognitive Science the class is related to. 

`area` should have a default value of `None`. 

Finally, add a method called `has_area` that returns `True` if the instance has an area defined (is not None), and returns `False` if area is equal to `None`.



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert TritonCogsCourse
test_class = TritonCogsCourse('COGS', '108', 'Data Science in Practice')
assert test_class
```




{:.input_area}
```python
cogs108 = TritonCogsCourse('COGS', '108', 'Data Science in Practice', 'Data Science')
assert cogs108
assert cogs108.area == 'Data Science'
assert cogs108.has_area() == True
```


## Part 3: Artificial Agents

In this last part of the assignment, we will create some 'Bots' - little artificial agents that can move around a predefined space.

They will be in the style of PacMan, or little exploration bots. 

Each of these bots will be able to explore a predefined world, which is a grid of 'dots' (locations).  

This grid has labelled locations that can be referenced by a list of integers, with [0, 0] being the top left most corner, and so on.

Each bot will have a `move` method, which updates the bot's position, thus moving it around the world.

As you start building some bots, there will be a series of test cells that test out your bots on a 'board'. 

Make sure these cells run to completion without errors - if the cells with `play_board` in them raise an error, there is something wrong with your bot. 

Note that some errors could come from the functions your wrote above that get used here. 



{:.input_area}
```python
# This function provided to you to run your bots on a grid world
#   You don't have to do anything with this function
def play_board(bots, n_iter=25, grid_size=5, sleep_time=0.3):
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]
    
    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    for it in range(n_iter):

        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character    

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()
```


### Q7 - Bot Base Class

Create a class called `Bot`. This will be our base class for all the bots that we make in this section. 

- Instance Attibutes:
    - `character` - string
    - `position` - list of [int, int]
    - `moves` - list of list of [int, int]
    - `grid_size` - `None` or int

Of these instance attributes, only `character` should be taken in as an input to `__init__`, with a default value of 8982.

Inside the init:
- `self.character` should be set as the `chr` of input `character`
- `self.position` should be set to starting position `[0, 0]`
- `self.moves` should be set as the list of possible moves, which are `[[-1, 0], [1, 0], [0, 1], [0, -1]]`
- `self.grid_size` should be initialized as None



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert Bot()

bot = Bot()
assert bot.position == [0, 0]
assert bot.character == chr(8982)
assert bot.moves == [[-1, 0], [1, 0], [0, 1], [0, -1]]
assert bot.grid_size == None
```


### Q8 - WanderBot

Create a class called `WanderBot`, that inherits from `Bot`. `WanderBot` is a bot that will wander around randomly. 

- In the `__init__`, it should simply call the init from `super` (and adds no extra instance attributes)
- Note that to do this, the `__init__` should take a `character` input, with the same default (8982)
    - This value will need to be passed into the super's `__init__`

Add two methods to WanderBot:

#### Method:  `wander`

This method will choose a random move from the possibilities, making sure that move is valid on the current grid.

Procedure:
- Initialize a boolean variable `has_new_pos` as `False`
- Use a while loop, with the condition `not has_new_pos`
    - Set a variable `move` as the ouput of calling `random.choice` on `self.moves`
    - Add `move` to `self.position`, using `add_lists` (a function we created earlier), and assign the output to a new variable `new_pos`
    - Call `check_bounds` on `new_pos`, also passing `self.grid_size` into `check_bounds`
        - Assign the output of `check_bounds` to `has_new_pos`
        - This will lead to exiting the loop when a valid new position has been assigned
- Return `new_pos`

#### Method: `move`
- No inputs (other than `self`) or outputs, just sets `self.position` to be the output of calling `self.wander()`. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert WanderBot
wbot = WanderBot()
assert wbot
```




{:.input_area}
```python
wbot = WanderBot()
wbot.grid_size = 3
assert wbot.wander()
assert isinstance(wbot.wander(), list)
wbot.move()
assert wbot.position != [0, 0]
```




{:.input_area}
```python
# Test out our WanderBot
#   You should see a 'bot' that steps around different positions randomly
bot = WanderBot()
play_board(bot, grid_size=5)
```




{:.input_area}
```python
# Test out running a group of WanderBots
bots = [WanderBot(character=1175), WanderBot(character=1175), WanderBot(character=1175)]
play_board(bots, grid_size=8, n_iter=25)
```


### Example: Random Probabilistic Choices

For our next bot, we want to be able to make random choice, but with a specified probability. 

We will use a quick trick to do so:
- from the `random` module, we can use the `random()` function to uniformly sample a decimal between 0 and 1
- by checking if that random sample is below some value `prob`, we will (on average) make that choice `prob` % of the time

An example of this idea is shown below. 



{:.input_area}
```python
# Print out a random decimal value between 0 - 1
print(random.random())
```




{:.input_area}
```python
# Example of a random probabilistic choice with a specified probability
if random.random() < 0.75:
    print('This will print out 75% of the time')
```


### Q9 - ExploreBot

Create a class called `ExploreBot`, that inherits from `Bot`. 

`ExploreBot` is a bot that will explore more systematically, generally continuing in the same direction on consecutive steps.

- In the `__init__`, it should call the `__init__` from `super`
- Note that to do this, the `__init__` should take a `character` input, with the same default (8982)
    - This value will need to be passed into the super's `__init__`
- The `__init__` should take an extra input, `move_prob` with default value of 0.75
- Add `move_prob` as an instance attribute, and also add a new instance attribute `last_move`, that's initialized as `None`

Add three methods to ExploreBot:

#### Method:  `biased_choice`

This method will chose a new move, but be biased to chose the same move as was taken on the previous step. 

Procedure:
- Initialize a variable called `move` as `None`
- if `self.last_move` is not equal to `None`
    - Using the random probability procedure described above, if `random.random()` is less that `self.move_prob`
        - Set `move` to be `self.last_move`
- if `move` is still None, set `move` to be a random choice of `self.moves`
- return `move`

#### Method:  `explore`

Explore should be the same as the `wander()` method in `WanderBot`, with two differences:
- Inside the `while` loop, `move` should be the return of `self.biased_choice()` (instead of `wander()`)
- At the end of the `while` loop (inside the loop), set `self.last_move` to `move`

####  Method: `move`
- No inputs (other than `self`) or outputs, just sets `self.position` to be the output of calling `explore()`. 



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert ExploreBot
ebot = ExploreBot()
assert ebot
assert ebot.last_move == None
assert ebot.move_prob == 0.75
assert ExploreBot(move_prob=0.5)
```




{:.input_area}
```python
assert ExploreBot

ebot = ExploreBot()
ebot.grid_size = 3
assert ebot.explore()
assert isinstance(ebot.explore(), list)
ebot.move()
assert ebot.position != [0, 0]
```




{:.input_area}
```python
# Test out our ExploreBot
#   You should see a 'bot' that steps around different positions, often moving in the same direction
bot = ExploreBot()
play_board(bot)
```




{:.input_area}
```python
# Test out running a group of WanderBots & ExploreBots
bots = [WanderBot(character=1175), WanderBot(character=1175), 
        ExploreBot(character=1127), ExploreBot(character=1127)]
play_board(bots, grid_size=10, n_iter=50)
```


### Q10 - TeleportBot

Create a class called `TeleportBot`, that inherits from `WanderBot`.

`TeleportBot` is a modified version of `WanderBot`, that will generally wander around randomly, but sometimes teleport to a brand new location.

- In the `__init__`, it should call the `__init__` from `super`
- Note that to do this, the `__init__` should take a `character` input, with the same default (8982)
    - This value will need to be passed into the super's `__init__`
- The `__init__` should take an extra input, `tele_prob` with default value of 0.2 
    - Add `tele_prob` as an instance attribute

Add two methods to `TeleportBot`:

####  Method: `teleport`

This method will chose a totally random location anywhere on the map, 'teleporting' there.

To do so, it needs to return a list of two random numbers that define a location of the map (for the current grid size).

Use `random.choice` with `range` and `self.grid_size` to create a list of two randomly chosen numbers within the grid size. 

Note - this will entail using each of these three things twice - one for each number. 

Return this list. 

#### Method: `move`
- No inputs (other than `self`) or outputs
- Using the random probability procedure from before, use an `if` with `random.random() < self.tele_prob`. 
    - Inside the `if`, set `self.position` to the ouput of `self.teleport()`
- `else`, set `self.position` as the ouput of `self.wander()`
    - Note that this bot inherits `wander()` from it's super (`WanderBot`)



{:.input_area}
```python
# YOUR CODE HERE
raise NotImplementedError()
```




{:.input_area}
```python
assert TeleportBot
tbot = TeleportBot()
assert tbot
assert tbot.tele_prob == 0.2
assert TeleportBot(tele_prob=0.5)
```




{:.input_area}
```python
assert TeleportBot

tbot = TeleportBot()
tbot.grid_size = 3
assert tbot.teleport()
assert isinstance(tbot.teleport(), list)
tbot.move()
assert tbot.position != [0, 0]
```




{:.input_area}
```python
# Test out our TeleportBot
#   You should see a 'bot' that steps around randomly, sometimes teleporting to a new location
bot = TeleportBot()
play_board(bot, grid_size=5)
```


### Running it all together



{:.input_area}
```python
# Define a group of bots
bots = [WanderBot(character=1078), WanderBot(character=1078), WanderBot(character=1078),
        ExploreBot(character=1127), ExploreBot(character=1127), ExploreBot(character=1127),
        TeleportBot(character=1279), TeleportBot(character=1279)]

# Play the board with our bot list
play_board(bots, grid_size=15, n_iter=50)
```


## Extending Our Agents

So far, we have some 'artificial agents' that can explore a world, with different strategies to do so.

Note that if you want to explore using these bots some more, you can add a new cell, defining a list of bots (changing some inputs to them, if you want to), and use the `play_board` function to run a 'board' (also changing some inputs to `play_board`, if you want to).

From here, we could think about ways we could make these agents interact with each other, and/or respond more directly the environment. 

More broadly - there is any number of ways we could build in more 'cognitive' behaviour, given this starting point.

If you are interested in this topic, extending these kinds of 'artificial agents' (or ones like them) is one of your project options.

## The End!

After you've explored running the bots, you are done!

Have a look back over your answers, and also make sure to Restart & Run All from the kernel menu to double check that everything is working properly.

When you are ready to submit your assignment, upload it to TritonED under Assignment-4.
