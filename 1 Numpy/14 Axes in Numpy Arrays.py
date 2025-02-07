#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
vertical axis (axis 0)
horizontal axis (axis 1)
"""


# In[2]:


import numpy as np
 
# Create a numpy 3x5 array
n = np.array([[2, 5, 7, 9, 6], [15, 25, 35, 45, 55], [100, 200, 300, 400, 500]])
 
print("Iterating 2D array...")
for a in n:
    print(a)
 
print("\nMinimum value = ", n.min())
print("\nMinimum value with axis 0 (vertical axes) = ", n.min(axis=0))
print("\nMinimum value with axis 1 (horizontal axes) = ", n.min(axis=1))


"""
Iterating 2D array...
[2 5 7 9 6]
[15 25 35 45 55]
[100 200 300 400 500]
 
Minimum value =  2
 
Minimum value with axis 0 (vertical axes) =  [2 5 7 9 6]
 
Minimum value with axis 1 (horizontal axes) =  [  2  15 100]

"""


# In[ ]:




