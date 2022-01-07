#!/usr/bin/env python
# coding: utf-8

# ### Module Import

# In[1]:


from twentiethx import ducklings_race


# In[2]:


bark = ducklings_race()
bark.add_duckling('Donald', 5, 'aka Mr. Duck')
bark.add_duckling('Daisy', 7, 'aka Mrs. Duck')
bark.add_duckling('Mickey', 2, 'not a duck, but it is fine')
print(bark.roster)
bark.winner()


# ### Script Execution

# In[3]:


get_ipython().system('python twentiethx_script.py')

