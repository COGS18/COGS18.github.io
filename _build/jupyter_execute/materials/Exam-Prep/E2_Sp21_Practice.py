# COGS 18 - Practice Exam 2

This is the second practice exam for Spring 2021. It covers topics through the Classes Lecture.

This is worth 0 points and worth 0% of your grade, but the real total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam (due Sat 8AM).
- If it takes you longer than 1h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
- You may not talk to any humans about this exam. 
- The following are all *prohibited*:
    - text/phone/online chat communication
    - posting questions to a message board where a human could respond (Campuswire, Discord, Chegg, any similar site)
    - viewing exam questions from a message board (as described above)
    - asking anyone via any form about a question on this test directly
- Clarification questions will ***not*** be allowed and there will be no posting on Campuswire about the exam at all. 
    - Campuswire posts about the exam will not be answered and will be deleted. 
    - Students who post questions about the exam to Campuswire are at risk of losing points on the exam.
    - If you are confused about wording, add a note to your exam explaining your confusion and how you interpreted the question. 
    - Note: This policy is b/c we are incapable of responding for 24h straight. This is the only way to make it fair across the board for students.

 <span style="color: red;">Note: </span> There _is_ a chance for partial credit on some questions, so _some_ code is better than _no_ code. Even if it throws an error, having some code that partially answers the question will benefit you/your grade.

### Q0 - Honor Code (0.1 points)

In the cell below, include a variable `honor_code` that stores the boolean `True` if you agree to the following statement:

>I agree that this exam was completed individually with the knowlege in my brain, information the notes from this course, and/or with searching for help on the Internet *without searching for answers to the text from these questions directly*. I did not ask anyone about specific questions on this exam. I did not post these questions (in part or in whole) on the Internet. I did not copy answers to these questions from anywhere or anyone else. I understand all code I've written on this exam and could explain my answers to someone else if asked.


### BEGIN SOLUTION
honor_code = True
### END SOLUTION

assert honor_code

## Part 1: Methods & Debugging (3.5 points)

### Q1 - Method I (0.75 points)

`isalpha()` is a string method that determines if all the characters in a string are in the alphabet (meaning letters or numbers: A-Z, a-z).

Use the `isalpha()` method on two strings (of your choosing) below to create two variables:
- `true_var` | should store the value `True`
- `false_var` | should store the value `False`

### BEGIN SOLUTION
true_var = 'asdf'.isalpha()
false_var = '!!!!'.isalpha()
### END SOLUTION

assert true_var is not None
### BEGIN HIDDEN TESTS
assert true_var
### END HIDDEN TESTS

assert false_var is not None
### BEGIN HIDDEN TESTS
assert not false_var
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

- uses `isalnum()` (**0.6 pts**)

=== END MARK SCHEME ===

### Q2 - Debugging

In the cell below, there is a function that is not operating as anticipated.

`count_consonants` is _supposed_ to take a string as input and count the number of each consonant in the `input_string` (input parameter), storing the output in a dictionary where the key is the consonant and the value is the number of times it appears in the input. 

Note that we want capitalization to be considered such that the capital and lower case letters are counted together, and the lower case letter is used as the key (i.e. 'A' and 'a' would both be counted under the key 'a')

Specifically, if the `input_string` were "Mohammed", the function ould return: `{'m': 3, 'h': 1, 'd': 1}`

Debug, edit, and test the function provided below so that it accomplishes the intended goal.

def count_consonants():
    out = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for char in input_string:
        
        if char not in vowels:
            if char not in out:
                out[char] = 1

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

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert count_consonants is not None

### BEGIN HIDDEN TESTS
assert count_consonants('Taylor') == {'t': 1, 'y': 1, 'l': 1, 'r': 1}
### END HIDDEN TESTS

assert callable(count_consonants)

### BEGIN HIDDEN TESTS
assert count_consonants('AaBbCc') == {'b': 2, 'c': 2}
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===
- input parameter included (**0.2 points**)
- captitalization accounted for (**0.2 points**)
- else condition (or equivalent) included (**0.2 points**)
- return statement included (**0.2 points**)

=== END MARK SCHEME ===

### Q3 - Debugging

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

## Part 2: Functions (4.4 points)

Note this section has *more* questions than your real exam will have. This is just to get you additional practice.

### Q4 - Function execution

The cell below includes a function that has been provided for you. After running the cell below (to define this function), execute (use) this function to create the following variables under the specified conditions:

1. `square_default` | execute the `square_all` function using the default parameter such that the output will carry out the function on a list of input values containing the integers 2, 3, and 4. 
2. `power_three` | Use the same input values as above, but this time, use the `square_all` function provided to raise all input values to the power 3
3. `out_4` | Execute the `square_all` function such that `out_4` will store a list with 4 values, each of which is the integer 4.

def square_all(collection, power=2):
    
    square_list = []
    for val in collection:
        square_list.append(val**power)
    
    return square_list

# BE SURE YOUR ANSWER IS IN THE CELL BELOW
# but you can use this cell to test/execute/check your thinking (optional)

### BEGIN SOLUTION
square_default = square_all([2,3,4])
power_three = square_all([2,3,4], 3)
out_4 = square_all([2,2,2,2]) # this execution could differ
### END SOLUTION

assert square_default is not None

### BEGIN HIDDEN TESTS
assert  square_default == [4,9,16]
### END HIDDEN TESTS

assert power_three is not None

### BEGIN HIDDEN TESTS
assert power_three  == [8, 27, 64]
### END HIDDEN TESTS

assert out_4 is not None

### BEGIN HIDDEN TESTS
assert out_4  == [4,4,4,4]
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

function executed appropriately for variable creation (aka not hard coded) (**1 point** ; 0.33 per function call)

=== END MARK SCHEME ===

### Q5 - `count_int` 

Write a function `count_int` that will take a tuple or list as the input and count the number (count) of integer values in that tuple/list, returning this value from the function. 

For example, if 3 of the values in the input list were integers, the function would return 3.

Note: You can assume the input to this function will be a tuple or list and do *not* need to write code to check whether or not this is true.

### BEGIN SOLUTION
def count_int(col):
    count = 0
    
    for val in col:
        if type(val) == int:
            count += 1
    
    return count
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert callable(count_int)

### BEGIN HIDDEN TESTS
assert count_int((1,2,3,4,5,'string',4.4)) == 5
assert count_int([1,2,3,4,5,'string',4.4]) == 5
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly (**0.5 points**)
- input parameter specified  (**0.5 points**)
- counter initialized (**0.5 points**)
- for loop (or equivalent) correct (**0.2 points**)
- conditional (or equivalent) correct (**0.3 points**)
- counter incremented correctly (**0.5 points**) 
- `return` statement included (**0.5 points**)

=== END MARK SCHEME ===

### Q6 - `provide_info` (1 point)

Write a function `provide_info` that takes three parameters: `name`, `year`, and `school` .

Set the default value for `school` to be 'UCSD'.

This function should `return` the string "Hi. I'm `name`. I am a `year` at `school`." (where the variable names are replaced by the values input to the function upon execution).

For example, one possible execution of this function could return "Hi! I'm Shannon. I am a sophomore at UCSD."

Note: Be sure punctuation and spacing match that specified in the instructions.

### BEGIN SOLUTION
def provide_info(name, year, school='UCSD'):
    output = "Hi. I'm " + name + '. I am a ' + year + ' at ' + school + '.'
    return output
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert callable(provide_info)

### BEGIN HIDDEN TESTS
assert provide_info(name = 'Taylor', year = 'junior', school = 'UCLA') == "Hi! I'm Taylor. I am a junior at UCLA." or provide_info(name='Taylor', year='junior', school = 'UCLA') == "Hi. I'm Taylor. I am a junior at UCLA."
### END HIDDEN TESTS

# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure defaul parameter is correct
assert provide_info(name = 'Taylor', year = 'junior') == "Hi! I'm Taylor. I am a junior at UCSD." or provide_info(name='Taylor', year='junior') == "Hi. I'm Taylor. I am a junior at UCSD."
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly (**0.5 points**)
- 3 parameters specified (**0.5 points**)
- default parameter specified correctly (**0.5 points**)
- string concatenation attempted correctly (even if typos in string) (**1 point**)
- `return` statement included (**0.3 points**)

=== END MARK SCHEME ===

### Q7 - `modify_string` (1 point)


In this question, you're going to define a function called `modify_string()` that will change `input_string` using the key-value pairs in `new_language` (provided below), ultimately returning the updated name from the function.

Specifically, if any of the letters in your name (`input_string`) are keys in the dictionary `new_language` below, use that key's value in that letter's place in the string being output from the function. If the letter is not in `new_language`, add the original character from `input_string` to the string being output from the function.

For example, if `input_string` were 'Shannon', `modif_string()` would `return` 'Shӓnnðn' (the a and the o have the modified character from `new_language`)


This function should have a single parameter: `input_string` - the string to be modified.

new_language = {'a': 'ӓ',
                'e' : 'ɚ',
                'i' : '¡',
                'o' : 'ð',
                'u' : 'û',
                'A' : 'Ӓ'
                'E' : 'ɛ',
                'O' : 'Ó',
                'U' : 'Ü'}

### BEGIN SOLUTION
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
                
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert modify_string

### BEGIN HIDDEN TESTS
assert modify_string('Taylor') == 'Tӓylðr'
### END HIDDEN TESTS

assert callable(modify_string)

### BEGIN HIDDEN TESTS
# check functioning for capital letters
assert modify_string('AaBbCcEe') == 'ӒӓBbCcɛɚ'
### END HIDDEN TESTS


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly & input parameter specified (**0.1 points**)
- for loop (or equivalent) correct (**0.1 points**)
- conditional (or equivalent) correct (**0.1 points**)
- string updated correctly (**0.1 points**) 
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

### Q8 - `calculate_points` (1 point)

Write a function `calculate_points` that has a single input parameter: `hand`. `hand` can be assumed to be a list of string values, where each string corresponds to a value in a deck of cards (2-10, J, Q, K, or A)

This function should calculate the total number of "pointer" cars in your hand, where ***a "pointer" is either a 10, J, Q, K, or A***. Each "pointer" is worth one point. All other cards are worth zero points. The function should `return` the total number of points in the `hand` as an integer.

For example, if your `hand` input was: 

```python
['J', '10', '2', '5', 'K']
```

executing the `calculate_points()` function with the above list as the input to the `hand` parameter, the function would `return` the integer 3 (one point each for the `'J'`, `'10'`, and `'K'`.

If there are no pointers in the input `hand`, the function should return 0.

### BEGIN SOLUTION
def calculate_points(hand):
    pointers = ['10', 'J', 'Q', 'K', 'A']
    counter = 0
    
    for card in hand:
        if card in pointers:
            counter += 1
        
    return counter
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

assert callable(calculate_points)

### BEGIN HIDDEN TESTS
# use default parameter
assert calculate_points(['K']) == 1
### END HIDDEN TESTS

# hidden tests for function above
### BEGIN HIDDEN TESTS
# assure returns zero if no pointers
assert calculate_points(['2', '7', '9']) == 0
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

partial credit for answer above:

- function defined correctly with single parameter (**0.1 points**)
- loop (or equivalent) correct (**0.1 points**)
- conditional (or equivalent) correct (**0.1 points**)
- counter incremented correctly (**0.1 points**)
- `return` statement included (**0.1 points**)

=== END MARK SCHEME ===

## Part 3: Objects & Classes (4.5 points)

Note this section has *more* questions than your real exam will have. This is where students tend to struggle the most as the material is new and puts all the pieces we've talked about so far this quarter together, so I wanted you to have extra practice.

### Q9 - `Kingdom()`

For this question (and the next one), imagine you want to create a video game with a handful of characters. You want this game to have a royal kingdom theme.

Here, define a class `Kingdom()`.

This class should have two instance attributes: `name` and `title`, which will be strings specifying the name and title of the character (in that order).

This class will also have a method `introduce()`. This method should `return` (*not* just `print`) a string, similar to:

```
'Hello, my name is Ferdinand, and I am a King.' 
```

...where 'Ferdinand' corresponds to whatever is stored in `Kingdom()` object's `name` attribute is and 'King' corresponds to whatever is stored in the `Kingdom()` object's `title` attribute.


### BEGIN SOLUTION
class Kingdom():
    
    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def introduce(self):
        return 'Hello, my name is ' + self.name + ', and I am a ' + self.title + '.'
### END SOLUTION


# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your function (optional)

# Tests for the object
assert Kingdom

### BEGIN HIDDEN TESTS
queen = Kingdom('Elizabeth', 'Queen')
assert isinstance(queen, Kingdom)
assert queen.name == 'Elizabeth'
assert queen.title == 'Queen'
### END HIDDEN TESTS

# Tests for introduce method
assert callable(Kingdom)

### BEGIN HIDDEN TESTS
assert callable(queen.introduce)
assert isinstance(queen.introduce(), str)
### END HIDDEN TESTS

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

### Q10 - `NewYear()`

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

### Q11 - `BasketballGame`

Generate a class called `BasketballGame`.

This class should have four instance attributes: `home_team`, `away_team`, `home_points`, and `away_points`

It should also have one method, `play_game()`. 

Within the `play_game` method, add code that would determine who the winner of the game is (determined by the team with the most points), returning Winner: ' and the winning team's name.

For ties, return: 'Winner: tie'

### BEGIN SOLUTION
class BasketballGame():
    def __init__(self, home_team, away_team, home_points, away_points):
        self.home_team = home_team
        self.away_team = away_team
        self.home_points = home_points
        self.away_points = away_points
    
    def play_game(self):
        if self.home_points > self.away_points:
            out = 'Winner: ' + self.home_team
        elif self.away_points > self.home_points:
            out = 'Winner: ' + self.away_team
        else:
            out = 'Winner: tie'
        
        return out
### END SOLUTION

# use this cell to test/execute/check your class (optional)

assert callable(BasketballGame)

### BEGIN HIDDEN TESTS
game = BasketballGame(home_team='Warriors', away_team='Sixers', 
                      home_points=100, away_points=105)

# test attributes
assert game.home_team == 'Warriors'
assert game.away_team == 'Sixers'
assert game.home_points == 100
assert game.away_points == 105
### END HIDDEN TESTS

assert callable(BasketballGame.play_game)

### BEGIN HIDDEN TESTS
# test method
assert game.play_game() == 'Winner: Sixers'
### END HIDDEN TESTS

This "blank" cell included intentionally. Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

rubric for partial credit

=== END MARK SCHEME ===

### (Practice) Exam II complete!

Good work - you're done with the second (practice) exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.