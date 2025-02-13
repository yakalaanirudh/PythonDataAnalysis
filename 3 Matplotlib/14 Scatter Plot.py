#!/usr/bin/env python
# coding: utf-8

# In[1]:


#use the scatter() method

import matplotlib.pyplot as plt
 
# Data to plot
# Score of two Teams
team1_Score = [25, 47, 34, 38, 27, 40, 42, 18]
team2_Score = [7, 22, 40, 29, 27, 10, 19, 31]
 
# Score Range of tailenders (lower order batsman) in Cricket
scoreRange = [5, 10, 15, 20, 25, 30, 35, 40]
 
# Plot a Scatter Plot using pyplot.scatter() method
plt.scatter(team1_Score, scoreRange, color='r')
plt.scatter(team2_Score, scoreRange, color='b')
 
# The labels for x-coordinate and y-coordinate
plt.xlabel("Team Score")
plt.ylabel("Score Range")
 
# Display the figure
plt.show()


# In[ ]:




