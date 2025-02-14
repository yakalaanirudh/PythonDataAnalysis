#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.columns = mart.columns.str.lower()
mart.head(10)


# In[]:3
"""
We create a new table where row index is year and there are 3 columnswith outlet size
"""


martPiv = mart.pivot_table(index='outlet_year',columns='outlet_size',values='sales')
martPiv


# In[4]:
"""
square =True amkes the boxes sqaure shaped
annot=True makes the values of that box appear
fmt=.0f means no decimals
annot_kws=dict(size=15,weight='bold') means the size of the numbers in cells and make em bold
cmap means the color palette to color the cells
"""

sns.set_style('white')
plt.figure(figsize=(5,5))

sns.heatmap(martPiv
#            ,square=True
           ,annot=True
           ,fmt='.0f'
           ,annot_kws=dict(size=15,weight='bold')
           ,linewidths=0.5
           ,linecolor='black'
           ,cmap='OrRd_r')


# In[5]:
"""

mart.corr() creates a correlation map
we make a heat map of this correlation map
vmin,vmax and center are the min max and center values
"""
sns.heatmap(mart.corr()
           ,vmin=-1
           ,vmax=1
           ,center=0
           ,cmap='OrRd_r'
           ,annot=True
           ,fmt='.1f'
           ,annot_kws=dict(size=15,weight='bold')
           ,linecolor='black'
           ,linewidths=0.5)

