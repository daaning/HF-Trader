
import json
"""
these are the settings you have to set before trading
"""


# markets where to trade in
markets = ["BTCBNB",
           "BNBUSDT"]

# stake amount in tradecurrency
stakeamount = 0.001

# maximum amount of trades the bot will acquire
maxstakes = 5

# if your strategy doesnt sell without profit set. minimum Return of investment
# 1.00 is 100 procent return on original investment
minROI = 1.01  # minimum ROI in % * 100 on selling with stoploss

"""
these are the settings you have to set in the Config.json file they are to be found 
at twitter and binance
"""

config = json.load(open('../config.json'))
# the keys to your twitter API
twitter_key = config['twitter_key']
twitter_secret = config['twitter_secret']
twitter_tokenkey = config['twitter_tokenkey']
twitter_tokensecret = config['twitter_tokensecret']

# the keys to your binance API
key = config['binance_key']
secret = config['binance_secret']
