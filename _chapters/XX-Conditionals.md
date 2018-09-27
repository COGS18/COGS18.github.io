---
title: 'Xx-conditionals'
permalink: '/chapters/XX-Conditionals'
previouschapter:
  url: /chapters/XX-ComplexDataTypes
  title: 'Xx-complexdatatypes'
nextchapter:
  url: /chapters/XX-DataTypes
  title: 'Xx-datatypes'
redirect_from:
  - '/chapters/xx-conditionals'
---

# Conditionals

### Recap: Booleans

Booleans are a data type that take values of `True` or `False`. 



{:.input_area}
```python
condition = True

if condition:
    print('This code executes if the condition evaluates as True.')
else: 
    print('This code executes if the condition evaluates as False')
```


{:.output_stream}
```
This code executes if the condition evaluates as True.

```

### Comparing Contents

We might often want to 

To ask if two variable have the same contents,  evaluates, , we can use `==`. 



{:.input_area}
```python
print(True == True)
```


{:.output_stream}
```
True

```



{:.input_area}
```python
print(True == False)
```


{:.output_stream}
```
False

```

### Comparing Identity





{:.input_area}
```python
a = True
a is True
```





{:.output_data_text}
```
True
```



### Comparing Contents vs. Comparing Identity



{:.input_area}
```python
a = 1
b = int(a)
c = a

print(a is b)
print(a == c)
```


{:.output_stream}
```
True
True

```



{:.input_area}
```python
a = [1, 2, 3]
b = a
c = list(a)
```




{:.input_area}
```python
print(a == b)
print(a is b)

print(a == c)
print(a is c)
```


{:.output_stream}
```
True
True
True
False

```



{:.input_area}
```python
print(id(a))
print(id(b))
print(id(c))
```


{:.output_stream}
```
4362733256
4362733256
4362732744

```



{:.input_area}
```python
a = 1
hex(id(a))
```





{:.output_data_text}
```
'0x101579830'
```





{:.input_area}
```python
data = 12

if data == 
```

