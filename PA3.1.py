#!/usr/bin/env python
# coding: utf-8

# # PA 3 - Pandas

# In[1]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# ## Problem 1

# In[2]:


display = pd.concat([cars.iloc[0:5],cars.iloc[27:32]])
print("The first and last 5 cars are:")
display


# In[ ]:




