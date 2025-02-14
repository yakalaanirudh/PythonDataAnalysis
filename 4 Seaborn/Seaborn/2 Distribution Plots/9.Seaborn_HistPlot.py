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


# **1. Create a basic HISTOGRAM on X or Y axis**

# In[1]:


sns.histplot(data=mart,y='Total')


# **2. Change the Bins Width using binwidth arguement**

# In[2]:

#sns.histplot(data=mart,x='Total',bins=30)
sns.histplot(data=mart,x='Total',binwidth=150)


# **3. Change Number of Bins and Interval**

# In[3]:


plt.figure(figsize=(15,5))
sns.histplot(data=mart,x='Total',bins=np.arange(0,1100,50))
plt.xticks(np.arange(0,1100,50))            #x axis labels


# **4. Combine with KDE**

# In[4]:
# adds a smooth lien of normal distribution

sns.histplot(data=mart,x='Total',kde=True)


# **5. Use a categorical variable in HUE and STACK it using MULTIPLE agruement**

# In[5]:
# Here each payment range is divided[in the same bar liked stacked] by different color

sns.histplot(data=mart,x='Total',hue='Payment',multiple='stack')


# **6. Make it a step/poly plot using ELEMENT arguement and change the FILL**

# In[6]:
#Looks Like an area graph

sns.histplot(data=mart,x='Total',hue='Payment',element='poly')


# **7. Use categorical variable and shrink it**

# In[50]:
# we can use probability, count, frequency and density
# Like hoe much probability payment might be through card, cash,ewallet
sns.histplot(data=mart,x='Total',stat='probability')


# **8. Create a Bivariate Histogram**

# In[51]:
# A histogram for two variables

sns.histplot(data=mart,x='Total',y='gross income')

