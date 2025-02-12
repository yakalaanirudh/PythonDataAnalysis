#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The groupby() method is used in Pandas to split the object. 
#We can define groupby() as grouping the rows/columns into specific groups.
import pandas as pd
 
# Our Dataset
data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Year': [2023, 2022, 2021, 2022, 2018, 2019]
}
 
# Our DataFrame
df = pd.DataFrame(data)
 
# Display the records
print("Player Records\n\n", df)
 
# Group the data on Player value
res = df.groupby('Player')
 
# Print the first entry
print("\n", res.first())

"""
Player Records
 
   Player  Rank  Year
0   Amit     1  2023
1   John     4  2022
2   Amit     3  2021
3  David     5  2022
4  Steve     2  2018
5   John     7  2019
 
         Rank  Year
Player            
Amit       1  2023
David      5  2022
John       4  2022
Steve      2  2018
"""


# In[2]:


import pandas as pd
 
# Our Dataset
data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Year': [2023, 2022, 2021, 2022, 2018, 2019]
}
 
# Our DataFrame
df = pd.DataFrame(data)
 
# Display the records
print("Player Records\n\n", df)
 
# Group by Player
groupRes = df.groupby('Player')
 
for name,group in groupRes:
   print("\n",name)
   print(group)
    
    
"""
 Player Records
 
   Player  Rank  Year
0   Amit     1  2023
1   John     4  2022
2   Amit     3  2021
3  David     5  2022
4  Steve     2  2018
5   John     7  2019
 
 Amit
  Player  Rank  Year
0   Amit     1  2023
2   Amit     3  2021
 
 David
  Player  Rank  Year
3  David     5  2022
 
 John
  Player  Rank  Year
1   John     4  2022
5   John     7  2019
 
 Steve
  Player  Rank  Year
4  Steve     2  2018   
"""


# In[3]:


#Use the groups property in Python Pandas to view the group
import pandas as pd
 
# Our Dataset
data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Year': [2023, 2022, 2021, 2022, 2018, 2019]
}
 
# Our DataFrame
df = pd.DataFrame(data)
 
# Display the records
print("Player Records\n\n", df)
 
# Group by Player and Display
print(df.groupby('Player').groups)


"""
Player Records
 
   Player  Rank  Year
0   Amit     1  2023
1   John     4  2022
2   Amit     3  2021
3  David     5  2022
4  Steve     2  2018
5   John     7  2019
{'Amit': [0, 2], 'David': [3], 'John': [1, 5], 'Steve': [4]}
"""


# In[4]:


#To get the mean of the grouped data, first, group and then use the agg() method with numpy.mean().

import pandas as pd
import numpy as np
 
# Our Dataset
data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Points': [95, 70, 65, 80, 90, 50],
    'Year': [2023, 2022, 2021, 2022, 2023, 2019]
}
 
# Our DataFrame
df = pd.DataFrame(data)
 
# Display the records
print("Player Records\n\n", df)
 
# Use the groupby() to group
groupRes = df.groupby('Year')
 
# The agg() is used to perform aggregation
print("\n",groupRes['Points'].agg(np.mean))

"""
Player Records
 
   Player  Rank  Points  Year
0   Amit     1      95  2023
1   John     4      70  2022
2   Amit     3      65  2021
3  David     5      80  2022
4  Steve     2      90  2023
5   John     7      50  2019
 
 Year
2019    50.0
2021    65.0
2022    75.0
2023    92.5
Name: Points, dtype: float64
"""


# In[5]:


"""
To get the size of each group, use the Numpy size attribute in Pandas. 
We have grouped by the Player column using the groupby().
"""

import pandas as pd
import numpy as np
 
# Our Dataset
data = {
    'Player': ["Amit", "John", "Amit", "David", "Steve", "John"],
    'Rank': [1, 4, 3, 5, 2, 7],
    'Points': [95, 70, 65, 80, 90, 50],
    'Year': [2023, 2022, 2021, 2022, 2023, 2019]
}
 
# Our DataFrame
df = pd.DataFrame(data)
 
# Display the records
print("Player Records\n\n", df)
 
# Use the groupby() to group
groupRes = df.groupby('Player')
 
# The agg() is used to perform aggregation
# The numpy.size attribute returns the size of each group
print("\n",groupRes.agg(np.size))

"""
Player Records
 
   Player  Rank  Points  Year
0   Amit     1      95  2023
1   John     4      70  2022
2   Amit     3      65  2021
3  David     5      80  2022
4  Steve     2      90  2023
5   John     7      50  2019
 
         Rank  Points  Year
Player                    
Amit       2       2     2
David      1       1     1
John       2       2     2
Steve      1       1     1
"""


# In[ ]:




