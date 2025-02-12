#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
To sort the data in Pandas, we can use various methods. 
we will see how to sort the DataFrame in Pandas using the sort_values() method.

Sort the Pandas DataFrame (default ascending order)
Sort the Pandas DataFrame in Descending Order
"""


# In[2]:


import pandas as pd
 
# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
res = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'], )
 
# Display the Records
print("Student Records\n\n", res)
 
# Sort the data in ascending order (default)
# The data is sort by the 'Rank' column using the 'by' parameter
print("\nSorting in ascending order:\n", res.sort_values(by=['Rank']))


# Sort the data in descending order using the 'ascending' parameter with 'False' value
# The data is sort by the 'Rank' column using the 'by' parameter
print("\nSorting in descending order:\n", res.sort_values(by=['Rank'], ascending=False))


"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Sorting in ascending order:
      Student  Rank  Marks
RowA    Amit     1     95
RowE   Steve     2     90
RowC   Jacob     3     80
RowB    John     4     70
RowD   David     5     60

Sorting in descending order:
      Student  Rank  Marks
RowD   David     5     60
RowB    John     4     70
RowC   Jacob     3     80
RowE   Steve     2     90
RowA    Amit     1     95
"""


# In[ ]:




