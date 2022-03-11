#!/usr/bin/env python
# coding: utf-8

# In[1]:


import playlist as pl

# YOUR CODE HERE
new_playlist = pl.Playlist('Anime')
new_playlist.add_song({'Departure' : 'jfkj'})
new_playlist.song_list


# In[3]:


your_playlist = pl.Playlist('100% worry free')
your_playlist.add_song({'Magic!' : 'MAZE1981'})
your_playlist.add_song({'Count What You Have Now' : 'Vantage'})
your_playlist.add_song({'Lean on Me' : 'Bill Withers'})
your_playlist.add_song({'Are You Ready(On Your Own)' : 'Distant Cousins'})
your_playlist.add_song({'Mayonaka no Door / Stay With Me' : 'Miki Matsubara'})
your_playlist.add_song({"Can't Tale My Eyes off You" : 'Frankie Valli'})
your_playlist.song_list


# In[4]:


get_ipython().system('python playlist_script.py')

