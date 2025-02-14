#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Displot can create hist plot kde plot rug plot and ecdf

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income','Branch']]
mart.head()


# In[3]:
#rug_kws is rug keywords . It should be a dictionary

sns.displot(data=mart,y='Total',kde=True,rug=True,rug_kws={'height':0.05},hue='Payment',multiple='stack',col='Branch',row='Gender')


# In[4]:
#many plots based on branch and gender
#Has 2 rows cause of 2 genders
#has 3 cols because 3 branch locations

sns.displot(data=mart,y='Total',kind='ecdf',hue='Payment',col='Branch',row='Gender')

