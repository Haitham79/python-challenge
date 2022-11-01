#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv


# In[12]:


with open(r"C:\Users\Owner\Desktop\PyBank\Resources\budget_data.csv", 'r') as file:
    csvreader = csv.reader(file)
    date=[]
    profitLosses=[]
    
    for line in csvreader:
        date.append(line[0])
        profitLosses.append(line[1])
    


# In[13]:


numberOfMonthes = len(date)-1
print("number of monthes: " + str(numberOfMonthes))


# In[15]:


totalProfitLosses=0
for i in range(1, len(profitLosses)):
    totalProfitLosses = totalProfitLosses + int(float(profitLosses[i]))


# In[16]:


print("Total Profit/Losses: " + str(totalProfitLosses))


# In[17]:


ChangeProfitLosses=[]
for j in range(2,len(profitLosses)):
    ChangeProfitLosses.append(float(profitLosses[j])-float(profitLosses[j-1]))


# In[18]:


AVG_ChangeProfitLosses=sum(ChangeProfitLosses)/len(ChangeProfitLosses)


# In[19]:


print("Average Change: " + str(AVG_ChangeProfitLosses))


# In[24]:


maximum_increase=max(ChangeProfitLosses)
maximum_decrease=min(ChangeProfitLosses)
print(maximum_increase,maximum_decrease)


# In[ ]:





# In[26]:


with open(r"C:\Users\Owner\Desktop\PyBank\Analysis\analysis.txt" , "w") as writingFile:
    writingFile.write("Total number of months: " +  str(numberOfMonthes)+'\n')
    writingFile.write("\n"+"Total Profit/Losses: " + "$"+str(totalProfitLosses)+'\n')
    writingFile.write("\n"+"Average Change: " + "$"+str(AVG_ChangeProfitLosses)+'\n')
    writingFile.write("\n"+"Maximum Increase: " +"$"+str(maximum_increase)+'\n')
    writingFile.write("\n"+"Maximum Decrease: " +"$"+str(maximum_decrease)+'\n')


# In[ ]:




