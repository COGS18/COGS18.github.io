#!/usr/bin/env python
# coding: utf-8

# ### Module Import

# In[1]:


import airline as air

group = []
Aticket = air.PlaneTicket('Bob', 'Delta', 'business', '7A', 'Barbados')
Bticket = air.PlaneTicket('Sally', 'Southwest', 'first', '1B', 'Seattle')
Cticket = air.PlaneTicket('Ashley', 'United', 'economy', '34A', 'New York')
Dticket = air.PlaneTicket('Josh', 'Emirates', 'economy', '17C', 'Dubai')
group.extend([Aticket, Bticket, Cticket ,Dticket])

air.group_tickets(group)


# In[2]:


air.group_destination(group)


# ### Script Execution

# In[3]:


get_ipython().system('python new_airline.py')

