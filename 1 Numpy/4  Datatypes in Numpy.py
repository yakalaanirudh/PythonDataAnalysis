#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
b – boolean
u – unsigned integer
f – float
c – complex float
m – timedelta
M – datetime
O – object
S – string
U – unicode string
"""

"""
Get the datatype of a Numpy array with integers
To get the datatype of a Numpy array, use the dtype attribute. Let us see an example:
"""

import numpy as np
 
n = np.array([10, 20, 30])
print(n.dtype)

#int32


# In[2]:



n = np.array(["amit", "rohit", "ashwin", "jadeja", "virat"])
print(n.dtype)

#U6


# In[3]:


import numpy as np
 
n = np.array(['amit', 'rohit', 'ashwin', 'jadeja', 'virat'], dtype='S5')
print(n.dtype)

#S5


# In[4]:


"""
Convert one datatype to another
Use the astype() to create a copy of an array and then set the new data type. 
This is how you can convert one type to another.
"""

import numpy as np
 
n = np.array(['10', '20', '30', '40', '50'])
print(n)
print(n.dtype)
 
n2 = n.astype('i')
print(n2)
print(n2.dtype)

"""
Output

['10' '20' '30' '40' '50']
<U2
[10 20 30 40 50]
int32

"""


# In[ ]:




