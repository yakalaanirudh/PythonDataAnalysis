#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Addition Operation on Numpy Arrays
The Addition Operation is adding a value to each element of a NumPy array. Let us see an example:
"""

import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# performing addition on each element
n1 = n1 + 10;
n2 = n2 + 20;
 
print("Array1 (updated) ", n1)
print("Array2 (updated) ", n2)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Array1 (updated)  [25 30 35 40]
Array2 (updated)  [ 85  95 105 115]

"""


# In[2]:


"""
Subtraction Operation on Numpy Arrays
The Subtraction operation is subtracting a value from each element of a NumPy array. Let us see an example:
"""

import numpy as np
 
# Create two Numpy arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# performing subtraction on each element          
n1 = n1 - 5;
n2 = n2 - 10;
 
print("Array1 (updated) ", n1)
print("Array2 (updated) ", n2)

"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Array1 (updated)  [10 15 20 25]
Array2 (updated)  [55 65 75 85]
"""


# In[3]:


"""
Multiplication Operation on Numpy Arrays
The Multiplication operation is multiplying a value to each element of a NumPy array. Let us see an example:
"""
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# performing multiplication on each element          
n1 = n1 * 5;
n2 = n2 * 10;
 
print("Array1 (updated) ", n1)
print("Array2 (updated) ", n2)
 
"""
Output

Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Array1 (updated)  [ 75 100 125 150]
Array2 (updated)  [650 750 850 950]
"""


# In[4]:


"""
Division Operation on Numpy Arrays
The Division operation is to divide a value from each element of a  NumPy array. Let us see an example:
"""

 
import  numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# performing division on each element
n1 = n1 / 5;
n2 = n2 / 5;
 
print("Array1 (updated) ", n1)
print("Array2 (updated) ", n2)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Array1 (updated)  [3. 4. 5. 6.]
Array2 (updated)  [13. 15. 17. 19.]
"""


# In[ ]:




