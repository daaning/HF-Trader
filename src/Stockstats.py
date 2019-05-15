import talib
import numpy
import Database

# statiscal functions from the ta-lib


def MACD(df, fast, slow, signal):
    return talib.MACD(df.close, fast=fast, slow=slow, signalperiod=signal)


def RSI(df, period):
    return talib.RSI(df.close, period=period)


def STOCH(df, period):
    return talib.STOCH(df.close, period=period)


def DEMA(df, period):
    return talib.DEMA(df.close, period=period)


def ADX(df, period):
    return talib.ADX(df.high, df.low, df.close, period=period)


def Bollinger(df, period):
    return talib.BBANDS(df.close, period=period)
