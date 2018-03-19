import talib as ta
import numpy


def make_stockstats(data):
    
    df = data
    df['EMA_32']= ta.EMA(df.close, timeperiod=32)
    df['MACD'], df["signal"], df['histogram'] = ta.MACD(
        df.close, fastperiod=12, slowperiod=26, signalperiod=9)

    return df