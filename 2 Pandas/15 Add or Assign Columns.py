#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
To insert a new column into a DataFrame, use the insert() method. 
We can set the location, name, and the values as a parameter:

dataFrame.insert(2, "roll",  [101, 102, 103, 104, 105])


"""

import pandas as pd
 
# Dataset
data = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
dataFrame = pd.DataFrame(data)
print("Student Records\n\n",dataFrame)
 
# Insert a new column using the insert() method
# The location set is 2 i.e. 2nd index i.e. 3rd position
dataFrame.insert(2, "roll",  [101, 102, 103, 104, 105])
 
# DataFrame after adding a new column
print("\nUpdated DataFrame:\n",dataFrame)


"""
Student Records
 
     id student  rank  marks
0  S01    Amit     1     95
1  S02    John     4     70
2  S03   Jacob     3     80
3  S04   David     5     60
4  S05   Steve     2     90
 
Updated DataFrame:
     id student  roll  rank  marks
0  S01    Amit   101     1     95
1  S02    John   102     4     70
2  S03   Jacob   103     3     80
3  S04   David   104     5     60
4  S05   Steve   105     2     90
"""


# In[2]:


"""
To assign new columns to an already created Pandas DataFrame, use the assign() method. 
It adds a new column to the end. Set the new column with the column name as a parameter of the assign() method:


resDF = dataFrame.assign(roll =  [101, 102, 103, 104, 105])
 
 """

import  pandas as pd
 
# Dataset
data = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
dataFrame = pd.DataFrame(data)
print("Student Records\n\n",dataFrame)
 
# Insert a new column using the assign() method
# It automatically gets inserted at the end
resDF = dataFrame.assign(roll =  [101, 102, 103, 104, 105])
 
# DataFrame after adding a new column
print("\nUpdated DataFrame:\n",resDF)


"""
Student Records
 
     id student  rank  marks
0  S01    Amit     1     95
1  S02    John     4     70
2  S03   Jacob     3     80
3  S04   David     5     60
4  S05   Steve     2     90
 
Updated DataFrame:
     id student  rank  marks  roll
0  S01    Amit     1     95   101
1  S02    John     4     70   102
2  S03   Jacob     3     80   103
3  S04   David     5     60   104
4  S05   Steve     2     90   105
"""


# In[ ]:




