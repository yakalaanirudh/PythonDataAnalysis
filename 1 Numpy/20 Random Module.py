#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
from numpy import random

Command to import random module from numpy
"""


# In[2]:


#Generate a Random number
#To generate a random number, we have used the randint() method of the random module. Let us see an example:


from numpy import random
 
# Get random number from 0 to 5
n = random.randint(5)
 
print("Random number= ",n)

"""
Output

1
2
3
 
Random number=  4
"""


# In[3]:


#Generate a random array with a fixed size
#We will generate random elements of an array using the random.randint() method. 
#The size of the array is set using the size parameter. Let us see an example:

 
from numpy import random
 
# get 3 random numbers as array elements from 0 to 10
n = random.randint(10, size=(3))
 
print("Random number= ",n)

"""
Random number=  [6 0 1]
"""


# In[4]:


#Generate one of the random values based on an array of values
#One of the random values based on an array of values can be generated using the choice() method of the random module. 


 
from numpy import random
 
# get a random number from the following array values
n = random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
 
print("Random number= ",n)
 
"""
Output
 
Random number=  100
"""


# In[ ]:




