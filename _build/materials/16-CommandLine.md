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

## Course Announcements

- Exam 2 *next* Wednesday (11/13)
- A4 due *next* Friday 11/15 (11:59 PM)

## Exam Plan (60 points)

Part I: Variables & Operators (6 points)  
Part II: Indexing (4 points)  
Part III: Control Flow - Conditionals & Loops (4 points)  
Part IV: **Functions** (27 points)  
Part V: **Objects & Classes** (12 points)  
Part VI: True/False (7 points)  



# Command Line & Scripts

- command line & shell commands
- file paths (absolute and relative)
- scripts and modules

If you remember demos from the first day of class, I didn't use Jupyter Notebooks.

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
/Users/shannonellis/Desktop/Teaching/COGS18/Materials

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


{:.output_stream}
```
00-Introduction.ipynb        23-CodeProjects.ipynb
01-Tools.ipynb               24-AdvancedPython.ipynb
02-JupyterNotebooks.ipynb    25-WrapUp.ipynb
03-Variables.ipynb           A1-Syntax.ipynb
04-Operators.ipynb           A2-Examples.ipynb
05-Conditionals.ipynb        Check-In.ipynb
06-DataTypes.ipynb           E1-Answers.ipynb
07-Loops.ipynb               E2-Answers.ipynb
08-Encodings.ipynb           Exam1-Practice.ipynb
09-FunctionsI.ipynb          Exam1-Review.ipynb
10-Algorithms.ipynb          Exam2-Review.ipynb
11-FunctionsII.ipynb         Exam2_Practice.ipynb
12-Debugging.ipynb           LICENSE.txt
13-Objects.ipynb             Midterm.ipynb
14-Classes.ipynb             PythonParty.ipynb
15-Namespaces.ipynb          README.md
16-CommandLine.ipynb         Untitled.ipynb
17-APIs.ipynb                XX-Extra-Clicker-Qs.ipynb
18-ScientificComputing.ipynb [34m__pycache__[m[m
19-OpenSource.ipynb          [34mimg[m[m
20-Documentation.ipynb       [34mmy_module[m[m
21-CodeStyle.ipynb           remote.py
22-CodeTesting.ipynb         stw.py

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
/Users/shannonellis/Desktop/Teaching/COGS18/Materials

```



{:.input_area}
```python
# relative path
# this is specific to my computer
!ls ../COGS108/Lectures-Sp19
```


{:.output_stream}
```
01_intro_ethics.pdf               15_machine_learning.pdf
02_version_control.pdf            16_ml_examples.pdf
03_data.pdf                       17_machine_learning.ipynb
[34m04_data_wrangling[m[m                 18_geospatial.pdf
04_data_wrangling.pdf             19_geospatial.ipynb
04_data_wrangling.zip             20_Nonparametric.pdf
05_dataviz.pdf                    21_dimensionality_reduction.pdf
[34m06_datavizII[m[m                      22_dimensionality_reduction.ipynb
07_analysis.pdf                   23_future.pdf
[34m08_descriptive[m[m                    EDA_CaseStudy_12PM.pdf
09_EDA.ipynb                      EDA_CaseStudy_2PM.pdf
10_inference.pdf                  Inference_CaseStudy_12PM.pdf
11_regression.ipynb               Inference_CaseStudy_2PM.pdf
12_correlation.ipynb              README.md
13_binary.ipynb                   XX_Guest_Merchant.pdf
13_text.pdf                       [34mimg[m[m
14_text.ipynb

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
    

What is the **absolute path** to `cool_thing.py`?

- A) `/scripts/cool_thing.py`
- B) `scripts/cool_thing.py`
- C) `/root/scripts/cool_thing.py`
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


{:.output_stream}
```
/Users/shannonellis/Desktop/Teaching/COGS18/Materials

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


{:.output_stream}
```
00-Introduction.ipynb        23-CodeProjects.ipynb
01-Tools.ipynb               24-AdvancedPython.ipynb
02-JupyterNotebooks.ipynb    25-WrapUp.ipynb
03-Variables.ipynb           A1-Syntax.ipynb
04-Operators.ipynb           A2-Examples.ipynb
05-Conditionals.ipynb        Check-In.ipynb
06-DataTypes.ipynb           E1-Answers.ipynb
07-Loops.ipynb               E2-Answers.ipynb
08-Encodings.ipynb           Exam1-Practice.ipynb
09-FunctionsI.ipynb          Exam1-Review.ipynb
10-Algorithms.ipynb          Exam2-Review.ipynb
11-FunctionsII.ipynb         Exam2_Practice.ipynb
12-Debugging.ipynb           LICENSE.txt
13-Objects.ipynb             Midterm.ipynb
14-Classes.ipynb             PythonParty.ipynb
15-Namespaces.ipynb          README.md
16-CommandLine.ipynb         Untitled.ipynb
17-APIs.ipynb                XX-Extra-Clicker-Qs.ipynb
18-ScientificComputing.ipynb [34m__pycache__[m[m
19-OpenSource.ipynb          [34mimg[m[m
20-Documentation.ipynb       [34mmy_module[m[m
21-CodeStyle.ipynb           remote.py
22-CodeTesting.ipynb         stw.py

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

To create a file and see its contents, which commands and in which order would you use?    
   
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
