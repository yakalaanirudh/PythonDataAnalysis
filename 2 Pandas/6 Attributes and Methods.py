#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
dtype: Return the dtype.
ndim: Return the Number of dimensions
size: Return the number of elements.
name: Return the name of the Series.
hasnans: Returns True if NaNs are in the series.
index: The index of the series
head(): Return the first n rows.
tail(): Return the last n rows.
info(): Display the Summary of the series
"""


# In[2]:


#The pandas.series.dtype is used to return the datatype of the Series

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Datatype
print("\nSeries Datatype: ", s.dtype)

"""
Series: 
0     10
1     20
2     40
3     80
4    100
dtype: int64
 
Series Datatype:  int64
"""


# In[3]:


#The pandas.series.ndim is used to return the number of dimensions of the Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Dimensions
print("\nSeries Dimensions: ", s.ndim)

"""
Series: 
0     10
1     20
2     40
3     80
4    100
dtype: int64
 
Series Dimensions:  1
"""


# In[4]:


#The pandas.series.size is used to return the number of elements in the Pandas Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Return the number of elements in the Series
print("\nSeries Size: ", s.size)


"""
Series: 
0     10
1     20
2     40
3     80
4    100
dtype: int64
 
Series Size:  5
"""


# In[5]:


#The  pandas.series.name is used to return the name of the Series in  Pandas.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
# We have set the Series name using the name attribute
s = pd.Series(data, name ="MyNumberSeries")
 
# Display the Series
print("Series: \n", s)
 
# Return the name of the Series
print("\nSeries Name: ", s.name)


"""
Series: 
0     10
1     20
2     40
3     80
4    100
Name: MyNumberSeries, dtype: int64
 
Series Name:  MyNumberSeries
"""


# In[6]:


#The pandas.series.hasnans attribute returns True if NaNs are in the Pandas Series.


import pandas as pd
import numpy as np
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, np.NaN]
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Check whether the Series has NaNs
print("\nDoes the Series has NaN? ", s.hasnans)

"""
Series: 
0     10.0
1     20.0
2     40.0
3     80.0
4    100.0
5      NaN
dtype: float64
 
Does the Series has NaN?  True
"""


# In[8]:


#The pandas.series.index attribute is used to display the index of the Pandas Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]
 
# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE"])
 
# Display the Series
print("Series (with custom index labels): \n", s)
 
# Return the index of the Series
print("\nSeries Index: ", s.index)

"""

Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
 
Series Index:  Index(['RowA', 'RowB', 'RowC', 'RowD', 'RowE'], dtype='object')
"""


# In[9]:


#The  pandas.series.head() method is used to return the first n rows of the  Pandas Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, 200, 300, 500]
 
# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF", "RowG", "RowH"])
 
# Display the Series
print("Series (with custom index labels): \n", s)
 
# Return the first n rows. 
# The 5 is default for n
print("\nThe first 5 rows of the series:\n", s.head())


"""
Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
RowF    200
RowG    300
RowH    500
dtype: int64
 
The first 5 rows of the series:
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
 
"""


# In[10]:


#The pandas.series.tail() method is used to return the last n rows of the Pandas Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, 200, 300, 500]
 
# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF", "RowG", "RowH"])
 
# Display the Series
print("Series (with custom index labels): \n", s)
 
# Return the last n rows.
# The 5 is default for n
print("\nThe last 5 rows of the series:\n", s.tail())

"""
Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
RowF    200
RowG    300
RowH    500
dtype: int64
 
The last 5 rows of the series:
RowD     80
RowE    100
RowF    200
RowG    300
RowH    500
dtype: int64
"""


# In[12]:


#The pandas.series.info() method is used to display the Summary of the Pandas Series.

import pandas as pd
 
# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, 200, 300, 500]
 
# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF", "RowG", "RowH"])
 
# Display the Series
print("Series (with custom index labels): \n", s)
 
# Return the summary of the series
print("\nSeries Summary:\n", s.info())

"""
Series (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
RowF    200
RowG    300
RowH    500
dtype: int64
<class ' pandas.core.series.Series'>
Index: 8 entries, RowA to RowH
Series name: None
Non-Null Count  Dtype
--------------  -----
8 non-null      int64
dtypes: int64(1)
memory usage: 128.0+ bytes
"""


# In[ ]:




