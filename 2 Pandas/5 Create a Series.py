#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
data: The data to be stored in the Pandas Series
index: The index values should have the same length as the data.
dtype: It is the datatype for the output Series.
name: Set the series name with the name parameter
copy: To copy the input data
"""


# In[4]:


"""
To create a series in  Python, we use the Series() method

The 0,1,2,3, etc. are the index numbers i.e. labels.

"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n",s)

"""
Series: 

0     10
1     20
2     40
3     80
4    100
dtype: int64
"""


# In[5]:


"""
Let us see how to access a specific value from a Series. The [] is used to access a value. 
Set the index of the value you want to display inside []:
"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n",s)
 
# Access a value
print("\nValue from a Pandas Series: ",s[2])

"""
Series: 
0     10
1     20
2     40
3     80
4    100
dtype: int64
 
Value from a Pandas Series:  40
"""


# In[6]:


"""
The index argument is used to set and name your own indexes in a Series i.e. the labels can be set accordingly
"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
 
# Display the Series
print("Series (with custom index labels): \n",s)

"""
Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
"""


# In[7]:


"""
Acessing with label
"""

import  pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
 
# Display the Series
print("Series (with custom index labels): \n",s)
 
# Access a value referring the lable
print("\nValue from a  Pandas Series with label RowD: ",s["RowD"])

"""
Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
 
Value from a Pandas Series with label RowD:  80
"""


# In[ ]:




