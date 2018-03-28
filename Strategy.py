import pandas as pd
import Settings
import Database
import BinanceAPI
import numpy as np
import logging
import TwitterAPI


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
        print ("RSI signals: ", rsiarr)
        print ("RSIavg: ",rsiavg, buy, sell)
        del rsiarr[:]


adxarr = []
def ADX(time, currency):
    data = Database.get_xAmount_entry(time, currency, 2) 

    adxarr.append(data[0][12])
    if time ==3:
        adxavg = np.average(adxarr)
        print ("Signals ADX_strength: ", adxarr)
        print ("AVG ADX_strength: ", adxavg )
        del adxarr[:]

def twitter_sentiment(time, currency):

    if time == 3:
        data = TwitterAPI.get_sentiment(currency)
        print("Coins sentiment: ", data)

volarr = []
def volatility(time, currency):
    volarr.append(data[0][13])

    if time ==3:
        print ("Volitily range: volarr")
        del volarr[:]
    
