#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Plot pairwise relationships in a dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


iris = sns.load_dataset('iris')
# iris = iris[['species','sepal_length','petal_length']]
iris.head()


# **1. Creating a basic PAIR PLOT**

# In[3]:
"""
The diagonal is histogram by default and upper and lower triangles are scatter plots
"""

sns.pairplot(data=iris)


# **2. Changing the diagonal plot KIND to KDE, HIST or None**

# In[4]:
# Changing the diagonal kind from hist to kde

sns.pairplot(data=iris,diag_kind='kde')


# **3. Changing the non diagonal plot KIND to scatter, kde, hist or reg**

# In[5]: 


sns.pairplot(data=iris,kind="reg")


# **4. Adding hue to the PAIR PLOT**

# In[6]:


sns.pairplot(data=iris,hue='species')


# **5. Creating PAIR PLOT for specific list of variables (diag_kind=None)**

# In[7]:


sns.pairplot(data=iris,x_vars=['sepal_width','petal_width','petal_length'],y_vars=['sepal_length','sepal_width'],diag_kind=None)


# **6. Showing only the lower triangle using CORNOR arguement**

# In[8]:


sns.pairplot(data=iris,corner=True)


# **7. Making changes specific to Diagonal and Non-Diagonal plots separatly**

# In[9]:


sns.pairplot(data=iris,diag_kws=dict(color='green',kde=True)
            ,plot_kws=dict(color='red',marker=10,s=100))


# **8. Creating KDE plot on top of the PAIR PLOT using map_lower or upper**

# In[10]:
# This make sthe upper and lower triangle plots kde plots leaving the diagonal plots as histograms

l=sns.pairplot(data=iris,plot_kws=dict(color='red'))
l.map_upper(sns.kdeplot)
l.map_lower(sns.kdeplot)

