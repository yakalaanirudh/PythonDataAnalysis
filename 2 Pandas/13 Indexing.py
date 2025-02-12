#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
We can directly use the [] i.e. the indexing operator in Pandas to retrieve records

Since the index is name and we are only seeking marks, rank is omitted.
"""
import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv',index_col ="Student")
 
# Display the CSV file records
print("Our DataFrame =\n", df)
 
# Use the indexing operator
res = df["Marks"]
 
# Retrieving marks of students
print("\n",res)

"""
Our DataFrame =
 
Student Rank Marks
Amit      1  95 
Virat     2  90
David     3  80 
Will      4  75 
Steve     5  65
 
Student	
Amit	95
Virat	90
David	80
Will	75
Steve	65
"""


# In[2]:


"""
Fetch inly results of Amit
print("\n",df.loc["Amit"])
"""

import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv',index_col ="Student")
 
# Display the CSV file records
print("Our DataFrame =\n", df)
 
# Retrieving a single row with Name Amit
print("\n",df.loc["Amit"])

"""
Our DataFrame
 
Student	Rank Marks
Amit     1    95
Virat    2    90
David    3    80
Will     4    75
Steve    5    65
 
Rank    1
Marks  95
Student: Amit, dtype:object
"""


# In[3]:


"""
In iloc we use index
"""
import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv',index_col ="Student")
 
# Display the CSV file records
print("Our DataFrame =\n",df)
 
# Retrieving row 3 records
res = df.iloc[2]
print("\n",res)
 
"""
Our DataFrame =
 
Student	Rank	Marks
Amit	1	95
Virat	2	90
David	3	80
Will	4	75
Steve	5	65
 
Student David
Rank 3
Marks 80
 
"""


# In[ ]:




