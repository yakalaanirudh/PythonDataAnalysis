#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
To read an  Excel file in  Python, we use the Pandas read_csv() method. 
"""


# In[7]:


"""
This reads the file and prinst the dataframe
"""

import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv')
 
# Display the CSV file records
print("Our DataFrame =\n",df)


# In[8]:


"""
This reads the top n ros of the dataframeexcel file.
"""

import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv')
 
# Display the CSV file records
print("Our DataFrame =\n",df)
 
# Display the top n rows using the head()
print("Top 2 rows\n",df.head(2))


# In[9]:


"""
This reads the bottom n rows of the excel file.
"""

import pandas as pd
 
# Input CSV file
# Loading CSV in the DataFrame
df = pd.read_csv('Students.csv')
 
# Display the CSV file records
print("Our DataFrame =\n",df)
 
# Display the bottom n rows using the tail()
print(df.tail(2))


# In[ ]:




