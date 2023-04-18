#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Using the billionaire list created below.

Write a program that answers the following question:
    
    What is the average wealth in billionaires for following regions:
        North America
        Latin America
        Europe
    The correct output is:
        Average worth in Billions for North America is 44.01
        Average worth in Billions for Latin America is 19.49
        Average worth in Billions for Europe is 29.610000000000003

The layout for the list of dictionaires in Billionaire is:

name: str
rank: int
year: int
company: dict
    founded: int
    name: str
    relation: str
    sector: str
    type: str
demographics: dict
    age: int
    gender: str
location: dict
    citizenship: str
    country: str
    gdp: float
    region: str
wealth: dict
    type: str
    worth in billions: float
    how : dict:
        category: str
        from emerging: bool
        industry: str
        inherited: str
        was founder: bool
        was political: bool


DO NOT DOWNLOAD ANY .DATA FILE OR .PY FILE. DO NOT IMPORT ANY DATA OR CREATE A REPORT.
ONLY USE THE BILLIONAIRE LIST CREATED BELOW TO ANSWER THE QUESTION ABOVE.
'''

billionaire = [{'name': 'Bill Gates', 'rank': 1, 'year': 2014, 'company': {'founded': 1975, 'name': 'Microsoft', 'relationship': 'founder', 'sector': ' Software', 'type': 'new'}, 'demographics': {'age': 58, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 76.0, 'how': {'category': 'New Sectors', 'from emerging': True, 'industry': 'Technology-Computer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Carlos Slim Helu', 'rank': 2, 'year': 2014, 'company': {'founded': 1990, 'name': 'Telmex', 'relationship': 'founder', 'sector': ' Communications', 'type': 'privatization'}, 'demographics': {'age': 74, 'gender': 'male'}, 'location': {'citizenship': 'Mexico', 'country code': 'MEX', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'privatized and resources', 'worth in billions': 72.0, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Media', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Amancio Ortega', 'rank': 3, 'year': 2014, 'company': {'founded': 1975, 'name': 'Zara', 'relationship': 'founder', 'sector': 'Fashion', 'type': 'new'}, 'demographics': {'age': 77, 'gender': 'male'}, 'location': {'citizenship': 'Spain', 'country code': 'ESP', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 64.0, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Warren Buffett', 'rank': 4, 'year': 2014, 'company': {'founded': 1839, 'name': 'Berkshire Hathaway', 'relationship': 'founder', 'sector': ' Finance', 'type': 'aquired'}, 'demographics': {'age': 83, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 58.2, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Larry Ellison', 'rank': 5, 'year': 2014, 'company': {'founded': 1977, 'name': 'Oracle', 'relationship': 'founder', 'sector': ' software', 'type': ' new'}, 'demographics': {'age': 69, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 48.0, 'how': {'category': 'New Sectors', 'from emerging': True, 'industry': 'Technology-Computer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Charles Koch', 'rank': 6, 'year': 2014, 'company': {'founded': 1940, 'name': 'Koch industries', 'relationship': 'relation', 'sector': '  Oil refining', 'type': 'new'}, 'demographics': {'age': 78, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 40.0, 'how': {'category': 'Financial', 'from emerging': True, 'industry': 'Diversified financial', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'David Koch', 'rank': 6, 'year': 2014, 'company': {'founded': 1940, 'name': 'Koch industries', 'relationship': 'relation', 'sector': ' Oil refining', 'type': 'new'}, 'demographics': {'age': 73, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 40.0, 'how': {'category': 'Financial', 'from emerging': True, 'industry': 'Diversified financial', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Sheldon Adelson', 'rank': 8, 'year': 2014, 'company': {'founded': 1952, 'name': 'Las Vegas Sands', 'relationship': 'founder', 'sector': ' casinos', 'type': ' acquired'}, 'demographics': {'age': 80, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'self-made finance', 'worth in billions': 38.0, 'how': {'category': 'Financial', 'from emerging': True, 'industry': 'Real Estate', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Christy Walton', 'rank': 9, 'year': 2014, 'company': {'founded': 1962, 'name': 'Walmart', 'relationship': 'relation', 'sector': ' retail', 'type': ' new'}, 'demographics': {'age': 59, 'gender': 'female'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 36.7, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'spouse/widow', 'was founder': True, 'was political': True}}}, 
               {'name': 'Jim Walton', 'rank': 10, 'year': 2014, 'company': {'founded': 1962, 'name': 'Walmart', 'relationship': 'relation', 'sector': 'retail', 'type': ' new'}, 'demographics': {'age': 66, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 34.7, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Liliane Bettencourt', 'rank': 11, 'year': 2014, 'company': {'founded': 1909, 'name': "L'Oreal", 'relationship': 'relation', 'sector': 'cosmetics', 'type': 'new'}, 'demographics': {'age': 91, 'gender': 'female'}, 'location': {'citizenship': 'France', 'country code': 'FRA', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'inherited', 'worth in billions': 34.5, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Stefan Persson', 'rank': 12, 'year': 2014, 'company': {'founded': 1947, 'name': ' H&M', 'relationship': 'relation', 'sector': ' fashion', 'type': ' new'}, 'demographics': {'age': 66, 'gender': 'male'}, 'location': {'citizenship': 'Sweden', 'country code': 'SWE', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'inherited', 'worth in billions': 34.4, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Alice Walton', 'rank': 13, 'year': 2014, 'company': {'founded': 1962, 'name': 'Walmart', 'relationship': 'relation', 'sector': 'retail', 'type': ' new'}, 'demographics': {'age': 64, 'gender': 'female'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 34.3, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'S. Robson Walton', 'rank': 14, 'year': 2014, 'company': {'founded': 1962, 'name': 'Walmart', 'relationship': 'relation', 'sector': 'retail', 'type': ' new'}, 'demographics': {'age': 70, 'gender': 'male'}, 'location': {'citizenship': 'United States', 'country code': 'USA', 'gdp': 0.0, 'region': 'North America'}, 'wealth': {'type': 'inherited', 'worth in billions': 34.2, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Bernard Arnault', 'rank': 15, 'year': 2014, 'company': {'founded': 1987, 'name': 'LVMH', 'relationship': 'founder', 'sector': 'luxury goods', 'type': 'acquired'}, 'demographics': {'age': 64, 'gender': 'male'}, 'location': {'citizenship': 'France', 'country code': 'FRA', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 33.5, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Michele Ferrero', 'rank': 22, 'year': 2014, 'company': {'founded': 1946, 'name': 'Ferrero spa', 'relationship': 'relation', 'sector': 'chocolates', 'type': 'new'}, 'demographics': {'age': 88, 'gender': 'male'}, 'location': {'citizenship': 'Italy', 'country code': 'ITA', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'executive', 'worth in billions': 26.5, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Karl Albrecht', 'rank': 23, 'year': 2014, 'company': {'founded': 1914, 'name': 'Aldi Sud', 'relationship': 'relation', 'sector': 'groceries', 'type': 'new'}, 'demographics': {'age': 94, 'gender': 'male'}, 'location': {'citizenship': 'Germany', 'country code': 'DEU', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'executive', 'worth in billions': 25.0, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Dieter Schwarz', 'rank': 29, 'year': 2014, 'company': {'founded': 1930, 'name': 'Schwarz Group', 'relationship': 'relation', 'sector': 'groceries', 'type': 'new'}, 'demographics': {'age': 74, 'gender': 'male'}, 'location': {'citizenship': 'Germany', 'country code': 'DEU', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'inherited', 'worth in billions': 21.1, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Jorge Paulo Lemann', 'rank': 34, 'year': 2014, 'company': {'founded': 1999, 'name': 'Ambev', 'relationship': 'founder', 'sector': 'investment banking/beer', 'type': 'aquired'}, 'demographics': {'age': 74, 'gender': 'male'}, 'location': {'citizenship': 'Brazil', 'country code': 'BRA', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 19.7, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Theo Albrecht, Jr.', 'rank': 36, 'year': 2014, 'company': {'founded': 1913, 'name': 'Aldi Nord', 'relationship': 'Relation', 'sector': 'groceries', 'type': 'new'}, 'demographics': {'age': 63, 'gender': 'male'}, 'location': {'citizenship': 'Germany', 'country code': 'DEU', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'inherited', 'worth in billions': 19.3, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Retail, Restaurant', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Leonardo Del Vecchio', 'rank': 38, 'year': 2014, 'company': {'founded': 1961, 'name': '?Luxottica', 'relationship': 'founder', 'sector': 'glasses', 'type': 'new'}, 'demographics': {'age': 78, 'gender': 'male'}, 'location': {'citizenship': 'Italy', 'country code': 'ITA', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 19.2, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Alisher Usmanov', 'rank': 40, 'year': 2014, 'company': {'founded': 1999, 'name': 'Metalloinvest', 'relationship': 'founder', 'sector': 'metals', 'type': 'new'}, 'demographics': {'age': 60, 'gender': 'male'}, 'location': {'citizenship': 'Russia', 'country code': 'RUS', 'gdp': 0.0, 'region': 'Europe'}, 'wealth': {'type': 'privatized and resources', 'worth in billions': 18.6, 'how': {'category': 'Resource Related', 'from emerging': True, 'industry': 'Non-consumer industrial', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Joseph Safra', 'rank': 55, 'year': 2014, 'company': {'founded': 1955, 'name': 'Banco Safra (now Saftra Group)', 'relationship': 'founder', 'sector': 'banking', 'type': 'new'}, 'demographics': {'age': 75, 'gender': 'male'}, 'location': {'citizenship': 'Brazil', 'country code': 'BRA', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'self-made finance', 'worth in billions': 16.0, 'how': {'category': 'Financial', 'from emerging': True, 'industry': 'Money Management', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Iris Fontbona', 'rank': 58, 'year': 2014, 'company': {'founded': 1888, 'name': 'Antofagasta PLC', 'relationship': 'relation', 'sector': 'mining', 'type': 'aquired'}, 'demographics': {'age': 71, 'gender': 'female'}, 'location': {'citizenship': 'Chile', 'country code': 'CHL', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'inherited', 'worth in billions': 15.5, 'how': {'category': 'Resource Related', 'from emerging': True, 'industry': 'Mining and metals', 'inherited': 'spouse/widow', 'was founder': True, 'was political': True}}}, 
               {'name': 'German Larrea Mota Velasco', 'rank': 67, 'year': 2014, 'company': {'founded': 1978, 'name': 'Grupo Mexio', 'relationship': 'founder', 'sector': 'copper', 'type': 'new'}, 'demographics': {'age': 60, 'gender': 'male'}, 'location': {'citizenship': 'Mexico', 'country code': 'MEX', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'privatized and resources', 'worth in billions': 14.7, 'how': {'category': 'Resource Related', 'from emerging': True, 'industry': 'Mining and metals', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Luis Carlos Sarmiento', 'rank': 72, 'year': 2014, 'company': {'founded': 1971, 'name': 'Grupo Aval Acciones y Valores, SA', 'relationship': 'founder', 'sector': 'banking', 'type': 'aquired'}, 'demographics': {'age': 81, 'gender': 'male'}, 'location': {'citizenship': 'Colombia', 'country code': 'COL', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'self-made finance', 'worth in billions': 14.2, 'how': {'category': 'Financial', 'from emerging': True, 'industry': 'Money Management', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Alberto Bailleres Gonzalez', 'rank': 90, 'year': 2014, 'company': {'founded': 1960, 'name': 'Penoles', 'relationship': 'relation', 'sector': 'mining', 'type': 'privatization'}, 'demographics': {'age': 82, 'gender': 'male'}, 'location': {'citizenship': 'Mexico', 'country code': 'MEX', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'inherited', 'worth in billions': 12.4, 'how': {'category': 'Resource Related', 'from emerging': True, 'industry': 'Mining and metals', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Alejandro Santo Domingo Davila', 'rank': 102, 'year': 2014, 'company': {'founded': 1889, 'name': 'Santo Domingo Group', 'relationship': 'relation', 'sector': 'beer', 'type': 'aquired'}, 'demographics': {'age': 37, 'gender': 'male'}, 'location': {'citizenship': 'Colombia', 'country code': 'COL', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'inherited', 'worth in billions': 11.1, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'father', 'was founder': True, 'was political': True}}}, 
               {'name': 'Marcel Herrmann Telles', 'rank': 119, 'year': 2014, 'company': {'founded': 1885, 'name': 'Ambev', 'relationship': 'founder', 'sector': 'investment banking/beer', 'type': 'aquired'}, 'demographics': {'age': 64, 'gender': 'male'}, 'location': {'citizenship': 'Brazil', 'country code': 'BRA', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'founder non-finance', 'worth in billions': 10.2, 'how': {'category': 'Traded Sectors', 'from emerging': True, 'industry': 'Consumer', 'inherited': 'not inherited', 'was founder': True, 'was political': True}}}, 
               {'name': 'Joao Roberto Marinho', 'rank': 137, 'year': 2014, 'company': {'founded': 1925, 'name': 'Globo Organizations', 'relationship': 'relation', 'sector': 'media', 'type': 'new'}, 'demographics': {'age': 60, 'gender': 'male'}, 'location': {'citizenship': 'Brazil', 'country code': 'BRA', 'gdp': 0.0, 'region': 'Latin America'}, 'wealth': {'type': 'inherited', 'worth in billions': 9.1, 'how': {'category': 'Non-Traded Sectors', 'from emerging': True, 'industry': 'Media', 'inherited': 'father', 'was founder': True, 'was political': True}}}]
import matplotlib.pyplot as plt


NA = []
countNA = 0 #can be substituted with length function later on for less variables
LA = []
countLA = 0
EU = []
countEU = 0
#storing 
for i in billionaire:
    if i['location']['region'] == 'North America':
        NA.append(i['wealth']['worth in billions'])
        countNA +=1
    elif i['location']['region'] == 'Latin America':
        LA.append(i['wealth']['worth in billions'])
        countLA +=1
    elif i['location']['region'] == 'Europe':
        EU.append(i['wealth']['worth in billions'])
        countEU +=1
#print(NA)
#print(LA)
#print(EU)

#calculating avg worth
avgWorthNA = sum(NA)/len(NA) #could use count here but its not necessary
avgWorthLA = sum(LA)/len(NA)
avgWorthEU = sum(EU)/len(NA)

print(f"Average worth in Billions for North America is {avgWorthNA}")
print(f"Average worth in Billions for Latin America is {avgWorthLA}")
print(f"Average worth in Billions for Europe  is {avgWorthEU}")

#extra graph for visualization
avG = [avgWorthNA, avgWorthEU, avgWorthLA]     
regions = ["North America","Europe","Latin America"]   

plt.bar(regions,avG)
plt.xlabel("Regions")
plt.ylabel("Avg Worth of Billionaires")
plt.title("Avg Worth of Billionaires per region")
plt.show()
