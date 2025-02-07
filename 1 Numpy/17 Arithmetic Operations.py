#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Add the elements of Numpy arrays
 
import numpy as np
 
# Create arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Add the arrays elements
resarr = np.sum([n1, n2])
print("Sum = ", resarr)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Sum =  410
"""


# In[2]:


#Add column values using the axis parameter

 
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Add column values using axis parameter
resarr = np.sum([n1, n2], axis=0)
print("Sum = ", resarr)

"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Sum =  [ 80  95 110 125]
"""


# In[3]:


#Add individual array values using the axis parameter

 
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Add individual array values using axis parameter
resarr = np.sum([n1, n2], axis=1)
print("Sum result= ", resarr)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Sum result=  [ 90 320]
"""


# In[4]:


"""
Subtract Numpy arrays
Use the subtract() method to subtract one array from another. 
It subtracts and displays the result in a new array. Let us see an example to subtract NumPy arrays:

"""
 
import numpy as np
 
# Create two arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Subtract Numpy arrays
resarr = np.subtract(n1, n2)
print("Subtraction result = ", resarr)
 
"""
Output
 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Subtraction result =  [-50 -55 -60 -65]
"""


# In[5]:


"""
Multiply Numpy arrays
Use the multiply() method to multiply elements of one array to another. 
It multiplies and displays the result in a new array.
""" 

 
import numpy as np
 
# Create Numpy arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Multiply Numpy arrays
resarr = np.multiply(n1, n2)
print("Multiplication result = ", resarr)

"""
Output

 
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Multiplication result =  [ 975 1500 2125 2850]
"""


# In[6]:


"""
Divide Numpy arrays
The divide() method divides elements of one array with elements of another. 
It divides and displays the result in a new array. Let us see an example to divide NumPy arrays:

"""
import numpy as np
 
# Create two Numpy arrays
n1 = np.array([15, 20, 25, 30])
n2 = np.array([65, 75, 85, 95])
 
print("Array1 =", n1)
print("Array2 =", n2)
 
# Divide arrays
resarr = np.divide(n2, n1)
print("Division Result = ", resarr)
 
"""
Output
Array1 = [15 20 25 30]
Array2 = [65 75 85 95]
Division Result =  [4.33333333 3.75       3.4        3.16666667]
"""


# In[ ]:




