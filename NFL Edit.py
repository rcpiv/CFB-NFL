# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 08:55:19 2021

@author: rcpat
"""

#%% Packages
import pandas as pd
from pandasql import sqldf
import numpy as np
#%% Load Dataset
nfl = pd.read_csv(r'NFL_final.csv')
teams = nfl.Winner.unique()

#%%
q1 = """
    select *
    from nfl
    where Date >= '1966-09-10'
"""
q2 = """
    select *
    from cfb
    where start_date >= '1966-09-10'
"""

nfl2 = sqldf(q1)
cfb = sqldf(q2)

#%% New teams
teams2 = nfl2.Winner.unique()
pd.DataFrame(teams2).to_csv(r'nflteams.csv', index=False)

#%% Map to Code
teams3 = pd.read_csv(r'nflteams.csv')
nfl3 = nfl2
nfl3['Winner'] = nfl2['Winner'].map(teams3.set_index('Team')['ID'])
nfl3['Loser'] = nfl2['Loser'].map(teams3.set_index('Team')['ID'])

#%% Remove Duplicates on Teams4 manually in Excel
# ReMap to team names
teams4 = pd.read_csv(r'nflteams2.csv')
nfl4 = nfl3
nfl4['Winner'] = nfl3['Winner'].map(teams4.set_index('ID')['Team'])
nfl4['Loser'] = nfl3['Loser'].map(teams4.set_index('ID')['Team'])

#%% Export NFL4
nfl4.to_csv(r'NFL_final.csv',index=False)
cfb.to_csv(r'CFB_final.csv',index=False)
