---
download_link: assets/downloads/02-JupyterNotebooks.ipynb.zip
title: '02-jupyternotebooks'
permalink: '/chapters/02-JupyterNotebooks'
previouschapter:
  url: /chapters/01-Tools
  title: '01-tools'
nextchapter:
  url: 
  title: ''
redirect_from:
  - '/chapters/02-jupyternotebooks'
---

# Jupyter Notebooks

This is a quick introduction to Jupyter notebooks.

<div class="alert alert-success">
Jupyter notebooks are a way to combine executable code, code outputs, and text into one connected file.
</div>

<div class="alert alert-info">
The official documentation from project Jupyter is available 
<a href="https://jupyter-notebook.readthedocs.io/en/stable/" class="alert-link">here</a>
and they also have some example notebooks 
<a href="https://github.com/jupyter/notebook/tree/master/docs/source/examples/Notebook" class="alert-link">here</a>
.
</div>

## Menu Options & Shortcuts

To get a quick tour of the Jupyter user-interface, click on the 'Help' menu, then click 'User Interface Tour'.

There are also a large number of useful keyboard shortcuts. Click on the 'Help' menu, and then 'Keyboard Shortcuts' to see a list. 

## Cells

<div class="alert alert-success">
The main organizational structure of the notebook are 'cells'.
</div>

Cells, can be markdown (text), like this one.



{:.input_area}
```python
# Cell can also be code. Here, we are using a Python notebook.
a = 1
b = 2
```




{:.input_area}
```python
# Cells can also have output, that gets printed out below the cell.
print(a + b)
```


{:.output_stream}
```
3

```

## Accessing Documentation

<div class="alert alert-success">
Jupyter has useful shortcuts. Add a single '?' after a function or class get a window with the documentation, or a double '??' to pull up the source code. 
</div>



{:.input_area}
```python
# Import numpy for examples
import numpy as np
```




{:.input_area}
```python
# Check the docs for a numpy array
np.array?
```




{:.input_area}
```python
# Check the full source code for numpy append function
np.append??
```


## Autocomplete

<div class="alert alert-success">
Jupyter also has 
<a href="https://en.wikipedia.org/wiki/Command-line_completion" class="alert-link">tab complete</a>
capacities, which can autocomplete what you are typing, and/or be used to explore what code is available.  
</div>



{:.input_area}
```python
# Move your cursor just after the period, press tab, and a drop menu will appear showing all possible completions
np.
```




{:.input_area}
```python
# Autocomplete does not have to be at a period. Move to the end of 'ra' and hit tab to see completion options. 
ra
```




{:.input_area}
```python
# If there is only one option, tab-complete will auto-complete what you are typing
ran
```


## Kernel & Namespace

You do not need to run cells in order! This is useful for flexibly testing and developing code. 

The numbers in the square brackets to the left of a cell show which cells have been run, and in what order.

However, it can also be easy to lose track of what has already been declared / imported, leading to unexpected behaviour from running cells.

The kernel is what connects the notebook to your computer behind-the-scenes to execute the code. 

It can be useful to clear and re-launch the kernel. You can do this from the 'kernel' drop down menu, at the top, optionally also clearing all ouputs.

## Magic Commands

<div class="alert alert-success">
'Magic Commands' are a special (command-line like) syntax in IPython/Jupyter to run special functionality. They can run on lines and/or entire cells. 
</div>

<div class="alert alert-info">
The iPython <a href="http://ipython.readthedocs.io/en/stable/interactive/magics.html" class="alert-link">documentation</a> has more information on magic commands.
</div>



{:.input_area}
```python
# You can check a list of available magic commands
%lsmagic
```


### Line Magics


Line magics use a single '%', and apply to a single line. 



{:.input_area}
```python
# For example, we can time how long it takes to create a large list
%timeit list(range(100000))
```


### Cell Magics

Cell magics use a double '%%', and apply to the whole cell. 



{:.input_area}
```python
%%timeit
# For example, we could time a whole cell
a = list(range(100000))
b = [n + 1 for n in a]
```


### Running terminal commands

Another nice thing about notebooks is being able to run terminals commands



{:.input_area}
```python
# You can run a terminal command by adding '!' to the start of the line
!pwd

# Note that in this case, '!pwd' is equivalent to line magic '%pwd'. 
# The '!' syntax is more general though, allowing you to run anything you want through command-line 
```




{:.input_area}
```bash
%%bash
# Equivalently, (for bash) use the %%bash cell magic to run a cell as bash (command-line)
pwd
```


<div class="alert alert-info">
For more useful information, check out Jupyter Notebooks 
<a href="https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/" class="alert-link">tips & tricks</a>
, and more information on how 
<a href="http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html" class="alert-link">notebooks work</a>.
</div>
