from binance.client import Client
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
timeframe = Settings.interval


#dictionairies and arrays for pandas are being made
markets = []
for m in range(lenmarket):
    markets.append(tradewith[m] + tradecurrency)

#make pandas dataframes for all the whitelisted currencies
dicts = [{} for dic in range(len(markets))]
df = ["df"+str(m) for m in range(len(markets))]
for n in range(lenmarket):
    df[n] = pd.DataFrame(dicts[n], columns=['timestamp', 'close'])


# get candle data binance, and calculate stockstats for a set timeframe
def get_data(i, rep):

    try:
        dataArray = client.get_klines(symbol=markets[i], interval=Client.KLINE_INTERVAL_1MINUTE)
        for y in range(len(dataArray)):
            df[i].loc[y] = [dataArray[y][0], dataArray[y][4]]
        
    except:
            print ("API not responding")

    stock_df = stockstats.StockDataFrame.retype(df[i])
    df[i]['macd'] = stock_df.get('macd')
    df[i]['rsi'] = stock_df.get('rsi')
    
    return df[i]


# get historical data timeframe in Client.KLINE_INTERVAL_5MINUTE format 
def get_historical_data(market, from_time):
    data = client.get_historical_klines(market, timeframe, from_time)
    return data


# get market price of selected market
def get_price_now(market):
    value = client.get_ticker(symbol=market)
    return value['lastPrice']


#market buy and sell, price is exaclty marketprice automatically 
def market_buy(market, quant):
    order = client.order_market_buy(
        symbol= market,
        quantity= quant
    )
def market_sell(market, quant):
    order = client.order_market_sell(
        symbol= market,
        quantity= quant
    )


#check all balances in wallet
def wallet_balance():
    status = client.get_account()
    bal = status['balances']
    for l in range(len(bal)):
        if float(bal[l]['free']) > 0.0001:
            print (bal[l])



# blaa blaa 