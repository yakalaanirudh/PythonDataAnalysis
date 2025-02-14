#!/usr/bin/env python
# coding: utf-8

# In[1]:
"""
Factor plot is deprecated and we use cat plot
We can draw all types of before discussed plot use cat plot by passing its type in king argument

we can create multiple plots for each gender and city
in the below example 2 cols for gender and 3 rows for cities.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# In[57]:

#p=sns.catplot(data=mart,x='Payment',y='Total',col='Gender',kind='box',row='Customer type',color='black')
p=sns.catplot(data=mart,x='Payment',y='Total',col='Gender',kind='box',row='Customer type',palette='CMRmap_r')
# p.set_titles(col_template="{col_name}")

