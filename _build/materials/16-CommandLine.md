---
interact_link: content/materials/16-CommandLine.ipynb
download_link: assets/downloads/16-CommandLine.ipynb.zip
pdf_link: assets/pdf/16-CommandLine.pdf
layout: materials
title: '16-CommandLine'
prev_page:
  url: /materials/15-Namespaces
  title: '15-Namespaces'
next_page:
  url: /materials/A1-Syntax
  title: 'A1-Syntax'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Command Line & Scripts

## File Systems

<div class="alert alert-success">
Computers use a hierierarchical file systems that organize files & folders.
</div>

## Command Line

<div class="alert alert-success">
A 'command line interface' is a way to interact with a computer through written commands.
</div>

### Shell Commands

#### Check current directory



{:.input_area}
```python
!pwd
```


{:.output_stream}
```
/Users/tom/Documents/EdCode/18Org/Materials

```

#### Change directory



{:.input_area}
```python
!cd ~/Desktop/
```


#### List files in a directory



{:.input_area}
```python
!ls
```


{:.output_stream}
```
00-Introduction.ipynb           13-Objects.ipynb
00-Introduction.slides.html     14-Classes.ipynb
01-Tools.ipynb                  15-Namespaces.ipynb
01-Tools.slides.html            16-CommandLine.ipynb
02-JupyterNotebooks.ipynb       A1-Syntax.ipynb
02-JupyterNotebooks.slides.html A2-Examples.ipynb
03-Variables.ipynb              A3-Dictionary.ipynb
03-Variables.slides.html        Midterm.ipynb
04-Operators.ipynb              MidtermPractice.ipynb
04-Operators.slides.html        README.md
05-Conditionals.ipynb           TEMPLATES.ipynb
05-conditionals.slides.html     Untitled.ipynb
06-DataTypes.ipynb              XX-Assert.ipynb
06-DataTypes.slides.html        ZZ-CheckInQuestions.ipynb
07-Loops.ipynb                  [34m__pycache__[m[m
08-Encodings.ipynb              assignment_notes.ipynb
09-FunctionsI.ipynb             [34mdir_name[m[m
10-Algorithms.ipynb             [34mimg[m[m
11-FunctionsII.ipynb            remote.py
12-Debugging.ipynb              zz-Misc.ipynb

```

### More Shell Commands

#### Make a new directory



{:.input_area}
```python
!mkdir dir_name
```


{:.output_stream}
```
mkdir: dir_name: File exists

```

#### Create a file



{:.input_area}
```python
!touch new_file.py 
```


#### Move a file



{:.input_area}
```python
!mv new_file.py dir_name/new_file.py
```


### And Some More

#### Print out a message



{:.input_area}
```python
!echo Hello World!
```


{:.output_stream}
```
Hello World!

```

#### Print the contents of a file



{:.input_area}
```python
!cat remote.py
```


{:.output_stream}
```

def my_remote_function(input_1, input_2):
    """A function from far away. 
    
    This function returns the sum of the two inputs. 
    """
    
    return input_1 + input_2


def choice(list_to_choose_from):
    """Choose and return an item from a list. 
       
    Notes: I am a custom choice function! I am not from `random`. 
    
    Hint: my favourite is the last item. 
    """
    
    return list_to_choose_from[-1]
    
    
class MyNumbers():
    
    kind_of_thing = 'numbers'
    
    def __init__(self, num1, num2):
        
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        
        return self.num1 + self.num2
        
    def subtract(self):
        
        return self.num2 - self.num1

```

## Windows Command Prompt

Some commands are slightly different if you are using windows command prompt:

- `dir`
    - lists files in current directory
- `move`	
    - moves a file
- `copy`	
    - copies a file
- `rename`	
    - renames a file
- `type`
    - can be used to print out a file
    
Note that `pwd`, `cd`, `mkdir`, `echo` are all the same in Windows command prompt.

If you want to make a new empty file, you can do:

`'' > file.txt`

^This construction puts an empty string into a file. If the filename is not found, it will create a new (empty) file.

### Clicker Question #1

Which is the best description of the following command:
    
    `ls -l`

- a) `ls -l` is most analogous to a class in Python
- b) The whole `ls -l` is like a function call
- c) `-l` is analogous to a function call, and `ls` is like a parameter
- d) `ls` is analogous to a function, and `-l` is like a parameter
- e) There is no clear analogy here to Python

## Python Files

<div class="alert alert-success">
Python files are plain-text files, with Python code in them, that can be executed and/or imported from.
</div>

### Script vs. Module File

### Scripts

<div class="alert alert-success">
A script is a Python file that can be run to execute a particular task. 
</div>

### Module Files

<div class="alert alert-success">
A module file is a file with Python code (typically functions & classes) that we can import and use.
</div>

## Text Editors

<div class="alert alert-success">
Text-editors are programs made for editing text. Many text-editors are designed for writing code specifically. 
</div>

### Terminal Based Text Editors

There are text editors designed to be used within a terminal, such as `vim` and `emacs`. 

### Non-Terminal Text Editors

For writing code (outside of notebooks and the terminal), you probably want a code focused stand-alone text editor, like Sublime.
