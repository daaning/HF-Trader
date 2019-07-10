from newsapi import NewsApiClient
import numpy as np
import json
from textblob import TextBlob

config = json.load(open('../config.json'))
newsapi = NewsApiClient(api_key=config['news_api'])

sources = newsapi.get_sources()
polarr = []
sentarr = []


def get_sentiment():
    try:
        public_articles = []
        all_articles = newsapi.get_everything(q='ethereum',
                                              sources='bbc-news,the-verge')
    except:
        print("Problem with loading twitterdata")
    del polarr[:]
    del sentarr[:]
    for article in all_articles['articles']:
        analysis = TextBlob(article['content'])
        sentiment = analysis.sentiment
        polarr.append(sentiment[0])
        sentarr.append(sentiment[1])

    return np.average(polarr), np.average(sentarr)


print(get_sentiment())
