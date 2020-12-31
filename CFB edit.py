# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:21:13 2020

@author: rcpat
"""

#%% Load in CFB data
import pandas as pd
cfb = pd.read_csv(r'C:\Users\rcpat\Desktop\IAA\Personal Projects\CFB_NFL\all_cfb_seasons.csv')

#%% Create Win or Lose Column
def func(row):
    if row['home_points'] == row['away_points']:
        return 'Tie'
    elif row['home_points'] > row['away_points']:
        return row['home_team']
    else:
        return row['away_team']
def func2(row):
    if row['home_points'] == row['away_points']:
        return 'Tie'
    elif row['home_points'] < row['away_points']:
        return row['home_team']
    else:
        return row['away_team']

cfb['Winner'] = cfb.apply(func,axis=1)
cfb['Loser'] = cfb.apply(func2,axis=1)


cfb.head()

#%% Export CFB
cfb.to_csv(r'C:\Users\rcpat\Desktop\IAA\Personal Projects\CFB_NFL\CFB.csv', index=False)