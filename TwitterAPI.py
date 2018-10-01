import tweepy
from textblob import TextBlob
import numpy as np
import time
import json

with open('data.json') as d:
      data = json.load(d)
running = True
error = ""

try:
    auth = tweepy.OAuthHandler(data['consumer_token'], data['consumer_key'])
    auth.set_access_token(data['acces_token'], data['acces_key'])
    api = tweepy.API(auth)
    print("twitter api connected and ready...")
except:
    running = False
    error = "login failed...."

    
def get_tweets():
    'gets the tweets from the twitter api'
    tweets = ""
    tweets = api.search("merkel", "en")        

    return tweets


def get_sentiment():
    '''uses textblob analysis to scan tweets from twitter api and return polarity
    and subjectivity'''
    sent = [0.0]
    obj = [0.0]
    print(running)
    tweets = get_tweets()
    if running:
        for tweet in tweets:
            blobtext = TextBlob(tweet.text)
            sent.append(blobtext.sentiment.polarity)
            obj.append(blobtext.sentiment.subjectivity)
    else:
        print('error with the twitterApi')
        return (0.0, 0.0)
    return (np.mean(sent), np.mean(obj))


print(get_sentiment())