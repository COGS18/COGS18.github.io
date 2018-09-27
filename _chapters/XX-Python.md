---
title: 'Xx-python'
permalink: '/chapters/XX-Python'
previouschapter:
  url: /chapters/XX-Objects
  title: 'Xx-objects'
nextchapter:
  url: /chapters/XX-Variables
  title: 'Xx-variables'
redirect_from:
  - '/chapters/xx-python'
---

## Python is a whitespace language

## Comments vs. Code



{:.input_area}
```python
Python 
```


## Literals: commas

## Code Execution

Computer code is a set of instructions, that can be interpreted and executed by a computer.



{:.input_area}
```python
aa = 'aa'
aa = aa + 'b'
```




{:.input_area}
```python
my_message = "Hello, I am Tom"

# Encoding
encoded_message = ""
for char in my_message:
    encoded_message = encoded_message + chr(ord(char) + 1)
    
print("Encoded Message: ", encoded_message)
    
# Decoding
decoded_message = ""
for char in encoded_message:
    decoded_message = decoded_message + chr(ord(char) -1)

print("Decoded Message: ", decoded_message)
```


{:.output_stream}
```
Encoded Message:  Ifmmp-!J!bn!Upn
Decoded Message:  Hello, I am Tom

```

Question: what is the most common letter that will appear in the above encoding procedure?
