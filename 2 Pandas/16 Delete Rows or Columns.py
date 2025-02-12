#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
The drop() method is used in  Python to delete rows/ columns in a Pandas DataFrame. 
It is used to remove a particular row or column. Under the parameters of the drop() method, 
mention the column you want to delete with the axis.

The axis is set to 1 since we want to drop a column. 
The columns axis can also be used for the drop() method to remove the specified column:

axis='columns'
or
axis = 1
 


"""


# In[2]:


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
 
# Drop a column using the drop() method
# The marks column is deleted
resDF = dataFrame.drop("marks", axis='columns')
 
# DataFrame after dropping a column
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
     id student  rank
0  S01    Amit     1
1  S02    John     4
2  S03   Jacob     3
3  S04   David     5
4  S05   Steve     2
"""


# In[4]:


"""
The rows are dropped using the index label set as a parameter of the drop() method. 
The rows of that particular label are removed. Set the axis to 0 since we want to drop a row. 
The rows axis i.e. index can also be used for the drop() method to remove the specified row:

axis='index'
Or
axis = 0

"""


# In[7]:


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
 
# Drop a row using the drop() method
# The row with index 2 is removed
resDF = dataFrame.drop(2, axis='index')
 
# DataFrame after dropping a column
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
     id student  rank  marks
0  S01    Amit     1     95
1  S02    John     4     70
3  S04   David     5     60
4  S05   Steve     2     90
"""


# In[ ]:




