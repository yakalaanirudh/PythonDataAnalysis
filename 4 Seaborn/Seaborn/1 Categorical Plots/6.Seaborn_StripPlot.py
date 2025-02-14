#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**
# A strip plot has a point for every observation
#If a point exits at same point w euse gitter to slightly move teh point 
# a strip plot can be combined with both violin plot and box plot
# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Import the supermart data excel file**

# In[2]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **3. Create a basic STRIP PLOT**

# In[3]:


sns.stripplot(data=mart, y='Total')


# **4. Expand markers in STRIP PLOT using jitter**

# In[4]:
#If a point exits at same point w euse gitter to slightly move teh point 
# a strip plot can be combined with both violin plot and box plot

sns.stripplot(data=mart, y='Total',jitter=0.2)


# **5. Draw line around the points using LINEWIDTH**

# In[5]:
#the width of the line around each dot

sns.stripplot(data=mart, y='Total',linewidth=0.2)


# **6. Include third categorical variable with HUE**

# In[6]:
# each category gets two different points in same graph

sns.stripplot(data=mart, y='Total',x='Payment',hue='Gender',jitter=0.2,linewidth=0.5)


# **7. Separate each level of hue using DODGE**
# dodge =true creates two different graphs for each hue
# In[7]:


sns.stripplot(data=mart, y='Total',x='Payment',hue='Gender',jitter=0.2,linewidth=0.5,dodge=True)


# **8. Draw the strips on top of VIOLIN PLOT**

# In[8]:


sns.stripplot(data=mart, y='Total',x='Payment',jitter=0.1)
sns.violinplot(data=mart, y='Total',x='Payment',color='gray')


# **9. Draw the strips on top of BOX PLOT**

# In[9]:


sns.stripplot(data=mart, y='Total',x='Payment',color="black")
sns.boxplot(data=mart, y='Total',x='Payment',color='gray')

