# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 23:30:07 2023

@author: adwal

The Business Dynamics Statistics (BDS) includes measures of establishment openings and closings, firm startups, 
job creation and destruction by firm size, age, and industrial sector, and several other statistics on business dynamics. 
The U.S. economy is comprised of over 6 million establishments with paid employees. The population of these businesses is 
constantly churning -- some businesses grow, others decline and yet others close. New businesses are constantly replenishing this pool. The BDS series provide annual statistics on gross job gains and losses for the entire economy and by industrial sector, state, and MSA. These data track changes in employment at the establishment level, and thus provide a picture of the dynamics underlying aggregate net employment growth.

There is a longstanding interest in the contribution of small businesses to job and productivity growth in the U.S.
 Some recent research suggests that it is business age rather than size that is the critical factor. The BDS permits
 exploring the respective contributions of both firm age and size.

BDS is based on data going back through 1976. This allows business dynamics to be tracked, measured and analyzed 
for young firms in their first critical years as well as for more mature firms including those that are in the process 
of reinventing themselves in an ever changing economic environment.

State(str)
Year(int)
Data
    DHS Denominator(int)
    Number of Firms(int)
    Calculated
        Net Job Creation(int)
        Net Job Creation Rate(float)
        Reallocation Rate(float)
    Establishments
        Entered(int)
        Entered Rate(float)
        Exited(int)
        Exited Rate(float)
    Firm Exits
        Count(int)
        Establishment Exit(int)
        Employments(int)
    Job Creation
        Births(int)
        Continuers(int)
        Count(int)
        Rate(float)
        Rate/Births(float)
    Job Destruction
        Continuers(int)
        Count(int)
        Deaths(int)
        Rate(float)
        Rate/Deaths(float)

what is the difference in the rate of jobs created in the state of NY in the year 1999 in comparison to 2018
example of data
[{'State': 'Alabama',
  'Year': 1978, 
  'Data': {'DHS Denominator': 972627, 'Number of Firms': 54597, 
           'Calculated': {'Net Job Creation': 74178, 'Net Job Creation Rate': 7.627, 'Reallocation Rate': 29.183}, 
           'Establishments': {'Entered': 10457, 'Entered Rate': 16.375, 'Exited': 7749, 'Exited Rate': 12.135, 'Physical Locations': 65213}, 
           'Firm Exits': {'Count': 5248, 'Establishment Exit': 5329, 'Employments': 28257}, 
           'Job Creation': {'Births': 76167, 'Continuers': 139930, 'Count': 216097, 'Rate': 22.218, 'Rate/Births': 7.831}, 
           'Job Destruction': {'Continuers': 81829, 'Count': 141919, 'Deaths': 60090, 'Rate': 14.591, 'Rate/Deaths': 6.178}}}

 Problem:
     For the year 2018, I want to know how the state of NY compares to all 47 states in the U.S. in relation to the rate of jobs created
     From the information given, I can know if NY produced underperformed, or overperformed in terms of the rate of jobs created in the year.
 """

import business_dynamics
import matplotlib.pyplot as plt
record = business_dynamics.get_record()

NYrates = []
years =[]
NJrates = []
NJstates =[]
count = 0
Acount = 0
counts = 0

for i in record:
    if i['State'] == "New York":
        count+=1
        NYrates.append(i['Data']['Job Creation']['Rate'])
        years.append(i['Year'])
    if i['State'] == "New Jersey":
        Acount+=1
        NJrates.append(i['Data']['Job Creation']['Rate'])

        
print(sum(NYrates)/count)    
print(sum(NJrates)/Acount)   
#print(NJyears,NJrates)       
#print(NYyears,NYrates)

plt.plot(years, NJrates, color='skyblue',linewidth = 3)
plt.plot(years,NYrates, color='red',linewidth = 3)
plt.title("Job Creation Rates in NY vs NJ")
plt.xlabel("Years")
plt.ylabel("Rates")
plt.legend(["NJ","NY"])
plt.show()

