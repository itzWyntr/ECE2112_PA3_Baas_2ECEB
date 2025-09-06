#!/usr/bin/env python
# coding: utf-8

# # PA 3

# In[2]:


import pandas as pd

cars = pd.read_csv('cars.csv')
cars


# ## Problem 2

# a. Display First 5 odd number columns

# In[16]:


odd_num_rows = cars.iloc[:,::2]
odd_num_rows


# b. Display the row of the model "Mazda RX4"

# In[14]:


cars.loc[cars['Model'] == 'Mazda RX4']


# c. How many cylinders does Camaro Z28 have?

# In[23]:


cam_cyl = cars.loc[cars['Model']== 'Camaro Z28','cyl'].iloc[0]

print("Cylinders of Camaro Z28: ",cam_cyl)


# d. how many cylinders and what gear type do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have?

# In[ ]:


Mazda = cars.loc[cars["Model"]== 'Mazda RX4 Wag', ['Model','cyl', 'gear']] 
Ford = cars.loc[cars["Model"]== 'Ford Pantera L', ['Model','cyl', 'gear']]
Honda = cars.loc[cars["Model"]== 'Honda Civic', ['Model','cyl', 'gear']]

print("The car's gears and cylinders are: ")
pd.concat([Mazda, Ford, Honda])


# In[ ]:




