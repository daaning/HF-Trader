import pandas as pd
import Settings
import Database
import BinanceAPI
import numpy as np
import logging


markets = Settings.tradewith
lenmarket = len(markets)
sellstats = [False, False, False, False]
buystats = sellstats

def MACD_crossover(time, currency, timeloop):
    global sellstats
    global buystats
    data = Database.get_all_entries(time, currency)
    if timeloop:
        sellstats = [False, False, False, False]
        buystats = sellstats

    def buy():
        if (data[-1][9] > 0):
            if(data[-2][9] < 0): 
                return True
        return False
    def sell():
        if data[-1][9] < 0:
            if data[-2][9] >0:
                return True
        return False    

    if time == 0 and buy():
        buystats[0] == True
    elif time == 1 and buy():
        buystats[1] == True
    elif time == 2 and buy():
        buystats[2] == True
    elif time == 3 and buy():
        buystats[3] == True

    if time == 0 and sell():
        sellstats[0] == True
    elif time == 1 and sell():
        sellstats[1] == True
    elif time == 2 and sell():
        sellstats[2] == True
    elif time == 3 and sell():
        sellstats[3] == True

    
    return markets[currency], buystats, sellstats
    
