'''


    We want to answer the following question:
        Considering only their "Avg Temp" (average temperature), how does the
        weather between "San Diego" and "Blacksburg" compare?

    To answer this question show two line plots, with the "Avg Temp"
    for weather in each city, in a single graph.
    
    Remember to consult your diagram of the weather dataset and
    the weather dataset documentation at:
        https://corgis-edu.github.io/corgis/python/weather/
        
    For this question, upload the Python file with the code that answers
    the question above.
'''

import matplotlib.pyplot as plt
import weather

reports = weather.get_report()
print(reports)
SanDiego = []
Blacksburg = []


for i in reports:
    if i['Station']['City']=="San Diego":
        SanDiego.append(i['Data']['Temperature']['Avg Temp'])
    if i['Station']['City']=="Blacksburg":
        Blacksburg.append(i['Data']['Temperature']['Avg Temp'])
print(SanDiego)
print(Blacksburg)
        
        
    

plt.plot(SanDiego,label="San Diego", color='red')
plt.plot(Blacksburg,label ="Blacksburg", color='black')
plt.xlabel("Weeks in a year")
plt.ylabel("Avg Temperature")
plt.title("Comparison of Avg Temp of San Diego and Blacksburg")
plt.legend()
plt.show()