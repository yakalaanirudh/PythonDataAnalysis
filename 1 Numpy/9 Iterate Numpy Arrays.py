#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
 
# Create a Numpy 1D array
n = np.array([5, 10, 15, 20, 25, 30])
print("One-Dimensional Array = ",n)
print("Type = ",type(n))
print("DataType = ",n.dtype)
 
print("\nIterating...")
for a in n:
  print(a)

"""
One-Dimensional Array =  [ 5 10 15 20 25 30]
Type =  <class 'numpy.ndarray'>
DataType =  int32
 
Iterating...
5
10
15
20
25
30
"""


# In[2]:


import numpy as np
 
# Create a Numpy 2D array
n = np.array([[5, 10], [15, 20], [25, 30]])
print("Two-Dimensional Array = \n", n)
print("Type = ", type(n))
print("DataType = ", n.dtype)
 
print("\nIterating...")
for a in n:
    print(a)
    
"""

Two-Dimensional Array = 
 [[ 5 10]
 [15 20]
 [25 30]]
Type =  <class 'numpy.ndarray'>
DataType =  int32
 
Iterating...
[ 5 10]
[15 20]
[25 30]
"""    


# In[3]:


import numpy as np
 
# Create a Numpy 3D array
n = np.array([[[5, 10], [15, 20]], [[25, 30], [35, 40]]])
print("Three-Dimensional Array = \n",n)
print("Dimensions = ",n.ndim)
print("Type = ",type(n))
print("DataType = ",n.dtype)
 
print("\nIterating...")
for a in n:
  print("Each matrix (2D)=")
  print(a)
    
"""
Three-Dimensional Array = 
 [[[ 5 10]
  [15 20]]
 
 [[25 30]
  [35 40]]]
Dimensions =  3
Type =  <class ' numpy.ndarray'>
DataType =  int32
 
Iterating...
Each matrix (2D)=
[[ 5 10]
 [15 20]]
Each matrix (2D)=
[[25 30]
 [35 40]]
 
"""


# In[ ]:




