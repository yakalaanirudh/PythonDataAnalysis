#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Access elements from a One-Dimensional array

Example: Access the 1st element (index 0) from a One-Dimensional array

"""

import numpy as np
 
n = np.array([10, 20, 30, 40, 50])
print(n[0])

#10


# In[2]:


import numpy as np
 
n = np.array([10, 20, 30, 40, 50])
print(n[3])

#40


# In[3]:


import numpy as np
 
n = np.array([[1,3,5],[4,8,12]])
 
print(n[0,0])
print(n[0,1])
print(n[0,2])

"""
1
3
5
"""


# In[4]:


import numpy as np
 
n = np.array([[1,3,5],[4,8,12]])
print(n[1,0])
print(n[1,1])
print(n[1,2])


"""
4
8
12
"""


# In[5]:


import  numpy as np
 
n = np.array([[[5,10,15],[20,25,30]],[[35,40,45],[50,55,60]]])
print(n[0,0,0])
print(n[0,0,1])
print(n[0,0,2])

"""
5
10
15
"""


# In[6]:


import numpy as np
 
n = np.array([[[5,10,15],[20,25,30]],[[35,40,45],[50,55,60]]])
 
print(n[1,0,0])
print(n[1,0,1])
print(n[1,0,2])

"""
35
40
45
"""


# In[7]:


#Access the last element from a 1D array with negative indexing

import numpy as np
 
n = np.array([5, 10, 15])
print('Last element = ', n[-1])

#Last element =  15


# In[8]:


#Access the last element from a 2D array with negative indexing
import numpy as np
 
n = np.array([[1, 3, 5], [4, 8, 12]])
print('Last element = ', n[0, -1])

#Last element =  5


# In[9]:


import numpy as np
 
n = np.array([[1,3,5],[4,8,12]])
print('Last element = ', n[1,-1])

#Last element =  12


# In[ ]:




