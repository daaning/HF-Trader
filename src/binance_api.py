from binance.client import Client
from binance.client import BinanceAPIException
import time
import csv
import json 
import database


config = json.load(open('../config.json'))
client = Client(config["binance-key"], config["binance-secret"])
tradewith = config["trade-market"]


def fill_database():
    try:
        klines = client.get_historical_klines(tradewith, Client.KLINE_INTERVAL_1MINUTE, "1 Jul, 2019")
    except BinanceAPIException as ex:
        print (ex)
    
    for kline in klines:
        database.insert_data(kline[0],kline[1],kline[2],kline[3],kline[4],kline[5])

    print("database filled")


def get_data():
    try:
        kline = client.get_historical_klines(tradewith, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    except BinanceAPIException as ex:
        print (ex)
    timestamp, opens, high, low, close, volume  = kline[len(kline)-1][0], kline[len(kline)-1][1], kline[len(kline)-1][2], kline[len(kline)-1][3], kline[len(kline)-1][4], kline[len(kline)-1][5] 
    database.insert_data(timestamp, opens, high, low, close, volume)


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

def wallet_balance():
    try:
        status = client.get_account()
        bal = status['balances']
        for l in range(len(bal)):
            if float(bal[l]['free']) > 0.0001:
                print (bal[l])
    except BinanceAPIException as ex:
        print (ex)

