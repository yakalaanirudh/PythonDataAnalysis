#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
 
n = np.array(10)
 
print(n)
print(n.ndim)
print(n.shape)

"""
10
0
()
"""


# In[3]:


import numpy as np
 
n = np.array([10, 20, 30])
 
print(n)
print(n.ndim)
print(n.shape)

"""
[10 20 30]
1
(3,)
"""


# In[4]:


import numpy as np
 
n = np.array([[1, 3, 5], [4, 8, 12]])
 
print(n)
print(n.ndim)
print(n.shape)

"""
[[ 1  3  5]
 [ 4  8 12]]
2
(2, 3)
"""


# In[5]:


import numpy as np
 
n = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
 
print(n)
print(n.ndim)
print(n.shape)

"""
[[[ 1  2  3]
  [ 4  5  6]]
 
 [[ 7  8  9]
  [10 11 12]]]
3
(2, 2, 3)
"""


# In[ ]:




