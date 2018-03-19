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


        
