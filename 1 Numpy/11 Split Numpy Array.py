#!/usr/bin/env python
# coding: utf-8

# In[4]:


# In split axis 0 is vertical and axis 1 is horizaontal
#array_split(arr_name, split_num)

import numpy as np
 
# Create a Numpy array
n = np.array([10, 20, 30, 40, 50, 60])
 
print("Iterating array...")
for a in n:
    print(a)
 
# splitting array into 2
resarr = np.array_split(n, 2)
 
print("\nArray after splitting i.e. returns 2 arrays");
for a in resarr:
    print(a)
    
"""
Iterating array...
10
20
30
40
50
60
 
Array after splitting i.e. returns 2 arrays
[10 20 30]
[40 50 60]
"""


# In[2]:


import numpy as np
 
n = np.array([10, 20, 30, 40, 50, 60])
 
print("Iterating array...")
for a in n:
  print(a)
 
# splitting into 2
# The resultsant two arrays are stored in a list with two arrays at first two indices
resarr = np.array_split(n, 2)
 
print("\nArray after splitting i.e. returns 2 arrays");
print(resarr)
 
print("\nAccess splitted array individually...");
print("Array1 = ",resarr[0])
print("Array2 = ",resarr[1])

print("Array1 Dimensions = ",resarr[0].ndim)
print("Array2 Dimensions = ",resarr[1].ndim)
"""
Iterating array...
10
20
30
40
50
60
 
Array after splitting i.e. returns 2 arrays
[array([10, 20, 30]), array([40, 50, 60])]
 
Access splitted array individually...
Array1 =  [10 20 30]
Array2 =  [40 50 60]
"""


# In[3]:


"""
Split a 2D array and access
The split result will be a 2D array, for example, if a 2D array is split into two, there will be two 2D arrays as a result
"""
import  numpy as np
 
n = np.array([[1,3,5],[4,8,12]])
 
print("Iterating array...")
for a in n:
 print(a)
 
# splitting into 2
# Each part is still a 2D array with shape (1,3).
# resarr is a list containing the split arrays.
# The two 2D arrays are stored in indices 0 and 1 of a list
resarr = np.array_split(n, 2)
 
print("\nArray after splitting (returns 2 arrays)");
print(resarr)
 
print("\nAccess splitted array individually...");
print("Array1 = ",resarr[0])
print("Array2 = ",resarr[1])

print("Array1 Dimensions = ",resarr[0].ndim)
print("Array2 Dimensions = ",resarr[1].ndim)

# Print each element of the 2d array
print(resarr[0][0, 0])
print(resarr[0][0, 1])
print(resarr[0][0, 2])


print(resarr[1][0, 0])
print(resarr[1][0, 1])
print(resarr[1][0, 2])
"""
Iterating array...
[1 3 5]
[ 4  8 12]
 
Array after splitting (returns 2 arrays)
[array([[1, 3, 5]]), array([[ 4,  8, 12]])]
 
Access splitted array individually...
Array1 =  [[1 3 5]]
Array2 =  [[ 4  8 12]]
"""


# In[ ]:




