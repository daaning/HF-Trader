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


# functions that make the stockstats with TA-LIB from database data.db

def get_macd(df, fastperiod, slowperiod, signalperiod):
    MACD, signal, histogram = ta.MACD(
        df.close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    return MACD.iloc[-1], signal.iloc[-1], histogram.iloc[-1]

def get_RSI(df, timeperiod):
    RSI = ta.RSI(df.close, timeperiod=timeperiod)
    return RSI.iloc[-1]

    



# function that calculates the polarity of the macd crossover strategy i created 
# based on four different timeframes that spike the polarity when triggert to than
# be reduced every loop thereafter returns a buy/sell polarity to be compared and optimized against
# the delayed optimized buysell polarity 

lowestpoint=highestpoint=crossover= [[0.0,0.0,0.0,0.0] for l in range(lenmarket)]
macd_data = [[[],[],[],[]] for s in range(lenmarket)]
def macd_crossover(df, currency, timeframe):
    
    # the buy/sell polarity value ranges from 1 to -1 
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



# different TA-LIB rsi functions run over different timeframes, averaged and multiplied
# by a relative signal strength indicator as a buy/sell polarity

rsi_data = [[[],[],[],[]] for s in range(lenmarket)]
polArr = [[0.0,0.0,0.0,0.0] for l in range(lenmarket)]
def RSI(df, currency, timeframe):
    
    polarity = 0.0 
    rsi_data[currency][timeframe].append(get_RSI(df, 14))
    entry = rsi_data[currency][timeframe]
    polArr[currency][timeframe] = (entry[0]- 50.0) / 50.0 

    if timeframe == 3:
        polarity = np.average(polArr[currency])    

    if len(rsi_data[currency][timeframe]) > 3:
        del rsi_data[currency][timeframe][0] 
    
    return polarity


# returns a perfect tradesingal starting one turn ago 
lowest=highest= [[] for l in range(lenmarket)]
def historic_perfect_signal(df, currency, timeframe):
    
    polarity = 0.0

    if timeframe == 3:
        if df.close[-1] > highest[currency]:
            highest[currency] = (df.close[-1], df.index[-1])
            polarity = 1.0
        elif df.close[-1] < lowest[currency]:
            lowest[currency] = (df.close[-1], df.index[-1])
            polarity = -1.0

    # have to reduce the polarity by relative distance to last lower/higher or perfect buy/sell event 

def get_volume_weigthed(stockstatsArray):
    volumeArray = []
    length = len(stockstatsArray)
    data = Database.get_xAmount_entry(time, currency, length)
    for i in range(length):
        volumeArray.append(data[i][4])


    




strategies = ["macd"]
outcomes = [[[],[]] for r in range(lenmarket)]
def run(df, timeframe, currency, rep, loopdone, timeloopdone):
    
    strat01 = macd_crossover(df, currency, timeframe)
    strat02 = RSI(df, currency, timeframe)
    if timeframe == 3:
        outcomes[currency][0].append(strat01)
        outcomes[currency][1].append(strat02)
        print (outcomes)
       
