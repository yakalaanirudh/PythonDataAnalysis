#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
To find the difference between two arrays, use the numpy.setdiff1d() method. 
This means if we are subtracting two arrays, then setdiff1d() will subtract 
the common elements from the 1st array and display the rest of the elements of the 1st array.

setdiff1d(array1, array2)

"""


# In[3]:


import numpy as np
 
# Create two arrays
n1 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
n2 = np.array([30, 35, 50, 55, 60, 65, 75, 85, 95, 100])
 
print("Iterating array1...")
for a in n1:
    print(a)
 
print("\nIterating array2...")
for a in n2:
    print(a)
 
# n1 - n2
diffarr = np.setdiff1d(n1, n2)
print("\nDifference = \n", diffarr)
 
"""
Output
 
Iterating array1...
5
10
15
20
25
30
35
40
45
50
 
Iterating array2...
30
35
50
55
60
65
75
85
95
100
 
Difference = 
 [ 5 10 15 20 25 40 45]
"""


# In[4]:


import numpy as np
 
# Create two arrays
n1 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
n2 = np.array([30, 35, 50, 55, 60, 65, 75, 85, 95, 100])
 
print("Iterating array1...")
for a in n1:
    print(a)
 
print("\nIterating array2...")
for a in n2:
    print(a)
 
# Get the difference 
resarr = np.setdiff1d(n2, n1)
print("\nDifference = \n", resarr)
 

    
"""
Output

 
Iterating array1...
5
10
15
20
25
30
35
40
45
50
 
Iterating array2...
30
35
50
55
60
65
75
85
95
100
 
Difference = 
 [ 55  60  65  75  85  95 100]
"""
 


# In[ ]:




