#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Select Two columns
"""

import pandas as pd
 
# Dataset
data = {
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
dataFrame = pd.DataFrame(data)
 
print("Student Records\n\n",dataFrame)
print("\nSelecting only two columns:\n",dataFrame[['rank', 'marks']])


"""
Student Records
 
   student  rank  marks
0    Amit     1     95
1    John     4     70
2   Jacob     3     80
3   David     5     60
4   Steve     2     90
 
Selecting only two columns:
    rank  marks
0     1     95
1     4     70
2     3     80
3     5     60
4     2     90
"""


# In[2]:


"""
Select multiple columns in a range
dataFrame[dataFrame.columns[2:5]]
"""

import pandas as pd
 
# Dataset
data = {
   'Id': ["S01", "S02", "S03", "S04", "S05"],
   'Student': ["Amit", "John", "Jacob", "David", "Steve"],
   'Roll': [101, 102, 103, 104, 105],
   'Rank': [1, 4, 3, 5, 2],
   'Marks': [95, 70, 80, 60, 90],
   'Address': ["East", "North", "West", "South", "SouthWest"]
}
 
dataFrame = pd.DataFrame(data)
 
print("Student Records\n", dataFrame)
 
# 3rd to 5th columns are selected
print("\nSelecting columns in a range:\n", dataFrame[dataFrame.columns[2:5]])


"""
Student Records
     Id Student  Roll  Rank  Marks    Address
0  S01    Amit   101     1     95       East
1  S02    John   102     4     70      North
2  S03   Jacob   103     3     80       West
3  S04   David   104     5     60      South
4  S05   Steve   105     2     90  SouthWest
 
Selecting columns in a range:
    Roll  Rank  Marks
0   101     1     95
1   102     4     70
2   103     3     80
3   104     5     60
4   105     2     90
"""


# In[ ]:




