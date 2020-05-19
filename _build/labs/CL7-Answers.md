---
interact_link: content/labs/CL7-Answers.ipynb
download_link: assets/downloads/CL7-Answers.ipynb.zip
layout: notebooks
title: 'CL7-Answers'
prev_page:
  url: /labs/CL6-Answers
  title: 'CL6-Answers'
next_page:
  url: /labs/CL8-ProjectOverview
  title: 'CL8-ProjectOverview'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# CL7: Command Line

Welcome to the seventh coding lab!

In this CodingLab we will be working with the command line, and with python files (module files and scripts). 

While this _may_ feel like busy work, understanding and completing this coding lab will be essential when it comes time for your project. Do your very best to complete all parts of this CodingLab!

## Part I: Command Line

Open a terminal from the Jupyter notebook server (either on your local computer or datahub), and do the following:

- Navigate to your desktop (or home directory on datahub)
- Make a new directory
- Move inside that directory
- Create a new Python file
- Inside your terminal, use a text editor to open the file
- Write some Python code inside that file
    - For example: print('Hello World')
- Save and exit from the terminal text editor
- Execute the Python file from the terminal

Describe your success/struggles/failures with the above steps here:


## Part II: Module Files

First, in notebook below, do the following:

- Write a new Class, and two derived classes that inherit from this base Class
    - This could be, for example, base class `Animal` and derived classes `Cat` and `Dog`
    - Make sure there is at least one method in the class that prints something out
- Write two new functions, that do something with instances of your new classes
    - For example, take a list of custom objects, and call a method on each one

### Student Example: Emma Garcia



{:.input_area}
```python
# Classes here
class Academics(): 
    
    def __init__(self, study = None, grades = None):
        self.study = study
        self.grades = grades
        
    def print_info(self):
        study_string = ''
        grades_string = ''
        if self.study == None:
            study_string = 'nothing'
        else:
            study_string = self.study
            
        if self.grades == None:
            grades_string = 'Schrödingers grade'
        else:
            grades_string = self.grades
            
        print('I studied ' + study_string + ' and my grade is ' + grades_string + '.')
```




{:.input_area}
```python
# New functions here
def report_card(student):
    if student.grades in passing_grades:
        print('you shall pass.')
    else:
        print('you shall not pass.')

def change_major(student, major):
    if major in new_majors:
        student.study = major 
        student.grades = 'reset'
    else:
        print('denied')
```


{:.output_stream}
```
you shall not pass.
denied
I studied psychology and my grade is atrocious.
I studied Gender Studies and my grade is reset.

```

Emma then stored two files in the same folder as their notebook:
- `derrrp.py` : stored `Academics`, `change_major`, and `report_card`
- `Academics` & `change_major` are imported and used below
- The following cell will not run if you don't create the module with the same name




{:.input_area}
```python
from derrrp import Academics, change_major
```




{:.input_area}
```python
print("Jim Example")
Jim = Academics(study = 'psychology', grades = 'atrocious')
change_major(Jim, 'bio')
Jim.print_info()

print('\nJess Example')
Jess = Academics(study = 'math', grades = 'good')
change_major(Jess, 'Gender Studies')
Jess.print_info()
```


{:.output_stream}
```
Jim Example
denied
I studied psychology and my grade is atrocious.

Jess Example
No change
I studied Gender Studies and my grade is reset.

```

Next, we are going to move this code to an external file - a Python module file. 

- Open a new text file, from the Jupyter server page
- Copy your classes and functions into that file
- Save that file, with some name that you give it, and a '.py' extension
- Now, import the classes and functions from that file into the notebook, and check that you can use them. 



{:.input_area}
```python
import ...
```


## Part III: Python Scripts

Now write a small script that imports from your module file, and uses that code to do something.

To do so, start with the new text file. It should import your classes and functions from the file you made above. Then, use these functions and classes to do something (write some Python code that does something with these objects). Save your file with a '.py' extension, and then execute it from the terminal.

Explain your success/struggles/failures with the above here:
