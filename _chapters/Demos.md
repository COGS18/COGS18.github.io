---
title: 'Demos'
permalink: '/chapters/Demos'
previouschapter:
  url: /chapters/01-Introduction
  title: '01-introduction'
nextchapter:
  url: /chapters/ProgrammingIsForHumans
  title: 'Programmingisforhumans'
redirect_from:
  - '/chapters/demos'
---



{:.input_area}
```python
!source activate eeg36

import mne
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ModuleNotFoundError                       Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-2-fa9c19412b49> in <module>()
      1 get_ipython().system('source activate eeg36')
      2 
----> 3 import mne

```

{:.output_traceback_line}
```
ModuleNotFoundError: No module named 'mne'
```




{:.input_area}
```python
!source deactivate

import mne
```




{:.input_area}
```python
!conda info --envs
```


{:.output_stream}
```
# conda environments:
#
base                  *  /Users/tom/anaconda
dev_fooof                /Users/tom/anaconda/envs/dev_fooof
eeg35                    /Users/tom/anaconda/envs/eeg35
eeg36                    /Users/tom/anaconda/envs/eeg36
fooof                    /Users/tom/anaconda/envs/fooof
grade                    /Users/tom/anaconda/envs/grade
mpl36                    /Users/tom/anaconda/envs/mpl36
mvpa                     /Users/tom/anaconda/envs/mvpa
present                  /Users/tom/anaconda/envs/present
py27                     /Users/tom/anaconda/envs/py27
py36                     /Users/tom/anaconda/envs/py36
scrape                   /Users/tom/anaconda/envs/scrape
strm                     /Users/tom/anaconda/envs/strm
task                     /Users/tom/anaconda/envs/task
textbook                 /Users/tom/anaconda/envs/textbook
wonam                    /Users/tom/anaconda/envs/wonam


```



{:.input_area}
```python
!which python
```


{:.output_stream}
```
/Users/tom/anaconda/bin/python

```



{:.input_area}
```python
import mne
```



{:.output_traceback_line}
```
---------------------------------------------------------------------------
```

{:.output_traceback_line}
```
ModuleNotFoundError                       Traceback (most recent call last)
```

{:.output_traceback_line}
```
<ipython-input-1-39fc8b1a8697> in <module>()
----> 1 import mne

```

{:.output_traceback_line}
```
ModuleNotFoundError: No module named 'mne'
```




{:.input_area}
```python
# Note: generate pictures & sounds
```

