import talib as ta
import numpy


def make_stockstats(data):
    df = data

    df['EMA_32'] = ta.EMA(df.close, timeperiod=32)

    return df