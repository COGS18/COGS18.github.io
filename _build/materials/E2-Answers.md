---
interact_link: content/materials/E2-Answers.ipynb
download_link: assets/downloads/E2-Answers.ipynb.zip
pdf_link: assets/pdf/E2-Answers.pdf
layout: materials
title: 'E2-Answers'
prev_page:
  url: /materials/Exam2-Practice
  title: 'Exam2-Practice'
next_page:
  url: /labs/CL1-Tooling
  title: 'Coding Labs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---



{:.input_area}
```python
#Q1

my_variable = 17.6
print(type(my_variable))

my_variable = True 
print(type(my_variable))

my_variable = 'name'
print(type(my_variable))

my_variable = [1, 2, 3]
print(type(my_variable))

my_variable = (1, 2, 3)
print(type(my_variable))

my_variable = 'None'
print(type(my_variable))


```


{:.output_stream}
```
<class 'float'>
<class 'bool'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'str'>

```



{:.input_area}
```python
#Q2
print(6 / (2 + 4))
print(18 % 9)
#print(2 = 2)
print((22 < 5) or (20 == 20))
print(False and not False)
print('COG' in 'COGS 18')
```


{:.output_stream}
```
1.0
0
True
False
True

```



{:.input_area}
```python
#Q3

cogs18 = ['Devendra', 'Shreenivas', 'Andrew', 'Chau', 'Duolan', 
          'Byungkwon', 'Severine', 'Stephen', 'Zekria']

print(cogs18[-1])
print(cogs18[4:7])
```


{:.output_stream}
```
Zekria
['Duolan', 'Byungkwon', 'Severine']

```



{:.input_area}
```python
#Q4

my_list = [1, 2, 3]

for value in my_list:
    if value > 0:
        pass
    elif value < 0:
        pass
    else:
        pass
```




{:.input_area}
```python
#Q5
def subtraction(num1, num2):
    return num1 - num2

print(subtraction(num1 = 19, num2 = 17))
print(subtraction(19, 17))
print(subtraction(num2 = 3, num1 = 6))
# print(subtraction(num1 = 19, 17))

```


{:.output_stream}
```
2
2
3

```



{:.input_area}
```python
#Q6A
def state_country(country = 'USA'):
    output = 'I am from ' + country
    return output
```




{:.input_area}
```python
#Q6B
state_country()
```





{:.output_data_text}
```
'I am from USA'
```





{:.input_area}
```python
#Q6C
state_country(country = 'outer space')
```





{:.output_data_text}
```
'I am from outer space'
```





{:.input_area}
```python
#Q8A
def sum_tuple(my_tuple):
    total = 0
    for item in my_tuple:
        total += item
    return total
```




{:.input_area}
```python
#Q8B
sum_tuple((1, 2, 3))
```





{:.output_data_text}
```
6
```





{:.input_area}
```python
#Q8C
sum_tuple([1, 2, 3])
```





{:.output_data_text}
```
6
```





{:.input_area}
```python
#Q9
import random
print(random.choice([1, 2, 3, 4]))
print(random.choice(range(0, 5)))

#OR

from random import choice
print(choice([1, 2, 3, 4]))
print(choice(range(0, 5)))
```


{:.output_stream}
```
3
0
2
4

```



{:.input_area}
```python
# Q12A
class BasketballGame():
    
    def __init__(self, home_team, away_team, 
                 home_points, away_points):
        self.home_team = home_team
        self.away_team = away_team
        self.home_points = home_points
        self.away_points = away_points

    def play_game(self):
        if self.home_points > self.away_points:
            out = "Winner: " + self.home_team
        elif self.away_points > self.home_points:
            out = "Winner: " + self.away_team
        else:
            out = "Winner: tie"

        return out
```




{:.input_area}
```python
#Q12B
my_game = BasketballGame(home_team = "Warriors",  away_team = "Sixers",  
                         home_points = 100, away_points = 105)
my_game.play_game()
```





{:.output_data_text}
```
'Winner: Sixers'
```


