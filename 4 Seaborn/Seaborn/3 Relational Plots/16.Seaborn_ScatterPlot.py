#!/usr/bin/env python
# coding: utf-8

# In[1]:
# A scatter plot shhows the relationship between two properties

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:
"""
Read Excel file and and load a sample of size 50 rows
Here, you're creating a new column 'Tier' in the DataFrame mart.

mart['Outlet_Location_Type'].str.split(expand=True) splits 
each value in the 'Outlet_Location_Type' column into separate columns.

[1] selects the second column created by the split operation, 
which contains the 'Tier' information (assuming your location types are formatted consistently).
"""

mart = pd.read_csv("E:\Seaborn\supermarket_sales.xlsx").sample(50)
mart[['Tier']]=mart['Outlet_Location_Type'].str.split(expand=True)[1]
mart.to_excel("E:\Seaborn\supermarket_sales.xlsx",index=False)


# **1. Create a basic SCATTER PLOT**

# In[3]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales')


# **2. Grouping basis on a categorical variable using HUE**

# In[4]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',hue='Outlet_Size')


# **3. Grouping basis on a categorical variable using STYLE and Styling Markers as well**

# In[5]:

# Style the points based on outlet size
sns.scatterplot(data=mart,x='Item_MRP',y='Sales',style='Outlet_Size'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **4. Grouping basis on a categorical variable using HUE & STYLE both together**

# In[6]:
# Color,style and size the points based on outlet size

sns.scatterplot(data=mart,x='Item_MRP',y='Sales',style='Outlet_Size'
                ,hue='Outlet_Size'
                ,s=200
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **5. Grouping basis on numeric variable using HUE and use PALETTE**

# In[7]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales'
#                 ,style='Outlet_Size'
                ,hue='Outlet_Size'
                ,palette='Purples_r'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **6. Grouping basis on a numeric variable using HUE & SIZE**

# In[8]:
# Here size is in a range of 2 to 200

sns.scatterplot(data=mart,x='Item_MRP',y='Sales'
                ,hue='Outlet_Size'
                ,size='Tier'
                ,sizes=(20,200)
                ,legend='full'
                ,palette='Purples_r'
                ,markers={"High":"^","Small":"v","Medium":"o"})


# **7. Change the Marker size with S arguement**

# In[9]:


sns.scatterplot(data=mart,x='Item_MRP',y='Sales',s=500,color='red',edgecolor='black')

