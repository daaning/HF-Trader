import talib as ta
import numpy
import Database

# takes from the TA-Lib checkout https://github.com/mrjbq7/ta-lib 

def get_macd(df, fastperiod, slowperiod, signalperiod):
    MACD, signal, histogram = ta.MACD(
        df.close, fastperiod=12, slowperiod=26, signalperiod=9)
    return MACD, signal, histogram

def get_rsi(df, timeperiod):
    RSI = ta.RSI(df.close, timeperiod=timeperiod)
    return RSI

def get_dema(df, timeperiod):
    DEMA = ta.DEMA(df.close, timeperiod=50)
    return DEMA

def get_adx(df, timeperiod):
    ADX = ta.ADX(df.high, df.low, df.close, timeperiod=20)
    return ADX

def get_bollinger(df, timeperiod):
    Bollinger = ta.BBANDS(df.close, timeperiod=20)
    return Bollinger

def get_volume_weigthed(stockstatsArray):
    volumeArray = []
    length = len(stockstatsArray)
    data = Database.get_xAmount_entry(time, currency, length)
    for i in range(length):
        volumeArray.append(data[i][4])


    