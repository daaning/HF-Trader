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
interval = "Client.KLINE_INTERVAL_30MINUTE"
timeframe = 60 # timeframe in seconds

# stake amount in tradecurrency
stakeamount = 0.001

# maximum amount of trades it will buy
maxstakes = 5

# if your strategy doesnt sell without profit set minimum Return of investment
minROI = 1.01 # minimum ROI in % * 100 on selling with stoploss


# twitter 

twitterkey = ""
twittersecret = ""
tokenkey = ""
tokensecret = ""

