#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Categorical data in Pandas. 
It is a Pandas data type corresponding to categorical variables in statistics. 
A categorical variable takes on a limited number of possible values. 
Examples are gender, blood type, country affiliation, rating, etc.
"""


# In[2]:


"""
Use the dtype=”category” while creating a series to create a Categorical Series.
"""

import pandas as pd
 
# Creating a Categorical Series 
s = pd.Series(["p", "q", "r", "s", "q"], dtype="category")
 
# Display the Series
print("Series = \n", s)

"""
Series = 
0    p
1    q
2    r
3    s
4    q
dtype: category
Categories (4, object): [p, q, r, s]
"""


# In[3]:


"""
Create Categorical DataFrame
Use the dtype=”category” while creating a DataFrame to create a Categorical DataFrame
"""

import pandas as pd
 
# Creating a Categorical DataFrame 
df = pd.DataFrame({"Cat1": list("pqrs"), "Cat2": list("pqrp"), "Cat3": list("qrrr")}, dtype="category")
 
# Display the DataFrame
print("DataFrame = \n", df)
 
# Display the datatypes
print("\nDataType of each column = \n", df.dtypes)

"""
DataFrame = 
   Cat1 Cat2 Cat3
0    p    p    q
1    q    q    r
2    r    r    r
3    s    p    r
 
DataType of each column = 
Cat1    category
Cat2    category
Cat3    category
dtype: object
"""


# In[ ]:




