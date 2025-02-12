#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
 
# Dataset
data = {
  'Student': ["Amit", "John", "Jacob", "David", "Steve"],
  'Rank': [1, 4, 3, 5, 2],
  'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data,  index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'],)
 
print("Student Records\n\n",df)


# In[16]:


import pandas as pd
 
# Dataset
data = {
  'Student': ["Amit", "John", "Jacob", "David", "Steve"],
  'Rank': [1, 4, 3, 5, 2],
  'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data,  index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'],)

print("One Answer")
print(df.loc['RowA','Rank'])
print("Two Answer")
print(df.loc[['RowA','RowB']])
print("Three Answer")
print(df.loc[['RowA','RowB'],'Rank'])
print("Four Answer")
print(df.loc[['RowA','RowB'],['Student','Rank']])
print("Five Answer")
print(df.loc['RowA'])
print("Six Answer")
print(df['Rank'])


# In[17]:


"""
Expression	Output Type	Description
df.iloc[1,2]	Scalar (single value)	Retrieves a single element from row 1, column 2.
df.iloc[[1,2]]	DataFrame	Retrieves multiple rows (1 and 2) with all columns.
"""


# In[ ]:




