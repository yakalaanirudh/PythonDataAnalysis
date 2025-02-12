#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
lower(): Perform lowercase on text data
upper(): Perform uppercase on text data
title(): Convert text data to camel case
len(): To get the length of each element in the Series.
count(): Count the non-empty cells for each column or row
contain(): Search for a value in a column.
"""


# In[2]:


import  pandas as pd
 
# Data to be stored in the Pandas Series
data = ['Jacob', 'Amit', 'TRENT', 'Nathan', 'MaRtIN']
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Convert the text data to lowercase
print("\nLowercase data:\n",s.str.lower())

# Convert the text data to uppercase
print("\nUppercase data:\n",s.str.upper())

# Convert the text data to camel case
print("\nCamel case data:\n",s.str.title())

# Get the length of each element
print("\nLength:\n",s.str.len())

"""
Series: 
0     Jacob Oram
1           Amit
2          Trent
3    Nathan Lyon
4         Martin

Lowercase data:
0     jacob
1      amit
2     trent
3    nathan
4    martin

Uppercase data:
0     JACOB
1      AMIT
2     TRENT
3    NATHAN
4    MARTIN

Camel case data:
0     Jacob
1      Amit
2     Trent
3    Nathan
4    Martin


Length:
0    10
1     4
2     5
3    11
"""


# In[3]:


"""
To count the non-empty cells for each column or row in a Series, use the count() method
"""
import  numpy as np
import pandas as pd
 
# Data to be stored in the Pandas Series
data = [np.nan, "Amit Diwan", "Trent", "Nathan Lyon", np.nan]
 
# Create a Series using the Series() method
series = pd.Series(data)
 
# Display the Series
print("Series:\n", series)
 
# Get the count
print("\nCount:\n", series.count())

"""
Series:
0            NaN
1     Amit Diwan
2          Trent
3    Nathan Lyon
4            NaN
dtype: object
 
Count:
 3
 
"""


# In[4]:


"""
The contains() method is used in Pandas to search for a value in a column.
"""

import pandas as pd
 
# Data to be stored in the Pandas Series
data = ['Jacob Oram', 'Amit', 'Trent', 'Nathan Lyon', 'Martin']
 
# Create a Series using the Series() method
s = pd.Series(data)
 
# Display the Series
print("Series: \n", s)
 
# Search for a specific value
print("\nDoes the specific value exist?\n",s.str.contains('Amit'))

"""
Series: 
0     Jacob Oram
1           Amit
2          Trent
3    Nathan Lyon
4         Martin
 
Does the specific value exist?
0    False
1     True
2    False
3    False
4    False
 
"""


# In[ ]:




