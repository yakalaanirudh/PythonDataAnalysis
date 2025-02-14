#!/usr/bin/env python
# coding: utf-8

# In[1]:
# A relational plot can switch between line and scatter plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:
#.str.lower() converts all column names to lowercase.

mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx").sample(n=50)
mart.columns=mart.columns.str.lower()
mart.head()


# In[3]:


mart.to_excel("E:\Seaborn\supermarket_sales.xlsx",index=False)


# In[4]:
#kind=line make sthe plot line plot in relplot default is scatter
#by specifying row and col we create multiple plots
#col wrap controls the number of columns
"""
sns.relplot(data=mart,x='outlet_year',y='sales',s=100,hue='outlet_size', kind='line'
#            ,col='outlet_size'
#            ,row='tier'
#            ,hue='outlet_size'
           ,palette=['green','red','yellow'],
           col_wrap=3)

"""

sns.relplot(data=mart,x='outlet_year',y='sales',s=100,hue='outlet_size'
#            ,col='outlet_size'
#            ,row='tier'
#            ,hue='outlet_size'
           ,palette=['green','red','yellow'])

