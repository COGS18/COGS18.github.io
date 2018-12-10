---
interact_link: content/materials/A2-Examples.ipynb
download_link: assets/downloads/A2-Examples.ipynb.zip
pdf_link: assets/pdf/A2-Examples.pdf
layout: materials
title: 'A2-Examples'
prev_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
next_page:
  url: /materials/Midterm
  title: 'Midterm'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Examples

The following is a set of quick examples of the code constructs that we work through in class. 

This notebook does not have any explanations - so do check the course Materials for those details. 

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
my_dictionary = {'name1' : True, 'name2' : 12}
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
# Equality comparisons
print('Equal:  \t', 1 == 1)
print('Unequal:\t', 2 != 1)
```


{:.output_stream}
```
Equal:  	 True
Unequal:	 True

```



{:.input_area}
```python
# Magnitude Comparisons
print('Less Than:     \t\t\t', 2 < 3)
print('Greater Than:  \t\t\t', 4 > 5)
print('Less Than Or Equal to:     \t', 2 <= 2)
print('Greater Than Or Equal to:  \t', 3 >= 5)
```


{:.output_stream}
```
Less Than:     			 True
Greater Than:  			 False
Less Than Or Equal to:     	 True
Greater Than Or Equal to:  	 False

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
# While Loop
ind = 0
while ind < 3:
    print('Looping!')
    ind = ind + 1
```


{:.output_stream}
```
Looping!
Looping!
Looping!

```



{:.input_area}
```python
# For Loop
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
# For Loop using Range
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



{:.input_area}
```python
# Define a function with default values
def multiply(num1, num2=2):
    return num1 * num2
```




{:.input_area}
```python
# Calling a function that has default values
print(multiply(2))
print(multiply(2, 3))
```


{:.output_stream}
```
4
6

```

## Combining Functions with Control Flow



{:.input_area}
```python
# Defining a Function with a Conditional inside it
def conditional_function(input_boolean):
    
    if input_boolean == True:
        output = 'Yay!'
    else:
        output = 'Nay.'
    
    return output
```




{:.input_area}
```python
# Calling our function
returned = conditional_function(True)
print(returned)
```


{:.output_stream}
```
Yay!

```



{:.input_area}
```python
# Defining a Function with a Loop inside it
def loop_function(my_list):
    
    new_list = []
    for item in my_list:
        temp = item + 1
        new_list.append(temp)
        
    return new_list
```




{:.input_area}
```python
# Calling our function
out_list = loop_function([1, 2, 3])
print(out_list)
```


{:.output_stream}
```
[2, 3, 4]

```



{:.input_area}
```python
# Function with everything
def busy_function(complex_list):
    """This function takes a complex list, and returns the numbers of booleans in the list."""
    
    boolean_counter = 0
    
    for item in complex_list:
        if item == True or item == False:
            boolean_counter = boolean_counter + 1
            
    return boolean_counter
```




{:.input_area}
```python
# Calling our function
busy_function([True, 7.2, 'and', 13, False, '', None, 'word', True])
```





{:.output_data_text}
```
3
```



# Errors



{:.input_area}
```python
# Raise an error
raise ValueError('The value you gave is no good.')
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ValueError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-25-3fd7c3ac350e> in <module>()
      1 # Raise an error
----> 2 raise ValueError('The value you gave is no good.')

```

{:.output_traceback_line}
```
ValueError: The value you gave is no good.
```




{:.input_area}
```python
# Try / Except
try:
    sum()
except TypeError:
    print('Hmm. It seems that did not work.')
```


{:.output_stream}
```
Hmm. It seems that did not work.

```

# Classes



{:.input_area}
```python
class Animal():
    
    # Create a class attribute
    domain = 'eukaryota'

    # Use init to define instance attributes
    def __init__(self, sound):
        self.sound = sound

    # Define a class method
    def speak(self):
        print(self.sound)
```




{:.input_area}
```python
# Create an instance of our class
gary = Animal('woof')
gary.speak()
```


{:.output_stream}
```
woof

```

### Class Inheritance



{:.input_area}
```python
class Monkey(Animal):
    
    def __init__(self, sound):
        super().__init__(sound)
        self.has_hands = True
       
    def check_hands(self):
        if self.has_hands:
            print('This animal has hands!')    
```




{:.input_area}
```python
# Create an instance of our derived
jeff = Monkey('Monkey noise.')
jeff.speak()
jeff.check_hands()
```


{:.output_stream}
```
Monkey noise.
This animal has hands!

```
