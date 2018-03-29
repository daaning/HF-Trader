
"""
these are the settings you have to set before trading

"""


# set your trade currency
tradecurrency = "BTC"

# markets where to trade in
tradewith = ["ETH",
             "XVG",
             "XMR"]

# stake amount in tradecurrency
stakeamount = 0.001

# maximum amount of trades the bot will acquire 
maxstakes = 5

# if your strategy doesnt sell without profit set minimum Return of investment
minROI = 1.01 # minimum ROI in % * 100 on selling with stoploss



"""
these are the settings you have to set in the Config.json file they are to be found 
at twitter and binance

"""

import json
config = json.load(open('Config.json'))

#the keys to your twitter API 
twitter_key = config['twitter_key']
twitter_secret = config['twitter_secret']
twitter_tokenkey = config['twitter_tokenkey']
twitter_tokensecret = config['twitter_tokensecret']

# the keys to your binance API
key= config['key']
secret= config['secret']


"""
These are the expert settings we dont recommend changing

"""

# Timeframe: 1MINUTE, 3MINUTE, 5MINUTE, 15MINUTE, 30MINUTE, 1HOUR or bigger
timeframes = ["1hour", "30minute",
              "5minute", "1minute"]
