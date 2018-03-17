import json
config = json.load(open('Config.json'))

# the keys to your binance API
key= config['key']
secret= config['secret']

# set your trade currency
tradecurrency = "BTC"

# markets where to trade in
tradewith = ["ETH",
             "XVG",
             "XMR"]

# Timeframe: 1MINUTE 3MINUTE, 5MINUTE, 15MINUTE, 30MINUTE, 1HOUR
timeframes = ["KLINE_INTERVAL_1HOUR", "Client.KLINE_INTERVAL_30MINUTE",
              "Client.KLINE_INTERVAL_5MINUTE", "Client.KLINE_INTERVAL_1MINUTE"]
timeframe = 10 # timeframe in seconds for the loop to check for data

# stake amount in tradecurrency
stakeamount = 0.001

# maximum amount of trades it will buy
maxstakes = 5

# if your strategy doesnt sell without profit set minimum Return of investment
minROI = 1.01 # minimum ROI in % * 100 on selling with stoploss

# twitter 
twitter_key = config['twitter_key']
twitter_secret = config['twitter_secret']
twitter_tokenkey = config['twitter_tokenkey']
twitter_tokensecret = config['twitter_tokensecret']

