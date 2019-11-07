---
interact_link: content/materials/E1-Answers.ipynb
download_link: assets/downloads/E1-Answers.ipynb.zip
pdf_link: assets/pdf/E1-Answers.pdf
layout: materials
title: 'E1-Answers'
prev_page:
  url: /materials/Exam1-Practice
  title: 'Exam1-Practice'
next_page:
  url: /materials/Exam2-Review
  title: 'Exam2-Review'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---



{:.input_area}
```python
# Q2
print((4 + 2) / 2)
print(16 % 5)
print(4 ** 2)
print(2 * 4)
print('python'  +  'love')
print(2 + 'python')
```


{:.output_stream}
```
3.0
1
16
8
pythonlove

```


{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-36-cd2cf6df932c> in <module>()
      5 print(2 * 4)
      6 print('python'  +  'love')
----> 7 print(2 + 'python')

```

{:.output_traceback_line}
```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```




{:.input_area}
```python
#Q3
print(3 <= 8)
print(2 != 2)
print((3 >= 8) or (20 != 20))
print((12 < 20) and (20 == 20))
```


{:.output_stream}
```
True
False
False
True

```



{:.input_area}
```python
#Q4
print(True and False)
print(False or True)
print(True or not False)
```


{:.output_stream}
```
False
True
True

```



{:.input_area}
```python
#Q5
my_string = 'I love COGS18!'
my_list = ['Sarah', 'Titan', 'Zijian']

print('sarah' in my_list)
print('love' in my_list)
print('Titan' in my_list)
print('COGS' in my_string)
```


{:.output_stream}
```
False
False
True
True

```



{:.input_area}
```python
# Q6
val_a = 4
val_b = 2
val_c = 3 + (2 * val_b/val_a) 
print(val_c + 2)
```


{:.output_stream}
```
6.0

```



{:.input_area}
```python
#Q9
#my_list[4]
#my_list[-2]
#my_list[3:]
```




{:.input_area}
```python
# Q10
cogs18 = ['Devendra', 'Shreenivas', 'Andrew', 'Chau', 'Duolan', 
          'Byungkwon', 'Severine', 'Stephen', 'Zekria']

#output A
print(cogs18[4:7])

# all of these work for Output B
print(cogs18[0::3])
print(cogs18[0:7:3])
print(cogs18[::3])
print(cogs18[:7:3])
print(cogs18[:-2:3])
```


{:.output_stream}
```
['Duolan', 'Byungkwon', 'Severine']
['Devendra', 'Chau', 'Severine']
['Devendra', 'Chau', 'Severine']
['Devendra', 'Chau', 'Severine']
['Devendra', 'Chau', 'Severine']
['Devendra', 'Chau', 'Severine']

```



{:.input_area}
```python
#Q11
cogs18_dict = { 'Devendra' : 'TA',  'Shreenivas' : 'TA', 'Ellis' : 'Prof' }

print(len(cogs18_dict))
print(cogs18_dict['Ellis'])
type(cogs18_dict)

```


{:.output_stream}
```
3
Prof

```




{:.output_data_text}
```
dict
```





{:.input_area}
```python
# Q12
var_1 = ('a', 'b', 'c')
var_2 = ['d', 'e', 'f']
```




{:.input_area}
```python
# option A
var_1[3]
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-17-f775984d1a59> in <module>()
----> 1 var_1[3]

```

{:.output_traceback_line}
```
IndexError: tuple index out of range
```




{:.input_area}
```python
# option B
var_2[4]
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
IndexError                                Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-18-e5147cea4f3a> in <module>()
----> 1 var_2[4]

```

{:.output_traceback_line}
```
IndexError: list index out of range
```




{:.input_area}
```python
# option C
var_1[1] = 'z'
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-19-e3edd5605fda> in <module>()
----> 1 var_1[1] = 'z'

```

{:.output_traceback_line}
```
TypeError: 'tuple' object does not support item assignment
```




{:.input_area}
```python
# option D
var_2[1] = 'z'
```




{:.input_area}
```python
# option E
var_1 + var_2
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
TypeError                                 Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-21-fe46618820fc> in <module>()
----> 1 var_1 + var_2

```

{:.output_traceback_line}
```
TypeError: can only concatenate tuple (not "list") to tuple
```




{:.input_area}
```python
#Q15
ind = 2
while ind < 4: 
    print(ind) # added to demonstrate how many times it iterates
    ind = ind + 1    
```


{:.output_stream}
```
2
3

```



{:.input_area}
```python
#Q16
cond_a = 7 >= 7
cond_b = 'word'

if cond_a: 
    print('First Condition')
elif cond_b:
    print('Second Condition')
else:
    print('Third Condition')
```


{:.output_stream}
```
First Condition

```



{:.input_area}
```python
#Q16
cond_a =7 > 7
cond_b = False

if cond_a: 
    print('First Condition')
elif cond_b:
    print('Second Condition')
else:
    print('Third Condition')
```


{:.output_stream}
```
Third Condition

```



{:.input_area}
```python
#Q16
cond_a = 7 > 7
cond_b = 3 == 3

if cond_a: 
    print('First Condition')
elif cond_b:
    print('Second Condition')
else:
    print('Third Condition')
```


{:.output_stream}
```
Second Condition

```



{:.input_area}
```python
#Q17
out_val = 0

for val in range(2, 11, 2):
    if(val <= 5):
        out_val = out_val + val
    else:  
        break
        
print(out_val)
```


{:.output_stream}
```
6

```



{:.input_area}
```python
#Q18
counter = 0

for ltr in 'shannon':
    counter = counter + 1

print(counter)
```


{:.output_stream}
```
7

```
