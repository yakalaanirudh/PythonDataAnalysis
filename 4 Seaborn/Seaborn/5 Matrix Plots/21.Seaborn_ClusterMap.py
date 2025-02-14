#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Cluster map plots a matrix dataset as a hierarchially clustered heatmap

import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
import seaborn as sns
# from sunbird.categorical_encoding import frequency_encoding

pd.set_option('display.max_rows',None)


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.columns = mart.columns.str.lower()
mart.head(10)


# In[3]:


martPiv=mart.pivot_table(index='outlet_year',columns='outlet_size',values='sales')
martPiv.head()


# In[4]:
"""
In the cluster map all values of similar range are sorted together
,col_cluster=False
,row_cluster=False
removes columns and rows clustering

initially years are arranged based on similar values afte rremoving row clustering all years are ranged based on 
time
"""

sns.clustermap(martPiv
#               ,col_cluster=False
               ,row_cluster=False
               ,annot=True
               ,fmt='.0f'
#                ,z_score=1
               ,standard_scale=1
               ,linewidth=.5
              )


