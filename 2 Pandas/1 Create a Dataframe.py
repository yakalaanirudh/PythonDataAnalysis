
"""
Create a Pandas DataFrame
To create a dataframe in  pandas, use the pandas.DataFrame() method.
"""

import pandas as pd
 
# Dataset
data = {
  'student': ["Amit", "John", "Jacob", "David", "Steve"],
  'rank': [1, 4, 3, 5, 2],
  'marks': [95, 70, 80, 60, 90]
}
 
df = pd.DataFrame(data)
 
print("Student Records\n\n",df)

"""
The 0, 1, 2, etc. are the index or label that gets automatically added to the table.
Student Records
 
   student  rank  marks
0    Amit     1     95
1    John     4     70
2   Jacob     3     80
3   David     5     60
4   Steve     2     90
"""


# In[2]:


"""
The dataframe.loc is used in Pandas to access a group of rows or columns in a DataFrame
"""

 
# Dataset
data = {
  'Student': ["Amit", "John", "Jacob", "David", "Steve"],
  'Rank': [1, 4, 3, 5, 2],
  'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data,  index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'],)
 
print("Student Records\n\n",df)
 
# Access the value in the student column corresponding to the RowA label
print("\nValue = ",df.loc['RowA', 'Student'])

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Value =  Amit
"""


# In[3]:


"""
Access a group of rows or columns by integer positions in a Pandas DataFrame
The dataframe.iloc is used to access a group of rows or columns by integers
"""

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
 
# Access using rows and columns by integer positions
print("\nValue = \n",df.iloc[[1,2]])

"""
Student Records
 
      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90
 
Value = 
      Student  Rank  Marks
RowB    John     4     70
RowC   Jacob     3     80
"""


# In[4]:


#The index argument is used to set and name your indexes in a DataFrame

import  pandas as pd
 
# Dataset
data = {
  'Student': ["Amit", "John", "Jacob", "David", "Steve"],
  'Rank': [1, 4, 3, 5, 2],
  'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method
# The index argument is used to set the index
df = pd.DataFrame(data,  index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'],)
 
print("Student Records\n\n",df)

"""
Student Records
 
          Student  Rank  Marks
Student1    Amit     1     95
Student2    John     4     70
Student3   Jacob     3     80
Student4   David     5     60
Student5   Steve     2     90
"""


# In[5]:


"""
Iterate a DataFrame
To iterate a DataFrame and display the column names, use the for loop
"""

import pandas as pd
 
# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve"],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}
 
# Create a DataFrame using the DataFrame() method
# The index argument is used to set the index
df = pd.DataFrame(data, index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'], )
 
print("Student Records\n\n", df)
 
# Iterating to display the columns
print("\nDisplaying the columns:")
for col in df:
   print(col)

"""
Student Records
 
          Student  Rank  Marks
Student1    Amit     1     95
Student2    John     4     70
Student3   Jacob     3     80
Student4   David     5     60
Student5   Steve     2     90
 
Displaying the columns:
Student
Rank
Marks
"""


# In[6]:


"""
Here we access multiple rows and the specific columns in those rows
"""

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
 
# Access the value in the student column corresponding to the RowA label
print("\nValue = ",df.loc[['RowA','RowB','RowC'],'Student'])

"""
Student Records

      Student  Rank  Marks
RowA    Amit     1     95
RowB    John     4     70
RowC   Jacob     3     80
RowD   David     5     60
RowE   Steve     2     90

Value =  RowA     Amit
RowB     John
RowC    Jacob
Name: Student, dtype: object
"""


# In[ ]:




