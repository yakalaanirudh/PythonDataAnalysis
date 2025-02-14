#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**
# violin plot is combination of box plot and kernel density
# the width of the violin plot is kernel density
# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import the supermart data excel file**

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **3. Create a basic VIOLINPLOT**

# In[3]:


sns.violinplot(y="Total",data=mart)


# **4. Create a VIOLINPLOT on two categorical and one numeric variable and use split**

# In[4]:


sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True)


# **5. Change the box in the VIOLINPLOT to horzontal lines**

# In[5]:
#a violin plot the left and right are mirror images
# by using split = true we can make left as one property and right as another
#like left is hue gender male and right is hue gender femlae
# this way left and right are not mirror images
# inner =quartile removes the inner box plot and replaces it with quartile values
sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile')


# **6. Draw line for each observations in a VIOLINPLOT**

# In[6]:
#inner=stick makes a line for every observationn in the data [very slow]

sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='stick')


# **7. Change the amount of smoothing using bw attribute**

# In[7]:
#we can smoothen the violin plot by using bandwidth parameter

sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile',bw=.2)


# **8. Cut out the extreme values**

# In[8]:
# cut=0 removes the extreme values of the violin plot

sns.violinplot(x='Payment',y='Total',hue='Gender',data=mart,split=True,inner='quartile',bw=.2,cut=0)

