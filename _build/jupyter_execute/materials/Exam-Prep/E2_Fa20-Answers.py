# COGS 18 - Exam 2

This is the second exam for Fall 2020. It covers topics through the Namespaces Lecture.

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

## Part 1: E1 Review (3 points)

### Q1 - Variables & Indexing (0.5 points)

Define a tuple `my_tuple` that stores 6 items: 2 integers, 1 dictionary, 2 lists, and 1 float (in any order).

Then, write code that (*using indexing*) accomplishes the following:

1. Assigns the second element of `my_tuple` to the variable `tuple_out_a`
2. Assigns the single element in the second position from the end of `my_tuple` to the variable `tuple_out_b`

Note: "element" refers to the position in the list - so the element at index 0 is the *first* element in any list.

# specific tuple will differ
my_tuple = (1, 2, {'a': 3}, [1, 2], [3, 4], 1.3)
tuple_out_a = my_tuple[1]
tuple_out_b = my_tuple[-2]

assert my_tuple is not None

assert type(my_tuple) == tuple
assert len(my_tuple) == 6

assert my_tuple

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

assert tuple_out_a is not None
assert tuple_out_a == my_tuple[1]

assert tuple_out_b is not None
assert tuple_out_b == my_tuple[-2]

### Q2 - Loops (1.25 points)

1. Explain the difference between `for` and `while` loops. 
2. Describe an example (using a text explanation or pseudocode) of a situation that would create an infinite `while` loop.
3. Describe what you would need to do to fix the loop you describe in #2 so that it was no longer an infinite loop.


Note: Your response here should be a written explanation. It could (but does not have to) include some pseudocode. We are expecting a text response/explanation below.

REPLACE THIS WITH YOUR ANSWER.

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- difference between for and while clear and correct (**0.25 points**)
- while loop described clearly and would be infinite (**0.5 points**)
- explanation of what's needed to fix while loop clear and correct (**0.5 points**)
    - i.e.: conditional statement that will be false at some point, likely to include a counter and an updated counter
                                                                        
=== END MARK SCHEME ===

### Q3 - `for` loop (1.25 points)

Store your first name as a string in the variable `my_name`.

In this question, you're going to change `my_name` using the key-value pairs in `new_language` (defined below), ultimately storing the updated name in `modified_name`. Specifically, if any of the letters in your name (`my_name`) are keys in the dictionary `new_language` below, use that key's value in that letter's place in `modified_name`. If the letter is not in `new_language`, add the original character from `my_name` to `modified_name`.

For example, if `my_name` stored 'Shannon', `modified_name` would store 'Shӓnnðn' (the a and the o have the modified character from `new_language`)

Note that if your name does not have any vowels in it, the code should still run, but the string stored in `modified_name` will be the same as the string in `my_name`. In other words, your code should accomplish the specified task, regardless of what name is stored in `my_name`.

# run this to create list
new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð', 
                'u' : 'û',
                'A' : 'Ӓ', 
                'E' : 'ɛ', 
                'O' : 'Ó', 
                'U' : 'Ü'}

# code will differ based on who is taking the exam
my_name = 'Shannon'
modified_name = ''

for letter in my_name:
    if letter in new_language:
        modified_name = modified_name + new_language[letter]
    else:
        modified_name = modified_name + letter

modified_name

assert modified_name

mod_name = ''
for letter in my_name:
    if letter in new_language:
        mod_name = mod_name + new_language[letter]
    else:
        mod_name = mod_name + letter
        
assert mod_name == modified_name

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- for loop set up correctly (**0.25 points**)
- conditional correct (**0.25 points**)
- string initialized + extended correctly (**0.25 points**)

=== END MARK SCHEME ===

## Part 2: Functions (4.25 points)

### Q4 - Function execution (0.75 points)

The cell below includes a function that has been provided for you. After understanding the code in the function, run the cell below (to define this function). Then, execute (use) this function to create the following variables under the specified conditions:

1. `tempA` | execute the `convert_temp` function to convert the temperature 95 degrees Fahrenheit into degrees Celsius
2. `tempB` | execute `convert_temp` to convert the temperature 17 degrees Celsius into degrees Fahrenheit

def convert_temp(temp, input_unit='F'):
    
    if input_unit == 'F':
        out_temp = (temp - 32) * 5/9
    elif input_unit == 'C':
        out_temp = (temp * 9/5) + 32
    else:
        print("Please specify either 'F' or 'C' for input_unit")
        
    return out_temp

# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)

tempA = convert_temp(95)
tempB = convert_temp(17, 'C')

assert tempA
assert tempA == 35.0


assert tempB
assert tempB == 62.6

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

function executed appropriately for variable creation (aka not hard coded)  (**0.25 points**)

=== END MARK SCHEME ===

### Q5 - `modify_string` (1 point)

In Q3, you wrote code that would modify your name, replacing vowels with the corresponding character defined in `new_language`. 

Here, define a function called `modify_string` that will accomplish the same task as in Q3, taking a string as input and `return`ing the modified string from the function.

This function should have a single parameter: `input_string` - the string to be modified.

def modify_string(input_string):
    
    new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð', 
                'u' : 'û',
                'A' : 'Ӓ', 
                'E' : 'ɛ', 
                'O' : 'Ó', 
                'U' : 'Ü'}
    
    modified_name = ''
    for letter in input_string:
        if letter in new_language:
            modified_name = modified_name + new_language[letter]
        else:
            modified_name = modified_name + letter

    return modified_name

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert modify_string
assert modify_string('Taylor') == 'Tӓylðr'

assert callable(modify_string)
# check functioning for capital letters
assert modify_string('AaBbCcEe') == 'ӒӓBbCcɛɚ'

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly & input parameter specified (**0.1 points**)
- for loop (or equivalent) correct (**0.1 points**)
- conditional (or equivalent) correct (**0.1 points**)
- string updated correctly (**0.1 points**) 
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

### Q6 - `calculate_points` (1 point)

Write a function `calculate_points` that has a single input parameter: `hand`. `hand` can be assumed to be a list of string values, where each string corresponds to a value in a deck of cards (2-10, J, Q, K, or A)

This function should calculate the total number of "pointer" cars in your hand, where ***a "pointer" is either a 10, J, Q, K, or A***. Each "pointer" is worth one point. All other cards are worth zero points. The function should `return` the total number of points in the `hand` as an integer.

For example, if your `hand` input was: 

```python
['J', '10', '2', '5', 'K']
```

executing the `calculate_points()` function with the above list as the input to the `hand` parameter, the function would `return` the integer 3 (one point each for the `'J'`, `'10'`, and `'K'`.

If there are no pointers in the input `hand`, the function should return 0.

def calculate_points(hand):
    pointers = ['10', 'J', 'Q', 'K', 'A']
    counter = 0
    
    for card in hand:
        if card in pointers:
            counter += 1
        
    return counter

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert callable(calculate_points)

# use default parameter
assert calculate_points(['K']) == 1

# hidden tests for function above
# assure returns zero if no pointers
assert calculate_points(['2', '7', '9']) == 0

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly with single parameter (**0.1 points**)
- loop (or equivalent) correct (**0.1 points**)
- conditional (or equivalent) correct (**0.1 points**)
- counter incremented correctly (**0.1 points**)
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

### Q7 - Debugging (1.5 points)

In the cell below, there is a function that is not operating as anticipated.

`count_consonants` is _supposed_ to take a string as input and count the number of each consonant in the `input_string` (input parameter), storing the output in a dictionary where the key is the consonant and the value is the number of times it appears in the input. 

Note that we want capitalization to be considered such that the capital and lower case letters are counted together, and the lower case letter is used as the key (i.e. 'A' and 'a' would both be counted under the key 'a')

Specifically, if the `input_string` were "Mohammed", the function ould return: `{'m': 3, 'h': 1, 'd': 1}`

Debug, edit, and test the function provided below so that it accomplishes the intended goal.

# original code
def count_consonants():
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        
        if char not in vowels:
            if char not in out:
                out[char] = 1

# debugged coode
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

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert count_consonants is not None
assert count_consonants('Taylor') == {'t': 1, 'y': 1, 'l': 1, 'r': 1}


assert callable(count_consonants)
assert count_consonants('AaBbCc') == {'b': 2, 'c': 2}

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- input parameter included (**0.2 points**)
- captitalization accounted for (**0.2 points**)
- else condition (or equivalent) included (**0.2 points**)
- return statement included (**0.2 points**)
=== END MARK SCHEME ===

## Part 3: Objects & Classes (5.25 points)

### Q8 - `random` (0.25 points)

Import the `random` module.

import random

assert random

### Q9 - `Kingdom()` (2.5 points)

For this question (and the next one), imagine you want to create a video game with a handful of characters. You want this game to have a royal kingdom theme.

Here, define a class `Kingdom()`.

This class should have two instance attributes: `name` and `title`, which will be strings specifying the name and title of the character (in that order).

This class will also have a method `introduce()`. This method should `return` (*not* just `print`) a string, similar to:

```
'Hello, my name is Ferdinand, and I am a King.' 
```

...where 'Ferdinand' corresponds to whatever is stored in `Kingdom()` object's `name` attribute is and 'King' corresponds to whatever is stored in the `Kingdom()` object's `title` attribute.


class Kingdom():
    
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def introduce(self):
        return 'Hello, my name is ' + self.name + ', and I am a ' + self.title + '.'

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

# Tests for the object
assert Kingdom

queen = Kingdom('Elizabeth', 'Queen')
assert isinstance(queen, Kingdom)
assert queen.name == 'Elizabeth'
assert queen.title == 'Queen'

# Tests for introduce method
assert callable(Kingdom)

assert callable(queen.introduce)
assert isinstance(queen.introduce(), str)

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class defined correctly (**0.25 points**)
- instance attributes initialized correctly with `self` + paramters (**0.25 points**)
- `self` used correctly in instance attribute code block (**0.25 points**)
- introduce method defined with `self` as parameter (**0.25 points**)
- `return` statement returns a string (**0.25 points**)
- `return` includes reference to `self.name` and `self.title` (**0.25 points**)

=== END MARK SCHEME ===

### Q10 - `CourtJester` (2.5 points)

Generate a class called `CourtJester()`.

This object should inherit all attributes and methods from `Kingdom()`.

Additionally, the `CourtJester()` object should have:
- a class attribute `headwear`, storing the value `'fool's cap'`
- a method `tell_a_joke()` that should `return` a joke at random from the list provided below

(Reminder: You imported the `random` module earlier. Use of a function from that module will likely be helpful in `tell_a_joke()`.)

# joke list provided
['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']

class CourtJester(Kingdom):

    headwear = "fool's cap"
        
    def tell_a_joke(self):
        joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']
        out_joke = random.choice(joke_list)
        return out_joke

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)

assert CourtJester

jester = CourtJester('Barney', 'Jester')
assert jester.headwear == "fool's cap"

assert callable(CourtJester)

assert jester.name == 'Barney'
assert jester.title == 'Jester'

assert callable(CourtJester.tell_a_joke)

joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']

assert jester.tell_a_joke() in joke_list

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class inherits correctly (**0.25 points**)
- class attribute defined correctly (**0.25 points**)
- list of jokes defined/included within class (**0.25 points**)
- `random.choice()` used in method correctly (**0.25 points**)

=== END MARK SCHEME ===

### Exam II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.