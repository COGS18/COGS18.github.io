---
interact_link: content/materials/E2_Practice_Sp20-PartII-Answers.ipynb
download_link: assets/downloads/E2_Practice_Sp20-PartII-Answers.ipynb.zip
pdf_link: assets/pdf/E2_Practice_Sp20-PartII-Answers.pdf
layout: materials
title: 'E2_Practice_Sp20-PartII-Answers'
prev_page:
  url: /materials/Exam2-Practice
  title: 'Exam2-Practice'
next_page:
  url: /labs/CL2-Answers
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# COGS 18 - Exam 2 (Part II)

This is the practice second exam for Spring 2020. It covers topics through the Command Line Lecture.

This is worth 0 points and worth 0% of your grade, but the real total exam is out of 20 points, worth 20% of your grade. 

**PLEASE DO NOT CHANGE THE NAME OF THIS FILE.**

**PLEASE DO NOT COPY & PASTE OR DELETE CELLS INLCUDED IN THE ASSIGNMENT.** (Note that you can add additional cells, if you want to test things out.

## Part 2: Functions (9 points)

### Q5 - Function execution (2 points)

The cell below includes a function that has been provided for you. After running the cell below (to define this function), execute (use) this function to create the following variable under the specified conditions:

1. `max_val_10` | execute the `find_max` function such that the function returns the value 10. 



{:.input_area}
```python
def find_max(random_list):
    
    list_max = 0

    for number in random_list:
        
        if number > list_max:
            list_max = number
            
    return list_max
```




{:.input_area}
```python
# use this cell to test/execute/check your thinking (optional)
```




{:.input_area}
```python
### BEGIN SOLUTION
max_val_10 = find_max([1, 2, 10])
### END SOLUTION
```




{:.input_area}
```python
assert max_val_10 is not None

### BEGIN HIDDEN TESTS
assert  max_val_10 == 10
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

specific rubric used in grading

=== END MARK SCHEME ===

### Q6 - `add_list` (3 points)

Write a function `add_list` that takes one input parameter `input_list`. Set the default value for `input_list` to be the list [1,2,3].

Within the function, write code that will add up all the values in the list, returning the sum of the values in the list and return this sum from the function.



{:.input_area}
```python
### BEGIN SOLUTION
def add_list(input_list = [1,2,3]):
    output = 0
    
    for val in input_list:
        output += val
        
    return output
### END SOLUTION
```




{:.input_area}
```python
# use this cell to test/execute/check your function (optional)
```




{:.input_area}
```python
assert callable(add_list)

### BEGIN HIDDEN TESTS
assert add_list() == 6
assert add_list([4,5]) == 9
### END HIDDEN TESTS
```


**This "blank" cell included intentionally.** Do not do anything here. (It's being used in grading.)


=== BEGIN MARK SCHEME ===

rubric for partial credit

=== END MARK SCHEME ===

### Q7 - `another_function` (4 points)

The real exam will include another function question here.

## Part 3: Objects & Classes (5 points)

### Q8 - objects (1 point)

The real exam will include an objects question here.

### Q9 - Classes (4 points)

Generate a class called `BasketballGame`.

This class should have four instance attributes: `home_team`, `away_team`, `home_points`, and `away_points`

It should also have one method, `play_game()`. 

Within the `play_game` method, add code that would determine who the winner of the game is (determined by the team with the most points), returning Winner: ' and the winning team's name.

For ties, return: 'Winner: tie'



{:.input_area}
```python
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
```




{:.input_area}
```python
# use this cell to test/execute/check your class (optional)
game = BasketballGame(home_team='Warriors', away_team='Sixers', 
                      home_points=100, away_points=105)
game.play_game()
```




{:.input_area}
```python
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
```




{:.input_area}
```python
assert callable(BasketballGame.play_game)

### BEGIN HIDDEN TESTS
# test method
assert game.play_game() == 'Winner: Sixers'
### END HIDDEN TESTS
```


This "blank" cell included intentionally. Do not do anything here. (It's being used in grading.)

=== BEGIN MARK SCHEME ===

rubric for partial credit

=== END MARK SCHEME ===

## Part 4: True & False (1 point)

For the statements below: depending upon whether the statement provided is True or False, store the appropriate boolean in the variable specified. 

For example, if the statement were:

`jupyter` | Jupyter Notebooks allow for text and code to be stored and executed in the same document.

your answer would be:

```python
jupyter = True
```

since, the statement above is `True` and the variable `jupyter` is what was specified at the start of the statement.

### Q10 - True/False (1 point)

Following the instructions & example above, store the appropriate boolean in the variable provided for each of the following statements:

- `car_inventory` | `car_inventory` is a better class name than `CarInventory`

The real exam will have more than one T/F here.



{:.input_area}
```python
### BEGIN SOLUTION
car_inventory = False
### END SOLUTION
```




{:.input_area}
```python
assert car_inventory is not None

### BEGIN HIDDEN TESTS
assert not car_inventory
### END HIDDEN TESTS
```


### Part II complete!

Good work - you're done with the second exam!

Check your work, and then when you're ready, **submit on datahub**.

We will not have your exam until you click submit and see this show up under 'submitted assignments'.
