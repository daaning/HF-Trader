import pandas as pd
import Settings
import Database
import BinanceAPI
import numpy as np
import logging


markets = Settings.tradewith
lenmarket = len(markets)



sellstats = [False,False,False,False]
buystats = [False,False,False,False]

def MACD_crossover(time, currency, timeloop):
    global sellstats
    global buystats
    data = Database.get_xAmount_entry(time, currency, 2)
    if (data[0][9] > 0.0) and (data[1][9] < 0.0): 
        buystats[time] = True    
    if data[0][9] < 0.0 and data[1][9] > 0.0:
        sellstats[time] = True
       
    if time == 3:
        print ("MACD_crossover: ", buystats, sellstats)    
        sellstats = [False,False,False,False]
        buystats = [False,False,False,False]


rsiarr = []

def RSI(time, currency, timeloop):
    buy = False
    sell = False
    data = Database.get_xAmount_entry(time, currency, 2)
    rsiarr.append(data[0][10])
    if time == 3:
        rsiavg = np.average(rsiarr) 
        if rsiavg < 30.0:
            buy = True    
        if rsiavg > 70.0:
            sell = True
        print ("RSIavg: ",rsiavg, buy, sell)
        del rsiarr[:]

