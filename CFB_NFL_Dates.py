# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:06:54 2020

@author: rcpat
"""

#%% To Do
# Assign week numbers to each date

#%% Import packages
import pandas as pd
import datetime # Used to get dates

#%% Load in tables
cfb = pd.read_csv(r'CFB.csv')
nfl = pd.read_excel(r'NFL_games.xlsx')

#%% Convert Date columns to date object
cfb.dtypes
nfl['Date'] = pd.to_datetime(nfl['Date'])
cfb['start_date'] = pd.to_datetime(cfb['start_date'], errors='coerce')

#%% Adjust Years for nfl
nfl['Day'] = nfl['Date'].dt.day
nfl['Month'] = nfl['Date'].dt.month
nfl['Year'] = nfl['Date'].dt.year

nfl.loc[nfl.Month.isin([1,2]), 'Year'] += 1
nfl['Date'] = pd.to_datetime(nfl[['Year', 'Month', 'Day']])
#%% Get Days of week
nfl['Day_of_Week'] = nfl['Date'].dt.dayofweek
cfb['Day_of_Week'] = cfb['start_date'].dt.dayofweek

#%% Add week numbers
nfl['WeekID'] = nfl['Date'].dt.strftime('%Y%W').astype(str).astype(int)
cfb['WeekID'] = cfb['start_date'].dt.strftime('%Y%W').astype(str).astype(int)
nfl['Week_of_Year'] = nfl['Date'].dt.strftime('%W').astype(str).astype(int)
cfb['Week_of_Year'] = cfb['start_date'].dt.strftime('%W').astype(str).astype(int)

#%% Change M-W to previous week
cfb.loc[cfb['Day_of_Week'] == 0, 'WeekID'] -= 1
cfb.loc[cfb['Day_of_Week'] == 1, 'WeekID'] -= 1
cfb.loc[cfb['Day_of_Week'] == 2, 'WeekID'] -= 1
nfl.loc[nfl['Day_of_Week'] == 0, 'WeekID'] -= 1
nfl.loc[nfl['Day_of_Week'] == 1, 'WeekID'] -= 1
nfl.loc[nfl['Day_of_Week'] == 2, 'WeekID'] -= 1

nfl.loc[nfl['Day_of_Week'].isin([0,1,2]), 'Week_of_Year'] -= 1
cfb.loc[cfb['Day_of_Week'].isin([0,1,2]), 'Week_of_Year'] -= 1

#%% Adjust -1 values
cfb.loc[cfb['Week_of_Year'] == -1, 'WeekID'] += 1

#%% Drop Columns from CFB
cfb.columns
cfb = cfb[['start_date','home_team','away_team','Winner','Loser','WeekID']]
#%% Export to CSV
cfb.to_csv(r'CFB_Final.csv',index=False)
nfl.to_csv(r'NFL_Final.csv',index=False)
