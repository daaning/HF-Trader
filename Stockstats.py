import talib as ta
import numpy


def make_stockstats(df):
    
    df['MACD'], df["signal"], df['histogram'] = ta.MACD(
        df.close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['RSI'] = ta.RSI(df.close, timeperiod=14)

    return df