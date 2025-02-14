#!/usr/bin/env python
# coding: utf-8

# In[1]:
"""
A rug plot plots marginal distributions by drawing ticks along x and y axis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as sts

pd.set_option('display.max_rows',None)


# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart = mart[['Gender','Payment','Unit price','Quantity','Total','gross income']]
mart.head(10)


# **1. Create a basic RUG plot for one variable**

# In[3]:


plt.figure(figsize=(15,5))
sns.rugplot(data=mart, x='Unit price')


# **2. Create a RUG plot for two variables**

# In[4]:


plt.figure(figsize=(15,5))
sns.rugplot(data=mart, x='Unit price',y='gross income')


# **3. Group it by a categorical variable using hue**

# In[5]:


plt.figure(figsize=(15,5))
sns.rugplot(data=mart, x='Unit price',y='gross income',hue='Gender')


# **4. Change the height of Rugs in the RUG Plot**

# In[6]:


plt.figure(figsize=(15,5))
sns.rugplot(data=mart, x='Unit price',y='gross income',hue='Gender',height=0.05)


# **5. Combine this with a KDE Plot**

# In[7]:


plt.figure(figsize=(15,5))
sns.kdeplot(data=mart, x='Unit price',y='gross income',hue='Gender',fill=True)
sns.rugplot(data=mart, x='Unit price',y='gross income',hue='Gender')


# **6. Combine this with a SCATTER PLOT**

# In[8]:


# plt.figure(figsize=(15,5))
sns.scatterplot(data=mart, x='Unit price',y='gross income',hue='Gender')
sns.rugplot(data=mart, x='Unit price',y='gross income',hue='Gender')


# **7. Show Rugs outside of the Axis**

# In[9]:
# Clip on and negative height makes the rugs appear outside of the graph like protruding outside

plt.figure(figsize=(15,5))
sns.kdeplot(data=mart, x='Unit price',y='gross income',hue='Gender',fill=True)
sns.rugplot(data=mart, x='Unit price',y='gross income',hue='Gender',height=-0.01,clip_on=False)

