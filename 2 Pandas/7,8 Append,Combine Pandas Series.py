#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
append()
Used for: Concatenating DataFrames by stacking them vertically (row-wise).
Similar to: pd.concat([df1, df2])
Deprecated: Since pandas 1.4.0, .append() has been deprecated, and it's recommended to use pd.concat() instead.
Behavior:
Adds rows from one DataFrame to another.
Does not modify the original DataFrame unless inplace=True (which was removed in pandas 1.4.0).
If column names don’t match, missing values (NaN) are introduced.

combine()
Used for: Merging two DataFrames element-wise using a custom function.
Behavior:
Applies a function element-wise to resolve conflicts when combining two DataFrames.
Works best for updating an existing DataFrame with new values.
"""


# In[2]:


import  pandas as pd
 
# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [150, 200]
 
# Create two Series using the Series() method
series1 = pd.Series(data1, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
series2 = pd.Series(data2, index = ["RowF", "RowG"])
 
# Display the Series
print("Series1 (with custom index labels): \n",series1)
print("\nSeries2 (with custom index labels): \n",series2)
 
# Append
# The ignore_index parameter is by default set to False:
result = series1.append(series2, ignore_index = False) 
  
# Print the result 
print("\nResult after appending (considering original indexes):\n",result)

"""
Series1 (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
 
Series2 (with custom index labels): 
RowF    150
RowG    200
dtype: int64
 
Result after appending (considering original indexes):
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
RowF    150
RowG    200
dtype: int64
"""


# In[3]:


"""
To append two series, use the append() method. 
For ignoring the original indexes and replacing them with 0, 1, 2, etc, 
set the ignore_index to True as discussed above.
"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [150, 200]
 
# Create two Series using the Series() method
series1 = pd.Series(data1, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
series2 = pd.Series(data2, index = ["RowF", "RowG"])
 
# Display the Series
print("Series1 (with custom index labels): \n",series1)
print("\nSeries2 (with custom index labels): \n",series2)
 
# Append
# The ignore_index parameter is set to True for ignoring original indexes
result = series1.append(series2, ignore_index = True) 
  
# Print the result 
print("\nResult after appending (ignoring original indexes):\n",result)

"""
Series1 (with custom index labels): 
RowA     10
RowB     20
RowC     40
RowD     80
RowE    100
dtype: int64
 
Series2 (with custom index labels): 
RowF    150
RowG    200
dtype: int64
 
Result after appending (ignoring original indexes):
0     10
1     20
2     40
3     80
4    100
5    150
6    200
dtype: int64
"""


# In[4]:


"""
To combine two Pandas series into one in  Python, use the combine() method. 
It uses a specific function for the decision, mentioned by the user as a parameter of the combine() method.
"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [25, 5, 75, 95, 45] 
 
# Create a Series using the Series() method
series1 = pd.Series(data1)
series2 = pd.Series(data2)
 
# Display the Series
print("Before combining the series:\n") 
print("Series1: \n",series1)
print("Series2: \n",series2)
 
def demo(x1, x2) :
  if (x1 > x2):
    return x1
  else:
    return x2
 
# Combine two series into one
# The function returns the largest value
res = series1.combine(series2, demo) 
  
# Display the result
print("\nAfter combining into one:\n",res)

"""
Before combining the series:
 
Series1: 
0     10
1     20
2     40
3     80
4    100
dtype: int64
Series2: 
0    25
1     5
2    75
3    95
4    45
dtype: int64
 
After combining into one:
 0     25
1     20
2     75
3     95
4    100
dtype: int64
"""


# In[ ]:




