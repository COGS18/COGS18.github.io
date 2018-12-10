---
interact_link: content/materials/04-Operators.ipynb
download_link: assets/downloads/04-Operators.ipynb.zip
pdf_link: assets/pdf/04-Operators.pdf
layout: materials
title: '04-Operators'
prev_page:
  url: /materials/03-Variables
  title: '03-Variables'
next_page:
  url: /materials/05-Conditionals
  title: '05-Conditionals'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
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


{:.output_stream}
```
5

```



{:.input_area}
```python
div_result = 4 / 2
print(div_result)
```


{:.output_stream}
```
2.0

```

### More Math

<div class="alert alert-success">
Python also has `**` for exponentiation and `%` for remainder (called modulus). These also return numbers.
</div>



{:.input_area}
```python
2 ** 3
```





{:.output_data_text}
```
8
```





{:.input_area}
```python
17 % 7
```





{:.output_data_text}
```
3
```



## Boolean Logic

<div class="alert alert-success">
Python has `and`, `or` and `not` for boolean logic. These operators return booleans.
</div>



{:.input_area}
```python
True and True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
True or True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
True and not False
```





{:.output_data_text}
```
True
```



### Clicker #1

What will the following boolean expression evaluate as:



{:.input_area}
```python
True and not True or False
```


- a) True
- b) False
- c) None
- d) This code will fail

## Comparison Operators

<div class="alert alert-success">
Python has comparison operators `==`, `!=`, `<`, `>`, `<=`, and `>=` for value comparisons. These operators return booleans.
</div>



{:.input_area}
```python
True == True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
'aa' == 'aa'
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
12 >= 13
```





{:.output_data_text}
```
False
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


{:.output_stream}
```
True
False

```



{:.input_area}
```python
a == b == c
```





{:.output_data_text}
```
True
```



## String Concatenation

<div class="alert alert-success">
Operators sometimes do different things on different data. For example, `+` on strings does concatenation.
</div>



{:.input_area}
```python
'a' + 'b' + 'c'
```





{:.output_data_text}
```
'abc'
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





{:.output_data_text}
```
False
```



### Clicker #2

What will the following expression evaluate as:



{:.input_area}
```python
2**2 >= 4 and 13%3 > 1
```


- a) True
- b) False
- c) None
- d) This code will fail
