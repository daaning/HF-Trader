from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
import Main
import Settings
import pandas as pd
import stockstats
import logging
import time
import Database


#get all the settings from settings
lenmarket = len(Settings.tradewith)
client = Client(Settings.key, Settings.secret)
tradewith = Settings.tradewith
tradecurrency = Settings.tradecurrency 

# format the markets array for binance input
markets = []
for m in range(lenmarket):
    markets.append(tradewith[m] + tradecurrency)


# making a 2d array of pandas dataframes for all the whitelisted currencies and timeframes
dicts = {}
df = [[[] for x in range(lenmarket)] for y in range(4)] 
def initiate():
    for ma in range(4):
        for ti in range(lenmarket):
            df[ma][ti] = pd.DataFrame(dicts, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
initiate()



# get candle data binance always gets 1000 of the last candles
def get_data(time, currency, rep, loopdone):
    
    try:
        if time == 0:
            dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_1HOUR)
        elif time == 1:
            dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_30MINUTE)
        elif time == 2:
            dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_5MINUTE)
        elif time == 3:
            dataArray = client.get_klines(symbol=markets[currency], interval=Client.KLINE_INTERVAL_1MINUTE)
    except BinanceAPIException as ex:
        print (ex)
        
    for y in range(len(dataArray)):
        df[time][currency].loc[y] = [ dataArray[y][0], dataArray[y][1],
                                    dataArray[y][2], dataArray[y][3],
                                    dataArray[y][4],dataArray[y][5]]
            
    
    return df[time][currency]


# get historical data timeframe in Client.KLINE_INTERVAL_5MINUTE format 
def get_historical_data(market, timeframe, from_time):
    
    try:
        data = client.get_historical_klines(market, timeframe, from_time)
        return data

    except BinanceAPIException as ex:
        print (ex)
        
        

# get market price of selected market
def get_price_now(market):
    try:
        value = client.get_ticker(symbol=market)
        return value['lastPrice']

    except BinanceAPIException as ex:
        print (ex)
    


#market buy and sell, price is exaclty marketprice automatically 
def market_buy(market, quant):
    try:
        order = client.order_market_buy(
            symbol= market,
            quantity= quant
        )
        print (order)
        return True

    except BinanceAPIException as ex:
        print (ex)
        return False


def market_sell(market, quant):
    try:
        order = client.order_market_sell(
            symbol= market,
            quantity= quant
        )
        print(order)
        return True

    except BinanceAPIException as ex:
        print (ex)
        return False

#check all balances in wallet
def wallet_balance():
    try:
        status = client.get_account()
        bal = status['balances']
        for l in range(len(bal)):
            if float(bal[l]['free']) > 0.0001:
                print (bal[l])
    except BinanceAPIException as ex:
        print (ex)


