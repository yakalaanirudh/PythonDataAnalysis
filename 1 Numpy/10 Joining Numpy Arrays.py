#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
In NumPy, the concatenate function is used to join two or more arrays along an existing axis. 
It can combine arrays with the same number of dimensions along a specified axis.
Here's the general syntax:

numpy.concatenate((array1, array2, ...), axis=0, out=None)

Parameters:
arrays: A sequence of arrays (e.g., list or tuple) to be concatenated. 
All arrays should have the same shape, except in the dimension corresponding to the axis along 
which they will be concatenated.
axis: The axis along which the arrays will be joined. 
The default is 0, meaning the arrays are stacked along the first axis (rows for 2D arrays).
out: An optional output array in which to place the result. If not specified, a new array is created.
"""

import numpy as np

# Create two 1D arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Concatenate them along axis 0 (default)
result = np.concatenate((array1, array2))
print(result)

"""
[1 2 3 4 5 6]

"""


# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Concatenate along axis 1 (columns)
result = np.concatenate((array1, array2), axis=1)
print(result)


"""
[[1 2 5 6]
 [3 4 7 8]]

"""


# In[3]:


"""
np.stack()
The stack function joins arrays along a new axis. 
This means that a new axis is created in the resulting array, 
and the input arrays are stacked along that axis. 
The number of dimensions of the resulting array increases by 1.


numpy.stack(arrays, axis=0, out=None)

arrays: Sequence of arrays to stack.
axis: The axis along which the arrays will be stacked. 
The default is 0, meaning the new axis will be added at the beginning (making the arrays stacked vertically).

"""

import numpy as np

array1 = np.array([1, 2])
array2 = np.array([3, 4])

#Axis 0 is vertical so the arrays are stacked vertically
result = np.stack((array1, array2), axis=0)
print(result)


"""
[[1 2]
 [3 4]]
"""

import numpy as np

array1 = np.array([1, 2])
array2 = np.array([3, 4])
#Axis 1 is horizontal so the arrays are stacked columnar
result = np.stack((array1, array2), axis=1)
print(result)

"""
[[1 3]
 [2 4]]
"""


# In[4]:


"""
np.vstack()
vstack is a shorthand for stacking arrays vertically (along axis 0). 
It is essentially equivalent to calling np.stack with axis=0.

Syntax:
numpy.vstack(arrays)
arrays: Sequence of arrays to stack. 
Arrays should have the same shape, except in the dimension corresponding to the vertical stacking axis.
"""

import numpy as np

array1 = np.array([1, 2])
array2 = np.array([3, 4])

result = np.vstack((array1, array2))
print(result)


"""
This stacks the arrays vertically (row-wise).
[[1 2]
 [3 4]]
"""


# In[5]:


"""
np.hstack()
hstack stacks arrays horizontally (along axis 1). This is like concatenating arrays along the columns.

Syntax:

numpy.hstack(arrays)
arrays: Sequence of arrays to stack. 
The arrays must have the same number of dimensions and compatible shapes along the stacking axis (axis 1).

"""

import numpy as np

array1 = np.array([1, 2])
array2 = np.array([3, 4])

result = np.hstack((array1, array2))
print(result)


"""
[1 2 3 4]

"""


# In[6]:


"""
np.dstack()
dstack stacks arrays along the third axis (depth-wise), which is useful for 3D arrays. 
It adds a new "depth" dimension (axis 2).

Syntax:

numpy.dstack(arrays)
arrays: Sequence of arrays to stack. The arrays must have the same shape, except for the third axis.
"""

import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result = np.dstack((array1, array2))
print(result)

"""
[[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]

"""


# In[7]:


"""
Summary:
stack: Adds a new axis for stacking along the specified axis.
vstack: Stacks arrays vertically (along axis 0).
hstack: Stacks arrays horizontally (along axis 1).
dstack: Stacks arrays along the third axis (depth-wise, axis 2).
"""


# In[8]:


"""
np.column_stack()
np.column_stack() is a function in NumPy that stacks 1D arrays (or sequences) as columns into a 2D array. 
If you provide 2D arrays, it stacks them column-wise. 
It essentially combines arrays into a 2D array by adding each input array as a new column.

numpy.column_stack(tup)

tup: A sequence of 1-D or 2-D arrays. If arrays are 1D, they are treated as columns and stacked. 
If arrays are already 2D, they are stacked column-wise.

Key Points:
If the input arrays are 1D, column_stack will convert them into columns of a 2D array.
If the input arrays are already 2D, column_stack stacks them along the second axis (axis 1), 
essentially adding them side by side as columns.

"""

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

result = np.column_stack((array1, array2))
print(result)


"""
[[1 4]
 [2 5]
 [3 6]]

"""


array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result = np.column_stack((array1, array2))
print(result)


"""
[[1 2 5 6]
 [3 4 7 8]]

"""


"""
When to Use column_stack():
Combining multiple 1D arrays into a single 2D array by treating each 1D array as a column.
Combining 2D arrays where you want to stack them column-wise, ensuring they align by row.
Difference from hstack():
np.hstack() works in a similar way, but it directly concatenates arrays along the second axis (axis 1) 
without regard to whether the input arrays are 1D or 2D. column_stack() will treat 1D arrays as columns.
"""


# In[ ]:




