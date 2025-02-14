#!/usr/bin/env python
# coding: utf-8

# In[1]:
# ECDF empirical Cummulative Distribution Functions
# Represnets the proportion or count of observations falling below each unique value in distribution

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

pd.set_option('display.max_rows',None)


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head()


# In[3]:
# stat can be count or proportion

sns.ecdfplot(data=mart,y='gross income',hue='Gender',stat='count')

