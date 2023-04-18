#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Author:
    Bar Classwork

     Using the code create a bar chart that will show the Average temperatures across the USA for all seasons. Such that the x axis labels would include
     Winter,Spring,Summer,Fall and the y axis would show the average temperatures for each season.
        
    Remember to consult your diagram of the weather dataset and 
    the weather dataset documentation at:
        https://corgis-edu.github.io/corgis/python/weather/
        
    For this question, upload the Python file with the code that answers
    the question above.
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
countSummer = 0
countWinter = 0
countSpring = 0
countFall = 0

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
    

seasons = ["Summer","Fall","Winter","Spring"]
xPositions=[1,2,3,4]
plt.bar(seasons, tempList,align='center')
plt.xlabel("Seasons")
plt.ylabel("Average Temperatures")
plt.title("Avg Temps across the U.S. for all Seasons")
plt.show()


