#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sort a 1D Numpy Integer array
import numpy as np
 
# Create a 1D integer array
n = np.array([50, 25, 35, 15, 55, 75, 65, 60, 30, 45])
 
print("Iterating array...")
for a in n:
    print(a)
 
# Sort the array using the sort() method
print("\nSorted array = ", np.sort(n))

"""
Iterating array...
50
25
35
15
55
75
65
60
30
45
 
Sorted array =  [15 25 30 35 45 50 55 60 65 75]
"""


# In[2]:


#Sort a 1D Numpy string array
import numpy as np
 
# Create a Numpy strungs array
n = np.array(['java', 'keras', 'android', 'express', 'jquery'])
 
print("Iterating array...")
for a in n:
    print(a)
 
# Sort the array
print("\nSorted array = ", np.sort(n))


"""
Iterating array...
java
keras
android
express
jquery
 
Sorted array =  ['android' 'express' 'java' 'jquery' 'keras']

"""


# In[3]:


#Sort a 2D array

import numpy as np
 
# Create Numpy 2d array
n = np.array([[5, 3, 7, 9, 6], [15, 25, 13, 20, 12]])
 
print("Iterating 2D array...")
for a in n:
    print(a)
 
# Sort the array
print("\nSorted 2D array =\n ", np.sort(n))

"""
Iterating 2D array...
[5 3 7 9 6]
[15 25 13 20 12]
 
Sorted 2D array =
  [[ 3  5  6  7  9]
 [12 13 15 20 25]]
"""


# In[ ]:




