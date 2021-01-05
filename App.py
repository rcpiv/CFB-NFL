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

#%% Load Tables
nfl = pd.read_csv(r'NFL_final.csv')
cfb = pd.read_csv(r'CFB_final.csv')

#%% Autocomplete
# User Input
ui_nfl = input('NFL Team: ')
ui_cfb = input('CFB Team: ')

def filter_list(ui, df):
    
    """
    ui : User input
    df: DataFrame to pull from
    """
    
    filtered = [x for x in df.Winner.unique().tolist() if x.startswith(ui)]
    
    if len(filtered) > 1:
        print('There are more than one team starting with "{0}"'.format(ui))
        print('Select from choices: ')
        for index, name in enumerate(filtered):
            print("{0}: {1}".format(index,name))
            
        index = int(input('Enter choice number: '))
        selection = filtered[index]
        return selection
        print('Selected team: {0}'.format(selection))
        print()
    else:
        print(filtered[0])
        selection = filtered[0]
        return selection
        print()