#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mean
#Mean is the average of the given values. Here, we will find the mean of the array elements using the mean() method.

import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# mean
resmean1 = np.mean(n1);
resmean2 = np.mean(n2);
 
print("\nArray1 mean = ", resmean1)
print("Array2 mean = ", resmean2)

"""
Output 

Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
 
Array1 mean =  22.5
Array2 mean =  80.0
"""


# In[2]:


#Median
#Median is the middle value of the given values. 
#Here, we will find the median of the array elements using the median() method.
 
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# median
resmedian1 = np.median(n1);
resmedian2 = np.median(n2);
 
print("\nArray1 median = ", resmedian1)
print("Array2 median = ", resmedian2)
 
"""
Output

Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
 
Array1 median =  22.5
Array2 median =  80.0
"""


# In[3]:


#Standard Deviation
#Standard Deviation is a measure of the amount of variation or dispersion of the given values. 
#Here, we will find the standard deviation of the array elements using the std() method.

 
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# standard deviation
resstd1 = np.std(n1);
resstd2 = np.std(n2);
 
print("\nArray1 Standard Deviation = ", resstd1)
print("Array2 Standard Deviation = ", resstd2)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
 
Array1 Standard Deviation =  5.5901699437494745
Array2 Standard Deviation =  11.180339887498949
"""

 


# In[ ]:




