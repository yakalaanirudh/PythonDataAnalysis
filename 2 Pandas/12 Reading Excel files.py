#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
To read an  Excel file in  Python, we use the Pandas read_excel() method. 
First, install the openpyxl package using pip. Type the following command to install openpyxl:
"""


# In[2]:


"""
This reads the file and prinst the dataframe
"""

import pandas as pd
 
# Input Excel File
# Load the Excel in the DataFrame
dataFrame = pd.read_excel('Tennis.xlsx')
 
# Display the Excel file records
print("Our DataFrame =\n", dataFrame)


# In[4]:


"""
This reads the top n ros of the dataframeexcel file.
"""
import pandas as pd
 
# Input Excel File
# Load the Excel in the DataFrame
dataFrame = pd.read_excel('Cricket.xlsx')
 
# Display the Excel file records
print("Our DataFrame =\n", dataFrame)
 
print("\nDisplay top 2 rows =\n",dataFrame.head(2))


# In[5]:


"""
This reads the bottom n rows of the excel file.
"""

import pandas as pd
 
# Input Excel File
# Load the Excel in the DataFrame
dataFrame = pd.read_excel('Cricket.xlsx')
 
# Display the Excel file records
print("Our DataFrame =\n", dataFrame)
 
print("\nDisplay last 2 rows =\n",dataFrame.tail(2))


# In[ ]:




