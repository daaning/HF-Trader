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
    if (data[1][9] > 0.0) and (data[0][9] < 0.0): 
        buystats[time] == True    
    if data[1][9] < 0.0 and data[1][9] > 0.0:
        sellstats[time] == True
       
    if time ==3:
        print ("MACD_crossover: ", markets[currency], buystats, sellstats)    
        sellstats = [False,False,False,False]
        buystats = [False,False,False,False]
    
def RSI(time, currency, timeloop):
    global sellstats
    global buystats
    data = Database.get_xAmount_entry(time, currency, 2)
    if data[1][10] < 20.0:
        buystats[time] == True    
    if data[1][10] > 80.0:
        sellstats[time] == True
       
    if time ==3:
        print ("RSI: ", markets[currency], buystats, sellstats)    
        sellstats = [False,False,False,False]
        buystats = [False,False,False,False]
    