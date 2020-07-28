---
interact_link: content/materials/13-CommandLine.ipynb
download_link: assets/downloads/13-CommandLine.ipynb.zip
pdf_link: assets/pdf/13-CommandLine.pdf
layout: materials
title: '13-CommandLine'
prev_page:
  url: /materials/12-Namespaces
  title: '12-Namespaces'
next_page:
  url: /materials/14-Documentation-Style
  title: '14-Documentation-Style'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Course Announcements

**Due Dates**
- **A4** due tonight (11:59 PM)
- **CL5** due Wed (5/13)
- **A5** due Friday (11:59 PM) 
    - syllabus says due Thursday
    - shorter than previous assignments
- **Final Exam** Friday (due Sat 11 AM)

**Notes**
- CL4 - "graded", but be sure to go back and "fix" your errors
- E2 - graded/answers posted _tomorrow_

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


{:.output_stream}
```
/Users/shannonellis/Desktop/Teaching/COGS18/LectureNotes-Su20

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
!ls /Users/shannonellis/Desktop/Teaching/COGS18/LectureNotes-Su20
```


{:.output_stream}
```
01-Introduction.ipynb        13-CommandLine.ipynb
02-Notebooks-Variables.ipynb 14-Documentation-Style.ipynb
03-Operators.ipynb           A1-Syntax.ipynb
04-Conditionals.ipynb        A2-Examples.ipynb
05-Collections.ipynb         Check-In.ipynb
06-Loops.ipynb               [34mExam-Prep[m[m
07-Dictionaries.ipynb        LICENSE.txt
08-FunctionsI.ipynb          README.md
09-FunctionsII.ipynb         [34m__pycache__[m[m
10-Testing-Debugging.ipynb   [34mimg[m[m
11-Classes.ipynb             remote.py
12-Namespaces.ipynb

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


{:.output_stream}
```
/Users/shannonellis/Desktop/Teaching/COGS18/LectureNotes-Su20

```



{:.input_area}
```python
# relative path
# this is specific to my computer
!ls ../COGS108/Lectures-Sp20
```


{:.output_stream}
```
[34m01_data_science[m[m     [34m04_viz[m[m              [34m07_machine_learning[m[m [34m10_communication[m[m
[34m02_git_data[m[m         [34m05_analysis[m[m         [34m08_geospatial[m[m       README.md
[34m03_wrangling[m[m        [34m06_text[m[m             [34m09_pca[m[m              [34mhow_tos[m[m

```


- `..` specify you want to move one directory up in your hierarchy
- `COGS108/Lectures-Sp20` specifies the path to the directory I want to list files in
- each directory is separated with a slash (`/`)

This **relative** path does _not_ start with a leading slash (b/c it's not an absolute path).

#### Clicker Question #1

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
    

If your current working directory is `notebooks`, what is the **absolute path** to `cool_thing.py`?

- A) `/scripts/cool_thing.py`
- B) `scripts/cool_thing.py`
- C) `notebooks/scripts/cool_thing.py`
- D) `../scripts/cool_thing.py`
- E) ¯\\\_(ツ)\_/¯

#### Clicker Question #2

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


{:.output_stream}
```
/Users/shannonellis/Desktop/Teaching/COGS18/LectureNotes-Su20

```

#### Change directory



{:.input_area}
```python
# change directory 
# helpful in terminal; less helpful in notebook
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


{:.output_stream}
```
01-Introduction.ipynb        13-CommandLine.ipynb
02-Notebooks-Variables.ipynb 14-Documentation-Style.ipynb
03-Operators.ipynb           A1-Syntax.ipynb
04-Conditionals.ipynb        A2-Examples.ipynb
05-Collections.ipynb         Check-In.ipynb
06-Loops.ipynb               [34mExam-Prep[m[m
07-Dictionaries.ipynb        LICENSE.txt
08-FunctionsI.ipynb          README.md
09-FunctionsII.ipynb         [34m__pycache__[m[m
10-Testing-Debugging.ipynb   [34mimg[m[m
11-Classes.ipynb             remote.py
12-Namespaces.ipynb

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


{:.output_stream}
```
Hello World!

```

#### Print the contents of a file



{:.input_area}
```python
!cat dir_name/new_file.py
```


#### Open to see and edit contents of a file

Disclaimer: does not work on datahub



{:.input_area}
```python
!open dir_name/new_file.py
```


#### Clicker Question #3

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
!ls -l
```


{:.output_stream}
```
total 1224
-rw-r--r--   1 shannonellis  staff  17097 Jun 30 08:19 01-Introduction.ipynb
-rw-r--r--   1 shannonellis  staff  41211 Jun 30 12:24 02-Notebooks-Variables.ipynb
-rw-r--r--   1 shannonellis  staff  51129 Jul  1 12:19 03-Operators.ipynb
-rw-r--r--   1 shannonellis  staff  18574 Jul  2 11:49 04-Conditionals.ipynb
-rw-r--r--@  1 shannonellis  staff  42437 Jul 20 07:41 05-Collections.ipynb
-rw-r--r--   1 shannonellis  staff  32465 Jul  7 12:19 06-Loops.ipynb
-rw-r--r--   1 shannonellis  staff  35823 Jul  9 10:13 07-Dictionaries.ipynb
-rw-r--r--   1 shannonellis  staff  43042 Jul 14 14:01 08-FunctionsI.ipynb
-rw-r--r--   1 shannonellis  staff  41948 Jul 15 13:34 09-FunctionsII.ipynb
-rw-r--r--   1 shannonellis  staff  59922 Jul 20 12:33 10-Testing-Debugging.ipynb
-rw-r--r--   1 shannonellis  staff  46193 Jul 21 11:43 11-Classes.ipynb
-rw-r--r--   1 shannonellis  staff  26606 Jul 21 13:39 12-Namespaces.ipynb
-rw-r--r--   1 shannonellis  staff  24708 Jul 27 11:44 13-CommandLine.ipynb
-rw-r--r--   1 shannonellis  staff  43455 Jul 27 10:14 14-Documentation-Style.ipynb
-rw-r--r--   1 shannonellis  staff  13083 Jul  9 09:55 A1-Syntax.ipynb
-rw-r--r--   1 shannonellis  staff  14457 Jul  9 09:55 A2-Examples.ipynb
-rw-r--r--   1 shannonellis  staff   7242 May 15  2019 Check-In.ipynb
drwxr-xr-x  13 shannonellis  staff    416 Jul 22 12:22 [34mExam-Prep[m[m
-rw-r--r--   1 shannonellis  staff  19752 Sep 26  2019 LICENSE.txt
-rw-r--r--@  1 shannonellis  staff    457 Jul  9 12:25 README.md
drwxr-xr-x   8 shannonellis  staff    256 Jul 21 12:11 [34m__pycache__[m[m
drwxr-xr-x  15 shannonellis  staff    480 Jul  9 09:55 [34mimg[m[m
-rw-r--r--@  1 shannonellis  staff    729 Jul 21 12:13 remote.py

```

#### Clicker Question #4

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

#### Clicker Question #5

To create a file and see its contents, which command line commands would you use (and in which order)?    
   
- A) `mkdir` > `cd`
- B) `pwd` > `ls`
- C) `cd` > `pwd`
- D) `touch` > `cat`
- E) `cat` > `touch`

#### Clicker Question #6

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
