#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Find the intersection between two arrays
The intersect1d() method finds the intersection between two arrays. 

"""

import numpy as np
 
# Create two arrays
n1 = np.array([5, 10, 15, 20])
n2 = np.array([5, 15, 30, 40])
 
print("Iterating array1...")
for a in n1:
    print(a)
 
print("\nIterating array2...")
for a in n2:
    print(a)
 
# Find intersection using the intersect1d() method
resarr = np.intersect1d(n1, n2)
print("\nIntersection = \n", resarr)
 
"""
Output

Iterating array1...
5
10
15
20
 
Iterating array2...
5
15
30
40
 
Intersection = 
 [ 5 15]
 
"""

 


# In[3]:


"""
The intersect1d() method finds the intersection and also sorts the result

"""

import numpy as np
 
# Create two arrays
n1 = np.array([10, 50, 30, 20, 60, 40])
n2 = np.array([80, 50, 90, 100, 40, 70])
 
print("Iterating array1...")
for a in n1:
    print(a)
 
print("\nIterating array2...")
for a in n2:
    print(a)
 
# Find the intersection
resarr = np.intersect1d(n1, n2)
print("\nIntersection (sorted result) = \n", resarr)


"""
Output
 
Iterating array1...
10
50
30
20
60
40
 
Iterating array2...
80
50
90
100
40
70
 
Intersection (sorted result) = 
 [40 50]

"""


# In[4]:


# When no Intersection between arrays
import  numpy as np
 
# Create two arrays
n1 = np.array([10, 20, 30, 40, 50])
n2 = np.array([60, 70, 80, 90, 100])
 
print("Iterating array1...")
for a in n1:
    print(a)
 
print("\nIterating array2...")
for a in n2:
    print(a)
 
# Find the intersection
resarr = np.intersect1d(n1, n2)
print("\nIntersection (different elements) = \n", resarr)
 
"""
Output

 
Iterating array1...
10
20
30
40
50
 
Iterating array2...
60
70
80
90
100
 
Intersection (different elements) = 
 []

"""


# In[ ]:




