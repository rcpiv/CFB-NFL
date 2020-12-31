# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:06:31 2020

@author: rcpat
"""

#%% Loaf packages
import requests
import statistics as stat #Load required packages
import csv
import pandas as pd
#%% Test API
year = 2017
seasontype = 'regular'
URL = 'https://api.collegefootballdata.com/games?year='
URL = URL + str(year) + '&seasonType=' + seasontype

response = requests.get( URL ) 

data = response.json()
df = pd.DataFrame(data)
df.head()

#%% Loop API
seasons = {}
for year in range(1869,2021):
    for stype in ['regular','postseason']:
        URL = 'https://api.collegefootballdata.com/games?year='
        URL = URL + str(year) + '&seasonType=' + stype
        
        response = requests.get( URL ) 
        
        data = response.json()
        seasons.setdefault(year,[]).append(pd.DataFrame(data))

#%% Clean Data Frames
seasons2 = {}
for year in range(1869,2021):
    seasons2[year] = pd.concat(seasons[year])

all_cfb_seasons = pd.concat(seasons2.values(),ignore_index=True)
cfb2 = all_cfb_seasons
#%% Reformat Date
cfb2.dtypes
cfb2['start_date'] = cfb2['start_date'].str.split('T')
cfb2['start_date'] = cfb2['start_date'].str[0]
#%% To CSV
cfb2.to_csv(r'C:\Users\rcpat\Desktop\IAA\Personal Projects\CFB_NFL\all_cfb_seasons.csv', index=False)
