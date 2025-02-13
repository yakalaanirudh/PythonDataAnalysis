#!/usr/bin/env python
# coding: utf-8

# In[1]:


#use the bar() method

import matplotlib.pyplot as plt
import numpy as np
 
# x and y coordinates
student = np.array(["Tim", "John", "Amit", "Jacob", "Karl", "Gary"])
marks = np.array([85, 59, 99, 77, 67, 95 ])
 
# Plot a bar graph using the pyplot.bar() method
# The x and y coordinates below are the student and marks respectively
plt.bar(student, marks)
 
# The labels for x-coordinate and y-coordinate
plt.xlabel("Student")
plt.ylabel("Marks")
 
# Display the figure
plt.show()


# In[ ]:




