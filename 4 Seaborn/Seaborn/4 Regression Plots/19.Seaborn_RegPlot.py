#!/usr/bin/env python
# coding: utf-8

# In[1]:
"""
PLot data and a linear regression model fit

Finds the best fit linear regression line which helps to predict the chnage in y for set change in x
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


tips = sns.load_dataset('tips')
tips.head()


# **1. Creat a basic reg plot**

# In[3]:


sns.regplot(data=tips,x='total_bill',y='tip')


# **2. Change the styling of reg plot, only line, only scatter, show/hide the ci, change the ci value, change n_boot**

# In[4]:
"""
modify the appearance of line and scatter plot independently
"""

sns.regplot(data=tips,x='total_bill',y='tip'
#            ,color='red'
#            ,marker='+'
           ,line_kws=dict(color='red',linestyle='--')
           ,scatter_kws=dict(s=100,color='green',alpha=0.5)
           ,ci=60
           ,n_boot=500)


# **3. Discuss aobut the statistical models in seaborn**

# In[5]:


sns.regplot(data=tips,x='total_bill',y='tip')

