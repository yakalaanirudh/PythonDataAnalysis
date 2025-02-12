#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
sum(): Return the sum of the values.
count(): Return the count of non-empty values.
max(): Return the maximum of the values.
min(): Return the minimum of the values.
mean(): Return the mean of the values.
median(): Return the median of the values.
std(): Return the standard deviation of the values.
describe(): Return the summary statistics for each column.
"""


# In[3]:


#The sum() method in Python Pandas is used to return the sum of the values

import pandas as pd
 
# Dataset
data = {
  'Maths': [90, 85, 98, 80, 55, 78],
  'Science': [92, 87, 59, 64, 87, 96],
  'English': [95, 94, 84, 75, 67, 65]
}
 
# DataFrame 
df = pd.DataFrame(data)
 
# Display the DataFrame
print("DataFrame = \n",df)
 
# Display the Sum of Marks in each column 
print("\nSum = \n",df.sum())


"""
DataFrame = 
    Maths  Science  English
0     90       92       95
1     85       87       94
2     98       59       84
3     80       64       75
4     55       87       67
5     78       96       65
 
Mean = 
Maths      486
Science    485
English    480
dtype: int64
"""


# In[4]:


#The count() method in Python Pandas is used to return the count of non-empty values

import pandas as pd
 
# Dataset
data = {
  'Maths': [90, 85, 98, None, 55, 78],
  'Science': [92, 87, 59, None, None, 96],
  'English': [95, None, 84, 75, 67, None]
}
 
# DataFrame 
df = pd.DataFrame(data)
 
# Display the DataFrame
print("DataFrame = \n",df)
 
# Display the Count of non-empty values in each column 
print("\nCount of non-empty values = \n",df.count())


"""
DataFrame = 
    Maths  Science  English
0   90.0     92.0     95.0
1   85.0     87.0      NaN
2   98.0     59.0     84.0
3    NaN      NaN     75.0
4   55.0      NaN     67.0
5   78.0     96.0      NaN
 
Count of non-empty values = 
Maths      5
Science    4
English    4
dtype: int64
"""


# In[5]:


#The max(), min() method in Python Pandas is used to return the maximun, minimum of the values
import  pandas as pd
 
# Dataset
data = {
  'Maths': [90, 85, 98, 80, 55, 78],
  'Science': [92, 87, 59, 64, 87, 96],
  'English': [95, 94, 84, 75, 67, 65]
}
 
# DataFrame 
df = pd.DataFrame(data)
 
# Display the DataFrame
print("DataFrame = \n",df)
 
# Display the Maximum of Marks in each column 
print("\nMaximum Marks = \n",df.max())
print("\nMaximum Marks = \n",df.min())

"""
DataFrame = 
    Maths  Science  English
0     90       92       95
1     85       87       94
2     98       59       84
3     80       64       75
4     55       87       67
5     78       96       65
 
Maximum Marks = 
Maths      98
Science    96
English    95
dtype: int64

Minimum Marks = 
Maths      55
Science    59
English    65
dtype: int64
"""


# In[6]:


"""
The mean() method in Python Pandas is used to return the mean of the values
The median() method in Python Pandas is used to return the median of the values
The std() method in Python Pandas is used to return the standard deviation of the values
"""

import pandas as pd
 
# Dataset
data = {
  'Maths': [90, 85, 98, 80, 55, 78],
  'Science': [92, 87, 59, 64, 87, 96],
  'English': [95, 94, 84, 75, 67, 65]
}
 
# DataFrame 
df = pd.DataFrame(data)
 
# Display the DataFrame
print("DataFrame = \n",df)
 
# Display the Mean of Marks in each column
print("\nMean = \n",df.mean())

# Display the Median of Marks in each column 
print("\nMedian = \n",df.median())

# Display the Standard Deviation of Marks in each column 
print("\nStandard Deviation = \n",df.std())

"""
DataFrame = 
    Maths  Science  English
0     90       92       95
1     85       87       94
2     98       59       84
3     80       64       75
4     55       87       67
5     78       96       65
 
Mean = 
Maths      81.000000
Science    80.833333
English    80.000000
dtype: float64

Median = 
Maths      82.5
Science    87.0
English    79.5
dtype: float64


Standard Deviation = 
Maths      14.642404
Science    15.432649
English    13.084342
dtype: float64
"""


# In[8]:


#The describe() method in Python Pandas is used to return the summary statistics for each column.

import pandas as pd
 
# Dataset
data = {
  'Maths': [90, 85, 98, None, 55, 78],
  ' Science': [92, 87, 59, None, None, 96],
  'English': [95, None, 84, 75, 67, None]
}
 
# DataFrame 
df = pd.DataFrame(data)
 
# Display the DataFrame
print("DataFrame = \n",df)
 
# Display the summary using the describe() method
print("\nSummary of  Statistics = \n",df.describe())

"""
DataFrame = 
    Maths  Science  English
0   90.0     92.0     95.0
1   85.0     87.0      NaN
2   98.0     59.0     84.0
3    NaN      NaN     75.0
4   55.0      NaN     67.0
5   78.0     96.0      NaN
 
Sumamry of Statistics = 
           Maths    Science    English
count   5.00000   4.000000   4.000000
mean   81.20000  83.500000  80.250000
std    16.36154  16.743158  12.038134
min    55.00000  59.000000  67.000000
25%    78.00000  80.000000  73.000000
50%    85.00000  89.500000  79.500000
75%    90.00000  93.000000  86.750000
max    98.00000  96.000000  95.000000
"""


# In[ ]:




