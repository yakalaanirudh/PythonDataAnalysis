#!/usr/bin/env python
# coding: utf-8

# **1.Installing Seaborn**

# In[ ]:


pip install seaborn


# **2.Importing all the required libraries**

# In[77]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **3.Import the data**

# In[76]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **4.Create a COUNTPLOT**

# In[78]:

# This creates a count plot with number of records for each gender

sns.countplot(x='Gender',data=mart)

