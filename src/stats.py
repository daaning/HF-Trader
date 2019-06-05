import talib
import numpy as np 
import twitter_api


def calculate(data):

    nopen = [] 
    nhigh = []
    nlow = [] 
    nclose = []
    nvolume = []
    for entry in data:
        nopen.append(entry[1])
        nhigh.append(entry[2])
        nlow.append(entry[3])
        nclose.append(entry[4])
        nvolume.append(entry[5])
    nc = np.array(nclose)
    hc = np.array(nhigh)
    lc = np.array(nlow)
    cc = np.array(nclose)
    vc = np.array(nvolume)

    rsi = talib.RSI(nc, timeperiod=14)
    macdsignal = talib.MACD(nc, fastperiod=12, slowperiod=26, signalperiod=9)
    sar = talib.SAR(hc, lc, acceleration=0, maximum=0)
    adosc = talib.ADOSC(hc, lc, cc, vc, fastperiod=3, slowperiod=10)
    aroon = talib.AROONOSC(hc, lc, timeperiod=14)
    ult = talib.ULTOSC(hc, lc, cc, timeperiod1=7, timeperiod2=14, timeperiod3=28)
    obj, sent = twitter_api.get_sentiment()

    return rsi[-1], macdsignal[0][-1], sar[-1], adosc[-1], aroon[-1], ult[-1], sent, obj
