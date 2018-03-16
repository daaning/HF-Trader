import pandas as pd
import Settings
import numpy as np
import logging

markets = Settings.tradewith
lenmarkets = len(markets)
AVG_array = [[]for a in range(lenmarkets)]
avg = [0 for d in range(lenmarkets)]
startlines = []

output1 = 'close'
output2 = 'macdh'


def last_line(i, data):
    for index, row in data.iterrows():
        last_line = markets[i], index, row[output1], row[output2]
    return last_line

def all_lines(i, data):
    all_lines = []
    for index, row in data.iterrows():
        last_line = markets[i], index, row[output1], row[output2]
        all_lines.append(last_line)
    return last_line
    
        
