#!/usr/bin/env python
# coding: utf-8

# In[1]:
# A Joint plot can draw a plot of two variables with bivariate and univariate graphs
#Liek it has a scatter plot/kde plot in the middle and histograms/rug plots with kde on the x and y axis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns",None)


# In[2]:


iris = sns.load_dataset('iris')
iris.head()


# **1. Drawing a first basic JOINT Plot**

# In[3]:


sns.jointplot(data=iris,x='sepal_length',y='petal_length')


# **2. Change its kind to “scatter”|“kde”|“hist”|“hex”|“reg”|“resid”**

# In[4]:


sns.jointplot(data=iris,x='sepal_length',y='petal_length'
             ,kind='resid')


# **3. Grouping based on a categorical variable**

# In[5]:


sns.jointplot(data=iris,x='sepal_length',y='petal_length'
             ,hue='species')


# **4. Formatting All and Individual Plots**

# In[6]:
#joint kws is for formatting the main plot,  and marginal is for marginal plots

sns.jointplot(data=iris,x='sepal_length',y='petal_length'
#              ,color='red'
#              ,hue='species'
#              ,palette='BuPu'
             ,joint_kws=dict(marker='+'
                            ,color='red')
             ,marginal_kws=dict(color='green',kde=True))


# **5. Adjust height, ratio, space and show/hide the marginal_ticks**

# In[7]:
# ratio is size ratio to edge plots space is space between main and marginal plots
# marginal ticks is for having marginal ticks on the marginal graphs

sns.jointplot(data=iris,x='sepal_length',y='petal_length'
             ,height=5
             ,ratio=3
#              ,space=5
             ,marginal_ticks=True)


# **6. Plot KDE and RUG on top of Joint Plot**

# In[8]:
#  Here we plot a scatter plot, a kde and a rug plot in centre with marginal plots on margins

l=sns.jointplot(data=iris,x='sepal_length',y='petal_length',joint_kws=dict(color='red'))
l.plot_joint(sns.kdeplot)
l.plot_joint(sns.rugplot,height=0.1,color='red')

