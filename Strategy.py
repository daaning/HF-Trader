import pandas as pd
import Settings
import Stockstats
import Database
import BinanceAPI
import numpy as np
import logging
import TwitterAPI
import talib as ta
markets = Settings.tradewith
lenmarket = len(markets)


# gets the macd from database and calculates it  
def get_macd(df, fastperiod, slowperiod, signalperiod):
    MACD, signal, histogram = ta.MACD(
        df.close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    return MACD.iloc[-1], signal.iloc[-1], histogram.iloc[-1]

lowestpoint=highestpoint=crossover= [[0.0,0.0,0.0,0.0] for l in range(lenmarket)]
macd_data = [[[],[],[],[]] for s in range(lenmarket)]
def macd_crossover(df, currency, timeframe):
    
    polarity = 0.0

    # after crossover event happend quadratically returning to 0.0 polarity 
    crossover[currency][timeframe] = crossover[currency][timeframe] - (crossover[currency][timeframe] * crossover[currency][timeframe])
    
    # gets the lowest and the highest macdvalue 
    macd_data[currency][timeframe].append(get_macd(df, 12, 26, 9))
    if macd_data[currency][timeframe][0][-1] < lowestpoint[currency][timeframe]: 
        lowestpoint[currency][timeframe] = macd_data[currency][timeframe][0][-1]
    if macd_data[currency][timeframe][0][-1] > highestpoint[currency][timeframe]: 
        highestpoint[currency][timeframe] = macd_data[currency][timeframe][0][-1]

    # checks if the macd has a crossover of its lines
    # multiplies that for relative distance to the middle
    if len(macd_data[currency][timeframe]) > 2:
        if macd_data[currency][timeframe][2][-1] > 0.0 and macd_data[currency][timeframe][2][-2] < 0.0:
            crossover[currency][timeframe] == 1.0 * (macd_data[currency][timeframe][0][-1]/lowestpoint[currency][timeframe])
        elif macd_data[currency][timeframe][2][-1] < 0.0 and macd_data[currency][timeframe][2][-2] > 0.0:
            crossover[currency][timeframe] == -1.0 * (macd_data[currency][timeframe][0][-1]/lowestpoint[currency][timeframe])
        
    # Returns the avg polarity when the currencyloop whent through all its timeframes
    
    if timeframe == 3:
        polarity = np.average(crossover[currency])

    # keeps the array from getting to big
    if len(macd_data[currency][timeframe]) > 3:
        del macd_data[currency][timeframe][0] 
    
    return polarity


def get_volume_weigthed(stockstatsArray):
    volumeArray = []
    length = len(stockstatsArray)
    data = Database.get_xAmount_entry(time, currency, length)
    for i in range(length):
        volumeArray.append(data[i][4])


    




strategies = ["macd"]
outcomes = [[] for r in range(lenmarket)]
def run(df, timeframe, currency, rep, loopdone, timeloopdone):
    
    pol1 = macd_crossover(df, currency, timeframe)
    if timeframe == 3:
        outcomes[currency].append(pol1)
        print (outcomes)
       
