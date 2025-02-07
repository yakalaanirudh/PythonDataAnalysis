#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Slicing from index 1 to 3 (3 is excluded)
Slicing from index 2 to 5 (5 is excluded)
Slicing from index 5 to last
Slicing from the beginning to index 5 (5 is excluded)
"""


# In[2]:


import numpy as np
 
n = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(n[1:3])

#[25 30]


# In[3]:


import numpy as np
 
n = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(n[2:5])

#[30 35 40]


# In[4]:


import numpy as np
 
n = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(n[5:])

#[45 50 55 60, 65]


# In[5]:


import numpy as np
 
n = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
print(n[:5])

#[20 25 30 35 40]


# In[6]:


"""
Slicing with STEP
arr[start:end:step}
"""

import numpy as np
 
n = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
print(n[1:10:2])

#[10 20 30 40 50]


# In[7]:


import numpy as np
   
n = np.array([[10,30,50,70,90,95],[4,8,12,14,16,18]])
print(n[0,2:5])

#[50 70 90]


# In[8]:


import numpy as np
 
n = np.array([[10, 30, 50, 70, 90, 95], [4, 8, 12, 14, 16, 18]])
print(n[0:2, 2:5])

"""
[[50 70 90]
 [12 14 16]]
 """


# In[ ]:




