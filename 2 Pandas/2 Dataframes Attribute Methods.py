#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
dtypes: Return the dtypes in the DataFrame
ndim: Return the number of dimensions of the DataFrame
size: Return the number of elements in the DataFrame.
shape: Return the dimensionality of the DataFrame in the form of a tuple.
index: Return the index of the DataFrame
T: Transpose the rows and columns
head(): Return the first n rows.
tail(): Return the last n rows.
"""


# In[2]:


#The pandas.DataFrame.dtypes is used to return the dtypes in the DataFrame

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
 
# Datatypes in the DataFrame
print("\nDatatypes:\n", res.dtypes)

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Datatypes:
Student    object
Rank        int64
Marks       int64
dtype: object
"""


# In[3]:


#The pandas.DataFrame.ndim is used to return the number of dimensions of the DataFrame

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
 
# Number of Dimensions in the DataFrame
print("\nNumber of Dimensions:\n", res.ndim)

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Number of Dimensions:
 2
"""


# In[5]:


#The  pandas.DataFrame.size is used to return the number of elements in the DataFrame

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
 
# Number of elements in the DataFrame
print("\nNumber of Elements:\n", res.size)

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Number of Elements:
 15
"""


# In[6]:


#The pandas.DataFrame.shape is used to return the dimensionality of the DataFrame in the form of a tuple.


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
 
# Return the dimensionality of the DataFrame
# Result in a Tuple form
print("\nDimensionality:\n", res.shape)

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Dimensionality:
 (5, 3)
"""


# In[7]:


#The pandas.DataFrame.index is used to return the index of the DataFrame.

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
 
# Return the index of the DataFrame
print("\nDataFrame Index:\n", res.index)


"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
DataFrame Index:
 Index(['RowA', 'RowB', 'RowC', 'RowD', 'RowE'], dtype='object')
"""


# In[9]:


#The  pandas.DataFrame.T is used to Transpose the rows and columns.
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
 
# Return the Transpose
print("\nTranspose:\n", res.T)

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Transpose:
          RowA  RowB   RowC   RowD   RowE
Student  Amit  John  Jacob  David  Steve
Rank        1     4      3      5      2
Marks      95    70     80     60     90
"""


# In[10]:


#The pandas.DataFrame.head() is used to return the first n rows.

import pandas as pd
 
# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Nathan", "Steve"],
    'Rank': [1, 4, 3, 5, 6, 2],
    'Marks': [95, 70, 80, 60, 55, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
res = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE', 'RowF'], )
 
# Display the Records
print("Student Records\n\n", res)
 
# Return the first n rows
# Default value of n is 5
print("\nFirst 5 rows:\n", res.head())

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE  Nathan     6     55
RowF   Steve     2     90
 
First 5 rows:
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE  Nathan     6     55
"""


# In[12]:


#The pandas.DataFrame.tail() is used to return the last n rows.

import  pandas as pd
 
# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Nathan", "Steve"],
    'Rank': [1, 4, 3, 5, 6, 2],
    'Marks': [95, 70, 80, 60, 55, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
res = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE', 'RowF'], )
 
# Display the Records
print("Student Records\n\n", res)
 
# Return the last n rows
# Default value of n is 5
print("\nLast 5 rows:\n", res.tail(3))


"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE  Nathan     6     55
RowF   Steve     2     90
 
Last 5 rows:
      Student  Rank  Marks
RowD   David     5     60
RowE  Nathan     6     55
RowF   Steve     2     90
"""


# In[ ]:




