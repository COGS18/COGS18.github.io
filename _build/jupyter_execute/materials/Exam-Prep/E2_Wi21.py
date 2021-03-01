# COGS 18 - Exam 2

This is the second exam for Winter 2021. It covers topics through the Classes Lecture.

This total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE EXAM.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam (due Thurs 8AM).
- If it takes you longer than 1h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google.
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

### Q0 - Honor Code (0.1 points - bonus)

In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:

>I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet without searching for answers to these questions directly. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet.


### BEGIN SOLUTION
honor_code = True
### END SOLUTION

assert honor_code

## Part 1: E1 Review (3 points)

### Q1 - Variables, Operators, Indexing, and Loops (0.5 points)

Thanks to your efforts on E1, Prof Ellis now has her grocery list all in order! Execute the cell below to create the `grocery` list.

Then, write code that (*using indexing* and/or operators we've learned) accomplishes the following:

1. Assigns the second, fourth, and sixth (every other) element of `grocery` to the variable `out_a`.
2. Assigns the single element in the third position from the end of `grocery` to the variable `out_b`
3. Returns a list of booleans, storing `True` for any element in `grocery` that contains the letter `n` and `False` otherwise. Store this in the variable `out_c`. 

Note: "element" refers to the position in the list - so the element at index 0 is the *first* element in any list.

grocery = ['mushrooms', 'peanut butter', 'tahini', 
           'pineapple', 'udon noodles', 'romaine lettuce']

### BEGIN SOLUTION
 # specific indexing could differ
out_a = grocery[1::2]
out_b = grocery[-3]
out_c = [] 
for el in grocery:
    if 'n' in el:
        out_c.append(True)
    else:
        out_c.append(False)
### END SOLUTION

assert out_a
### BEGIN HIDDEN TESTS
assert isinstance(out_a, list)
assert out_a == ['peanut butter', 'pineapple', 'romaine lettuce']
### END HIDDEN TESTS

assert out_b
### BEGIN HIDDEN TESTS
assert isinstance(out_b, str)
assert out_b == 'pineapple'
### END HIDDEN TESTS

assert out_c
### BEGIN HIDDEN TESTS
assert out_c == [False, True, True, True, True, True]
### END HIDDEN TESTS

### Q2 - Conditionals & Loops (1.25 points)

Alice wants to encrypt a message to send to Bob. Help her with this process - storing the encrypted message as a string in `secret_message`, using the specific approach to encryption described:

1. Starting with the third character in the `message`, take every third element and and add it to the output `secret_message`. Be sure to remove these characters from the original `message` in this process. (Reminder: there are helpful string methods; `.replace()` may help you here, but there are multiple ways to approach this, so your answer does not *have* to use `.replace()`.)
2. For all remaining characters in original `message` after step 1, reverse the order of these characters, such that the first character becomes the last and the second character becomes the second to last. Add this reversed string to the end of `secret_message`.

For example, for the `message` `'funtimes'`, `secret_message` would store `'nmseituf'`, where `'n'`, `'m'`  are the 3rd and 6th elements in the original string and `'seituf'` is the remaining string (`'futies'`) reversed, added onto the end of `secret_message`.

**Note**: Do not hard code. Use the code constructs taught in class. In other words, your code should have `secret_message` should store the correct output, even if the string in `message` were to change.

# you can test other `message` strings
# but be sure when you submit
# message is 'todayis'
message = 'todayis'

### BEGIN SOLUTION
# specific solutions will and can vary
secret_message = ''

counter = 1
for char in message:
    if counter % 3 == 0: # get every third character
        secret_message += char # add to secret message
        message = message.replace(char, '', 1) # remove character from original message
    counter += 1

# after removal, reverse remaining string
secret_message += message[::-1]

secret_message
### END SOLUTION

assert secret_message
### BEGIN HIDDEN TESTS
assert isinstance(secret_message, str)
### END HIDDEN TESTS

# hidden test to ensure correct approach
### BEGIN HIDDEN TESTS
assert secret_message == 'disyaot' or secret_message == 'dieeaydsndwsyaot' or secret_message == 'dieeaysnwsyot'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Answer not hard-coded; remove autograded credit if answer is hard-coded.                                                   
=== END MARK SCHEME ===

### Q3 - Loop to Complete a Task (1.25 points)

The World Health Organization has contacted Professor Ellis to ask for her help sorting between people that should be quarantined and people that shouldn’t. Unfortunately, she’s too busy grading assignments, exams, and coding labs. As such, your task, should you choose to accept it (This a joke, you’re required to accept it), is to help Professor Ellis accomplish this task!

Given a dictionary called `quarantine_dict`, store the names (which are the keys in `quarantine_dict`) of people whose value is `True` in a list called `do_quarantine` and the names of people whose value is `False` in a list called `dont_quarantine`.

# run this to create list
quarantine_dict = {'King Triton': True,
                   'Racoon One': True,
                   'Sun God': False,
                   'Racoon Two': False,
                   'Cole Slaw': False,
                   'Racoon Three': True,
                   'Dr. Py T. Hon': True
                  }

### BEGIN SOLUTION
# code will differ based on who is taking the exam
do_quarantine = []
dont_quarantine = []

for person in quarantine_dict:
    if quarantine_dict[person]:
        do_quarantine.append(person)
    else:
        dont_quarantine.append(person)
        
print(do_quarantine, dont_quarantine)
### END SOLUTION

assert do_quarantine
### BEGIN HIDDEN TESTS
assert isinstance(do_quarantine, list)
### END HIDDEN TESTS

assert dont_quarantine
### BEGIN HIDDEN TESTS
assert isinstance(dont_quarantine, list)
### END HIDDEN TESTS

#hidden tests to ensure task completed 
### BEGIN HIDDEN TESTS
assert len(do_quarantine) == 4
assert len(dont_quarantine) == 3
### END HIDDEN TESTS

#hidden tests to ensure task completed 
### BEGIN HIDDEN TESTS
assert all(item in do_quarantine for item in ['King Triton', 'Racoon One', 'Racoon Three', 'Dr. Py T. Hon']) 
### END HIDDEN TESTS

#hidden tests to ensure task completed 
### BEGIN HIDDEN TESTS
assert all(item in dont_quarantine for item in ['Sun God', 'Racoon Two', 'Cole Slaw']) 
### END HIDDEN TESTS

## Part 2: Functions (4.5 points)

### Q4 - Function execution (0.75 points)

The cell below includes a function `court_jester_jokes` that has been provided for you. After understanding the code in the function, run the cell below (to define this function). Then, execute (use) this function to create the following variables under the specified conditions:

1. `joke_random` | execute the `court_jester_jokes` function to return a joke at random
2. `joke_nonrandom` | execute `court_jester_jokes` to return the second joke in `joke_list`

import random

def court_jester_jokes(random_joke=True):
    joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
                 'How does the court jester address the King of Ducks? Mal’Lard',
                 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
                 'What do you call a joke made by using sign language? A jester']
    if random_joke:
        out_joke = random.choice(joke_list)
    else:
        out_joke = joke_list[1]

    return out_joke

# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)

### BEGIN SOLUTION
joke_random = court_jester_jokes()
joke_nonrandom = court_jester_jokes(random_joke=False)
### END SOLUTION

assert joke_random

### BEGIN HIDDEN TESTS
jokes = ['A clown held the door open for me yesterday. I thought it was a nice jester',
         'How does the court jester address the King of Ducks? Mal’Lard',
         'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
         'What do you call a joke made by using sign language? A jester']
assert joke_random in jokes
### END HIDDEN TESTS

assert joke_nonrandom
### BEGIN HIDDEN TESTS
assert joke_nonrandom == 'How does the court jester address the King of Ducks? Mal’Lard'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

Function executed; remove autograder credit if hard-coded

=== END MARK SCHEME ===

### Q5 - `encrypt_message` (1.25 points)

In Q2, you wrote code that would encrypt a message.

Here, define a function called `encrypt_message` that will accomplish the same task as in Q2, taking a string as input and `return`ing the encrypted string from the function as specified in Q2.

This function should have a single parameter: `input_message` - the string to be modified.

### BEGIN SOLUTION
def encrypt_message(input_message):
    
    secret_message = ''

    counter = 1
    for char in input_message:
        if counter % 3 == 0: # get every third character
            secret_message += char # add to secret message
            input_message = input_message.replace(char, '', 1) # remove character from original message
        counter += 1

    # after removal, reverse remaining string
    secret_message += input_message[::-1]

    return secret_message   


## alternate solution
# def encrypt_message(input_message):
#     secret_message = input_message[2::3]
    
#     start_pos = len(input_message)-1
#     for position in range(start_pos, -1, -1):
#         if position % 3 != 2:
#             secret_message += input_message[position]
            
#     return secret_message
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert encrypt_message
### BEGIN HIDDEN TESTS
# check for correct output
# and correct parameter name
assert encrypt_message(input_message='happyweek7') == 'pwk7eeypah' or encrypt_message(input_message='happyweek7') == 'pwk7eeyah'
### END HIDDEN TESTS

assert callable(encrypt_message)
### BEGIN HIDDEN TESTS
# check if reverse string alone is working
assert encrypt_message('hi') == 'ih'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly & correct input parameter specified (**0.1 points**)
- for loop (or equivalent) correct (**0.1 points**)
- character removed from input message correctly (**0.1 points**)
- counter/conditional (or equivalent) correct (**0.2 points**)
- string reversal correct (**0.15 points**) 
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

### Q6 - `to_quarantine` (1.25 points)

In Q3, you wrote code that would determine who needed to quarantine (`do_quarantine`) and who did not (`dont_quarantine`) based on the values in an input dictionary. In this question, we're going to turn that task into a function.

Write a function called `to_quarantine`. This function should have two input values `input_dict`, and `quarantine`. The default value for `quarantine` should be `True`.

Within this function, the same task as was accomplished in Q3 should be accomplished; *however*, only a single list of names should be returned from the function. If `quarantine` is `True`, the function should return `do_quarantine`. If `quarantine` is `False`, the function should return `dont_quarantine`.

### BEGIN SOLUTION
def to_quarantine(input_dict, quarantine=True):
    
    do_quarantine = []
    dont_quarantine = []

    for person in input_dict:
        if input_dict[person]:
            do_quarantine.append(person)
        else:
            dont_quarantine.append(person)
    
    if quarantine:
        output = do_quarantine
    else:
        output = dont_quarantine

    return output

### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert to_quarantine
### BEGIN HIDDEN TESTS
# use default parameter; specify parameter name
assert to_quarantine(input_dict={'A': True, 'B': False, 'C': True, 'D': False}) == ['A', 'C']
### END HIDDEN TESTS

assert callable(to_quarantine)
### BEGIN HIDDEN TESTS
# change default parameter
assert to_quarantine({'A': True, 'B': False, 'C': True, 'D': False}, quarantine=False) == ['B', 'D']
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly with two parameters (**0.1 points**)
- default value for quarantine specified correctly (**0.1 points**)
- empty lists (or equivalent) initialized (**0.1 points**)
- loop + conditional for dictionary processing (or equivalent) correct (**0.15 points**)
- conditional to determine output (or equivalent) correct (**0.2 points**)
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

### Q7 - Debugging (1.25 points)

In the cell below, there is a function that is not operating as anticipated.

`new_encrypt` is _supposed_ to take a string as input and return the reverse alphabetical string as output, meaning, given a character, return the capitalized character in the reverse position within the alphabet. 

For example, if the input character is 'B' or 'b', the function would store 'Y' in the output string. If the character is 'A' or 'a', the function would store 'Z'. (and vice versa: the input 'Z' or 'z' would store 'A').

Specifically, if the `input_string` were "ABc", the function would `return`: 'ZYX'

Debug, edit, and test the function provided below so that it accomplishes the intended goal.

def new_encrypt():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    for char in input_string:
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
        
### BEGIN SOLUTION
def new_encrypt(input_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

    output_string = ''

    for char in input_string:
        char = char.upper()
        if char in alpha:
            position = alpha.find(char)
            output_string += reverse_alpha[position]
        else:
            output_string = None
            break
        
    return output_string
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert new_encrypt
### BEGIN HIDDEN TESTS
assert new_encrypt('mohammed') == 'NLSZNNVW'
### END HIDDEN TESTS

assert callable(new_encrypt)

### BEGIN HIDDEN TESTS
# will work even if they missed the .upper()
# has correct input parameter
assert new_encrypt(input_string='ABC') == 'ZYX'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- `input_string` parameter included (**0.15 points**)
- empty `output_string` initialized (**0.2 points**)
- capitalization accounted for (**0.2 points**)
- `return` statement included (**0.2 points**)

=== END MARK SCHEME ===

## Part 3: Objects & Classes (5 points)

### Q8 - `NewYear()` (2.5 points)

For this question, let's create a class to celebrate the Lunar New Year!

Here, define a class `NewYear()`.

This class should have:

- **one class attribute**: `zodiac_signs` that stores the dictionary specified in the cell below. This dictionary contains the zodiac sign as the key and the birth years that correspond to that sign.
- **one instance attribute**:  `year` that takes the birth `year` as input from the user upon creation of a `NewYear` type object.

This class will also have a method `return_sign()`. This method should `return` (*not* just `print`) a string, similar to:

```
'You were born in the year of the Dragon!' 
```

...where 'Dragon' corresponds to the key from the `zodiac_signs` corresponding to the value stored in the `year` attribute. (Be sure captitalization and punctuation match the string specified here. The only thing that should change is the last word in the string.)

For example `NewYear(year=2021).return_sign()` should return 'You were born in the year of the Ox!', since 2021 is a value in the `zodiac_signs` dictionary for the key 'Ox'. 

# provided for you
zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022], 
    'Rabbit' : [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023], 
    'Dragon' : [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024], 
    'Snake' : [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025], 
    'Horse' : [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026], 
    'Goat/Sheep' : [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027], 
    'Monkey' : [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028], 
    'Rooster' : [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029], 
    'Dog' : [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030], 
    'Pig' : [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031], 
    'Rat' : [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
} 

### BEGIN SOLUTION
class NewYear():
    
    zodiac_signs = {
    'Ox' : [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
    'Tiger' : [1938, 1950, 1962, 1974, 1986, 1998, 2010], 
    'Rabbit' : [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023], 
    'Dragon' : [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024], 
    'Snake' : [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025], 
    'Horse' : [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026], 
    'Goat/Sheep' : [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027], 
    'Monkey' : [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028], 
    'Rooster' : [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029], 
    'Dog' : [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030], 
    'Pig' : [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031], 
    'Rat' : [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
    } 
    
    
    def __init__(self, year):
        self.year = year
    
    def return_sign(self):
        for key in self.zodiac_signs:
            if self.year in self.zodiac_signs[key]:
                out = key
                break # answer would be fine without break here
                
        return 'You were born in the year of the ' + out + '!'
### END SOLUTION


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

# Tests for the object
assert NewYear
### BEGIN HIDDEN TESTS
dragon = NewYear(1988)
assert isinstance(dragon, NewYear)
### END HIDDEN TESTS

assert callable(NewYear)
# Tests for classs attribute
### BEGIN HIDDEN TESTS
assert dragon.year ==  1988
### END HIDDEN TESTS

# Tests for instance attribute
### BEGIN HIDDEN TESTS
assert isinstance(dragon.zodiac_signs, dict)
assert 'Ox' in dragon.zodiac_signs.keys()
### END HIDDEN TESTS

# tests for method
# be sure punctuation matches instructions
### BEGIN HIDDEN TESTS
assert dragon.return_sign() == 'You were born in the year of the Dragon!'
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class defined correctly (**0.25 points**)
- class attribute defined correctly (**0.25 points**)
- instance attribute defined correctly (with `self` + parameter) (**0.15 points**)
- method definition includes `self` (**0.1 points**)
- method code loop/conditional correct. (**0.25 points**)
- method code specifies self.name (**0.15 points**)
- method includes `return` statement (**0.1 points**)

=== END MARK SCHEME ===

### Q9 - `PresidentsDay` (2.5 points)

Generate a class called `PresidentsDay()`.

This should have:
- **one class attribute**: `when` that stores the string: `'Third Monday in February'`
- **one instance attribute**: `has_school` that stores the boolean `False` by default


Additionally, the `PresidentsDay()` object should have a single method `sleep_in()` that should `return` the string 'Go ahead and sleep in!' if the `has_school` attribute is `False` and the string "Get up! It's time for class" if the `has_school` attribute is `True`.

### BEGIN SOLUTION
class PresidentsDay():

    when = 'Third Monday in February'
    
    def __init__(self, has_school=False):
        self.has_school = has_school
        
    def sleep_in(self):   
        if self.has_school:
            return "Get up! It's time for class"
        else:
            return 'Go ahead and sleep in!'
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)

assert PresidentsDay
### BEGIN HIDDEN TESTS
no_school = PresidentsDay()
### END HIDDEN TESTS

assert callable(PresidentsDay)
### BEGIN HIDDEN TESTS
assert no_school.has_school == False
assert no_school.when == 'Third Monday in February'
### END HIDDEN TESTS

assert callable(PresidentsDay.sleep_in)
### BEGIN HIDDEN TESTS
assert no_school.sleep_in() == 'Go ahead and sleep in!'
### END HIDDEN TESTS

# hidden test for method
### BEGIN HIDDEN TESTS
yes_school = PresidentsDay(has_school=True)
assert yes_school.sleep_in() == "Get up! It's time for class"
### END HIDDEN TESTS

# hiddden tests for attributes
### BEGIN HIDDEN TESTS
# set has_school parameter
assert yes_school.has_school == True
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class defined correctly (**0.25 points**)
- class attribute defined correctly (**0.25 points**)
- instance attribute defined correctly w/ `self` (**0.25 points**)
- method defined correctly with `self` (**0.1 points**)
- method uses `self` correctly for `self.has_school` (**0.1 points**)
- condition in method correct (**0.1 points**)
- method has return statement (even if incorrect) (**0.1 points**)

=== END MARK SCHEME ===

### Exam II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.