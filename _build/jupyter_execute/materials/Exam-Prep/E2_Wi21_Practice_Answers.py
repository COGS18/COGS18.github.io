# COGS 18 - Practice Exam 2

This is the second practice exam for Winter 2021. It covers topics through the Classes Lecture.

This is worth 0 points and worth 0% of your grade, but the real total exam is out of 12.5 points, worth 12.5% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Instructions

#### Timing
- The exam is designed to take you ~1h.
- There will be a 24 hour window during which you can complete this exam.
- If it takes you longer than 1h, you're free to use that time.

#### The Rules
- You are to complete this exam on your own.
- This is open-notes & open-Google
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

## Part 1: E1 Review (3 points)

There will be 3 questions on Part I, as specified below, with these point values.

To review for this part of the exam, review Exam 1 and Practice Exam 1

### Q1 - Variables, Operators & Indexing (0.5 points)


### Q2 - Conditionals & Loops (1.25 points)


### Q3 - Loop to Complete a Task (1.25 point)


## Part 2: Functions (4.25 points)

### Q4 - Function execution (0.75 points)

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

### Q5 - `count_int` (1 point)

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

### Q7 - Debugging (1.5 points)

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

## Part 3: Objects & Classes (5.25 points)

Note this section has *more* questions than your real exam will have. This is where students tend to struggle the most as the material is new and puts all the pieces we've talked about so far this quarter together, so I wanted you to have extra practice.

### Q8 - `random` (0.25 points)

Import the `random` module.

### BEGIN SOLUTION
import random
### END SOLUTION

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

### Q10 - `CourtJester` (2.5 points)

Generate a class called `CourtJester()`.

This object should inherit all attributes and methods from `Kingdom()`.

Additionally, the `CourtJester()` object should have:
- a class attribute `headwear`, storing the value `'fool's cap'`
- a method `tell_a_joke()` that should `return` a joke at random from the list provided below

(Reminder: You imported the `random` module earlier. Use of a function from that module will likely be helpful in `tell_a_joke()`.)

**Note**: I said to skip this question during the Exam Review in class b/c I did not teach inheritance this quarter, which is required for this question...and I failed to consider this when I put it on the practice midterm.

# joke list provided
['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']

### BEGIN SOLUTION
class CourtJester(Kingdom):

    headwear = "fool's cap"
        
    def tell_a_joke(self):
        joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
 'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']
        out_joke = random.choice(joke_list)
        return out_joke
    
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)

assert CourtJester

### BEGIN HIDDEN TESTS
jester = CourtJester('Barney', 'Jester')
assert jester.headwear == "fool's cap"
### END HIDDEN TESTS

assert callable(CourtJester)

### BEGIN HIDDEN TESTS
assert jester.name == 'Barney'
assert jester.title == 'Jester'
### END HIDDEN TESTS

assert callable(CourtJester.tell_a_joke)

### BEGIN HIDDEN TESTS
joke_list = ['A clown held the door open for me yesterday. I thought it was a nice jester',
'How does the court jester address the King of Ducks? Mal’Lard',
 'What did the court jester call the balding crown prince? The Heir Apparent with no Hair Apparent',
 'What do you call a joke made by using sign language? A jester']

assert jester.tell_a_joke() in joke_list
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class inherits correctly (**0.25 points**)
- class attribute defined correctly (**0.25 points**)
- list of jokes defined/included within class (**0.25 points**)
- `random.choice()` used in method correctly (**0.25 points**)

=== END MARK SCHEME ===

### Q11 - Classes (2.5 points)

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

### Q12 - Classes (2.5 points)

Generate a class called `StudentInfo`.

This class should have four *instance attributes*: `name`, `year`, `school`, and `proj_grade`. 

This class must also have a single method: `follow_up`. This method should determine if `proj_grade` is 65 or below. If `proj_grade` is 65 or below, the method should return the name of the student as the key and their proj_grade as the value in a dictionary. (If the student has a grade above 65, this method should return an empty dictionary.)

### BEGIN SOLUTION
class StudentInfo():
    
    def __init__(self, name, year, school, proj_grade):
        self.name = name
        self.year = year
        self.school = school
        self.proj_grade = proj_grade
        
    def follow_up(self):
        out = {}
        if self.proj_grade <= 65:
            out[self.name] = self.proj_grade
        return out
    
### END SOLUTION

# BE SURE YOUR ANSWER IS IN THE CELL ABOVE
# but you can use this cell to test/execute/check your class (optional)

assert callable(StudentInfo)

### BEGIN HIDDEN TESTS
student1 = StudentInfo(name='Shannon', year='sophomore', school='UCSD', proj_grade=63)
student2 = StudentInfo(name='Josh', year='senior', school='UCSD', proj_grade=88)

# test attributes
assert student1.name == 'Shannon'
assert student1.school == 'UCSD'
assert student2.year == 'senior'
assert student2.proj_grade == 88
### END HIDDEN TESTS

assert callable(StudentInfo.follow_up)

### BEGIN HIDDEN TESTS
# test method
assert student1.follow_up() == {'Shannon': 63}
assert student2.follow_up() == {}
### END HIDDEN TESTS

**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

partial credit for answer above:

- class defined correctly (**0.5 points**)
- instance attribute def correct  (**0.5 points**)
- `self` used correctly in instance attribute (**0.5 points**)
- method defined correctly (**0.5 points**)
- dictionary + conditional correct (**0.5 points**) 
- `return` statement included (**0.5 points**)

=== END MARK SCHEME ===

### (Practice) Exam II complete!

Good work - you're done with the second (practice) exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.