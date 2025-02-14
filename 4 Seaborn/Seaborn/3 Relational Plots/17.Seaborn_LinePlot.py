#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


mart = pd.read_csv("E:\Seaborn\supermarket_sales.xlsx")
mart[['Tier']]=mart['Outlet_Location_Type'].str.split(expand=True)[1]
mart.head()


# **1. Creat a basic line plot and try different estimators**

# In[3]:


#---Estimator = None"
# height = [5, 5, 7, 5, 8]
# age    = [22,42,30,35,40]
# sns.lineplot(x=age,y=height,estimator=None)

#---Estimator = sum
"""
height = [5, 6, 7, 6.5,4]
age    = [22,25,30,25,25]
sns.lineplot(x=age,y=height,estimator=sum)
"""

# In[4]:
#confidence intervation is the shaded area around thhe line
#estimator can be mean or sum if we want a point for all observations then it is none

sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None,estimator=None)


# **2. Test with different Confidence Intervals and with different number of Bootstraping**

# In[5]:
"""
ci can be mean or sum or standard deviation or 20 percent or 90 percent
nboot is also confidence interval
sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None)
"""
sns.lineplot(data=mart,x="Outlet_Year",y="Sales",n_boot=2)


# **3. Grouping using HUE and use different Palettes**

# In[6]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
             ,hue='Outlet_Size'
            ,palette=['red','green','blue'])


# **4. Grouping using Style, use different Marker and Dashes**

# In[7]:
#markers mean we get markers on the line
#dahes mean we get markers only at specific points on the line

sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
             ,style='Outlet_Size'
            ,markers=True
            ,dashes=False)


# **5. Grouping using Size**

# In[8]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
            ,size='Outlet_Size'
            ,sizes=(.5,5))


# **6. Use different semantic styling parameters on same or different variables**

# In[9]:


sns.lineplot(data=mart,x="Outlet_Year",y="Sales",ci=None
            ,hue='Outlet_Size'
#             ,style='Outlet_Size'
#             ,markers=True
             ,size='Tier'
            )

