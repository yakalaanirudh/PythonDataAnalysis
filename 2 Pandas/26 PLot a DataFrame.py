#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
To plot in Pandas, we need to use the plot() method and the Matplotlib library. 
The pyplot module from Matplotlib is also used for plotting in Pandas. 
The pyplot.show() is used to display the figure
"""


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Dataset
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 27, 20, 19],
    'Wind': [12, 20, 8, 9, 30, 27, 22, 33, 37, 35],
    'Precipitation':[17, 25, 20, 19, 18, 30, 28, 26, 29, 22]
}
 
df = pd.DataFrame(data)
 
df.plot()
 
plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Dataset
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 27, 20, 19],
    'Wind': [12, 20, 8, 9, 30, 27, 22, 33, 37, 35],
    'Precipitation':[17, 25, 20, 19, 18, 30, 28, 26, 29, 22]
}
 
df = pd.DataFrame(data)
 
df["Humidity"].plot(kind = 'hist')
 
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Dataset
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 27, 20, 19],
    'Wind': [12, 20, 8, 9, 30, 27, 22, 33, 37, 35],
    'Precipitation':[17, 25, 20, 19, 18, 30, 28, 26, 29, 22]
}
 
df = pd.DataFrame(data,  index=['City1', 'City2', 'City3', 'City4', 'City5', 'City6','City7', 'City8', 'City9','City10' ])
 
df.plot.pie(y='Humidity')
 
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Dataset
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 27, 20, 19],
    'Wind': [12, 20, 8, 9, 30, 27, 22, 33, 37, 35],
    'Precipitation':[17, 25, 20, 19, 18, 30, 28, 26, 29, 22]
}
 
df = pd.DataFrame(data)
 
df.plot(kind = 'scatter', x = 'Temperature', y = 'Humidity')
 
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
 
# Dataset
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 27, 20, 19],
    'Wind': [12, 20, 8, 9, 30, 27, 22, 33, 37, 35],
    'Precipitation':[17, 25, 20, 19, 18, 30, 28, 26, 29, 22]
}
 
df = pd.DataFrame(data)
 
df.plot.area()
 
plt.show()


# In[ ]:




