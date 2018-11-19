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
  url: /materials/17-APIs
  title: '17-APIs'
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


### More Shell Commands

#### Make a new directory



{:.input_area}
```python
!mkdir dir_name
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


#### Print the contents of a file



{:.input_area}
```python
!cat remote.py
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

`'' > my_file.py`

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

There are text editors designed to be used within a terminal, such as `vim`, `emacs`, or `nano`. 

#### vim

`vim` is a terminal based text-editor. Type `vim filename` in command line to open a file in vim. 

`vim` has different modes:

- click `escape` + `i` to enter edit mode (insert mode). 
    - This will let you write text / code into the file
- To escape vim, press `escape` then type `:wq` and enter to save and quit vim
    - If you want to exit without saving, you can do `:!q` to force quit without saving

### Non-Terminal Text Editors

For writing code (outside of notebooks and the terminal), you probably want a code focused stand-alone text editor, like `Sublime`.

## Executing Python Files

From the command line, you can execute a Python script using the `python` command:

`python my_python_file.py`
