from binance.client import Client
from binance.exceptions import BinanceAPIException
import Main
import Settings
import pandas as pd
import stockstats
import logging
import time

#get all the settings from settings
lenmarket = len(Settings.tradewith)
client = Client(Settings.key, Settings.secret)
tradewith = Settings.tradewith
tradecurrency = Settings.tradecurrency
timeframes = Settings.timeframes


#dictionairies and arrays for pandas are being made
markets = []
for m in range(lenmarket):
    markets.append(tradewith[m] + tradecurrency)

#make pandas dataframes for all the whitelisted currencies
dicts = [{} for dic in range(len(markets))]
df = ["df"+str(m) for m in range(len(markets))]
for n in range(lenmarket):
    df[n] = pd.DataFrame(dicts[n], columns=['timestamp', 'close'])
dataArray = [[] for da in range(len(timeframes))]


# get candle data binance, and calculate stockstats for a set timeframe
def get_data(time, currency, rep):
    
    if time == 0:
        dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_1HOUR)
    elif time == 1:
        dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_30MINUTE)
    elif time == 2:
        dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_5MINUTE)
    elif time == 3:
        dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_1MINUTE)

    for y in range(len(dataArray)):
        df[currency].loc[y] = [dataArray[y][0], dataArray[y][4]]

    stock_df = stockstats.StockDataFrame.retype(df[currency])
    df[currency]['macd'] = stock_df.get('macd')
    df[currency]['rsi'] = stock_df.get('rsi')
    
    return df[currency]




# get historical data timeframe in Client.KLINE_INTERVAL_5MINUTE format 
def get_historical_data(market, from_time):
    
    try:
        data = client.get_historical_klines(market, timeframe, from_time)
        return data
    except:
        print ("Api not responding")

# get market price of selected market
def get_price_now(market):
    
    try:
        value = client.get_ticker(symbol=market)
        return value['lastPrice']
    except:
        print ("Api not responding")

#market buy and sell, price is exaclty marketprice automatically 
def market_buy(market, quant):
    try:
        order = client.order_market_buy(
            symbol= market,
            quantity= quant
        )
        return True
    except:
        print ("Buying failed")
        return False


def market_sell(market, quant):
    try:
        order = client.order_market_sell(
            symbol= market,
            quantity= quant
        )
        return True
    except:
        print("Selling failed")
        return False

#check all balances in wallet
def wallet_balance():
    try:
        status = client.get_account()
        bal = status['balances']
        for l in range(len(bal)):
            if float(bal[l]['free']) > 0.0001:
                print (bal[l])
    except:
        print("Getting wallet from api failed or your really broke haaah")
