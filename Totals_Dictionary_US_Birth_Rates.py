
# coding: utf-8

# In[1]:


f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
data = f.read()
data_split = data.split("\n")
print(data_split[0:10])


# In[6]:


def read_csv(inpt_Str):
    final_list = []
    data = open(inpt_Str).read()
    string_list = data.split("\n")[1:]
    
    for m in string_list:
        int_fields = []
        string_fields = m.split(",")
        for n in string_fields:
            int_fields.append(int(n))
        final_list.append(int_fields)
    return final_list
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[0:10])


# In[9]:


def month_births(inpt_lst):
    births_per_month = {}
    
    for string in inpt_lst:
        month = string[1]
        births = string[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)
cdc_month_births


# In[11]:


def dow_births(inpt_lst):
    day_of_week = {}
    
    for string in inpt_lst:
        day = string[3]
        births = string[4]
        if day in day_of_week:
            day_of_week[day] = day_of_week[day] + births
        else:
            day_of_week[day] = births
    return day_of_week

cdc_day_births = dow_births(cdc_list)
cdc_day_births
        
    
            
    


# In[14]:


def calc_counts(data, i):
    dictionary = {}
    
    for string in data:
        column = string[i]
        births = string[4]
        if column in dictionary:
            dictionary[column] = dictionary[column] + births
        else:
            dictionary[column] = births
    return dictionary

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

