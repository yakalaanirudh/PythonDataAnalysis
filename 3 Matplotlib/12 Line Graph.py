#!/usr/bin/env python
# coding: utf-8

# In[1]:


#use the plot() method. By default, plot() creates a line.


import matplotlib.pyplot as plt
import numpy as np
 
# Data to plot a line
xPts = np.array([1, 9])
yPts = np.array([4, 12])
 
# Plot a line graph using the pyplot.plot() method
# The two parameters are x and y axis
plt.plot(xPts, yPts)
 
# Display the figure
plt.show()


# In[ ]:




