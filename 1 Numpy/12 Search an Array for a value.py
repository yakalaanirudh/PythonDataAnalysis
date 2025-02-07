#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Search a Numpy Array for a value
import numpy as np
 
# Create a Numpy Array
n = np.array([10, 20, 30, 40, 50, 30])
 
print("Iterating array...")
for a in n:
    print(a)
 
# Searching a specific value 30
res = np.where(n == 30)
 
print("\nElement 30 found at following indexes:")
print(res)

"""
Iterating array...
10
20
30
40
50
30
 
Element 30 found at following indexes:
(array([2, 5], dtype=int64),)
"""


# In[ ]:




