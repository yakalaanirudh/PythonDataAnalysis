"""
Create a Zero-dimensional NumPy array
Let us create a zero-dimensional numpy array and check the dimensions using the ndim attribute:
"""

import numpy as np
 
n = np.array(25)
print(type(n))
print(n.shape)
print("Dimensions = ",n.ndim)

"""
Output
<class 'numpy.ndarray'>
()
Dimensions = 0

ndim stands for n-dimension array
"""


"""
Create a One-dimensional NumPy array
Let us create a one-dimensional numpy array and check the dimensions using the ndim attribute:


<class 'numpy.ndarray'>
"""

import numpy as np
 
n = np.array([10, 20, 30])
print(type(n))
print(n.shape)
print("Dimensions = ",n.ndim)


"""
Output

<class 'numpy.ndarray'>
(3,)
Dimensions = 1
 
"""




"""
Create a Two-dimensional NumPy array
"""

import numpy as np
 
n = np.array([[1,3,5],[4,8,12]])
print(type(n))
print(n.shape)
print("Dimensions = ",n.ndim)


"""
Output


<class 'numpy.ndarray'>
(2, 3)
Dimensions = 2
"""



"""
Create a Three-dimensional NumPy array
"""

import numpy as np
 
n = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(type(n))
print(n.shape)
print("Dimensions = ",n.ndim)

"""
Output

2 blocks (first dimension),
2 rows (second dimension),
3 columns in each row (third dimension).

<class 'numpy.ndarray'>
(2, 2, 3)
Dimensions = 3

"""



"""
Check how many dimensions an array has
"""

import numpy as np
 
n1 = np.array(10)
n2 = np.array([10, 20, 30])
 
print(n1.ndim)
print(n1.shape)
 
print(n2.ndim)
print(n2.shape)

"""
0
()
1
(3,)
"""



"""
n = np.array([[[1,2,3,4,5,6],[4,5,6]],[[7,8,9],[10,11,12]]]) 
gives an error because in a n dimension array all inner lists are supposed to be of equal length

so give dtype=object
"""
n = np.array([[[1,2,3,4,5,6],[4,5,6]],[[7,8,9],[10,11,12]]], dtype=object)
print(type(n))
print(n.shape)
print("Dimensions = ", n.ndim)

"""
Output

<class 'numpy.ndarray'>
(2, 2)
Dimensions =  2

"""




