from binance.client import Client
import time
import csv
import json
import database
import settings
import twitter


client = Client(settings.key, settings.secret)
markets = settings.markets


def fill_database():
    klines = client.get_historical_klines(
        markets, Client.KLINE_INTERVAL_1MINUTE, "1 May, 2019")
    for kline in klines:
        database.insert(kline)


def get_data():
    kline = client.get_klines(
        symbol="BNBBTC", interval=Client.KLINE_INTERVAL_1MINUTE)
    print(kline)


def market_buy(market, quant):
    try:
        order = client.order_market_buy(
            symbol=market,
            quantity=quant
        )
        print(order)
        return True

    except BinanceAPIException as ex:
        print(ex)
        return False


def market_sell(market, quant):
    try:
        order = client.order_market_sell(
            symbol=market,
            quantity=quant
        )
        print(order)
        return True

    except BinanceAPIException as ex:
        print(ex)
        return False


def wallet_balance():
    try:
        status = client.get_account()
        bal = status['balances']
        for l in range(len(bal)):
            if float(bal[l]['free']) > 0.0001:
                print(bal[l])
    except BinanceAPIException as ex:
        print(ex)


get_data()
