#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
A legend in a graph is a box on the left and right displaying the data from the columns. 
Legend generally helps the readers in understanding the graph.

The legend() function is used to create a legend in Matplotlib.
"""

"""
plt.plot(x, y)

Matplotlib implicitly creates a figure (plt.figure()) and an axis (plt.subplot(1,1,1)) behind the scenes.
This works fine for simple plots, but it limits control over multiple subplots, figure customization, or advanced plotting.


fig = plt.figure()  # Creates an empty figure
ax = plt.subplot()  # Creates an axis (subplot) inside the figure

More Control: You can modify figure properties separately from axes.
Multiple Subplots: Helps when working with multiple plots in the same figure.
Object-Oriented Approach (Recommended): This method makes it easier to work with multiple axes.

Summary
plt.plot(x, y)	Simple, single-plot visualizations.
fig, ax = plt.subplots()	When you need multiple subplots or more customization.


"""

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
 
# Data
a = np.arange(5)      #creates a NumPy array with values ranging from 0 to 4.
b = [2,4,6,8,10]
c = [5, 6, 7, 8, 9]
 
# Create plots
fig = plt.figure()               #Creates a figure (a blank canvas for plotting).
ax = plt.subplot()              #Creates an axes object (ax), where the actual plotting happens.
ax.plot(a, b, 'k--', label='Frequency')
ax.plot(a, c, 'k:', label='Periods')
 
# Create a legend using the Matplotlib Axes.legend() method in  Python
ax.legend()
 
# Plot Title
plt.title("Frequency of a Signal")
 
# Display
plt.show()


# In[3]:


"""
Position of the legend

‘upper left’, ‘upper right’, ‘lower left’, ‘lower right’
‘upper center’, ‘lower center’, ‘center left’, ‘center right’
‘center’

"""


import numpy as np
import matplotlib.pyplot as plt
 
# Data
a = np.arange(5)
b = [2,4,6,8,10]
c = [5, 6, 7, 8, 9]
 
# Create plots
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label='Frequency')
ax.plot(a, c, 'k:', label='Periods')
 
# Create a legend using the Matplotlib Axes.legend() method in  Python.
# Set the position using the loc parameter of the legend() method
ax.legend(loc='upper center')
 
# Plot Title
plt.title("Frequency of a Signal")
 
# Display
plt.show()
 


# In[4]:


"""
The set_facecolor() function in Matplotlib is used to set the background color of the legend

"""

import  numpy as np
import matplotlib.pyplot as plt
 
# Data
a = np.arange(5)
b = [2,4,6,8,10]
c = [5, 6, 7, 8, 9]
 
# Create plots
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label='Frequency')
ax.plot(a, c, 'k:', label='Periods')
 
# Create a legend using the Matplotlib Axes.legend() method in Python.
# Set the position using the loc parameter of the legend() method
legend = ax.legend(loc='upper center')
 
# Set the background color of the legend using the set_facecolor() function
legend.get_frame().set_facecolor('red')
 
# Plot Title
plt.title("Frequency of a Signal")
 
# Display
plt.show()


# In[5]:


"""
To increase or decrease the font size of legends in a graph, use the fontsize parameter of the legend() method. 
The value of the fontsize can be:

xx-small
x-small
small
medium
large
x-large
xx-large
"""


import  numpy as np
import matplotlib.pyplot as plt
 
# Data
a = np.arange(5)
b = [2,4,6,8,10]
c = [5, 6, 7, 8, 9]
 
# Create plots
fig = plt.figure()
ax = plt.subplot()
ax.plot(a, b, 'k--', label='Frequency')
ax.plot(a, c, 'k:', label='Periods')
 
# Create a legend using the Matplotlib Axes.legend() method in Python.
# Set the position using the loc parameter of the legend() method
# Set the fontsize parameter of the legend() method to change the font size
legend = ax.legend(loc='upper center', fontsize='xx-large')
 
# Plot Title
plt.title("Frequency of a Signal")
 
# Display
plt.show()


# In[ ]:




