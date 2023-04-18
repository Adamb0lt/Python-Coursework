#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:11:05 2022

@author: sharonkalafut
"""

'''

    Author:
    Pie Classwork

     Using the code create a pie chart that will show the Average temperatures across the USA for all seasons. Such that the pie labels would include
     Winter,Spring,Summer,Fall and it would show the percentage of when in each season has the avg temperature.
        
    Remember to consult your diagram of the weather dataset and 
    the weather dataset documentation at:
        https://corgis-edu.github.io/corgis/python/weather/
        
    For this question, upload the Python file with the code that answers
    the question above.
    ￼Answer:
        Summer = 32.7%
        Fall = 26.4%
        Spring = 24.4%
        Winter = 16.5%
    ￼￼
'''

import weather
import matplotlib.pyplot as plt
reports = weather.get_report()

temperature_listSummer = []
temperature_listWinter = []
temperature_listSpring = []
temperature_listFall = []
summer = [6,7,8]
winter = [12,1,2]
spring = [3,4,5]
fall = [9,10,11]
allSeasons = []
countSummer = 0
countWinter = 0
countSpring = 0
countFall = 0
summerCnt =0
winterCnt = 0
springCnt = 0
fallCnt = 0


for i in reports:
    if i['Date']['Month'] in summer:
        temperature_listSummer.append(i['Data']['Temperature']['Avg Temp'])
        countSummer +=1
    elif i['Date']['Month'] in winter:
        countWinter+=1
        temperature_listWinter.append(i['Data']['Temperature']['Avg Temp'])
    elif i['Date']['Month'] in spring:
        countSpring+=1
        temperature_listSpring.append(i['Data']['Temperature']['Avg Temp'])
    elif i['Date']['Month'] in fall:
        countFall+=1
        temperature_listFall.append(i['Data']['Temperature']['Avg Temp'])
    
    
totalSummer= sum(temperature_listSummer)
totalWinter=sum(temperature_listWinter)
totalSpring =sum(temperature_listSpring)
totalFall =sum(temperature_listFall)

avgSummer = totalSummer/countSummer
avgWinter = totalWinter/countWinter
avgFall = totalFall/countFall
avgSpring = totalSpring/countSpring

tempList = [avgSummer, avgWinter, avgSpring, avgFall]
    

my_labels = ["Summer","Fall","Winter","Spring"]
explode = [0,0,0,0.1]
plt.title("Avg Temperature")
plt.pie(tempList,explode=explode,labels=my_labels,shadow=True,startangle=90,autopct='%1.1f%%')
plt.axis('equal')
plt.show()


    
