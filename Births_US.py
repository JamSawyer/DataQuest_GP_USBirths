
# coding: utf-8

# In[15]:


f = open("births.csv", "r")
birth_data = f.read()
print(birth_data)


# In[6]:


births_rowsplit = birth_data.split("\n")
births_rowsplit


# In[17]:


days_counts = {}
data_noheader = births_rowsplit[1:len(births_rowsplit)]
for row in data_noheader:
    m = row.split(",")
    day_of_week = m[3]
    births = int(m[4])
    if day_of_week in days_counts:
        days_counts[day_of_week] = days_counts[day_of_week] + births
    else:
        days_counts[day_of_week] = births
days_counts


# #Births in the US
# 
# We have taken data from births.csv (file containing raw data behind a Five Thirty Eight story on superstition) and created a reference dictionary for the number of births per day of the week (1 = Sunday, 2=Monday, etc).
# 
# The data contains 5 columns(Year, Month, Date of Month, Day of Week, and Births).
# 
