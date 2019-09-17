#!/usr/bin/env python
# coding: utf-8

# In[85]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# In[86]:


purchase_data.head()


# In[87]:


total_players = len(purchase_data["SN"].unique())
total_players_table = pd.DataFrame({"Total Players": [total_players]})
total_players_table


# In[88]:


unique_items = len(purchase_data["Item ID"].unique())
avg_price = purchase_data["Price"].mean()
num_purchases = len(purchase_data["Purchase ID"].value_counts())
total_rev = purchase_data["Price"].sum()


# In[89]:


purchase_analysis = pd.DataFrame({"Unique Items Count": [unique_items], "Average Price": [avg_price], 
                                  "Total Purchase": [num_purchases], "Total Revenue": [total_rev]})
purchase_analysis['Average Price'] = purchase_analysis['Average Price'].map('${0:,.2f}'.format)
purchase_analysis['Total Revenue'] = purchase_analysis['Total Revenue'].map('${0:,.2f}'.format)
purchase_analysis


# In[90]:


gender_count = purchase_data.groupby("Gender")
gender_total = gender_count.nunique()["SN"]
gender_percent = gender_total / total_players * 100
gender_demographics = pd.DataFrame({"Percentage of Players": gender_percent, "Total Count": gender_total})
gender_demographics.index.name = None
gender_demographics.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}%"})


# In[91]:


gender_purchase_count = gender_count["Purchase ID"].count()
gender_purchase_avg = gender_count["Price"].mean()
gender_total_spent = gender_count["Price"].sum()
gender_Purchase_avgpp = gender_total_spent / gender_total

gender_purch_demo = pd.DataFrame({"Purchase Count" : gender_purchase_count, "Purchase Average" : gender_purchase_avg,
                     "Total Spent" : gender_total_spent, "Avg Total Spent Per Person" : gender_Purchase_avgpp})
gender_purch_demo.index.name = ("Gender")
gender_purch_demo.style.format({"Total Spent":"${:,.2f}","Purchase Average":"${:,.2f}","Avg Total Spent Per Person":"${:,.2f}"})


# In[92]:


age_bins = [0,9,14,19,24,29,34,39,100]
age_title = [">10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


# In[93]:


purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=age_title)
age_grouped = purchase_data.groupby("Age Group")
total_age = age_grouped["SN"].nunique()
percent_age = (total_age/total_players) * 100
age_demographics = pd.DataFrame({"Total Count": total_age, "Percentage of Players": percent_age})
age_demographics.index.name = None
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})


# In[94]:


age_purchase = age_grouped["Purchase ID"].count()
age_purchase_avg = age_grouped["Price"].mean()
age_total_purchase = age_grouped["Price"].sum()
age_pp_avg = age_total_purchase/total_count_age
age_demographics = pd.DataFrame({"Purchase Count": age_purchase,"Average Purchase Price": age_purchase_avg,
                                 "Total Purchase":age_total_purchase,"Avg Total Purchase Per Person": age_pp_avg})
age_demographics.index.name = None
age_demographics.style.format({"Average Purchase Price":"${:,.2f}","Total Purchase":"${:,.2f}",
                               "Avg Total Purchase Per Person":"${:,.2f}"})


# In[95]:


spenders = purchase_data.groupby("SN")
spender_purchases = spenders["Purchase ID"].count()
spender_avg_price = spenders["Price"].mean()
spender_purch_total = spenders["Price"].sum()
top_spenders = pd.DataFrame({"Purchase Count": spender_purchases,"Average Purchase Price": spender_avg_price,
                             "Total Purchase":spender_purch_total})
top_spenders = top_spenders.sort_values(["Total Purchase"], ascending=False).head()
top_spenders.index.name = None
top_spenders.style.format({"Average Purchase Total":"${:,.2f}","Average Purchase Price":"${:,.2f}", 
                            "Total Purchase":"${:,.2f}"})


# In[114]:


items = purchase_data[["Item ID", "Item Name", "Price"]]
items_group = items.groupby(["Item ID","Item Name"])
purch_items = items_group["Price"].count()
purchase_total = (items_group["Price"].sum()) 
item_price = purchase_total / purch_items
pop_items = pd.DataFrame({"Purchase Count": purch_items, "Item Price": item_price,
                            "Total Purchase":purchase_value})
pop_items = pop_items.sort_values(["Purchase Count"], ascending=False).head()
pop_items.index.name = None
pop_items.style.format({"Item Price":"${:,.2f}", "Total Purchase":"${:,.2f}"})


# In[118]:


pop_items = pop_items.sort_values(["Total Purchase"], ascending=False).head()
pop_items.index.name = None
pop_items.style.format({"Item Price":"${:,.2f}", "Total Purchase":"${:,.2f}"})


# In[ ]:


# THREE TRENDS 

#1 Our biggest spends are people ages 20-24 with 15-19 year olds coming in a far second.
#  We should focus a larger portion of our marketing towards these two age ranges but still cater to our other ages

#2 We have a lot of Male customers at 84% but the Female demographic is at 14%, id like to keep track of the growing 
#  or slimming gender gap to see if we should invest into growing the female customer demographic 

#3 "Oathbreaker, Last Hope of the Breaking Storm" is our top seller item but "Nirvana" and "Fiery Glass Crusader" are 
#  a close second, with all other items below the top 4 not making as much revenue. What is it about these items that
#  make them sell at larger volumes even though they are more expensive items. 


# In[ ]:




