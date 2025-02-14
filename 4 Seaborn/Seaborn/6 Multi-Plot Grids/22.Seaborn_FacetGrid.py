#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.columns = mart.columns.str.lower()
mart.head()


# In[3]:


mart.outlet_size.unique()
#  we get an array of size 3 which is the outlet size small, medium and large

# In[4]:


mart.outlet_location_type.unique()
#  we get an array of size 3 which is the location type Tier1,Tier2 and Tier3

# In[5]:
"""
the plot can be any scatter,hist,box,kde any plot
we get three plots absed on outlet size
in each of these plots we apply hue
"""

Example1=sns.FacetGrid(mart,col='outlet_size')
Example1.map_dataframe(sns.scatterplot,x='outlet_year',y='sales',hue='outlet_location_type'
                       ,marker='+'
                       ,alpha=0.5
                       ,color='red'
                       ,s=100)


# In[6]:
"""
Example1=sns.FacetGrid(mart,row='outlet_location_type',col='outlet_size')
a matrix based on rows and columns

Example2=sns.FacetGrid(mart,col='outlet_size',row='outlet_location_type',sharey=False,ylim=(0,1000))
setting y axis limit for all plts and setting if the all plots same share same axis limits or not

Example2.map_dataframe(sns.histplot,x='sales')
setting what type of plot to plot and on what data

Example2.set_axis_labels('sales','count')
set the labels for the x and y axis

Example2.set_titles(col_template='{col_name} Size',row_template='{row_name} Type')
setting plot titles for each graph based on row and column names
"""

Example2=sns.FacetGrid(mart,col='outlet_size',row='outlet_location_type',sharey=False,ylim=(0,1000))
Example2.map_dataframe(sns.histplot,x='sales')
Example2.set_axis_labels('sales','count')
Example2.set_titles(col_template='{col_name} Size',row_template='{row_name} Type')
 