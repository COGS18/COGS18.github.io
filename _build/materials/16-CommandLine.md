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
## Course Announcements

- **Coding Lab 7** due Wednesday (5/13)
- **Exam 2** Friday (5/15)
    - 24 hours like E1 (released Fri @ 8AM PDT)
    - fetched, completed, and submitted on datahub
    - details to be discussed during review Wed
- **A4** due Mon (5/18)


# Command Line & Scripts

- command line & shell commands
- file paths (absolute and relative)
- scripts and modules

Jupyter Notebooks are a helpful tool, but they're _bulky_.

## File Systems

<div class="alert alert-success">
Computers use a hierarchical file systems that organizes files & folders.
</div>

When you click through the folders (directories) on your computer, you're interacting with this hierarchical system.

## Command Line

<div class="alert alert-success">
A <b>command line interface</b> is a way to interact with a computer through written commands.
</div>

The command line allows us to:

- create files
- edit files
- run python scripts
- etc.

...without clicking on anything.

### The Terminal

The **terminal** is where you can type these commands into the command line.

Accessing the terminal...

- possible on your computer
- and on datahub

### Shell Commands

...can be run in the terminal _and_ Jupyter notebooks

Do this by starting with `!`

#### Check current directory



{:.input_area}
```python
# print working directory
!pwd
```


## An important aside: File Paths

<div class="alert alert-success">
The specific location of a file or folder on your computer. </div>

When using a Graphical User Interface (GUI), you click on directories to access subdirectories and finally find the file you're interested in.

When using the command line, you specify a file's path explicitly with text. 

### Absolute vs. Relative Paths

The two ways to specify the path to your file of interest allow for flexibility in programming.

#### Absolute Paths

<div class="alert alert-success">
<b>Absolute paths</b> specify the <b>full</b> path for a given file system (starting from the root directory). 
</div>

**root** specifies the 'highest' directory in the file structure (the start).

An absolute file path starts with a slash `/` specifying the root directory.




{:.input_area}
```python
## absolute path
## this is specific to my computer
## look at the path output above for you computer
!ls /Users/shannonellis/Desktop/Teaching/COGS18/Materials
```


#### Relative Paths

<div class="alert alert-success">
<b>Relative paths</b> specify the path to a file from your <b>current working directory</b> (where your computer is working right now). 
</div>



{:.input_area}
```python
# remind us of our current working directory
!pwd
```




{:.input_area}
```python
# relative path
# this is specific to my computer
!ls ../COGS108/Lectures-Sp19
```



- `..` specify you want to move one directory up in your hierarchy
- `COGS108/Lectures-Sp19` specifies the path to the directory I want to list files in
- each directory is separated with a slash (`/`)

This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

### Clicker Question #1

Given the following file structure: 

- `/`
    - `scripts/`
        - cool_thing.py
        - super_cool_thing.py
    - `images/`
        - image1.png
        - image2.png
    - `notebooks/`
        - 00_intro.ipynb
        - 01_variables.ipynb
    

If your current working directory is `notebooks`, shat is the **absolute path** to `cool_thing.py`?

- A) `/scripts/cool_thing.py`
- B) `scripts/cool_thing.py`
- C) `scripts/cool_thing.py`
- D) `../scripts/cool_thing.py`
- E) ¯\\\_(ツ)\_/¯

### Clicker Question #2

Given the same file structure: 

- `/`
    - `scripts/`
        - cool_thing.py
        - super_cool_thing.py
    - `images/`
        - image1.png
        - image2.png
    - `notebooks/`
        - 00_intro.ipynb
        - 01_variables.ipynb
    

If your current working directory is `notebooks`, what is the **relative path** to `cool_thing.py`?

- A) `/notebooks/../scripts/cool_thing.py`
- B) `scripts/cool_thing.py`
- C) `/scripts/cool_thing.py`
- D) `../scripts/cool_thing.py`
- E) ¯\\\_(ツ)\_/¯

### Shell Commands

...can be run in the terminal _and_ Jupyter notebooks

#### Check current directory



{:.input_area}
```python
# print working directory
!pwd
```


#### Change directory



{:.input_area}
```python
# change directory
!cd ~/Desktop 
```


Here, we saw `~/Desktop/`. 

- `~` specifies the user's home directory of your computer
- `Desktop` is a directory in my home directory (`~`)
- each directory is separated with a slash (`/`)

#### List files in a directory



{:.input_area}
```python
# list files (list segments)
!ls
```


### More Shell Commands

#### Make a new directory



{:.input_area}
```python
# make directory 
!mkdir dir_name
```


#### Create a file



{:.input_area}
```python
# create an empty file
!touch new_file.py 
```


#### Move a file



{:.input_area}
```python
# move file
# notice the relative file path
!mv new_file.py dir_name/
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
!cat dir_name/new_file.py
```


#### Open to see and edit contents of a file



{:.input_area}
```python
!open dir_name/new_file.py
```


### Clicker Question #3

Which is the best description of the following command:
    
`ls -l`

- A) `ls -l` is most analogous to a class in Python
- B) The whole `ls -l` is like a function call
- C) `-l` is analogous to a function call, and `ls` is like a parameter
- D) `ls` is analogous to a function, and `-l` is like a parameter
- E) There is no clear analogy here to Python



{:.input_area}
```python
## test out here
```


### Clicker Question #4

Which creates a file?     
   
- A) `mkdir`
- B) `pwd`
- C) `cd`
- D) `touch`
- E) `cat`

## Windows Command Prompt

Some commands are slightly different if you are using windows command prompt:

- `dir` : lists files in current directory
- `move` : moves a file
- `copy` : copies a file
- `rename` : renames a file
- `type` : can be used to print out a file
    
Note that `pwd`, `cd`, `mkdir`, `echo` are all the same in Windows command prompt.

If you want to make a new empty file, you can do:

`'' > my_file.py`

^This construction puts an empty string into a file. If the filename is not found, it will create a new (empty) file.

## Python Files

<div class="alert alert-success">
Python files are plain-text files, with Python code in them, that can be executed and/or imported from.
</div>

### Script vs. Module File

### Scripts

<div class="alert alert-success">
A <b>script</b> is a Python file that can be run to execute a particular task. 
</div>

### Module Files

<div class="alert alert-success">
A <b>module</b> file is a file with Python code (typically functions & classes) that we can import and use.
</div>

Remember: if you're writing code, you cannot just click through to the file you want. You need to specify _using code_ where the file you want is. 

This is where understanding file paths is critically important.

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

`python dir_name/new_file.py`

### Clicker Question #5

To create a file and see its contents, which command line commands would you use (and in which order)?    
   
- A) `mkdir` > `cd`
- B) `pwd` > `ls`
- C) `cd` > `pwd`
- D) `touch` > `cat`
- E) `cat` > `touch`

### Clicker Question #6

Given the file structure from earlier: 

- `/`
    - `scripts/`
        - cool_thing.py
        - super_cool_thing.py
    - `images/`
        - image1.png
        - image2.png
    - `notebooks/`
        - 00_intro.ipynb
        - 01_variables.ipynb

Your currently working within `notebooks` and you want to execute the code in 'cool_thing.py' from the command line. How would you do that?


- A) `python cool_thing.py` 
- B) `python ../notebooks/cool_thing.py` 
- C) `python ../scripts/cool_thing.py` 
- D) `python ../cool_thing.py` 
- E) ¯\\\_(ツ)\_/¯ 
