---
download_link: assets/downloads/A2-Examples.ipynb.zip
pdf_link: assets/pdf/A2-Examples.pdf
title: 'A2-examples'
permalink: '/chapters/A2-Examples'
previouschapter:
  url: /chapters/A1-Syntax
  title: 'A1-syntax'
nextchapter:
  url: 
  title: ''
redirect_from:
  - '/chapters/a2-examples'
---

# Examples

The following is a quick 

## Defining Variables

### Basic Types



{:.input_area}
```python
my_int = 1
my_float = 12.2
my_boolean = True
```


### Collection Types



{:.input_area}
```python
my_string = 'abc'
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dictionary = {}
```


## Operators

### Mathematical Operators



{:.input_area}
```python
print('Addition: \t', 12 + 3)
print('Subtraction: \t', 12 - 3)
print('Multiplication: ', 12 * 3)
print('Division: \t', 12 / 3)
```


{:.output_stream}
```
Addition: 	 15
Subtraction: 	 9
Multiplication:  36
Division: 	 4.0

```



{:.input_area}
```python
print('Exponentiation:\t', 2**2)
print('Remainder: \t', 7%2)
```


{:.output_stream}
```
Exponentiation:	 4
Remainder: 	 1

```

### Boolean Operators



{:.input_area}
```python
# Boolean `and`
True and True
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Boolean `or`
True or False
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Boolean `not`
not True
```





{:.output_data_text}
```
False
```



### Other Operators



{:.input_area}
```python
# String concatenation
print('a' + 'b' + 'c')
```


{:.output_stream}
```
abc

```

## Value Comparisons



{:.input_area}
```python
# Is equal
1 == 1
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Is not equal 
2 != 1
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# Less than
```




{:.input_area}
```python
# 
```


## Conditionals



{:.input_area}
```python
first_condition = False
other_condition = True

if first_condition:
    print('if condition')
elif other_condition:
    print('elif condition')
else:
    print('else condition')    
```


{:.output_stream}
```
elif condition

```

## Loops



{:.input_area}
```python
i = 0
condition = True

while condition:
    print('In a loop')
```




{:.input_area}
```python
list_of_items = [1, 2, 3]

for item in list_of_items:
    print(item)
```


{:.output_stream}
```
1
2
3

```



{:.input_area}
```python
for iteration in range(5):
    print(iteration)
```


{:.output_stream}
```
0
1
2
3
4

```

## Functions



{:.input_area}
```python
# Defining a function
def function_name(function_input_1, function_input_2):

    output = function_input_1 + function_input_2
    
    return output
```




{:.input_area}
```python
# Calling a function
answer = function_name(1, 2)

print('Answer:\t', answer)
```


{:.output_stream}
```
Answer:	 3

```
