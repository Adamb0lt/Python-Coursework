#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Author: 
    Histogram Classwork

    We want to answer the following question:
        What is the distribution of rainfall in Blacksburg?

    In order to answer this question, show a histogram of the "Precipitation"
    of the recorded weather reports.
    
    Remember to consult your diagram of the weather dataset and
    the weather dataset documentation at:
        https://corgis-edu.github.io/corgis/python/weather/
        
    For this question, upload the Python file with the code that answers
           the question above.
'''

import matplotlib.pyplot as plt
import weather

weather_reports = weather.get_report()
print(weather_reports)
count = 0
lol = []
rainBlacksburgh = []
for i in weather_reports:
    if i['Station']['City'] == "Blacksburg":
        rainBlacksburgh.append(i['Data']['Precipitation'])
        lol.append(i['Date']['Full'])
        
        count+=1
print(rainBlacksburgh, count)
print(lol)

plt.hist(rainBlacksburgh, bins = [0,1,2])
plt.xlabel("Weeks")
plt.ylabel("distribution of rainfall")
plt.title("Distribution of rainfall per Quarter for Blacksburg")
    

