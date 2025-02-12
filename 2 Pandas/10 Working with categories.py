#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To append new categories, use the add_categories() method in Python Pandas

import pandas as pd 
 
# Creating a Categorical Series
s = pd.Series(["p", "q", "r", "s", "q"], dtype="category")
 
# Display the Series
print("Series = \n", s)
 
# Append Category
s = s.cat.add_categories([5])
 
# Display the updated category
print("\nUpdated Categories = ",s.cat.categories)

"""
Series = 
0    p
1    q
2    r
3    s
4    q
dtype: category
Categories (4, object): [p, q, r, s]
 
Updated Categories =  Index(['p', 'q', 'r', 's', 5], dtype='object')
"""


# In[2]:


#To remove a category, use the remove_categories() method in Python Pandas


import pandas as pd 
 
# Creating a Categorical Series
s = pd.Series(["p", "q", "r", "s", "q"], dtype="category")
 
# Display the Series
print("Series\n", s)
 
# Remove a Category
# Display the updated category after removing a specific category
print("\nUpdated Categories\n",s.cat.remove_categories("r"))
 
    
"""
Series
0    p
1    q
2    r
3    s
4    q
dtype: category
Categories (4, object): [p, q, r, s]
 
Updated Categories
0      p
1      q
2    NaN
3      s
4      q
dtype: category
Categories (3, object): [p, q, s]
"""


# In[ ]:




