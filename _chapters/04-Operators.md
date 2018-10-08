---
download_link: assets/downloads/04-Operators.ipynb.zip
pdf_link: assets/pdf/04-Operators.pdf
title: '04-operators'
permalink: '/chapters/04-Operators'
previouschapter:
  url: /chapters/03-Variables
  title: '03-variables'
nextchapter:
  url: 
  title: ''
redirect_from:
  - '/chapters/04-operators'
---

# Operators

## Assignment Operator

<div class="alert alert-success">
Python uses `=` for assignment.
</div>



{:.input_area}
```python
my_var = 1
```


## Math Operators

<div class="alert alert-success">
Python uses mathematical operators `+`, `-`, `*`, `/` for 'sum', 'substract', 'multiply', and 'divide'. These operators return numbers.
</div>



{:.input_area}
```python
print(2 + 3)
```




{:.input_area}
```python
div_result = 4 / 2
print(div_result)
```


### More Math

<div class="alert alert-success">
Python also has `**` for exponentiation and `%` for remainder (called modulus). These also return numbers.
</div>



{:.input_area}
```python
2 ** 3
```




{:.input_area}
```python
17 % 7
```


## Boolean Logic

<div class="alert alert-success">
Python has `and`, `or` and `not` for boolean logic. These operators return booleans.
</div>



{:.input_area}
```python
True and True
```




{:.input_area}
```python
True and not False
```


### Clicker #1

What will the following boolean expression evaluate as:

True and not True or False

- a) True
- b) False
- c) None
- d) This code will fail

### Clicker Question Answer



{:.input_area}
```python
True and not True or False
```


## Comparison Operators

<div class="alert alert-success">
Python has comparison operators `==`, `!=`, `<`, `>`, `<=`, and `>=` for value comparisons. These operators return booleans.
</div>



{:.input_area}
```python
True == True
```




{:.input_area}
```python
12 >= 13
```


## Comparing Identity Operators

<div class="alert alert-success">
Python uses `is` and `is not` to compare identity. These operators return booleans.
</div>



{:.input_area}
```python
a = 927
b = a
c = 927
```




{:.input_area}
```python
print(a is b)
print(c is a)
```




{:.input_area}
```python
a == b == c
```


## String Concatenation

<div class="alert alert-success">
Operators sometimes do different things on different data. For example, `+` on strings does concatenation.
</div>



{:.input_area}
```python
'a' + 'b' + 'c'
```


## Chaining Operators

<div class="alert alert-success">
Operators and variables can also be chained together into arbitrarily complex expressions.
</div>



{:.input_area}
```python
# Note that you can use parentheses to chunk sections
(13 % 7 >= 7) and ('COGS' + '18' == 'COGS18')
```


### Clicker #2

What will the following expression evaluate as:

`2**2 >= 4 and 13%3 > 1`

- a) True
- b) False
- c) None
- d) This code will fail

### Clicker Question Answer



{:.input_area}
```python
2**2 >= 4 and 13%3 > 1
```

