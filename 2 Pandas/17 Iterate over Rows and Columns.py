#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To iterate over rows, use the  Python Pandas iterrows() method. 
import pandas as pd
 
# Dataset
data = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2]
}
 
dataFrame = pd.DataFrame(data)
print("Student Records\n", dataFrame)
 
# Iterate over rows in the DataFrames
print("\nDisplay the rows")
for row in dataFrame.iterrows():
  print(row)
 
    
"""
Student Records
     id student  rank
0  S01    Amit     1
1  S02    John     4
2  S03   Jacob     3
3  S04   David     5
4  S05   Steve     2
 
Display the rows
(0, id          S01
student    Amit
rank          1
Name: 0, dtype: object)
(1, id          S02
student    John
rank          4
Name: 1, dtype: object)
(2, id           S03
student    Jacob
rank           3
Name: 2, dtype: object)
(3, id           S04
student    David
rank           5
Name: 3, dtype: object)
(4, id           S05
student    Steve
rank           2
Name: 4, dtype: object)
"""


# In[4]:


"""
iterrows()
Returns each row as a (index, Series) pair.
The row is represented as a Pandas Series, which means each iteration creates a new Series object.
Slower compared to itertuples() due to the overhead of creating Series objects.

itertuples()
Returns each row as a named tuple where column names become attributes.
Named tuples are faster and more memory-efficient than Series.
Since tuples are immutable, you cannot modify values directly.
"""


# In[2]:


#To iterate over rows, use the Python Pandas itertuples() method. Here, each row is returned as a Python Tuple object.

import pandas as pd
 
# Dataset
data = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2]
}
 
dataFrame = pd.DataFrame(data)
print("Student Records\n", dataFrame)
 
# Iterate over rows in the DataFrames
print("\nDisplay records as a Tuple object")
for row in dataFrame.itertuples():
  print(row)

"""
Student Records
     id student  rank
0  S01    Amit     1
1  S02    John     4
2  S03   Jacob     3
3  S04   David     5
4  S05   Steve     2
 
Display records as a Python object
 Pandas(Index=0, id='S01', student='Amit', rank=1)
Pandas(Index=1, id='S02', student='John', rank=4)
Pandas(Index=2, id='S03', student='Jacob', rank=3)
Pandas(Index=3, id='S04', student='David', rank=5)
Pandas(Index=4, id='S05', student='Steve', rank=2)

"""


# In[3]:


"""
To iterate each and every column, use the Pandas items() method. 
The result will display a label object that is the name of the column and a column object that is 
what you have in the column.
"""

import  pandas as pd
 
# Dataset
data = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2]
}
 
dataFrame = pd.DataFrame(data)
print("Student Records\n")
 
# Iterate over columns in the DataFrame
for a, b in dataFrame.items():
  print(a)
  print(b)
    
"""

Student Records
 
id
0    S01
1    S02
2    S03
3    S04
4    S05
Name: id, dtype: object
student
0     Amit
1     John
2    Jacob
3    David
4    Steve
Name: student, dtype: object
rank
0    1
1    4
2    3
3    5
4    2
Name: rank, dtype: int64
"""


# In[ ]:




