#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""

To plot a pie chart in Matplotlib, use the pie() method. The pyplot.pie() method has the following parameters:

The 1st parameter is x, the wedge sizes are set here
The labels parameter is the sequence of strings providing the labels for each wedge
The third parameter is autopct, a string that labels the wedges with their numeric value. 
The label will be placed inside the wedge. If autopct is a format string, the label will be fmt % pct
"""


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
 
# Data
player = np.array(["Tim", "John", "Amit", "Jacob", "Karl", "Gary"])
score = np.array([85, 59, 99, 77, 67, 95 ])
 
# Plot a pie chart using the pyplot.pie() method
plt.pie(score, labels = player, autopct='%1.2f%%')
 
# Display the figure
plt.show()


# In[ ]:




