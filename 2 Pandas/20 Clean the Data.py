#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
isnull(): Find the NULL values and replace them with True.
notnull(): Find the NOT NULL values and replace them with True.
df.dropna(): Drop rows with NULL values.
df.fillna(x): Replace NULL values with a specific value
"""


# In[3]:


"""
The isnull() method in Pandas is used to find the NULL values and replace them with True. 
For non-NULL values, False is returned.
"""

import pandas as pd
 
# Input CSV file
df = pd.read_csv(r"C:\Users\hp\Desktop\demo.csv")
 
# Display the CSV file records
print("Our DataFrame\n",df)
 
# Find and Replace Null with True
resdf = df.isnull()
 
# Return the new DataFrame
print("\nNew DataFrame \n",resdf.to_string())

"""
Our DataFrame
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1     NaN
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
6        4.5     NaN
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
 
New DataFrame
    Frequency  Points
0      False   False
1      False   False
2      False    True
3      False   False
4      False   False
5      False   False
6      False    True
7      False   False
8      False   False
9      False   False
"""


# In[4]:


"""
The notnull() method in Pandas is used to find the NOT NULL values and replace them with True. 
For NULL values, False is returned.
"""

import pandas as pd
 
# Input CSV file
df = pd.read_csv(r"C:\Users\hp\Desktop\demo.csv")
 
# Display the CSV file records
print("Our DataFrame\n",df)
 
# Find and Replace NOT NULL values with True
resdf = df.notnull()
 
# Return the new DataFrame
print("\nNew DataFrame\n",resdf.to_string())

"""
Our DataFrame
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1     NaN
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
6        4.5     NaN
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
 
New DataFrame
    Frequency  Points
0       True    True
1       True    True
2       True   False
3       True    True
4       True    True
5       True    True
6       True   False
7       True    True
8       True    True
9       True    True
"""


# In[5]:


#The dropna() method in  Pandas is used to drop and remove rows with null values

import  pandas as pd
 
# Input CSV file
df = pd.read_csv(r"C:\Users\hp\Desktop\demo.csv")
 
# Display the CSV file records
print("Our DataFrame\n",df)
 
# Find and remove rows with NULL value
resdf = df.dropna()
 
# Return the new DataFrame
print("\nNew DataFrame (after removing rows with NULL)\n",resdf.to_string())

"""
Our DataFrame
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1     NaN
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
6        4.5     NaN
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
 
New DataFrame (after removing rows with NULL)
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
"""


# In[6]:


#The fillna() method in Pandas is used to replace NULL values with a specific value.

import pandas as pd
 
# Input CSV file
df = pd.read_csv(r"C:\Users\hp\Desktop\demo.csv")
 
# Display the CSV file records
print("Our DataFrame\n",df)
 
# Find and replace NULL values with a specific value 111
resdf = df.fillna(111)
 
# Return the new DataFrame
print("\nNew DataFrame (after replacing NULL with a specific value)\n",resdf.to_string())


"""
Our DataFrame
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1     NaN
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
6        4.5     NaN
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
 
New DataFrame (after replacing NULL with a specific value)
    Frequency  Points
0        2.4    83.5
1        3.2    21.6
2        6.1   111.0
3        1.2    45.9
4        2.9    19.3
5        3.8    23.9
6        4.5   111.0
7        8.3    66.3
8        7.9    74.7
9        5.8    67.5
"""


# In[ ]:




