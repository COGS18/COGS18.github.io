#!/usr/bin/env python
# coding: utf-8

# In[1]:


import diary_module as dm

new_diary = dm.Diary()
new_diary.diary_entry('first entry')
new_diary.entries
dm.read_diary(new_diary)
dm.create_diary()


# In[2]:


get_ipython().system('python script.py')

