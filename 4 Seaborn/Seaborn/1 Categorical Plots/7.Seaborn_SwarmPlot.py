#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**
"""
A swarm plot is similar to scatter plot except each point in a swarm plot is represnted separately.
A swarm plot can be combined with violin and box plot
"""
# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import the supermarket sales data excel file**

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **3. Create a basic SWARM PLOT on Total column**

# In[3]:


sns.swarmplot(data=mart,y='Total')


# **4. Create SWARM PLOT group by CATEGORIES**

# In[4]:


sns.swarmplot(data=mart,y='Total',x='Payment',hue='Gender')


# **5. Showing Hues Separatly on the categorical axis**

# In[5]:
# Hue creates two interlying plots
# split seperates them

plt.figure(figsize=(15,5))
sns.swarmplot(data=mart,y='Total',x='Payment',hue='Gender',split=True)


# **6. Styling a SWARM - Change the marker, size, color, edge color.....**
#marker='*', color='greeen    marker turns from  dot to *   color of points
#edge color of points and size
# In[6]:


plt.figure(figsize=(15,5))
sns.swarmplot(data=mart,y='Total',x='Payment',size=10,color='green',edgecolor='black')


# **7. Overlay a SWARM PLOT on a BOX PLOT**

# In[7]:


sns.boxplot(data=mart,y='Total',x='Payment')
sns.swarmplot(data=mart,y='Total',x='Payment',color='black')


# **8. Overlay a SWARM PLOT on a VIOLIN PLOT**
#inner=None removes inner box plot from violin plot
# In[8]:


sns.violinplot(data=mart,y='Total',x='Payment',inner=None,width=1)
sns.swarmplot(data=mart,y='Total',x='Payment',color='white')

