#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
To find duplicates from rows in a Pandas DataFrame or Series, use the duplicated() method. 
It returns a Series with True and False values i.e. for duplicate rows True is returned.
"""

import pandas as pd
 
# Dataset
data = {
    'student': ["Amit", "John", "Amit", "David", "Steve"],
    'rank': [1, 4, 1, 5, 3],
    'marks': [95, 70, 95, 60, 90]
}
 
df = pd.DataFrame(data)
 
print("Student Records\n\n", df)
 
# Find duplicates
res = df.duplicated()
print("\nDescribing Duplicates:\n",res)

"""
Student Records
 
   student  rank  marks
0    Amit     1     95
1    John     4     70
2    Amit     1     95
3   David     5     60
4   Steve     3     90
 
Describing Duplicates:
0    False
1    False
2     True
3    False
4    False
"""


# In[2]:


"""
To remove duplicates from rows in a Pandas DataFrame or Series, use the drop_duplicates() method
"""

import pandas as pd
 
# Dataset
data = {
    'student': ["Amit", "John", "Amit", "David", "Steve"],
    'rank': [1, 4, 1, 5, 3],
    'marks': [95, 70, 95, 60, 90]
}
 
df = pd.DataFrame(data)
 
print("Student Records\n\n", df)
 
# Delete duplicates using the drop_duplicates()
res = df.drop_duplicates()
print("\nNew DataFrame after deleting duplicates:\n",res)


"""
Student Records
 
   student  rank  marks
0    Amit     1     95
1    John     4     70
2    Amit     1     95
3   David     5     60
4   Steve     3     90
 
New DataFrame:
   student  rank  marks
0    Amit     1     95
1    John     4     70
3   David     5     60
4   Steve     3     90
"""


# In[ ]:




