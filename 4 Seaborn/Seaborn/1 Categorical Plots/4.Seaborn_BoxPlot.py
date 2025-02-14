#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required LIBRARIES**

"""
Box Plot provides mean, median,min,max,1st quartile,3rd quartile and outliers
"""

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import MART dataframe**

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")


# **3. Create a basic BOX plot on one NUMERIC variable**

# In[3]:
# width is the width of the box

sns.boxplot(y='Total',data=mart, width=0.2)


# **4. Create a basic BOX plot on one numeric variable by a CATEGORICAL variable**

# In[4]:


sns.boxplot(x='Payment',y='Total',data=mart)


# **5. Create a basic BOX plot on one numeric variable by TWO CATEGORICAL variable using HUE attribute**

# In[5]:


sns.boxplot(x='Payment',y='Total',hue='Gender',data=mart)


# **6. Add MEAN marker in the box plot using Showmeans attribute and change its style using meanprops**

# In[6]:
# mean is represented by a circular dot we need to activate it ny showmeans=True and its properties

sns.boxplot(x='Payment',y='Total',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"10"
                                                                                  ,"markeredgecolor":"black"})


# **7. Make HORIZONTAL box plot**

# In[7]:


sns.boxplot(x='Total',y='Payment',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"5"
                                                                                  ,"markeredgecolor":"black"})


# **8. Change PALETTE, LINE WIDTH etc..**

# In[8]:
# Line width is the width of the lines extending out

sns.boxplot(x='Total',y='Payment',hue='Gender',data=mart,showmeans=True,meanprops={"marker":"o"
                                                                                  ,"markerfacecolor":"white"
                                                                                  ,"markersize":"5"
                                                                                  ,"markeredgecolor":"black"}
           ,palette='CMRmap'
           ,linewidth=5)


# **9. Create box plot for EACH OF THE NUMERIC VARIABLE in the dataframe**

# In[9]:
# If we just pass data to box plot it will create a box plot for every parameter and we increased the size to make 
#every parameter visible

plt.figure(figsize=(15,5))

sns.boxplot(data=mart)

