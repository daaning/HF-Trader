import tweepy
from textblob import TextBlob
import json
import numpy as np
import time
import json
import settings

try:
    auth = tweepy.OAuthHandler(settings.twitter_key,
                               settings.twitter_secret)
    auth.set_access_token(settings.twitter_tokenkey,
                          settings.twitter_tokensecret)
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
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        polarr.append(sentiment[0])
        sentarr.append(sentiment[1])

    return np.average(polarr), np.average(sentarr)
