import talib as ta
import numpy


# takes from the TA-Lib checkout https://github.com/mrjbq7/ta-lib 
# returns the last 1000 entries for filling the db at the start
def make_stockstats(df):
    
    df['MACD'], df["signal"], df['histogram'] = ta.MACD(
        df.close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['RSI'] = ta.RSI(df.close, timeperiod=14)
    df['DEMA'] = ta.DEMA(df.close, timeperiod=50)
    df['ADX'] = ta.ADX(df.high, df.low, df.close, timeperiod=20)
    df['range'] = ta.TRANGE(df.close, timeperiod=50)

    return df

# returns the last entry for updating the database
def update_stockstats(df):
    
    df['MACD'], df["signal"], df['histogram'] = ta.MACD(
        df.close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['RSI'] = ta.RSI(df.close, timeperiod=14)
    df['DEMA'] = ta.DEMA(df.close, timeperiod=50)
    df['ADX'] = ta.ADX(df.high, df.low, df.close, timeperiod =20)
    
    # print (df.tail(1))
    return df.tail(1)

