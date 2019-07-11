from newsapi import NewsApiClient
import numpy as np
import json
from textblob import TextBlob

try:
    config = json.load(open('../config.json'))
    newsapi = NewsApiClient(api_key=config['news_api'])
except:
    print("connection to newsserver failed")

#sources = newsapi.get_sources()
polarr = []
sentarr = []


def get_sentiment():
    try:
        all_articles = newsapi.get_everything(q='ethereum',
                                              sources='bbc-news, the-verge, vice')
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
