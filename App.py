# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:11:24 2021

@author: rcpat
"""

#%% Packages
import pandas as pd
from pandasql import sqldf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

#%% Load Tables
nfl = pd.read_csv(r'NFL_final.csv')
cfb = pd.read_csv(r'CFB_final.csv')

nfl.name = 'NFL'
cfb.name = 'CFB'
#%% Autocomplete

def filter_list(league):
    
    """
    league : sports league to pull from
    
    List of leagues supported:
        NFL (National Football League)
        CFB (College Football (FBS))
    """
    # User inout
    ui = input("{l} Team: ".format(l = league.name)).title()
    
    # Tells python that we want this variable to exist outside of the function too
    global selection
    
    # Checks to see if selection exists already
    try:
        selection
    except NameError:
        selection = {}
    
    # Filters team names that start with string given    
    filtered = [x for x in league.Winner.unique().tolist() if x.startswith(ui)]
    
    # Gives list of team names that start with the string given
    if len(filtered) > 1:
        print('There are more than one team starting with "{0}"'.format(ui))
        print('Select from choices: ')
        for index, name in enumerate(filtered):
            print("{0}: {1}".format(index,name))
            
        index = int(input('Enter choice number: '))
        selection[league.name] = filtered[index]
        print('Selected team: {0}'.format(selection[league.name]))
        print()
    else:
        print(filtered[0])
        selection[league.name] = filtered[0]
        print('Selected team: {0}'.format(selection[league.name]))
        print()
#%% Test
filter_list(cfb)
filter_list(nfl)
#%% Last time teams won same week
cfb_win = cfb[cfb['Winner'] == selection['CFB']]
nfl_win = nfl[nfl['Winner'] == selection['NFL']]
cfb_lose = cfb[cfb['Loser'] == selection['CFB']]
nfl_lose = nfl[nfl['Loser'] == selection['NFL']]

both_win = pd.merge(cfb_win,nfl_win, how='inner', on='WeekID')
nfl_win_cfb_lose = pd.merge(cfb_lose,nfl_win, how='inner', on='WeekID')
nfl_lose_cfb_win = pd.merge(cfb_win,nfl_lose, how='inner', on='WeekID')
both_lose = pd.merge(cfb_lose,nfl_lose, how='inner', on='WeekID')

print('The last time {NFL} and {CFB} won the same week was {Date}.'\
      .format(NFL=selection['NFL'], \
              CFB=selection['CFB'], \
              Date = max(max(pd.to_datetime(both_win['Date'])),\
                         max(pd.to_datetime(both_win['start_date']))).strftime('%B %d, %Y')))

#%% Do it with a function

def get_dates(n):
    """
    Gets the most frequent date(s) of desired combination

    Returns
    -------
    None.

    """
    dfs = {
    1 : cfb[cfb['Winner'] == selection['CFB']],
    2 : nfl[nfl['Winner'] == selection['NFL']],
    3 : cfb[cfb['Loser'] == selection['CFB']],
    4 : nfl[nfl['Loser'] == selection['NFL']]}
    
    # User chooses what they want to see
    choices = ['Both NFL and CFB win','NFL win and CFB lose','NFL lose and CFB win','Both NFL and CFB lose']
    print('What combination do you wish to select?') 
    for index, name in enumerate(choices):
            print("{0}: {1}".format(index,name))
    ui = input('Select from choices above: ')   
    
    global df
    
    if ui == 0:
        df = pd.merge(dfs[1],dfs[2], on='WeekID', how='inner')
    elif ui == 1:
        df = pd.merge(dfs[2],dfs[3], on='WeekID', how='inner')
    elif ui == 2:
        df = pd.merge(dfs[1],dfs[4], on='WeekID', how='inner')
    else:
        df = pd.merge(dfs[3],dfs[4], on='WeekID', how='inner')
        
    dict_of_dates = {'NFL Date':[],'CFB Date':[]}
    
    

#%%
get_dates()
