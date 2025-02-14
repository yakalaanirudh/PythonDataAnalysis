#!/usr/bin/env python
# coding: utf-8

# **1. Import all the required libraries**

# In[1]:
# Bar plot is similar to count plot
# In bar plot we can calculate aggreagte values like mean and median and we have error bars as well

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# **2. Display the SEBORN dataset names and load one of them for example**

# In[2]:


# sns.get_dataset_names()
titanic=sns.load_dataset('titanic')
titanic.head()


# **3. Import mart dataframe**

# In[3]:


mart = pd.read_excel("E:\Seaborn\supermarket_sales.xlsx")
mart.head()


# **4. Create a basic BARPLOT**

# In[4]:

# fig size to modify size of graph
plt.figure(figsize=(15,5))          

sns.barplot(x='Product line',y='Total',data=mart)


# **5. Add HUE to the barplot**

# In[5]:

# Hue to split in this case based on gender like a 3rd dimension
plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart)


# **6. Make the barplot HORIZONTAL**

# In[6]:


plt.figure(figsize=(15,5))

sns.barplot(x='Total',y='Product line',data=mart)


# **7. Plot the bars in a given ORDER**

# In[7]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female'])


# In[8]:


x=mart['Product line'].sort_values()
x.unique()


# **8. Add CAP on the ERROR BAR**

# In[9]:
# capsize is the error bar above the bars

plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,capsize=0.2)


# **9. REMOVE the error bar using ci**

# In[10]:
# ci=None removes the error bars

plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,ci=None)


# **10. Change bar colors using COLOR attribute**

# In[11]:


plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,hue_order=['Male','Female']
           ,color='red')


# **11. Change color using PALLETE attribute**

# In[12]:
# color is single color while palette gives a range if colors

plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis')


# **12. Using SATURATION parameter**

# In[13]:
# saturation is color brightness

plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis'
           ,saturation=0.1)


# **13. CHANGE DEFAULT AGGREGATION METHOD USING ESTIMATOR PARAMETER**

# In[14]:
# in bar graph the default aggregation is mean by using estimator we can chnage it to other aggregation methods

plt.figure(figsize=(15,5))

sns.barplot(x='Product line',y='Total',hue='Gender',data=mart,order=['Electronic_accessories', 'Fashion_accessories','Food_and_beverages', 'Health_and_beauty', 'Home_and_lifestyle','Sports_and_travel']
           ,palette='cividis'
           ,estimator=np.median)

