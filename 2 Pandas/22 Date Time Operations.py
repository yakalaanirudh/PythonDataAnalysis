#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Get the current date and time
Get the day of the week
Get the day of the year
Get the number of days in a month
Check if the year is a leap year
Check if the date is the last day of the month
Check if the date is the first day of the month
Check if the date is the last day of the year
Check if the date is the first day of the yea
"""


# In[3]:


"""
The Timestamp.now() method is used in Python Pandas to get the current date and time in the local timezone:

To get the day of the week, use the Pandas.dayofweek attribute in Python Pandas:

To get the day of the year, use the Pandas.dayofyear attribute in Python Pandas:

To get the number of days in a month, use the Pandas.days_in_month attribute in Python Pandas:

To check if the year is a leap year, use the Pandas.is_leap_year attribute in Python Pandas:

To check if the date is the last day of the month, use the Pandas.is_month_end attribute in Python Pandas:

To check if the date is the first day of the month, use the Pandas.is_month_start attribute in Python Pandas:

To check if the date is the last day of the year, use the Pandas.is_year_end attribute in Python Pandas:

To check if the date is the first day of the year, use the Pandas.is_year_start attribute in Python Pandas:
"""


import pandas as pd
 
print("Current Date and Time\n",pd.Timestamp.now())

# Timestamp
timeStamp = pd.Timestamp(2023, 10, 25)
 
# Display the date and time
print("Date and Time = ",timeStamp)
 
# Display the day of week
print("Day of Week = ",timeStamp.dayofweek)

# Display the day of year
print("Day of Year = ",timeStamp.dayofyear)

# Display the number of days in the month
print("Days in the month = ",timeStamp.daysinmonth)

# Check if the year is a leap year
print("Is this year leap year? = ",timeStamp.is_leap_year )

# Check if the date is the end of the month
print("Is this the month end? = ",timeStamp.is_month_end)

# Check if the date is the first day of the month
print("Is this the first day of the month? = ",timeStamp.is_month_start)

# Check if the date is the last day of the year
print("Is this the last day of the year? = ",timeStamp.is_year_end)

# Check if the date is the first day of the year
print("Is this the first day of the year? = ",timeStamp.is_year_start)

"""
Current Date and Time
 2025-02-03 15:46:50.413377
Date and Time =  2023-10-25 00:00:00
Day of Week =  2
Day of Year =  298
Days in the month =  31
Is this year leap year? =  False
Is this the month end? =  False
Is this the first day of the month? =  False
Is this the last day of the year? =  False
Is this the first day of the year? =  False
"""


# In[ ]:




