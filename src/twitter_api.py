import tweepy
from textblob import TextBlob
import json
import numpy as np
import time 
import json 

config = json.load(open('/home/daan/Desktop/daan/LF-trader/config.json'))


twitter_key = config['twitter_key']
twitter_secret = config['twitter_secret']
twitter_tokenkey = config['twitter_tokenkey']
twitter_tokensecret = config['twitter_tokensecret']

try:
    auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
    auth.set_access_token(twitter_tokenkey, twitter_tokensecret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
except:
    print("Problem with loading twitter data")


polarr = []
sentarr = []
def get_sentiment(subject):
    try:
        public_tweets = api.search(subject, "en")
    except:
        print("Problem with loading twitterdata")
    del polarr[:]
    del sentarr[:]
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        print(sentiment)
        polarr.append(sentiment[0])
        sentarr.append(sentiment[1])

    return np.average(polarr), np.average(sentarr)

