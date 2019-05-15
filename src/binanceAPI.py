from binance.client import Client
import time
import csv
import json
import server
import settings
import twitterAPI


client = Client(settings.key, settings.secret)
markets = settings.markets


def fill_database():
    klines = client.get_historical_klines(
        markets[0], Client.KLINE_INTERVAL_1HOUR, "1 Apr, 2019")
    for kline in klines:
        server.insert("daan", "daan")


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
