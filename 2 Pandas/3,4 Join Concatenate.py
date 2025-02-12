
"""
Join is used for combining columns of two potentially differently-indexed DataFrames into a single DataFrame 
based on a common column or index.

Concatenate is used for combining DataFrames or Series together along an axis.
"""


# In[2]:


#join Pandas DataFrames using the join() method

import pandas as pd
 
# Dataset
data1 = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'roll': [101, 102, 103, 104, 105]
}
data2 = {
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
# DataFrame
dataFrame1 = pd.DataFrame(data1)
print("DataFrame1 =\n",dataFrame1)
dataFrame2 = pd.DataFrame(data2)
print("\nDataFrame2 =\n",dataFrame2)
 
# Join two DataFrames
resDF = dataFrame1.join(dataFrame2)
print("\nJoining DataFrames =\n",resDF)


"""
DataFrame1 =
     id student  roll
0  S01    Amit   101
1  S02    John   102
2  S03   Jacob   103
3  S04   David   104
4  S05   Steve   105
 
DataFrame2 =
    rank  marks
0     1     95
1     4     70
2     3     80
3     5     60
4     2     90
 
Joining DataFrames =
     id student  roll  rank  marks
0  S01    Amit   101     1     95
1  S02    John   102     4     70
2  S03   Jacob   103     3     80
3  S04   David   104     5     60
4  S05   Steve   105     2     90
"""


# In[3]:


#concatenate Pandas DataFrames in  Python using the concat() method

import pandas as pd
 
# Dataset
data1 = {
  'id': ["S01", "S02", "S03", "S04", "S05"],
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'roll': [101, 102, 103, 104, 105]
}
data2 = {
  'id': ["S06", "S07", "S08"],
  'student': ["Ben", "Kane", "Rohit"],
  'roll': [106, 107, 108]
}
 
# DataFrame
dataFrame1 = pd.DataFrame(data1, index=[0, 1, 2, 3, 4])
print("DataFrame1 =\n",dataFrame1)
dataFrame2 = pd.DataFrame(data2, index=[5, 6, 7])
print("\nDataFrame2 =\n",dataFrame2)
 
# Concatenating two DataFrames
resDF = pd.concat([dataFrame1, dataFrame2])
print("\nConcatenating DataFrames =\n",resDF)

"""
DataFrame1 =
     id student  roll
0  S01    Amit   101
1  S02    John   102
2  S03   Jacob   103
3  S04   David   104
4  S05   Steve   105
 
DataFrame2 =
     id student  roll
5  S06     Ben   106
6  S07    Kane   107
7  S08   Rohit   108
 
Concatenating DataFrames =
     id student  roll
0  S01    Amit   101
1  S02    John   102
2  S03   Jacob   103
3  S04   David   104
4  S05   Steve   105
5  S06     Ben   106
6  S07    Kane   107
7  S08   Rohit   108
"""


# In[ ]:




