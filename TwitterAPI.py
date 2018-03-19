import tweepy
from textblob import TextBlob
import Settings
import numpy as np

# set all the twitter variables 
auth = tweepy.OAuthHandler(Settings.twitter_key, Settings.twitter_secret)
auth.set_access_token(Settings.twitter_tokenkey, Settings.twitter_tokensecret)
markets = Settings.tradewith


language = "en" #language in ISO 639.1 code
polarr = [[] for i in range(len(markets))]
sentarr = polarr



# gets the last text from twitter about a coin/market
# runs textblob polarity testing over it 
# returns the average 
def get_sentiment(i):
    
    subject = markets[i]
    api = tweepy.API(auth, wait_on_rate_limit=True)
    public_tweets = api.search(subject, language)

    #loop through the tweets
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        polarr[i].append(sentiment[0])
        sentarr[i].append(sentiment[1])

    return np.average(polarr[i]), np.average(sentarr[i])

