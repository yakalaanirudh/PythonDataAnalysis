#!/usr/bin/env python
# coding: utf-8

# In[1]:


#use the hist() method
import matplotlib.pyplot as plt
import numpy as np
 
# Data to plot
arr = np.array([10, 50, 34, 67, 21, 7, 59, 62, 45, 48, 10, 8, 41, 32, 66, 59, 18, 26, 51, 9])
 
# Plot a Histogram using pyplot.hist() method
# The bins parameter sets the bin i.e. an integer or sequence
plt.hist(arr, bins = [0, 20, 40, 60, 80])
 
# The labels for x-coordinate and y-coordinate
plt.xlabel("Score")
plt.ylabel("Player")
 
# Display the figure
plt.show()


# In[ ]:




