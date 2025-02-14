#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# **1. Create a basic KDE plot for Total column**

# In[3]:


sns.kdeplot(data=mart, x='Total')


# **2. Create KDE for all the numeric variables in dataframe**

# In[4]:
# If we dont specify aprameter it creates a kde plot for all variables

sns.kdeplot(data=mart)


# **3. Adjust the smooting using bw_adjust**
#band width adjustment for smoothening
# In[5]:


sns.kdeplot(data=mart,x='Total',bw_adjust=0.5)


# **4. Group the KDE on a category variable**

# In[6]:


sns.kdeplot(data=mart,x='Total',hue='Payment')


# **5. Stack KDE on a category using MULTIPLE arguement**

# In[7]:


sns.kdeplot(data=mart,x='Total',hue='Payment',multiple='stack')


# **6. Use log scaling to map the variable in KDE**

# In[8]:
#x axis is logarithmic

sns.kdeplot(data=mart,x='Total',log_scale=True)


# **7. Change styling of hued KDE using linewidth, palette, alpha etc....**

# In[9]:
# alpha is transparency

sns.kdeplot(data=mart,x='Total',hue='Payment',multiple='stack',linewidth=5,palette='Dark2',alpha=0.5)


# **8. Creat a bivariate KDE**

# In[10]:
# Like a bivariate histogram

sns.kdeplot(data=mart, x='Unit price',y='gross income')


# **9. Group the bivariate KDE on a categorical variable and show the contours**

# In[11]:


sns.kdeplot(data=mart, x='Unit price',y='gross income',hue='Gender',fill=True,levels=5,thresh=0.2)

