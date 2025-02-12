#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
strip(): Strip whitespace (including newlines) or specific characters from the left and right
lstrip(): Strip whitespace (including newlines) or specific characters from only the left side
rstrip(): Strip whitespace (including newlines) or specific characters from only the right side
"""


# In[2]:


import pandas as pd
 
# Data to be stored in the Pandas Series
data = ["!Jacob", "Amit\n\n", "Trent", "Nathan\t", "Martin"]
 
# Create a Series using the Series() method
series = pd.Series(data)
 
# Display the Series
print("Series:\n", series)
 
# Strip the values
print("\nStrip from both the sides\n",series.str.strip("!\n\t"))


"""
Series:
0      !Jacob
1    Amit\n\n
2       Trent
3    Nathan\t
4      Martin
dtype: object
 
Strip from both the sides
0     Jacob
1      Amit
2     Trent
3    Nathan
4    Martin
dtype: object
"""


# In[3]:


# lstrip() method in Python Pandas
# Code by Studyopedia
 
import pandas as pd
 
# Data to be stored in the Pandas Series
data = ["!Jacob", "\n\tAmit\n\n", "!Trent!", "Nathan\t", "Martin"]
 
# Create a Series using the Series() method
series = pd.Series(data)
 
# Display the Series
print("Series:\n", series)
 
# Strip from the left
print("\nStrip from the left side:\n", series.str.lstrip("!\n\t"))

# Remove characters from the right side
print("\nRemove from the right:\n", series.str.rstrip("\n\t!"))

"""
Series:
 0          !Jacob
1    \n\tAmit\n\n
2         !Trent!
3        Nathan\t
4          Martin
dtype: object
 
Strip from the left side:
 0       Jacob
1    Amit\n\n
2      Trent!
3    Nathan\t
4      Martin
dtype: object


Remove from the right:
 0      !Jacob
1    \n\tAmit
2      !Trent
3      Nathan
4      Martin
dtype: object
"""


# In[ ]:




