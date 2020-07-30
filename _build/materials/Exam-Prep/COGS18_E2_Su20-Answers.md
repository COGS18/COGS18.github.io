---
interact_link: content/materials/Exam-Prep/COGS18_E2_Su20-Answers.ipynb
download_link: assets/downloads/COGS18_E2_Su20-Answers.ipynb.zip
title: 'E2_Su20_Answers'
prev_page:
  url: /materials/Exam-Prep/E2_Practice_Su20_Answers
  title: 'E2_Practice_Su20_Answers'
next_page:
  url: /materials/Exam-Prep/Final-Review
  title: 'Final-Review'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 2

This is the second exam for Summer 2020. It covers topics through the Namespaces Lecture.

This total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1 hour.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 1 hour, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Piazza about the exam at all. 
    - Piazza posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Piazza are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

## Part 1: E1 Review (2.25 points)

### Q1 - Variables & Indexing (0.75 points)

Define a tuple `my_tuple` that stores 6 items: 2 integers, 1 dictionary, 2 lists, and 1 float (in any order).

Then, write code that (*using indexing*) accomplishes the following:

1. Store the second element of `my_tuple` in the variable `tuple_out_a`
2. Store the second element from the end of of `my_tuple` in the variable `tuple_out_b`

Note: "element" refers to the position in the list - so the element at index 0 is the *first* element in any list.



{:.input_area}
```python
### BEGIN SOLUTION
my_tuple = (1, 2, {'a': 3}, [1, 2], [3, 4], 1.3)
tuple_out_a = my_tuple[1]
tuple_out_b = my_tuple[-2]
### END SOLUTION
```




{:.input_area}
```python
assert my_tuple is not None

### BEGIN HIDDEN TESTS
assert type(my_tuple) == tuple
assert len(my_tuple) == 6
### END HIDDEN TESTS
```




{:.input_area}
```python
assert my_tuple

### BEGIN HIDDEN TESTS
# check for specific type satistfied
num_int = 0
num_list = 0
num_dict = 0
num_float = 0

for el in my_tuple: 
    if type(el) == int: 
        num_int += 1
    if type(el) == list:
        num_list += 1
    if type(el) == dict:
        num_dict += 1
    if type(el) == float:
        num_float += 1
               
assert num_int == 2
assert num_list == 2
assert num_dict == 1
assert num_float == 1
### END HIDDEN TESTS
```




{:.input_area}
```python
assert tuple_out_a is not None

### BEGIN HIDDEN TESTS
assert tuple_out_a == my_tuple[1]
### END HIDDEN TESTS
```




{:.input_area}
```python
assert tuple_out_b is not None

### BEGIN HIDDEN TESTS
assert tuple_out_b == my_tuple[-2]
### END HIDDEN TESTS
```


### Q2 - Loops (0.5 points)

Write code that will extract the lists from the `my_tuple` variable you created in the previous question, storing all values from the lists into a single, new list called `list_output`.

For example, if you had two lists `['a', 'b']` and `[1, 2]` in `my_tuple`, the output would be either `['a', 'b', 1, 2]` or `[1, 2, 'a', 'b']` (you get to decide which list comes first in `list_output`).

A reminder: to combine the elements from two lists together, you _can_ use the `+` operator. (i.e.: `['a', 'b'] + [1, 2]`)

Note: This code should work regardless of what specific values you've stored in `my_tuple`. If I were to change `my_tuple` (as long as it still contained two lists, as specified in Q1), this code should work to accomplish the task. In other words: don't hard-code. Use code constructs we've discussed in class to accomplish this task.



{:.input_area}
```python
### BEGIN SOLUTION
# output will differ based on who is taking the exam
list_output = []

for my_list in my_tuple:
    if type(my_list) == list:
        list_output = list_output + my_list
        
list_output
### END SOLUTION
```





{:.output_data_text}
```
[1, 2, 3, 4]
```





{:.input_area}
```python
assert list_output is not None

### BEGIN HIDDEN TESTS
assert isinstance(list_output, list)

check_list_output = []

for my_list in my_tuple:
    if type(my_list) == list:
        check_list_output = check_list_output + my_list
        
assert set(check_list_output) == set(list_output)
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- list_output created (0.05)
- correctly accesses lists in `my_tuple` (0.1)
- creates output list correctly (0.1) 

=== END MARK SCHEME ===

### Q3 - Writing code to accomplish a task (1 point)

`summer` provided below stores the activities of (fictional) students in COGS 18 this summer. Use this dictionary  to complete this task. (In other words, run the cell below and then use the `summer` dictionary in your answer.)

**The task**: Take a look at the dictionary below and write code that will extract all the possible student activities (using the key `activity` from the inner-dictionary) and compile all of the student activities into a singe list `activity_out`. `activity_out` should contain a single list of strings with each element corresponding to one the activities listed in the values for the the 'activity' key (from the inner dictionary). 

For example if the dictionary were `{'Shannon': {'job': ['professor'], 'activity': ['beach volleyball', 'baking']}}`, the code in your answer should return `['beach volleyball', 'baking']`.

Each activity should show up in `activity_out` as many times as it shows up in the inner list for the 'activity' key across the `summer` dictionary (some strings may show up more than once).

Your response should use code constructs discussed in class (i.e conditionals, loops, operators, etc.) to carry out the process specified. You should *not* "hard-code" the answer.

#### <span style="color:red">Common Mistake(s):</span>
- output contained a list of lists, rather than a list of individual values



{:.input_area}
```python
# The following dictionary provided for you
summer = {'Amir':{'job' : ['internship'], 
                  'activity' : ['walk dog']},
         'Quynh':{'activity' : ['baking', 'reading']},
         'George':{'job' : ['Amazon'], 
                   'activity' : ['cook', 'workout']},
         'Camilla':{'activity' : ['practice foreign languages']},
         'Rachel':{'activity' : ['video games', 'read', 'paint']},
         'Sebi':{'activity' : ['skateboard', 'video games'],
                  'job' : ['internship']},
         'Alma':{'activity' : ['plant enthusiast', 'hiking', 'baking']}
          }   
```




{:.input_area}
```python
### BEGIN SOLUTION
activity_out = [] 

for key, val in summer.items():
    activity_list = val['activity']
    activity_out = activity_out + activity_list

### END SOLUTION
```




{:.input_area}
```python
assert isinstance(activity_out, list)

### BEGIN HIDDEN TESTS
activity_set = set(['walk dog',
 'baking',
 'reading',
 'cook',
 'workout',
 'practice foreign languages',
 'video games',
 'read',
 'paint',
 'skateboard',
 'video games',
 'plant enthusiast',
 'hiking',
 'baking'])

assert set(activity_out) == activity_set
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- answer not hard coded(0.25)                                                                        
- activity key accessed correctly (0.25)
- output list generated correctly (0.25)
                                                                        
=== END MARK SCHEME ===

## Part 2: Functions (5.25 points)

### Q4 - Function execution (0.75 points)

The cell below includes a function that has been provided for you. After running the cell below (to define this function), execute (use) this function to create the following variables under the specified conditions:

1. `out_olivia` | execute the `provide_info` function providing only the `name` 'Olivia' and the `year` 'freshman' as input
2. `out_jamal` | execute `provide_info` using same `year` as above, but so that the output stores the name 'Jamal' and the `school` indicates that Jamal attends 'UCLA'.

Note: Capitalization and spelling matter here, so be sure the strings specified are exactly the strings you use.



{:.input_area}
```python
def provide_info(name, year, school='UCSD'):
    
    output = "Hi. I'm " + name + '. I am a ' + year + ' at ' + school + '.'
    
    return output
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)
```




{:.input_area}
```python
### BEGIN SOLUTION
out_olivia = provide_info('Olivia', 'freshman')
out_jamal = provide_info('Jamal', 'freshman', 'UCLA')
### END SOLUTION
```




{:.input_area}
```python
assert isinstance(out_olivia, str)

### BEGIN HIDDEN TESTS
assert  out_olivia == "Hi. I'm Olivia. I am a freshman at UCSD."
### END HIDDEN TESTS
```




{:.input_area}
```python
assert isinstance(out_jamal, str)

### BEGIN HIDDEN TESTS
assert out_jamal  == "Hi. I'm Jamal. I am a freshman at UCLA."
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

function executed appropriately for variable creation (aka not hard coded)

=== END MARK SCHEME ===

### Q5 - `count_consonants` (2 points)

Write a function `count_consonants`that will take a string as input and will return a dictionary with any consonant (any letter other than a, e, i, o, or u) in the input as keys and the number of times each consonant appears in the input string as its value.

For example, if the input string were 'Shannon', the function would return {'s':1, 'h': 1, 'n':3}.

Be sure that your code considers capitalization, turning all keys in your dictionary into the lowercase letter. Spefically: both 'S' and 's' should be coundted in your dictionary as the letter 's' (lowercase).

If the input string has no consonants, your function should return an empty dictionary.

Note: You can assume the input to this function will be a string and do *not* need to write code to check whether or not this is true.

#### <span style="color:red">Common Mistake(s):</span>
- Answer did not count capital and lower case as same letter



{:.input_area}
```python
### BEGIN SOLUTION
def count_consonants(input_string):
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        char = char.lower()
        
        if char not in vowels:
            if char not in out:
                out[char] = 1
            else:
                out[char] += 1
    return out
                
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)
```




{:.input_area}
```python
assert count_consonants is not None

### BEGIN HIDDEN TESTS
assert count_consonants('taylor') == {'t': 1, 'y': 1, 'l': 1, 'r': 1}
### END HIDDEN TESTS
```




{:.input_area}
```python
assert callable(count_consonants)

### BEGIN HIDDEN TESTS
# check for capitalization
assert count_consonants('AaBbCc') == {'b': 2, 'c': 2}
### END HIDDEN TESTS

```




{:.input_area}
```python
# hidden test for question above 

### BEGIN HIDDEN TESTS
# check for no consonants
assert count_consonants('aeiou') == {}
### END HIDDEN TESTS

```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly & input parameter specified  (**0.25 points**)
- for loop (or equivalent) correct (**0.25 points**)
- conditional (or equivalent) correct (**0.25 points**)
- counter incremented correctly (**0.25 points**) 

=== END MARK SCHEME ===

### Q6 - `get_activities` (2.5 points)

Write a function `get_activities` that takes two input parameters: `input_dictionary` and `activity_key`. `activity_key` should take the default value 'activity'. 

Then, take a look back to Q3, as we're going to turn that task into a function. Specifically, for this task, you can assume that `input_dictionary` is a dictionary with strings as keys and dictionaries as values (like the dictionary `summer` in Q3). 

This function should loop through the keys in `input_dictionary`, accessing the values for each key. Considering this inner dictionary (which are the keys of the `input_dictionary`), store the values for the specified function parameter (`activity_key`) in a single list. The list of activities should be returned from the function.

For example, if your `input_dictionary` dictionary were:

```python
{ 'Shannon': {'activity': ['beach volleyball']},
  'Josh': {'activity': ['yoga', 'soccer']} } 
```

executing the `get_activities` function with that dictionary as `input_dictionary` would return `['beach volleyball', 'yoga', 'soccer']`

If the key you specified did not have any of the specified value for `activity_key`, the function should return an empty list.

Note: You can use the `summer` dictionary we defined earlier to test out this function. (Be sure to test out your function with other input values to `activity_key`.)

#### <span style="color:red">Common Mistake(s):</span>
- default value not correctly specified
- output was of incorrect type (should be list of single values)
- failed to account for activity_key input that did not have associated value for every member in list



{:.input_area}
```python
### BEGIN SOLUTION
def get_activities(input_dictionary, activity_key='activity'):
    
    output = []
    
    for key, val in input_dictionary.items():
        try:
            out = val[activity_key]
            output = output + out
        except:
            output = output
    return output

# alternate solution
# def get_activities(input_dictionary, activity_key = 'activity'):
    
#     output = []
    
#     for item in input_dictionary:
        
#         if activity_key in input_dictionary[item]:
#             student = input_dictionary[item]
#             activity += student[activity_key]
#         else: 
#             continue
    
#     return output

### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)
```




{:.input_area}
```python
assert callable(get_activities)

### BEGIN HIDDEN TESTS
# use default parameter
assert set(get_activities(summer)) == activity_set
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure defaul parameter is correct
assert get_activities(input_dictionary = summer, activity_key = 'job') == ['internship', 'Amazon', 'internship']
### END HIDDEN TESTS
```




{:.input_area}
```python
# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure if key not in inner dictionary, returns an empty list
assert get_activities(summer, 'ouch') == []
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly (**0.25 points**)
- 2 parameters & default parameter specified correctly (**0.25 points**)
- list extension correct (**0.5 points**)
- `return` statement included (**0.25 points**)

=== END MARK SCHEME ===

## Part 3: Objects & Classes (5 points)

### Q7 - objects (0.5 points)

In the cell below, import the `math` module so that you can use the `sqrt` function from the module. (Note: the `sqrt` function from the `math` module calculates the square root of the input value.)

Use the `sqrt` function from the `math` module such that it returns 6 (or 6.0).

Store the output from this operation in the variable `square_root`.



{:.input_area}
```python
### BEGIN SOLUTION
from math import sqrt
square_root = sqrt(36)

# also valid:
# import math
# square_root = math.sqrt(36)
### END SOLUTION
```




{:.input_area}
```python
assert square_root is not None

### BEGIN HIDDEN TESTS
assert square_root == 6
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

**0.5 points** awarded if _either_ of the following are true:
- import statement correct 
- function syntax correct

=== END MARK SCHEME ===

### Q8 - `CarInventory` (2.5 points)

For this question, imagine you own a used car dealership and you need some way to track what cars you have in stock.

To do this, you will need to: create a class called `CarInventory`.

`CarInventory` should have two instance attraibutes `n_cars` and `cars` and a single method `add_car()`. 

**instance attributes**:
- `n_cars` should be initialized with the value `0`  
- `cars` should be initialized with an empty list.

**method**:

- `add_car` should have 4 input parameters: `make`, `model`, `year` and `mpg`. 
- `add_car` should create a dictionary from the values passed to each of its 4 input parameters. 
- This dictionary should be appended to the `cars` list in your `CarInventory`. 
- And then, the `n_cars` should increase by 1.

#### <span style="color:red">Common Mistake(s):</span>
- Instance attributes not initialized correctly
- `self` missing from method/not used appropriately
    - in method's parameter definition
    - and/or within code of method 



{:.input_area}
```python
### BEGIN SOLUTION
class CarInventory:
    
    def __init__(self):
        self.n_cars = 0
        self.cars = []
    
    def add_car(self, make, model, year, mpg):
        
        self.cars.append({'make': make, 
                          'model':model,
                          'year': year, 
                          'mpg': mpg})
        self.n_cars += 1
### END SOLUTION

```




{:.input_area}
```python
# Tests for the object
assert CarInventory

### BEGIN HIDDEN TESTS
test_car_inv = CarInventory()
assert isinstance(test_car_inv, CarInventory)
assert test_car_inv.n_cars == 0
assert isinstance(test_car_inv.cars, list)
### END HIDDEN TESTS
```




{:.input_area}
```python
# Tests for add_car method
assert callable(CarInventory.add_car)

### BEGIN HIDDEN TESTS
test_inv = CarInventory()
test_inv.add_car('Toyota', 'Prius', 2012, 36)
assert test_inv.n_cars == 1
assert test_inv.cars[0] == {'make': 'Toyota', 'model': 'Prius', 'year': 2012, 'mpg' : 36}
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class & instance attributes defined correctly (**0.25 points**)
- `self` used correctly throughout (**0.25 points**)
- method defined correctly w/ parameters (**0.25 points**)
- method dictionary correct & appended correctly (**0.5 points**)
- method increases self.n_cars correctly (**0.25 points**)


=== END MARK SCHEME ===

### Q9 - `FootballGame` (2 points)

Generate a class called `FootballGame`.

This class should have four *instance attributes*: `touchdowns`, `sacks`, `interceptions`, and `points` (specified in that order). 

This class must also have a single method: `play_game`. Within the `play_game` method, add code that would `return` `game_metric` such that `game_metric` is calculated as follows:
- for every one `touchdowns` *and* every one `sacks`, `game_metric` is increased by 1
- for every one `interceptions`, `game_metric` is decreased by 1
- for every 10 `points` scored, `game_metric` is increased by 1 (Note that if 20-29 points are scored, for example, `game_metric` would increase by 2. If 30-39 points are scored, `game_metric` would increase by 3.

#### <span style="color:red">Common Mistake(s):</span>
- method failed to pass `self`
- calculation not carried out correctly



{:.input_area}
```python
### BEGIN SOLUTION
class FootballGame():
    
    def __init__(self, touchdowns, sacks, interceptions, points):
        self.touchdowns = touchdowns
        self.sacks = sacks
        self.interceptions = interceptions
        self.points = points
        
    def play_game(self):
        game_metric = 0
        game_metric = self.touchdowns + self.sacks - self.interceptions + self.points//10
        return game_metric
    
### END SOLUTION
```




{:.input_area}
```python
# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)
```




{:.input_area}
```python
assert callable(FootballGame)

### BEGIN HIDDEN TESTS
game = FootballGame(1, 1, 2, 22)

# test attributes
assert game.touchdowns == 1
assert game.sacks == 1
assert game.interceptions == 2
assert game.points == 22
### END HIDDEN TESTS
```




{:.input_area}
```python
assert callable(game.play_game)

### BEGIN HIDDEN TESTS
# test method
assert game.play_game() == 2
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class & instance attributes defined correctly (**0.25 points**)
- `self` used correctly in instance attribute (**0.25 points**)
- method defined correctly (**0.25 points**)
- calculation correct (**0.25 points**) 

=== END MARK SCHEME ===

### Exam II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
