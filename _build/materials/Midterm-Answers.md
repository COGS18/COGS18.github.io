---
interact_link: content/materials/Midterm-Answers.ipynb
download_link: assets/downloads/Midterm-Answers.ipynb.zip
pdf_link: assets/pdf/Midterm-Answers.pdf
layout: materials
title: 'Midterm-Answers'
prev_page:
  url: /materials/MidtermPractice
  title: 'MidtermPractice'
next_page:
  url: /materials/PythonParty
  title: 'PythonParty'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---



{:.input_area}
```python
#Q28
%whos
```


{:.output_stream}
```
Interactive namespace is empty.

```



{:.input_area}
```python
#Q1
print(True and True)
print(True or False)
print(not True or True)
```


{:.output_stream}
```
True
True
True

```



{:.input_area}
```python
# Q2
print(8 % 2)
print((6 + 12) / 2)
print(3 ** 2)
print(3 * 2)
print('best' +  '_' +  'class')

```


{:.output_stream}
```
0
9.0
9
6
best_class

```



{:.input_area}
```python
#Q3
print(8 < 8)
print(8 <= 8)
print(8 != 2)
print((12 < 20) and (20!=20))
print((12 < 20) or (20!=20))
```


{:.output_stream}
```
False
True
True
False
True

```



{:.input_area}
```python
#Q4

my_str = 'I love COGS18!'
my_lst = ['Ahrial', 'Weilun', 'Myles']

print('myles' in my_lst	)
print('love' in my_lst)
print('love' in my_str)
print('love' or 'Ahrial' in my_lst)
```


{:.output_stream}
```
False
False
True
love

```



{:.input_area}
```python
# Q5
val_a = 6
val_b = 12
val_c = 3 + 2 * val_b/val_a  
print(val_c + 2)
```


{:.output_stream}
```
9.0

```



{:.input_area}
```python
#Q8
#my_list[1]
#my_list[-1]
#my_list[2:]
```




{:.input_area}
```python
# Q9
cogs18 = ['Charles', 'Shreenivas', 'Severine', 'Stephen', 'Ahrial', 
                'Weilun', 'Myles', 'Miranda', 'Edward']

print(cogs18[1:4])

print(cogs18[0::4])
print(cogs18[0:9:4])
print(cogs18[::4])
print(cogs18[:9:4])
```


{:.output_stream}
```
['Shreenivas', 'Severine', 'Stephen']
['Charles', 'Ahrial', 'Edward']
['Charles', 'Ahrial', 'Edward']
['Charles', 'Ahrial', 'Edward']
['Charles', 'Ahrial', 'Edward']

```



{:.input_area}
```python
#Q10
cogs18_dict = { 'Charles' : 'TA',  'Shreenivas' : 'TA', 'Ellis' : 'Prof' }

print(len(cogs18_dict))
print(cogs18_dict['Ellis'])
print(type(cogs18_dict))
cogs18_dict.keys()
```


{:.output_stream}
```
3
Prof
<class 'dict'>

```




{:.output_data_text}
```
dict_keys(['Charles', 'Shreenivas', 'Ellis'])
```





{:.input_area}
```python
try = 6
```



{:.output_traceback_line}
```
  File "<ipython-input-10-25c09f84a48a>", line 1
    try = 6
        ^
SyntaxError: invalid syntax

```




{:.input_area}
```python
# Q13

var_1 = ['a', 'b', 'c']
var_2 = ('d', 'e', 'f')
```




{:.input_area}
```python
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
<ipython-input-12-f775984d1a59> in <module>()
----> 1 var_1[3]

```

{:.output_traceback_line}
```
IndexError: list index out of range
```




{:.input_area}
```python
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
<ipython-input-13-e5147cea4f3a> in <module>()
----> 1 var_2[4]

```

{:.output_traceback_line}
```
IndexError: tuple index out of range
```




{:.input_area}
```python
var_1[1] = 'z'
```




{:.input_area}
```python
var_2[1] = 'z'
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
<ipython-input-15-c0923d1a441b> in <module>()
----> 1 var_2[1] = 'z'

```

{:.output_traceback_line}
```
TypeError: 'tuple' object does not support item assignment
```




{:.input_area}
```python
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
<ipython-input-16-fe46618820fc> in <module>()
----> 1 var_1 + var_2

```

{:.output_traceback_line}
```
TypeError: can only concatenate list (not "tuple") to list
```




{:.input_area}
```python
#Q17
cond_a = 6 > 7
cond_b = 'word'

if cond_a: 
    print('Yes!')
elif cond_b:
    print('No!')
else:
    print('Maybe?')

```


{:.output_stream}
```
No!

```



{:.input_area}
```python
#Q17
cond_a = 6 < 7
cond_b = False

if cond_a: 
    print('Yes!')
elif cond_b:
    print('No!')
else:
    print('Maybe?')
```


{:.output_stream}
```
Yes!

```



{:.input_area}
```python
#Q17
cond_a = 3 <= 3
cond_b = 3 == 3

if cond_a: 
    print('Yes!')
elif cond_b:
    print('No!')
else:
    print('Maybe?')

```


{:.output_stream}
```
Yes!

```



{:.input_area}
```python
#Q18
ind = 4	
while ind < 7: 
    print(ind)
    ind += 1    
```


{:.output_stream}
```
4
5
6

```



{:.input_area}
```python
#Q19
for val in range(1,7,2):
    if(val<5):
        continue
    else:      
        print(val)
```


{:.output_stream}
```
5

```



{:.input_area}
```python
# Q24
def count_false(input_list):
    counter = 0
    for val in input_list:
        if not val:
            counter = counter + 1
    return counter
```




{:.input_area}
```python
# friendly reminder
bool(0)
```





{:.output_data_text}
```
False
```





{:.input_area}
```python
# friendly reminder
bool(1)
```





{:.output_data_text}
```
True
```





{:.input_area}
```python
# true, true, false
count_false([True, True, False])
```





{:.output_data_text}
```
1
```





{:.input_area}
```python
# false, false, true
count_false([0, 0, 1])
```





{:.output_data_text}
```
2
```





{:.input_area}
```python
# true, true, true
count_false([True, 1, 'False'])
```





{:.output_data_text}
```
0
```


