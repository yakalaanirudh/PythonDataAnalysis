#!/usr/bin/env python
# coding: utf-8

# **1.Importing all the required libraries**

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2.Import the data**

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **3.Create a basic COUNTPLOT to get number of transaction for each of the product line and change the figure size**

# In[3]:
# We add figure size in matpllotlib to modify the graph scale

plt.figure(figsize=(15,5))

sns.countplot(x="Product line",data=mart)


# **4.Make it horizontal bar plot**

# In[4]:


sns.countplot(y="Product line",data=mart)


# **5.Add hue to get the count on two categories i.e. Product line and Gender**

# In[5]:
# Hue disscets each bar again by gender

plt.figure(figsize=(15,5))

sns.countplot(x="Product line",hue="Gender",data=mart)


# **6.Using different color palette**

# In[6]:
# palette assigns each gender a color


plt.figure(figsize=(15,5))

sns.countplot(x="Product line",hue="Gender",data=mart,palette='PuBuGn_r')


# **7.Change Style using facecolor, linewidth and edge color**

# In[7]:
# width of each bar and color of the edge and the color of the bars

plt.figure(figsize=(15,5))

sns.countplot(x='Product line',data=mart
             ,facecolor = (0,0,0,0)
             ,linewidth=5
             ,edgecolor=sns.color_palette('dark',3))

