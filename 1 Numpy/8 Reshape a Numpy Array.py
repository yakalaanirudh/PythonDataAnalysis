#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
when reshaping an array in NumPy using .reshape(), 
the total number of elements must remain the same. 
This means that all elements from the original array must be used in the reshaped array, 
and no extra elements can be introduced or left out.

"""


# In[2]:


import numpy as np
 
# Create a Numpy array
n = np.array([5, 10, 15, 20, 25, 30])
print("One-Dimensional Array = ",n)
 
# Reshape the array
resarr = n.reshape(2, 3)
 
print("Reshaped array (Two-Dimensional) = \n",resarr)


"""
One-Dimensional Array =  [ 5 10 15 20 25 30]
Reshaped array (Two-Dimensional) = 
 [[ 5 10 15]
 [20 25 30]]
"""


# In[3]:


import numpy as np
 
# Create a 3D array
n = np.array([[[5, 10, 15],[20, 25, 30]],[[35, 40, 45],[50, 55, 60]]])
print("3D array = \n ",n)
 
# Reshape the array
resarr = n.reshape(-1)
print("\nReshaped to 1D array = ",resarr)

"""
3D array = 
  [[[ 5 10 15]
  [20 25 30]]
 
 [[35 40 45]
  [50 55 60]]]
 
Reshaped to 1D array =  [ 5 10 15 20 25 30 35 40 45 50 55 60]
"""


# In[ ]:




