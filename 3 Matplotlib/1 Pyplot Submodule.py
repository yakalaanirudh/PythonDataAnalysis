#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
import matplotlib.pyplot as plt

bar(): For a bar plot
hist(): Plot a Histogram
pie(): Plot a pie chart
scatter(): Form a scatter plot
stem(): Form a stem plot
step(): Form a step plot
"""


# In[3]:


import matplotlib.pyplot as plt
import numpy as np
 
# xpts for x-coodinate
# ypts for y-coordinate

#Creates a NumPy array named xpts with two values: 0 and 10.
#Creates a NumPy array named ypts with two values: 0 and 125.
xpts = np.array([0, 10])
ypts = np.array([0, 125])
 
# Plot using the pyplot.plot() method
plt.plot(xpts, ypts)
 
# Display the figure
plt.show()


# In[ ]:




