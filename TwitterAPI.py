import tweepy
from textblob import TextBlob
import Settings
import numpy as np

# set all the twitter variables 
try:
    auth = tweepy.OAuthHandler(Settings.twitter_key, Settings.twitter_secret)
    auth.set_access_token(Settings.twitter_tokenkey, Settings.twitter_tokensecret)
except:
    print("Problem with loading twitter data")

markets = Settings.tradewith
language = "en" #language in ISO 639.1 code
polarr = []
sentarr = []

# gets the last text from twitter about a coin/market
# runs textblob polarity testing over it 
# returns the average 
def get_sentiment(currency):
    subject = markets[currency]
    try:
        api = tweepy.API(auth, wait_on_rate_limit=True)
        public_tweets = api.search(subject, language)
    except:
        print("Problem with loading twitterdata")
    del polarr[:]
    del sentarr[:]


    #loop through the tweets
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        polarr.append(sentiment[0])
        sentarr.append(sentiment[1])


    return np.average(polarr), np.average(sentarr)
