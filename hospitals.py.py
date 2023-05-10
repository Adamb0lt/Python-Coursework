# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:28:34 2023

@author: adwal
This Assignment connects to a SQL Database and runs a query to access what is needed.
Information is then converted to the necessary type to be added into a list for data visualization with Matplotlib

Question 1: What is the average Overall Rating of each Type of Facility? Create a bar plot to show the results. 

Question 2: Show the top 7 states by Rating Safety with the highest number of an “Above” rating. 
Use a pie chart to show the top 7 states.

Question 3:Show the relationship between the average cost of Pneumonia and the average rating overall. 
Use a scatter plot to show the relationship between the two averages. 
Remove Procedure.Pneumonia.Quality that is equal to “Unknown” and remove Rating.Overall that is -1.
"""

import sqlite3
import matplotlib.pyplot as plt

### connects to the database on SQL
conn = sqlite3.connect('hospitals.db')
c = conn.cursor()

###question 1
#lists for the bar graph
facility = []
avgOvRating = []

#executes SQL query and appends appropriate values to lists
rows = c.execute('''select "Facility.Type", avg("rating.Overall")"avg" from hospitals group by "Facility.Type";''')
for row in rows:
    facility.append(str(row[0]))
    avgOvRating.append(float(row[1]))

#bar graph
plt.bar(facility,avgOvRating)
plt.xlabel('Facility type')
plt.ylabel('Avg Overall Rating')
plt.show()



###question 2
#lists for the pie chart
facilityState = []
cntSafetyRating = []

#executes SQL query and appends appropriate values to lists
rows = c.execute('''select "Facility.State", count("Rating.Safety") from hospitals where 
                 "rating.Safety" = "Above" group by "Facility.State" order by count("rating.safety")desc limit 7;''')
for row in rows:
    facilityState.append(str(row[0]))
    cntSafetyRating.append(float(row[1]))

#pie chart
plt.pie(cntSafetyRating, labels=facilityState,autopct='%1.1f%%')
plt.show()



###question 3
#lists for the bar graph
facilityState1 = []
avgOvRating1 =[]
avgProcedureCost =[]

#executes SQL query and appends appropriate values to lists
rows = c.execute('''select "Facility.State", avg("rating.Overall"),avg("Procedure.Pneumonia.Cost") from hospitals 
                 where "Procedure.Pneumonia.Quality" != "Unknown" and "rating.overall" != -1 group by "Facility.State" ;''')
for row in rows:
    facilityState1.append(str(row[0]))
    avgOvRating1.append(float(row[1]))
    avgProcedureCost.append(float(row[2]))
#scatterplot
plt.scatter(avgOvRating1,avgProcedureCost)
#for loop for labeling all points in scatter
for i,x in enumerate(facilityState1):
    plt.annotate(x,(avgOvRating1[i],avgProcedureCost[i]))
plt.show()
    
    


    